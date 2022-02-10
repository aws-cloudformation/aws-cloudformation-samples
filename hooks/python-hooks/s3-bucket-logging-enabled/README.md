# AWSSamples::S3BucketLoggingEnabled::Hook

This AWS CloudFormation Hook validates that S3 buckets have logging enabled, and optionally that the log bucket and/or prefix is configured to the prescribed values.

## Configuration

```bash
# Create a basic type configuration json
cat <<EOF > type_config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode":"FAIL",
      "Properties": {}
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type HOOK \
  --type-name AWSSamples::S3BucketLoggingEnabled::Hook
```

## Specifying a bucket name and/or key prefix that are required

To specify a required bucket name or key prefix, add them to a Properties section of the hook configuration.

> NOTE: Key Prefix can use `%BUCKET_NAME%` to include the bucket's name in the prefix, if it is used, buckets must declare the `BucketName` property.

```json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode":"FAIL",
      "Properties": {
        "DestinationBucketName": "my-s3-bucket",
        "LogFilePrefix": "s3-logs/%BUCKET_NAME%/"
      }
    }
  }
}
```

## Example templates

Hook will always find this non-compliant
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties: {}
```

A hook configured to require `my-logging-bucket` to be the log destination will find this non-compliant
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      LoggingConfiguration: {}
```

This will be found compliant for a configuration that requires `my-logging-bucket` for log bucket and `logs/%BUCKET_NAME%/` for LogFilePrefix
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties: 
      BucketName: 'my-bucket'
      LoggingConfiguration:
        DestinationBucketName: 'my-logging-bucket'
        LogFilePrefix: 'logs/%BUCKET_NAME%/'
```