# AWSSamples::S3BlockPublicAccess::Hook

This AWS CloudFormation Hook checks S3 Buckets to determine if the Block Public Access settings (PublicAccessBlockConfiguration) are all enabled during CREATE or UPDATE actions on the stack. 

You can use this hook to exclude buckets from this requirement by using the `excludedBucketSuffixes` property. The configuration properties for this hook's settings are below.  
```
{
    "properties": {
        "excludedBucketSuffixes": {
            "description": "A comma separated list of bucket names that should be excluded from the BPA requirement. Each name provided will be matched using starts-with logic.",
            "type": "string"
        }
    }
}
```

## Subscribe to the hook
The following is an example that shows how you can subscribe to the hook. In this example, we are requiring that all S3 Buckets have the PublicAccessBlockConfiguration settings enabled while excluding any S3 Buckets that start with the name `baseline-` or `excluded-`.

```bash
# Create a basic type configuration json
cat <<EOF >> type_config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode": "FAIL",
      "Properties": {
        "excludedBucketSuffixes": "excluded-,baseline-"
      }
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type HOOK \
  --type-name AWSSamples::S3BlockPublicAccess::Hook
```

## Example CloudFormation Templates
The following CloudFormation templates demonstrate how this hook can be used using the above type configuration.

Fail example 1 - Not all 4 of the PublicAccessBlockConfiguration settings are specified
```
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub 'mybucket-${AWS::Region}-${AWS::AccountId}'
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
```

Fail example 2 - The PublicAccessBlockConfiguration settings are not specified
```
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub 'mybucket-${AWS::Region}-${AWS::AccountId}'
```

Success example 1 - The PublicAccessBlockConfiguration are all set to true
```
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub 'mybucket-${AWS::Region}-${AWS::AccountId}'
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
```

Success example 2 - The bucket name is excluded from the PublicAccessBlockConfiguration requirement.
```
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub 'baseline-${AWS::Region}-${AWS::AccountId}'
```


Success example 3 - The bucket name is not included, but the PublicAccessBlockConfiguration settings are all enabled.
```
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      PublicAccessBlockConfiguration:
        BlockPublicAcls: true
        BlockPublicPolicy: true
        IgnorePublicAcls: true
        RestrictPublicBuckets: true
```
