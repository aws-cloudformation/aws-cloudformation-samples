# AWSSamples::EksClusterLogging::Hook

Validates that EKS clusters have audit and authentication logging enabled.

## Configuration

```bash
# Create a basic type configuration json
cat <<EOF > type_config.json
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
  --type-name AWSSamples::EksClusterLogging::Hook
```

## Example templates

Hook will find this non-compliant
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  EksCluster:
    Type: AWS::EKS::Cluster
    Properties: 
      RoleArn: "<MY_EKS_SERVICE_ROLE_ARN>"
      ResourcesVpcConfig:
        SubnetIds: ["<MY_SUBNET_ID>"]
```

This will be found as compliant
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  EksCluster:
    Type: AWS::EKS::Cluster
    Properties: 
      RoleArn: "<MY_EKS_SERVICE_ROLE_ARN>"
      ResourcesVpcConfig:
        SubnetIds: ["<MY_SUBNET_ID>"]
      Logging: 
        ClusterLogging: 
          EnabledTypes:
          - {Type: audit}
          - {Type: authenticator}
```
