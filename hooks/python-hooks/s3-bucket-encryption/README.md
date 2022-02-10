# AWSSamples::S3BucketEncrypt::Hook

This AWS CloudFormation Hook checks Amazon S3 Buckets to determine if server-side encryption with KMS keys are enabled during CREATE or UPDATE operations on the stack. 


## Subscribe to the hook
The following is an example type configuration that shows how you can configure to the hook. In this example, we are requiring that all S3 Bucket encryption algorithm is set to aws:kms.

```bash
# Create a basic type configuration json
cat <<EOF >> type_config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode": "FAIL",
      "Properties": {
        "minBuckets": "1",
        "encryptionAlgorithm": "aws:kms"
      }
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type HOOK \
  --type-name AWSSamples::S3BucketEncrypt::Hook
```

## Example CloudFormation Templates
The following CloudFormation templates demonstrate how this hook will prevent an Amazon S3 bucket without proper encryption from being provisioned.

Fail example - No encryption properties are set for the bucket. 
```
AWSTemplateFormatVersion: "2010-09-09" 
Resources:
  S3Bucket:
    Type: AWS::S3::Bucket 
    Properties: {}
```

Success example 1 - The Amazon S3 bucket encryption properties are set and a KMS key is generated.
```
AWSTemplateFormatVersion: "2010-09-09"
Description: This CloudFormation template provisions an encrypted S3 Bucket
Resources:
  EncryptedS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub 'encryptedbucket-${AWS::Region}-${AWS::AccountId}'
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: 'aws:kms'
              KMSMasterKeyID: !Ref EncryptionKey
            BucketKeyEnabled: true
      Tags: 
        - Key: "keyname1"
          Value: "value1"

  EncryptionKey:  
    Type: AWS::KMS::Key
    Properties:
     Description: KMS key used to encrypt the resource type artifacts
     EnableKeyRotation: true
     KeyPolicy:
      Version: "2012-10-17"
      Statement:
      - Sid: Enable full access for owning account
        Effect: Allow
        Principal: 
          AWS: !Ref "AWS::AccountId"
        Action: kms:*
        Resource: "*"

Outputs:
  EncryptedBucketName:
    Value: !Ref EncryptedS3Bucket

```