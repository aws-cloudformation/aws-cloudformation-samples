# AWSSamples::Devtools::Devinstance

An example resource schema demonstrating some basic constructs and validation rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AWSSamples::Devtools::Devinstance",
    "Properties" : {
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Integer</i>,
        "<a href="#keypair" title="Keypair">Keypair</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: AWSSamples::Devtools::Devinstance
Properties:
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#disksize" title="DiskSize">DiskSize</a>: <i>Integer</i>
    <a href="#keypair" title="Keypair">Keypair</a>: <i>String</i>
</pre>

## Properties

#### InstanceType

The EC2 Instance Type of developer instance. You can only select instance types that support hibernation

_Required_: No

_Type_: String

_Allowed Values_: <code>c4.large</code> | <code>c4.xlarge</code> | <code>c4.2xlarge</code> | <code>c4.4xlarge</code> | <code>c4.8xlarge</code> | <code>c5.large</code> | <code>c5.xlarge</code> | <code>c5.2xlarge</code> | <code>c5.4xlarge</code> | <code>c5.9xlarge</code> | <code>c5.12xlarge</code> | <code>c5.18xlarge</code> | <code>m4.large</code> | <code>m4.xlarge</code> | <code>m4.2xlarge</code> | <code>m4.4xlarge</code> | <code>m5.large</code> | <code>m5.xlarge</code> | <code>m5.2xlarge</code> | <code>m5.4xlarge</code> | <code>m5.8xlarge</code> | <code>r4.large</code> | <code>r4.xlarge</code> | <code>r4.2xlarge</code> | <code>r4.4xlarge</code> | <code>r5.large</code> | <code>r5.xlarge</code> | <code>r5.2xlarge</code> | <code>r5.4xlarge</code> | <code>t2.nano</code> | <code>t2.micro</code> | <code>t2.small</code> | <code>t2.medium</code> | <code>t2.large</code> | <code>t2.xlarge</code> | <code>t2.2xlarge</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

The persistent disk size in Gibibytes

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keypair

The name of the SSH keypair to connect to your dev environment

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the UID.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### UID

The ID of the developer instance

#### SSH

The SSH URI for your dev environment

