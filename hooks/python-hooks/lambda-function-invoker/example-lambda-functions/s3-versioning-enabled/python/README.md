# s3-versioning-enabled example Lambda function


## Notes

This sample uses Python 3.11 or higher.


## Prerequisites

In order to be able to locally test the Lambda function on your
machine, make sure to install [AWS SAM
CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html). You'll
also need to use Docker with the SAM CLI: for more information, see
[Installing Docker to use with the AWS SAM
CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-docker.html).


## Testing the Lambda function locally

Once you've installed and configured prerequisites mentioned above,
use the SAM CLI to test the code locally (for the latter, make sure
you have Docker running, and the SAM CLI installed):

```
sam local invoke --event event-success.json

sam local invoke --event event-failed.json

sam local invoke --event event-invalid.json
```

If no errors occurred, the script will build and then invoke (with
SAM) the local Lambda function endpoint 3 times, one for each of the
`event*.json` files.


## Creating the Lambda function

First, create a ZIP archive containing the function code:

```
zip s3-versioning-enabled.zip lambda_function.py
```

To create the Lambda function when ready, create a [Lambda execution
role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)
for your Lambda function; when attaching a role policy, you could
choose to use `AWSLambdaBasicExecutionRole` or the policy you
need. When ready, note down the Amazon Resource Name (ARN) for the
role you created, and pass it to the following command:

```
aws lambda create-function \
    --function-name s3-versioning-enabled-python \
    --role REPLACE_WITH_YOUR_LAMBDA_FUNCTION_ROLE_ARN \
    --runtime python3.12 \
    --timeout 15 \
    --memory-size 128 \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://s3-versioning-enabled.zip
```

For subsequent code updates, as needed, you'll just need to run:

```
aws lambda update-function-code \
    --function-name s3-versioning-enabled-python \
    --zip-file fileb://s3-versioning-enabled.zip
```

When ready, configure the hook to run the Lambda function you created,
and test its functionality as needed.
