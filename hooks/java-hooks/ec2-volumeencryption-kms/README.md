# AWSSamples::Ec2VolumeEncryptionKms::Hook

This AWS CloudFormation Hook validates that any EC2 Volume has encryption configured and set to the compliant KMS key.

Below is a sample CloudFormation template that will be passed by the hook, please update `Your-KmsKeyId`:

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Sample template for the AWSSamples::Ec2VolumeEncryptionKms::Hook resource type that should pass (KMS Key ID matches the KmsKeyId property set in the type configuration of the hook)

Resources:
  EC2VolumeEncrypted:
    Type: AWS::EC2::Volume
    Properties:
      Encrypted: true
      KmsKeyId: Your-KmsKeyId
      AvailabilityZone: us-west-2a
      Size: 1
```

Below is a sample CloudFormation template that will be rejected by the hook:

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Sample template for the AWSSamples::Ec2VolumeEncryptionKms::Hook resource type that should not pass (KMS Key ID does not match the KmsKeyId property set in the type configuration of the hook)

Resources:
  EC2VolumeEncrypted:
    Type: AWS::EC2::Volume
    Properties:
      Encrypted: true
      KmsKeyId: Not-Your-KmsKeyId
      AvailabilityZone: us-west-2a
      Size: 1
```

This hook has one required property, `KmsKeyId` which references the KMS KeyId of the compliant KMS Key. Sample configuration below, please update `Your-KmsKeyId`, and `Your-Hook-ARN`:

```bash
# Create a basic type configuration json
cat <<EOF >> type_config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode": "FAIL",
      "Properties": {
        "KmsKeyId": "Your-KmsKeyId"
      }
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type HOOK \
  --type-name AWSSamples::Ec2VolumeEncryptionKms::Hook
```
