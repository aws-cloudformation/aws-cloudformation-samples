# s3-versioning-enabled


## Overview

In this directory you can find example code, implemented in a number
of programming languages, that you can bring to AWS Lambda functions
you create to evaluate if an Amazon S3 bucket has versioning
enabled. Once you create the Lambda function, you'll need to configure
the hook to invoke the Lambda function you created to evaluate S3
buckets you describe in CloudFormation templates that, in turn, you
use to create CloudFormation stacks.

Once you've created the Lambda function using the example code as a
starting point for experimentation, you can invoke the function using
a test event to simulate data coming in on a hook invocation, that
contain also the S3 bucket properties. Example for a compliant S3
bucket (versioning status enabled):

```
{
  "request": {
    "clientRequestToken": "REDACTED",
    "hookContext": {
      "awsAccountId": "REDACTED",
      "stackId": "REDACTED",
      "changeSetId": null,
      "hookTypeName": "AWSSamples::LambdaFunctionInvoker::Hook",
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

Example for a non-compliant S3 bucket (versioning status suspended):

```
{
  "request": {
    "clientRequestToken": "REDACTED",
    "hookContext": {
      "awsAccountId": "REDACTED",
      "stackId": "REDACTED",
      "changeSetId": null,
      "hookTypeName": "AWSSamples::LambdaFunctionInvoker::Hook",
      "hookTypeVersion": "00000001",
      "invocationPoint": "CREATE_PRE_PROVISION",
      "targetName": "AWS::S3::Bucket",
      "targetType": "RESOURCE",
      "targetLogicalId": "REDACTED",
      "targetModel": {
        "resourceProperties": {
          "VersioningConfiguration": {
            "Status": "Suspended"
          }
        }
      }
    }
  },
  "callbackContext": {}
}
```

When ready to test the hook calling the `s3-versioning-enabled`
function you created, use the following templates to create 2 stacks,
whereas one should pass validation, and the other shouldn't:

```
aws cloudformation create-stack \
    --stack-name test-s3-bucket-compliant \
    --template-body file://example-test-templates/test-s3-bucket-compliant.template

aws cloudformation create-stack \
    --stack-name test-s3-bucket-not-compliant \
    --template-body file://example-test-templates/test-s3-bucket-not-compliant.template
```


## Business logic rationale


### Hook invocation considerations

Each example code uses a common business logic to evaluate your S3
bucket target. Let's explore it in details.

The `AWSSamples::LambdaFunctionInvoker::Hook` uses a wildcard-based
mechanism to target, by default, all the AWS resource types for all
invocation points (`preCreate`, `preUpdate`, and `preDelete`). This
means that if you activate and configure that hook, when you create,
update, or delete stacks by default the hook will be invoked for each
of the AWS resource types in your templates and for all the invocation
points. You'll be billed for each hook invocation. See [AWS
CloudFormation
+Pricing](https://aws.amazon.com/cloudformation/pricing/) for more
+information on hooks pricing. You'll also be billed for relevant
invocations of this function, that is called by that hook.

If the above, default behavior is not the one you need, you can choose
to use `TargetFilters` in the configuration for the hook to only
invoke the hook for resource type targets and invocation points you
need; see [Using wildcards with Hook target
names](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-structure.html#wildcard-hook-targets)
for more information. You'll still be billed for hook invocations that
will result out of your configuration, and for invocations of this
Lambda function.

If you choose to invoke the hook for all the invocation points
(default behavior), and to not set `TargetFilters` for your hook, you
can define, in the example Lambda function code, for which invocation
points to run the code in this function. It is important to understand
that if you choose this method as opposed to target filters, the hook
will be invoked anyway for all of the AWS resource types in your
templates across all the invocation points, and you'll be billed for
all the invocations. To use this feature, comment out the line for
`HOOK_INVOCATION_POINTS` that corresponds to the invocation point you
do not want to run. Later on in this example code, you'll find a
conditional block that will return SUCCESS if the current invocation
point is something you do not need to evaluate on during the current
invocation.


### Target evaluation considerations

This section describes the business logic to validate that an S3
bucket described in a CloudFormation template is set up to have
versioning enabled. When you look at the model for an S3 bucket from a
CloudFormation resource type perspective, you note the
`VersioningConfiguration` property, that in this case you want to set
with a `Status` of `Enabled` as shown in the
[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-bucket.html)
page.

The code for the hook expects an input configuration (that is,
properties for the S3 bucket in the CloudFormation template) set as in
the following YAML-formatted template snippet:

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      VersioningConfiguration:
        Status: Enabled
```

or as in its equivalent in JSON format:

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "VersioningConfiguration": {
                    "Status": "Enabled"
                },
```

The code for the hook then needs to validate not only if `Status` for
`VersioningConfiguration` is set to `Enabled`, but also if all the
other parent properties are present in the template.
