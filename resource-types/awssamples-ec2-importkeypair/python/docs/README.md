# AWSSamples::EC2::ImportKeyPair

Sample resource schema demonstrating a model for an example resource type to import a key pair.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "AWSSamples::EC2::ImportKeyPair",
    "Properties" : {
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#publickeymaterial" title="PublicKeyMaterial">PublicKeyMaterial</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: AWSSamples::EC2::ImportKeyPair
Properties:
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#publickeymaterial" title="PublicKeyMaterial">PublicKeyMaterial</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tag.md">Tag</a></i>
</pre>

## Properties

#### KeyName

The name of the key is a mandatory element.

_Required_: Yes

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>255</code>

_Pattern_: <code>^[\x00-\x7F]{1,255}$</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### PublicKeyMaterial

The public key material is a mandatory element.

_Required_: Yes

_Type_: String

_Minimum_: <code>1</code>

_Pattern_: <code>^ssh-[a-z0-9-]+ AAAA[a-zA-Z0-9\+\/]+=*( .*)?$</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Tags

An array of key-value pairs to apply to the resource.

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the KeyPairId.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### KeyPairId

A Key Pair ID is automatically generated on creation and is assigned as the unique identifier.

#### KeyFingerprint

The MD5 public key fingerprint of the imported key.

#### KeyType

The type of the key pair.

