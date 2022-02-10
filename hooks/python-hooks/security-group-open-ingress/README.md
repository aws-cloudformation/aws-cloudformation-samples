# AWSSamples::SecurityGroupOpenIngress::Hook

This AWS CloudFormation Hook validates that Security Groups do not allow inbound traffic from any address (0.0.0.0/0)

## Configuration

```bash
# Create a basic type configuration json
cat <<EOF > type_config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode":"FAIL",
      "Properties": {}
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type HOOK \
  --type-name AWSSamples::SecurityGroupOpenIngress::Hook
```

## Example templates

Hook will find this non-compliant
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties: 
      GroupDescription: "wide open group"
      SecurityGroupIngress:
      - IpProtocol: -1
        CidrIp: 0.0.0.0/0
```

This will be found as compliant
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties: 
      GroupDescription: "less wide open group"
      SecurityGroupIngress:
      - IpProtocol: -1
        CidrIp: 10.0.0.0/16
```
