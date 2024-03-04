# s3-versioning-enabled example Lambda function


## Notes

This sample uses Go 1.20 or higher, and is meant to be built on a
Linux machine.


## Prerequisites

In order to be able to locally test the Lambda function on your Linux
machine, make sure to install [AWS SAM
CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html). You'll
also need to use Docker with the SAM CLI: for more information, see
[Installing Docker to use with the AWS SAM
CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-docker.html).


## Building and testing the Lambda function locally

Once you've installed and configured prerequisites mentioned above,
set up your environment by running the following commands in the same
directory where this `README.md` file is (the first command will fail
if there's already a `go.mod` file in the directory, which should be
the case; adding that command for documentation purposes for this
example nevertheless):

```
go mod init s3-versioning-enabled
go get github.com/aws/aws-lambda-go/lambda
```

When ready, run the following commands to build and test the code
locally (for the latter, make sure you have Docker running, and the
SAM CLI installed):

```
GOOS=linux go build -o bootstrap main.go
sam local invoke --event event-success.json
sam local invoke --event event-failed.json
sam local invoke --event event-invalid.json
```

If no errors occurred, the first command above will build the example
code, and create a `bootstrap` executable file. The other commands
will then invoke (with SAM) the local Lambda function endpoint 3
times, one for each of the `event*.json` files.

Next, create a ZIP archive you'll use next to deploy the Lambda
function:

```
zip s3-versioning-enabled.zip bootstrap
```


## Creating the Lambda function

To create the Lambda function when ready, create a [Lambda execution
role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)
for your Lambda function; when attaching a role policy, you could
choose to use `AWSLambdaBasicExecutionRole` or the policy you
need. When ready, note down the Amazon Resource Name (ARN) for the
role you created, and pass it to the following command:

```
aws lambda create-function \
    --function-name s3-versioning-enabled-golang \
    --role REPLACE_WITH_YOUR_LAMBDA_FUNCTION_ROLE_ARN \
    --runtime provided.al2023 \
    --timeout 15 \
    --memory-size 128 \
    --handler bootstrap \
    --zip-file fileb://s3-versioning-enabled.zip
```

For subsequent code updates, as needed, you'll just need to run:

```
aws lambda update-function-code \
    --function-name s3-versioning-enabled-golang \
    --zip-file fileb://s3-versioning-enabled.zip
```

When ready, configure the hook to run the Lambda function you created,
and test its functionality as needed.
