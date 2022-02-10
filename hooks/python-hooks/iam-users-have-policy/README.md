# AWSSamples::IamUsersHavePolicy::Hook

This AWS CloudFormation Hook validates that an IAM User has an assigned policy when created and when updated. 

* When creating a resource, this hook validates that at least one of the  `Policies`  and/or `ManagedPolicyArns` properties of the`AWS::IAM::User` resource is present.

* When updating a resource, this hook determines whether the existing resource has an assigned inline or managed policy.  If the resource does already have a policy assigned, it validates that at least one of the  `Policies`  and/or `ManagedPolicyArns` properties of the updated `AWS::IAM::User` resource is present.  If the existing resource does not already have a policy or managed policy ARN assigned, the hook does not enforce that one is added.

Below is sample CloudFormation template that will successfully be validated by the hook:
```
AWSTemplateFormatVersion: "2010-09-09"

Resources:
  UserWithPolicy:
    Type: AWS::IAM::User
    Properties: 
      Policies: 
        - PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Deny
                Action:
                  - '*'
                Resource: '*'
          PolicyName: test
      UserName: WithPolicy

  UserWithManagedPolicy:
    Type: AWS::IAM::User
    Properties: 
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AWSDenyAll
      UserName: WithManagedPolicy
```

Below is a sample CloudFormation template that will be rejected by the hook:
```
AWSTemplateFormatVersion: "2010-09-09"

Resources:
  
  UserWithNoPolicies:
    Type: AWS::IAM::User
    Properties: 
      UserName: NoPolicies
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
  --type-name AWSSamples::IamUsersHavePolicy::Hook
```
