# AWSSamples::IamPoliciesRequireMfa::Hook

This AWS CloudFormation Hook validates that MFA is required on all IAM polices, both standalone and inline in IAM Role definitions. This hook validates that the `aws:MultiFactorAuthPresent` property of the `Bool` Condition is not set to `true`.

Below is sample CloudFormation template that will successfully validate by the hook.
```
Description: Sample template for the AWSSamples::IamPoliciesRequireMfa::Hook resource type that shoud pass

Resources:
  RootRole: 
    Type: "AWS::IAM::Role"
    Properties: 
      AssumeRolePolicyDocument: 
        Version: "2012-10-17"
        Statement: 
          - 
            Effect: "Allow"
            Principal: 
              AWS: 
                - !Sub "arn:aws:iam::${AWS::AccountId}:root"
            Action: 
              - "sts:AssumeRole"
      Path: "/"
      Policies:
        - PolicyName: InlineRootOne
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action: 'dynamodb:*'
                Resource: '*'
                Condition:
                  Bool:
                    "aws:MultiFactorAuthPresent": "true"
        - PolicyName: InlineRootTwo
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action: 'logs:*'
                Resource: '*'
                Condition:
                  Bool:
                    "aws:MultiFactorAuthPresent": "true"

  MyPolicy:
    Type: 'AWS::IAM::Policy'
    Properties:
      PolicyName: ExternalRoot
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Action: 's3:*'
            Resource: '*'
            Condition:
              Bool:
                "aws:MultiFactorAuthPresent": "true"
          - Effect: Allow
            Action: 'ec2:*'
            Resource: '*'
            Condition:
              Bool:
                "aws:MultiFactorAuthPresent": "true"
      Roles:
        - !Ref RootRole
```
Below is sample CloudFromation template that will fail to validate by the hook.
```
AWSTemplateFormatVersion: "2010-09-09"
Description: Sample template for the AWSSamples::IamPoliciesRequireMfa::Hook resource type that shoud fail (no MFA conditions)

Resources:
  RootRole: 
    Type: "AWS::IAM::Role"
    Properties: 
      AssumeRolePolicyDocument: 
        Version: "2012-10-17"
        Statement: 
          - 
            Effect: "Allow"
            Principal: 
              AWS: 
                - !Sub "arn:aws:iam::${AWS::AccountId}:root"
            Action: 
              - "sts:AssumeRole"
      Path: "/"
  MyPolicy:
    Type: 'AWS::IAM::Policy'
    Properties:
      PolicyName: root
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Action: '*'
            Resource: '*'
      Roles:
        - !Ref RootRole
```

Sample configuration

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
  --type-name AWSSamples::IamPoliciesRequireMfa::Hook
```