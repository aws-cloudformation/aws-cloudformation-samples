cmake_minimum_required(VERSION 3.9)

set(CMAKE_CXX_STANDARD 11)

set(SERVICE_COMPONENTS s3)

project(s3-versioning-enabled LANGUAGES CXX)

find_package(AWSSDK REQUIRED COMPONENTS ${SERVICE_COMPONENTS})

find_package(aws-lambda-runtime)

add_executable(${PROJECT_NAME} "main.cpp")

target_link_libraries(${PROJECT_NAME} PRIVATE ${AWSSDK_LINK_LIBRARIES} AWS::aws-lambda-runtime)

target_compile_features(${PROJECT_NAME} PRIVATE "cxx_std_11")

target_compile_options(${PROJECT_NAME} PRIVATE "-Wall" "-Wextra")

aws_lambda_package_target(${PROJECT_NAME})
