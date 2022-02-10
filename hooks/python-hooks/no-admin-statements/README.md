# AWSSamples::IamPolicyDoesNotGiveAdmin::Hook

This example AWS CloudFormation Hook checks whether a PolicyDocument statement with the following attributes is defined within an AWS::IAM::Policy, AWS::IAM::Role, AWS::IAM::Group or AWS::IAM::User resource.
```
  - Effect: Allow
    Action: '*'
    Resource: '*'
```
Please note that this example hook does not attempt to determine if a different statement with equivalent or similar behaviour has been included, and is only intended to demonstrate the CloudFormation hooks capability.  

Below is a sample CloudFormation template that will be passed by the hook:
```
AWSTemplateFormatVersion: "2010-09-09"

Resources:
  UserWithEc2InlinePolicy:
    Type: AWS::IAM::User
    Properties: 
      Policies: 
        - PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action: 'ec2:*'
                Resource: '*'
          PolicyName: test
      UserName: WithInlineEc2Policy
```

Below is a sample CloudFormation template that will be rejected by the hook:
```
AWSTemplateFormatVersion: "2010-09-09"

Resources:
  UserWithAdminInlinePolicy:
    Type: AWS::IAM::User
    Properties: 
      Policies: 
        - PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action: '*'
                Resource: '*'
          PolicyName: test
      UserName: WithInlineAdminPolicy
```

This hook has no required properties.
Sample configuration:

```bash
# Create a basic type configuration json
cat <<EOF >> type_config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode": "FAIL",
      "Properties": {}
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type HOOK \
  --type-name AWSSamples::IamPolicyDoesNotGiveAdmin::Hook
```
