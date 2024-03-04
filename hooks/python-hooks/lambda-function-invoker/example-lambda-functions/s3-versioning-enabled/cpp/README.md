# s3-versioning-enabled example Lambda function


## Notes

This sample uses C++11 or higher, and is meant to be built on a Linux
machine.


## Prerequisites

In order to be able to locally test the Lambda function on your Linux
machine, make sure to install [AWS SAM
CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html). You'll
also need to use Docker with the SAM CLI: for more information, see
[Installing Docker to use with the AWS SAM
CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-docker.html).

You'll need the AWS SDK for C++ in order to be able to compile and use
this sample; to get started, see the [AWS SDK for C++ Developer
Guide](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/welcome.html),
where you can choose to follow instructions on how to compile the SDK,
for example [from
sources](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/sdk-from-source.html).

For this example function, you don't need to compile the full SDK,
unless you choose to; when you'll run `cmake` for example, you can
choose to run it as such:

```
cmake ../aws-sdk-cpp -DCMAKE_BUILD_TYPE=Debug -DCMAKE_PREFIX_PATH=/usr/local/ -DCMAKE_INSTALL_PREFIX=/usr/local/ -DBUILD_ONLY="s3"
```

to only include the Amazon S3 service package. This way, should you
elect in the future to update this sample function to make API calls
to S3, you'd already have the S3 package on your machine. Moreover,
the core AWS SDK is still needed in this project to consume classes
from the `Aws::Utils::Json`
[namespace](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-core/html/namespace_aws_1_1_utils_1_1_json.html).

You'll also need the AWS Lambda C++ Runtime to run this code in AWS
Lambda; for more information, see
[Prerequisites](https://github.com/awslabs/aws-lambda-cpp?tab=readme-ov-file#prerequisites)
in the [aws-lambda-cpp](https://github.com/awslabs/aws-lambda-cpp)
repository. After you've followed instructions to clone the repository
and created the `build` directory, choose to follow instructions to
run `cmake` by using `~/s3-versioning-enabled` for
`CMAKE_INSTALL_PREFIX`:

```
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=~/s3-versioning-enabled
```


## Building and testing the Lambda function locally

Once you've installed and configured prerequisites mentioned above,
adapt to your environment as needed the `build-and-invoke.sh` script,
that you can use to build and invoke the Lambda function locally with
SAM. This includes adjusting the `CMAKE_PREFIX_PATH` path values (if
you've used the default installation path for the AWS SDK for C++, the
path values already present in the file should work). Also, the
`cmake` invocation in the script, that should look like the following:

```
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=~/s3-versioning-enabled
```

should match the value for `CMAKE_INSTALL_PREFIX` that you used in the
prerequisites (that is, `~/s3-versioning-enabled`).

When ready, run the `build-and-invoke.sh` script to build and test the
code locally (for the latter, make sure you have Docker running, and
the SAM CLI installed):

```
./build-and-invoke.sh
```

If no errors occurred, the script will build and then invoke (with
SAM) the local Lambda function endpoint 3 times, one for each of the
`event*.json` files. At the end of the process, you should have a
`build/s3-versioning-enabled.zip` output file, that you'll use next.


## Creating the Lambda function

To create the Lambda function when ready, create a [Lambda execution
role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)
for your Lambda function; when attaching a role policy, you could
choose to use `AWSLambdaBasicExecutionRole` or the policy you
need. When ready, note down the Amazon Resource Name (ARN) for the
role you created, and pass it to the following command:

```
aws lambda create-function \
    --function-name s3-versioning-enabled-cpp \
    --role REPLACE_WITH_YOUR_LAMBDA_FUNCTION_ROLE_ARN \
    --runtime provided.al2023 \
    --timeout 15 \
    --memory-size 128 \
    --handler s3-versioning-enabled \
    --zip-file fileb://build/s3-versioning-enabled.zip
```

For subsequent code updates, as needed, you'll just need to run:

```
aws lambda update-function-code \
    --function-name s3-versioning-enabled-cpp \
    --zip-file fileb://build/s3-versioning-enabled.zip
```

When ready, configure the hook to run the Lambda function you created,
and test its functionality as needed.
