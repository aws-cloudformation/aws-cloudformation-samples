# AWSSamples::FSxWindowsOnly::Hook

This AWS CloudFormation Hook checks that the type of Amazon FSx file system is WINDOWS. This hook validates that the  `FileSystemType` property of the`AWS::FSx::FileSystem` resource is `WINDOWS`.

Below is a sample CloudFormation template that will trigger the hook.
```
{
    "Resources": {
        "BasicS3LinkedLustreFileSystem": {
            "Type": "AWS::FSx::FileSystem",
            "Properties": {
                "FileSystemType": "LUSTRE",
                "StorageCapacity": 1200,
                "SubnetIds": [
                    {
                        "Fn::ImportValue": "MySubnet01"
                    }
                ],
                "SecurityGroupIds": [
                    {
                        "Fn::ImportValue": "LustreIngressSecurityGroupId"
                    }
                ],
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "CFNs3linkedLustre"
                    }
                ],
                "LustreConfiguration": {
                    "AutoImportPolicy": "NEW",
                    "CopyTagsToBackups": true,
                    "DeploymentType": "PERSISTENT_1",
                    "PerUnitStorageThroughput": 200,
                    "DataCompressionType": "LZ4",
                    "ImportPath": {
                        "Fn::Join": [
                            "",
                            [
                                "s3://",
                                {
                                    "Fn::ImportValue": "LustreCFNS3ImportBucketName"
                                }
                            ]
                        ]
                    },
                    "ExportPath": {
                        "Fn::Join": [
                            "",
                            [
                                "s3://",
                                {
                                    "Fn::ImportValue": "LustreCFNS3ExportPath"
                                }
                            ]
                        ]
                    },
                    "WeeklyMaintenanceStartTime": "2:20:30"
                }
            }
        }
    },
    "Outputs": {
        "FileSystemId": {
            "Value": {
                "Ref": "BasicS3LinkedLustreFileSystem"
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
  --type-name AWSSamples::FSxWindowsOnly::Hook
```
