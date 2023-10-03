# AWSSamples::Ec2SsmSmOnly::Hook

This AWS CloudFormation Hook validates that an EC2 instance to be deployed, can only be accessed using [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html). 

The Hook currently checks [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) and [AWS::EC2::LaunchTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html) resource types. Instances deploed via [AWS::AutoScaling::LaunchConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html) are not currently checked. 

### Validation Overview ###
The validation consists of the following high-level steps:
1. Ensure the instance has a [IamInstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-iaminstanceprofile) assigned
2. Simulate the [IamInstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-iaminstanceprofile) role to ensure it 'Allows' the following permissions:
    * `ssmmessages:CreateControlChannel`
    * `ssmmessages:CreateDataChannel`
    * `ssmmessages:OpenControlChannel`
    * `ssmmessages:OpenDataChannel`

3. Verify none of the instance security groups allow ingress on 22/SSH if a Linux instance or 3389/RDP if a Windows instance. 
    
    Security Groups are checked depending on how specified for the instance:
    * `SecurityGroupIds` property (non-default VPC)
    * `SecurityGroups` property (EC2-Classic, default VPC)
    * `NetworkInterfaces` property

### Requiring KMS Encrypted SSM Sessions
The hook can enforce KMS key encryption of SSM Session data by requiring the instance [IamInstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-iaminstanceprofile) role to include the `kms:decrypt` permission. You can control this by setting the `requireSessionManagerEncryption` property in the Hook Configuration JSON as shown below. 

<pre>
{
    "CloudFormationConfiguration": {
        "HookConfiguration": {
            "TargetStacks": "ALL",
            "FailureMode": "FAIL",
            "Properties": {
                <b>"requireSessionManagerEncryption": true</b>
            }
        }
    }
}
</pre>
See [Defining the account-level configuration of an extension](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html#resource-type-howto-configuration) in the *CloudFormation CLI User Guide*. 

### Testing

An AWS CloudFormation template is provided in the `testing` folder to exercise various failure use-cases by manipulating the provided template parameters:

* `IncludeInstanceProfile: (True|False)`

  Set to `False` to remove the [IamInstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-iaminstanceprofile) property which should result in an `IamInstanceProfile property missing or empty value` error

* `ManagedOrManualIAMPolicy (Managed|Manual)`

  Set to `Managed` to generate the [IamInstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-iaminstanceprofile) role policy using the `arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore` IAM Managed policy.

  Set to `Manual` to generate the [IamInstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-iaminstanceprofile) role policy using an inline policy containing the required SSM Session Manager permissions
* `TestIllegalManualSSMPolicies (True|False)`

  Set to `True` to omit the `ssmmessages:OpenControlChannel` permission from the policy which should result in an `ssmmessages:OpenControlChannel: Implicit Deny` error

* `IncludeExplicitSecurityGroup (True|False)`

  Set to `True` to include a Security Group for the instance that does not reference port 22/SSH

* `IncludeExplicitSSHSecurityGroup (True|False)`

  Set to `True` to include a Security Group for the instance that does includes an ingress rule for 22/SSH. This should result in an `Security Group contains an SSH ingress rule` error

* `UseProvidedDefaultVpcValues (True|False)`

  Set to `False` to have the template create a custom VPC and Subnet, and deploy the instance into it

  Set to `True` to deploy the instance into the *default* VPC and Subnet you provide using the `DefaultVpc` and `DefaultVpcSubnetId` parameters. 

* `IncludeSSMKMS (True|False)`

  Set to 'True' to have the template generate an KMS key and reference it with the `kms:decrypt` action in the IAMInstanceRole. 

  If `requireSessionManagerEncryption` property in the Hook Configuration is set to `True` and you set `IncludeSSMKMS` to `False`, you should get a `kms:decrypt: Implicit Deny` error

> **IMPORTANT**

> During a stack update, if a dependant property of the instance is changed, the hook will not be called. This means its possible during a stack update, to bypass the validation checks such as adding an 22/SSH ingress rule to the instances' referenced Security Group. 