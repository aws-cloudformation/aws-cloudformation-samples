# AWSSamples::LambdaFunctionInvoker::Hook


- [Overview](#Overview)

- [Hook usage](#Hook-usage)

  - [Configure the hook](#Configure-the-hook)

- [Lambda function developer guide](#Lambda-function-developer-guide)

  - [Input](#Input)

  - [Output](#Output)

- [Hook tests](#Hook-tests)

  - [Unit tests](#Unit-tests)

  - [Contract tests](#Contract-tests)

  - [Example Lambda functions](#Example-Lambda-functions)

- [Hook development notes](#Hook-development-notes)


## Overview

LambdaFunctionInvoker is an [AWS CloudFormation
hook](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html)
that invokes [AWS Lambda](https://aws.amazon.com/lambda/) functions
you specify, where you implement proactive policy-as-code compliance
validation checks.

With this hook, you can invoke Lambda functions that are in the same
AWS region of the hook itself. Lambda functions you provide for the
hook to invoke can be either in the same AWS account as the hook (and
same region), or in another account you own (and same region) provided
that, for the latter, that you've configured your Lambda function with
a resource-based permission to allow the hook's execution role to
perform the `lambda:InvokeFunction` action. For more information, see
[Using resource-based policies for
Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html).

The hook uses a wildcard-based mechanism to target, by default, all
the AWS resource types for all invocation points (`preCreate`,
`preUpdate`, and `preDelete`). This means that if you activate and
configure this hook, when you create, update, or delete stacks by
default the hook will be invoked for each of the AWS resource types in
your templates and for all the invocation points. You'll be billed for
each hook invocation. See [AWS CloudFormation
Pricing](https://aws.amazon.com/cloudformation/pricing/) for more
information on hooks pricing. You'll also be billed for relevant
invocations of the function(s) that you configure to be invoked by the
hook.

If the above, default behavior is not the one you need, you can choose
to use `TargetFilters` in the configuration for the hook to only
invoke the hook for resource type targets and invocation points you
need; see [Using wildcards with Hook target
names](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-structure.html#wildcard-hook-targets)
for more information. You'll still be billed for hook invocations that
will result out of your configuration, and for invocations of Lambda
function(s) by the hook.


## Hook usage

Sections following next show you how to configure the hook, and what
to return from Lambda function(s) you create and invoke with this
hook.

First, install the [CloudFormation
CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html). You'll
also need the Python language plugin as this hook is written in
Python.

By default, this hook runs one Lambda function only. To be able to
specify more than one Lambda function to invoke with this hook, open
the `awssamples-lambdafunctioninvoker-hook.json` file, and change the
`maxItems` value for `LambdaFunctions` to a number of your choice, for
example: `5`.

When done, run the following commands to submit the hook to the
private registry for a given AWS region (`us-east-1` is shown as an
example):

```
cfn generate
cfn submit --dry-run
cfn submit --set-default --region us-east-1
```

When ready, continue with configuring the hook.


### Configure the hook

Create a `typeConfiguration.json` file with the hook configuration, as
shown next; note the `Properties` section, where you'll need to
configure `LambdaFunctions` with Lambda functions to invoke with the
hook:

```
cat <<EOF > typeConfiguration.json
{
    "CloudFormationConfiguration": {
        "HookConfiguration": {
            "TargetStacks": "ALL",
            "FailureMode": "FAIL",
            "Properties": {
                "LambdaFunctions": [
                    "LambdaFunctionInvokerHookTest-1"
                ]
            }
        }
    }
}
EOF
```

In the example above, you specify `LambdaFunctionInvokerHookTest-1`,
that is the name of a hypothetical Lambda function you own in your AWS
account in a given AWS region. You can also specify the [Amazon
Resource
Name](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
(ARN), name, version, or alias of your function.

Next, get the ARN for this hook, that you submitted to the private
registry earlier, by listing and filtering CloudFormation extensions
of type `HOOK` as shown next:

```
aws cloudformation list-types \
  --type HOOK \
  --filters TypeNamePrefix=AWSSamples::LambdaFunctionInvoker::Hook \
  --query 'TypeSummaries[?TypeName==`AWSSamples::LambdaFunctionInvoker::Hook`].TypeArn' \
  --output text
```

Use the value returned in the output above, and pass it to
`YOUR_HOOK_ARN` when you run this command to set the type
configuration for the hook using the file you created earlier:

```
aws cloudformation set-type-configuration \
  --configuration file://typeConfiguration.json \
  --type-arn 'YOUR_HOOK_ARN'
```


## Lambda function developer guide

This section shows which values to consume from within your Lambda
function(s) as an input, and what to return from your Lambda
function(s) as an output.

See also [Example Lambda functions](#Example-Lambda-functions) for
examples of how to use input and output values for Lambda functions
for this hook in a number of programming languages.


### Input

Resource properties for a resource type you describe in a
CloudFormation template are available as an input in the event request
that is passed in to your Lambda function's main method. For example,
for a Lambda function in Python, you'd first consume the `event`
variable to get the whole input request:

```
def lambda_handler(event, context):
    """Define the entry point of the function."""

    # Get the entire request from the input event.
    request = event["request"]
```

The `request` variable consumes the `request` node of the input
`event`. The full event request structure is shown in the following
example:

```
{
  "request": {
    "clientRequestToken": "REDACTED",
    "hookContext": {
      "awsAccountId": "REDACTED",
      "stackId": "REDACTED",
      "changeSetId": null,
      "hookTypeName": "AWS::LambdaFunctionInvoker::Hook",
      "hookTypeVersion": "00000001",
      "invocationPoint": "CREATE_PRE_PROVISION",
      "targetName": "AWS::S3::Bucket",
      "targetType": "RESOURCE",
      "targetLogicalId": "REDACTED",
      "targetModel": {
        "resourceProperties": {
          "VersioningConfiguration": {
            "Status": "Enabled"
          }
        }
      }
    }
  },
  "callbackContext": {}
}
```

When you develop your Lambda function, you consume the input event
above; in particular, you want to explore the data structure to search
for, and consume, `resourceProperties` (underneath `request` ->
`hookContext` -> `targetModel`), that exposes the properties the user
has specified in their CloudFormation template for a given
`targetName` resource type target that triggered the hook's
invocation. The example above shows a snippet of `resourceProperties`
for `AWS::S3::Bucket`, that is the `targetName` in the input request.


### Output

When you configure this hook to invoke your Lambda function, the hook
always expects to receive data from your function (more information on
output fields and data structure follows next). You need to return
JSON data from your function; if you return a JSON string instead,
this will result in an error that the hook will send.

An example of an expected JSON data output format from your Lambda
function is:

```
{"status": "SUCCESS", "errorCode": null, "message": "Versioning is enabled for the S3 bucket.", "callbackContext": null, "callbackDelaySeconds": 0}
```

as opposed to the following one, that is a JSON string, that is not
the format this hook expects:

```
"{\"status\": \"SUCCESS\", \"errorCode\": null, \"message\": \"Versioning is enabled for the S3 bucket.\", \"callbackContext\": null, \"callbackDelaySeconds\": 0}"
```

Let's take, as an example, the case of writing a Python Lambda
function; in particular, let's consider [Lambda function handler in
Python](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html)
and [Returning a
value](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html#python-handler-return). When
this hook calls your Lambda function, it uses a
`RequestResponse`-based [Synchronous
invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html),
and consumes JSON-serialized data from your Lambda function's
response. From your Python function, you'll need to return a
dictionary data type, such as:

```
    payload = {
        "status": "SUCCESS",
        "errorCode": None,
        "message": message,
        "callbackContext": None,
        "callbackDelaySeconds": 0,
    }

    return payload
```

that will result in this JSON-serialized data that the hook will
consume next:

```
{"status": "SUCCESS", "errorCode": null, "message": "Versioning is enabled for the S3 bucket.", "callbackContext": null, "callbackDelaySeconds": 0}
```

If you, instead, were to serialize directly the dictionary above
within your function handler, by using `json.dumps()` as in the
following example:

```
# This hook will not accept a JSON string as in this example.

import json

    # ...your code here...
    payload = {
        "status": "SUCCESS",
        "errorCode": None,
        "message": message,
        "callbackContext": None,
        "callbackDelaySeconds": 0,
    }

    return json.dumps(payload)
```

this will result in JSON data encoded into a JSON string, that the
hook will not accept:

```
"{\"status\": \"SUCCESS\", \"errorCode\": null, \"message\": \"Versioning is enabled for the S3 bucket.\", \"callbackContext\": null, \"callbackDelaySeconds\": 0}"
```

For more information on handler and return types for a number of
supported languages, see the AWS Lambda [Developer
Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html),
where you can find sections whose names start with "Building with
_language name_". For example, see [Handler
interfaces](https://docs.aws.amazon.com/lambda/latest/dg/java-handler.html#java-handler-interfaces)
in Java, where `RequestStreamHandler` is used for your own
serialization by writing directly to the output stream. The [Example
Lambda functions](#Example-Lambda-functions) section on this page
contains information for you to find a directory, in the same project
for this hook, with example Lambda functions: you can see also how a
Java example returns JSON data by using the method above.

When you author your Lambda function, you'll need to always return a
map data structure that contains a serialized set of information that
the hook will consume as a `ProgressEvent` object. **Make sure to
always return all fields in the response you'll send from the Lambda
function(s)** you write:

- `status`
- `errorCode`
- `message`
- `callbackContext`
- `callbackDelaySeconds`

that is, make sure fields above are always set in the response you
send from your Lambda function. Field values can be:

- `status` is either `FAILED`, `IN_PROGRESS`, or `SUCCESS`;

- `errorCode` is `NonCompliant` for a `FAILED` status when a resource
  is deemed not to be compliant by your function's code, or to an
  empty string or a null value for `SUCCESS` and `IN_PROGRESS`
  statuses. You can also return an [handler error
  code](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-contract-errors.html)
  that makes sense for your use case, for example: `InternalFailure`;

- `callbackContext`, if needed to continue evaluation of a target on a
  subsequent hook invocation: this is either a map structure, or an
  empty map or a null value;

- `callbackDelaySeconds` is the number of seconds to wait between
  reinvocations (see `callbackContext`). Specify `0` (as an integer,
  not as a string) if you don't need this functionality. Note that if
  you call more than one Lambda function from this hook, the value for
  `callbackDelaySeconds` used will be the highest value used in your
  functions. For example, if function1 uses `0` and function2 uses
  `3`, the value used by the hook for both functions will be `3`.

The following example shows sample Python code where you return a
dictionary of fields discussed above:

```
    if "InvalidPropertyKey" in resource_properties:
        payload = {
            "status": "FAILED",
            "errorCode": "NonCompliant",
            "message": "The resource is not compliant.",
            "callbackContext": None,
            "callbackDelaySeconds": 0,
        }
    else:
        if USE_CALLBACKS:
            payload = {
                "status": "IN_PROGRESS",
                "errorCode": None,
                "message": "In progress",
                "callbackContext":  {"test": 1},
                "callbackDelaySeconds": CALLBACK_DELAY_SECONDS,
            }
        else:
            payload = {
                "status": "SUCCESS",
                "errorCode": None,
                "message": "The resource is compliant.",
                "callbackContext": None,
                "callbackDelaySeconds": 0,
            }
    return payload
```

A sample Lambda function code, in Python, follows next:

```
"""Example Lambda function called by AWSSamples::LambdaFunctionInvoker::Hook."""


import logging

LOGGER = logging.getLogger()
LOGGER.setLevel("INFO")
# LOGGER.setLevel("DEBUG")

# Define for which invocation points to run. Comment out the line
# corresponding to the invocation point you do not want to run.
HOOK_INVOCATION_POINTS = [
    "CREATE_PRE_PROVISION",
    "UPDATE_PRE_PROVISION",
    "DELETE_PRE_PROVISION",
]

# Used for toggling between callback-based workflows or not.
# For testing purposes only.
USE_CALLBACKS = False
CALLBACK_CONTEXT = {"test": 1}
CALLBACK_DELAY_SECONDS = 1


def lambda_handler(event, context):
    """Define the entry point of the function."""
    LOGGER.debug(event)

    request = event["request"]
    invocation_point = request["hookContext"]["invocationPoint"]
    LOGGER.info(f"Invocation point: {invocation_point}")
    if invocation_point not in HOOK_INVOCATION_POINTS:
        return {
            "status": "SUCCESS",
            "errorCode": None,
            "message": f"Skipping target evaluation for {invocation_point}.",
            "callbackContext": None,
            "callbackDelaySeconds": 0,
        }

    target_model = request["hookContext"]["targetModel"]
    resource_properties = target_model["resourceProperties"]
    LOGGER.debug(f"Resource properties: {resource_properties}")

    callback_context = event["callbackContext"]
    LOGGER.debug(f"Callback context: {callback_context}")

    if callback_context:
        return {
            "status": "SUCCESS",
            "errorCode": None,
            "message": "(After a reinvocation of the handler) The resource is compliant.",
            "callbackContext": None,
            "callbackDelaySeconds": 0,
        }

    if "InvalidPropertyKey" in resource_properties:
        payload = {
            "status": "FAILED",
            "errorCode": "NonCompliant",
            "message": "The resource is not compliant.",
            "callbackContext": None,
            "callbackDelaySeconds": 0,
        }
    else:
        if USE_CALLBACKS:
            payload = {
                "status": "IN_PROGRESS",
                "errorCode": None,
                "message": "In progress",
                "callbackContext": CALLBACK_CONTEXT,
                "callbackDelaySeconds": CALLBACK_DELAY_SECONDS,
            }
        else:
            payload = {
                "status": "SUCCESS",
                "errorCode": None,
                "message": "The resource is compliant.",
                "callbackContext": None,
                "callbackDelaySeconds": 0,
            }
    LOGGER.debug(payload)
    return payload
```


## Tests

The following sections show tests you run as part of developing this
hook.


### Unit tests

Make sure you install the prerequisite first:

```
pip3 install pytest-cov
```

Next, to run unit tests, make sure you're at the top-level of this
project (that is, where this `README.md` file is), and run:

```
pytest --cov
```


### Contract tests

To run contract tests, create a Lambda function(s) using the
CloudFormation template provided as part of this project, as follows
(specify `yes` if you wish to configure Lambda function targets to use
callbacks, otherwise use `no`); make sure to be in the root directory
of the project (that is, where this `README.md` file is), when you run
the command below:

```
aws cloudformation create-stack \
    --stack-name awssamples-lambdafunctioninvoker-hook-test-lambda-functions \
    --template-body file://contract-tests-prerequisites/lambda-functions.template \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameters \
        ParameterKey=LambdaFunction1UseCallbacks,ParameterValue=no \
        ParameterKey=LambdaFunction2UseCallbacks,ParameterValue=no \
        ParameterKey=LambdaFunction3UseCallbacks,ParameterValue=no \
        ParameterKey=LambdaFunction4UseCallbacks,ParameterValue=no \
        ParameterKey=LambdaFunction5UseCallbacks,ParameterValue=no
```

This will create 5 Lambda functions:

 - LambdaFunctionInvokerHookTest-1
 - LambdaFunctionInvokerHookTest-2
 - LambdaFunctionInvokerHookTest-3
 - LambdaFunctionInvokerHookTest-4
 - LambdaFunctionInvokerHookTest-5

Next, update your `~/.cfn-cli/typeConfiguration.json` file before
running contract tests, and make sure to add the `LambdaFunction`
configuration item below with the names you've given to your Lambda
functions:

```
{
    "CloudFormationConfiguration": {
        "HookConfiguration": {
            "TargetStacks": "ALL",
            "FailureMode": "FAIL",
            "Properties": {
                "LambdaFunctions": [
                    "LambdaFunctionInvokerHookTest-1",
                    "LambdaFunctionInvokerHookTest-2",
                    "LambdaFunctionInvokerHookTest-3",
                    "LambdaFunctionInvokerHookTest-4",
                    "LambdaFunctionInvokerHookTest-5"
                ]
            }
        }
    }
}
```

Note that if `maxItems` in the
`awssamples-lambdafunctioninvoker-hook.json` file for the
`LambdaFunctions` property is set to `1` (default/typical behavior),
this shows the intent of only invoking one Lambda function: you should
then specify only one Lambda function in the list above.

Next, run `sam local start-lambda` in one terminal on your machine,
and keep it running; make sure you're in the root directory of the
project, that is where this README file is.

When ready, open another terminal window, make sure you're in the root
directory of the project as well, and follow steps following next:

- run `./update_contract_test_inputs.py` to generate contract test
  inputs;
- run `cfn generate && cfn submit --dry-run` followed by `cfn test`.


### Example Lambda functions

This project includes example code that you can use to create Lambda
functions to test and evaluate the hook, by configuring the hook to
invoke the Lambda function you'll create. Refer to the `README.md`
file for each project under the `example-lambda-functions` directory
for more information.

For more information on deploying Lambda functions, see [Deploying
Lambda
functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-deploy-functions.html).

For more information on AWS Lambda, see the [Developer
Guide](https://docs.aws.amazon.com/lambda/latest/dg/index.html).


## Hook development notes

> Don't modify `models.py` by hand; any modifications will be
> overwritten when the `generate` or `package` commands are run.
