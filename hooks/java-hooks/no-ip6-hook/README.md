# AWSSamples::NoIP6::Hook

This AWS CloudFormation Hook validates that IPv6 is not enabled when creating or updating a VPC Subnet. This hook validates that the  `AssignIpv6AddressOnCreation` property of the`AWS::EC2::Subnet` resource is not set to `True`.

Below is sample CloudFromation template that will trigger the hook.
```
{
    "Resources": {
        "mySubnet": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "VpcId": {
                    "Ref": "myVPC"
                },
                "CidrBlock": "10.0.0.0/24",
                "AvailabilityZone": "us-east-1a",
                "AssignIpv6AddressOnCreation": true,
                "Tags": [
                    {
                        "Key": "stack",
                        "Value": "production"
                    }
                ]
            }
        }
    }
}
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
  --type-name AWSSamples::NoIP6::Hook
```




