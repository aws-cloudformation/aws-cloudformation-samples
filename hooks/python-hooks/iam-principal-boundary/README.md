# AWSSamples::IAMPrincipalBoundary::Hook

This AWS CloudFormation Hook checks for IAM Principals (Roles or Users) to determine if a specific PermissionsBoundary must be specified during CREATE or UPDATE actions on the stack.

You can use this hook to ensure that a specific PermissionsBoundary is specified for IAM Principals, while also excluding a set of principals from the PermissionsBoundary requirement by using the `excludedPrincipalSuffixes` property. The configuration properties for this hook's settings are below.  
```
{
    "properties": {
        "iamPrincipalBoundaryArn": {
            "description": "The ARN that must be attached as an IAM Principal",
            "type": "string"
        },
        "excludedPrincipalSuffixes": {
            "description": "A comma separated list of principal names that should be excluded from the boundary. Each name provided will be matched using starts-with logic.",
            "type": "string"
        }
    }
}
```

## Subscribe to the hook
The following is an example that shows how you can subscribe to the hook. In this example, we are requiring that all IAM Principals have a specific `s3_deny_permissions_boundary` specified while excluding any IAM Principals that start with the name `iam-excluded` or `excluded`.

```bash
# Create a basic type configuration json
cat <<EOF >> type_config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode": "FAIL",
      "Properties": {
          "iamPrincipalBoundaryArn": "arn:aws:iam::555555555555:policy/s3_deny_permissions_boundary", 
          "excludedPrincipalSuffixes": "excluded,iam-excluded,test-excluded-user"
      }
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type HOOK \
  --type-name AWSSamples::IAMPrincipalBoundary::Hook
```

## Example CloudFormation Templates
The following CloudFormation templates demonstrate how this hook can be used using the above type configuration.

Fail example 1 - role name is not excluded and the permissions boundary specified is incorrect.
```
Resources:
  IAMRoleTest:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub 'iam-not-excluded-cfn-hooks-${AWS::StackName}-${AWS::AccountId}'
      PermissionsBoundary: 'arn:aws:iam::555555555555:policy/invalid_s3_deny_permissions_boundary'
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Action: sts:AssumeRole
            Effect: Allow
            Principal:
              Service: codepipeline.amazonaws.com
        
```

Fail example 2 - role name is auto-generated based on the stack name and it does not have the permissions boundary specified
```
Resources:
  IAMRoleTest:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Action: sts:AssumeRole
            Effect: Allow
            Principal:
              Service: codepipeline.amazonaws.com
```

Success example 1 - Permissions boundary is specified
```
Resources:
  IAMRoleTest:
    Type: AWS::IAM::Role
    Properties:
      PermissionsBoundary: 'arn:aws:iam::555555555555:policy/s3_deny_permissions_boundary'
      RoleName: !Sub 'cfn-hooks-pass-${AWS::AccountId}'
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Action: sts:AssumeRole
            Effect: Allow
            Principal:
              Service: codepipeline.amazonaws.com
```

Success example 2 - Role name is excluded from requiring the permissions boundary
```
Resources:
  IAMRoleTest:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub 'excluded-cfn-hooks-${AWS::StackName}-${AWS::AccountId}'
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Action: sts:AssumeRole
            Effect: Allow
            Principal:
              Service: codepipeline.amazonaws.com
```
Success example 3 - User name is excluded from requiring the permissions boundary
```
Resources:
  IAMUserTest:
    Type: AWS::IAM::User
    Properties:
      UserName: !Sub 'excluded-cfn-hooks-${AWS::StackName}-${AWS::AccountId}'
```
