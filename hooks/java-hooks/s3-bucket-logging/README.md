# AWSSamples::S3BucketLoggingCompliance::Hook

This AWS CloudFormation Hook validates that any S3 Bucket has logging configured to go to a specific bucket.

Below is a sample CloudFormation template that will be passed by the hook:

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Sample template for the AWSSamples::S3BucketLoggingCompliance::Hook resource type that should pass (LoggingConfiguration DestinationBucketName matches the LoggingBucket property set in the type configuration of the hook)

Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub "mybucket-${AWS::AccountId}-${AWS::Region}-sample"
      AccessControl: Private
      LoggingConfiguration:
        DestinationBucketName: !Sub "loggingbucket-${AWS::AccountId}-${AWS::Region}-sample"
        LogFilePrefix: "/logs-samples/"
  LoggingBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub "loggingbucket-${AWS::AccountId}-${AWS::Region}-sample"
      AccessControl: LogDeliveryWrite
      LoggingConfiguration:
        DestinationBucketName: !Sub "loggingbucket-${AWS::AccountId}-${AWS::Region}-sample"
        LogFilePrefix: "/logs-samples/"
Outputs:
  BucketName:
    Value: !Ref S3Bucket
    Description: Name of the sample Amazon S3 bucket with a logging configuration.
  LoggingBucket:
    Value: !Ref LoggingBucket
    Description: Name of the sample Amazon S3 logging bucket.
```

Below is a sample CloudFormation template that will be rejected by the hook:

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Sample template for the AWSSamples::S3BucketLoggingCompliance::Hook resource type that should fail (LoggingConfiguration DestinationBucketName does not match the LoggingBucket property set in the type configuration of the hook)

Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub "mybucket-${AWS::AccountId}-${AWS::Region}-sample"
      AccessControl: Private
      LoggingConfiguration:
        DestinationBucketName: !Sub "notmyloggingbucket-${AWS::AccountId}-${AWS::Region}-sample"
        LogFilePrefix: "/logs-samples/"
  LoggingBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub "loggingbucket-${AWS::AccountId}-${AWS::Region}-sample"
      AccessControl: LogDeliveryWrite
        LoggingConfiguration:
        DestinationBucketName: !Sub "notmyloggingbucket-${AWS::AccountId}-${AWS::Region}-sample"
        LogFilePrefix: "/logs-samples/"
Outputs:
  BucketName:
    Value: !Ref S3Bucket
    Description: Name of the sample Amazon S3 bucket with a logging configuration.
  LoggingBucket:
    Value: !Ref LoggingBucket
    Description: Name of the sample Amazon S3 logging bucket.
```

This hook has one required property, `LoggingBucket` which references the name of the compliant logging bucket. Sample configuration below, please update `${AWS::AccountId}`, `${AWS::Region}`, and `Your-Hook-ARN`:

## Sample type configuration

```bash
# Create a basic type configuration json
cat <<EOF >> type_config.json
{
    "CloudFormationConfiguration": {
        "HookConfiguration": {
            "TargetStacks": "ALL",
            "FailureMode": "FAIL",
            "Properties": {
                "LoggingBucket": "loggingbucket-${AWS::AccountId}-${AWS::Region}-sample"
            }
        }
    }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type HOOK \
  --type-name WSSamples::S3BucketLoggingCompliance::Hook
```
