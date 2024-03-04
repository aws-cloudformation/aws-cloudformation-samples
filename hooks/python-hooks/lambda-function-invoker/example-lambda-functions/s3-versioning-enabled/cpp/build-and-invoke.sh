#!/bin/sh


# Example script to build the s3-versioning-enabled sample project.


# Important: make sure to update paths below according to your configuration.
export CMAKE_PREFIX_PATH="/usr/local/lib64/cmake/AWSSDK:/usr/local/lib64/cmake/aws-cpp-sdk-core:/usr/local/lib64/aws-crt-cpp:/usr/local/lib64/aws-c-http:/usr/local/lib64/aws-c-io:/usr/local/lib64/s2n"


if [ ! -d build ]; then
    echo
    echo 'Creating build directory.'
    mkdir build
fi

cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=~/s3-versioning-enabled

echo
echo 'Cleaning project files, if present.'
make clean
echo 'Cleaning AWS SAM-related event(s) and template files.'
rm -f event*.json template.yml

echo
echo 'Building project.'
make && make aws-lambda-package-s3-versioning-enabled

if [ $? -gt 0 ]; then
    exit 1
fi

echo
echo 'Copying AWS SAM event(s) and template files.'
cp ../event*.json .
cp ../template.yml .

echo
echo 'Testing the SUCCESS use case.'
sam local invoke --event event-success.json

echo
echo 'Testing the FAILED use case.'
sam local invoke --event event-failed.json

echo
echo 'Testing the INVALID use case.'
sam local invoke --event event-invalid.json
