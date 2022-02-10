# AWSSamples::Ec2ImageIdCheckSsm::Hook

This AWS CloudFormation Hook validates EC2 instance resources are using the compliant AMI. The ImageID of the compliant AMI will be stored in a parameter in the AWS Systems
Manager (SSM) Parameter Store.

Create the SSM Parameter Store parameter that will contain the value of the compliant AMI’s ImageID. The ImageID `ami-0e5b6b6a9f3db6db8` represents the Amazon Linux 2 (HVM) (64-bit x86) AMI at the time this sample was written. Sample configuration:

```
aws ssm put-parameter --name "compliant-imageid-x86" --value "ami-
0e5b6b6a9f3db6db8" --type String
```

Below is a sample CloudFormation template that will be passed by the hook:

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Sample template for the AWSSamples::Ec2ImageIdCheckSsm::Hook resource type that should pass (ImageID matches the SSM Parameter store parameter)

Resources:
  EC2InstanceCompliant:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      SecurityGroups: [!Ref 'InstanceSecurityGroup']
      ImageId: ami-0e5b6b6a9f3db6db8
      Tags:
        - Key: Name
          Value: EC2InstanceCompliant
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Empty Security Group
      Tags:
        - Key: Name
          Value: SG-EC2-Empty
```

Below is a sample CloudFormation template that will be rejected by the hook:

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Sample template for the AWSSamples::Ec2ImageIdCheckSsm::Hook resource type that should fail (ImageID does not match the SSM Parameter store parameter)

Resources:
  EC2InstanceNonCompliant:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      SecurityGroups: [!Ref 'InstanceSecurityGroup']
      ImageId: ami-03d5c68bab01f3496
      Tags:
        - Key: Name
          Value: EC2InstanceNonCompliant
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Empty Security Group
      Tags:
        - Key: Name
          Value: SG-EC2-Empty
```

This hook has one required property, `SsmKey` which references the SSM parameter that has the ImageId of the compliant AMI. For this sample we will use `compliant-imageid-x86` for the `SsmKey` based on the parameter created previously. Sample configuration:


Sample configuration

```bash
# Create a basic type configuration json
cat <<EOF >> type_config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode": "FAIL",
      "Properties": {
        "SsmKey": "compliant-imageid-x86"
      }
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type HOOK \
  --type-name AWSSamples::Ec2ImageIdCheckSsm::Hook
```
