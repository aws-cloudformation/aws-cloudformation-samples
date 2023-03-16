This AWS CloudFormation Hook validates that encryption is enabled when creating or updating an AWS EFS filesystem. This hook checks if the `Encrypted` property of the `AWS::EFS::FileSystem` resource is not set, or if it is set to `false`.

Below is a sample CloudFormation template that will trigger the hook.
```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "MountTargetVPC": {
            "Type": "AWS::EC2::VPC",
            "Properties": {
                "CidrBlock": "172.31.0.0/16"
            }
        },
        "MountTargetSubnetOne": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "CidrBlock": "172.31.1.0/24",
                "VpcId": {
                    "Ref": "MountTargetVPC"
                },
                "AvailabilityZone": "us-east-1a"
            }
        },
        "MountTargetSubnetTwo": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "CidrBlock": "172.31.2.0/24",
                "VpcId": {
                    "Ref": "MountTargetVPC"
                },
                "AvailabilityZone": "us-east-1b"
            }
        },
        "MountTargetSubnetThree": {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "CidrBlock": "172.31.3.0/24",
                "VpcId": {
                    "Ref": "MountTargetVPC"
                },
                "AvailabilityZone": "us-east-1c
            }
        },
       "FileSystemResource": {
            "Type": "AWS::EFS::FileSystem",
            "Properties": {
                "PerformanceMode": "maxIO",
                "LifecyclePolicies":[
                    {
                        "TransitionToIA" : "AFTER_30_DAYS"
                    }
                ],
                "Encrypted": false,
                "FileSystemTags": [
                    {
                        "Key": "Name",
                        "Value": "TestFileSystem"
                    }
                ],
                "FileSystemPolicy": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": [
                                "elasticfilesystem:ClientMount"
                            ],
                            "Principal":  {"AWS": "arn:aws:iam::111122223333:role/EfsReadOnly"}
                        }
                    ]
                },
                "BackupPolicy": {
                    "Status": "ENABLED"
                    },
                "KmsKeyId": {
                    "Fn::GetAtt": [
                        "key",
                        "Arn"
                    ]
                }
            }
        },
        "key": {
            "Type": "AWS::KMS::Key",
            "Properties": {
                "KeyPolicy": {
                    "Version": "2012-10-17",
                    "Id": "key-default-1",
                    "Statement": [
                        {
                            "Sid": "Allow administration of the key",
                            "Effect": "Allow",
                            "Principal": {
                                "AWS": {
                                    "Fn::Join": [
                                        "",
                                        [
                                            "arn:aws:iam::",
                                            {
                                                "Ref": "AWS::AccountId"
                                            },
                                            ":root"
                                        ]
                                    ]
                                }
                            },
                            "Action": [
                                "kms:*"
                            ],
                            "Resource": "*"
                        }
                    ]
                }
            }
        },
        "MountTargetResource1": {
            "Type": "AWS::EFS::MountTarget",
            "Properties": {
                "FileSystemId": {
                    "Ref": "FileSystemResource"
                },
                "SubnetId": {
                    "Ref": "MountTargetSubnetOne"
                },
                "SecurityGroups": [
                    {
                        "Fn::GetAtt": [
                            "MountTargetVPC",
                            "DefaultSecurityGroup"
                        ]
                    }
                ]
            }
        },
        "MountTargetResource2": {
            "Type": "AWS::EFS::MountTarget",
            "Properties": {
                "FileSystemId": {
                    "Ref": "FileSystemResource"
                },
                "SubnetId": {
                    "Ref": "MountTargetSubnetTwo"
                },
                "SecurityGroups": [
                    {
                        "Fn::GetAtt": [
                            "MountTargetVPC",
                            "DefaultSecurityGroup"
                        ]
                    }
                ]
            }
        },
        "MountTargetResource3": {
            "Type": "AWS::EFS::MountTarget",
            "Properties": {
                "FileSystemId": {
                    "Ref": "FileSystemResource"
                },
                "SubnetId": {
                    "Ref": "MountTargetSubnetThree"
                },
                "SecurityGroups": [
                    {
                        "Fn::GetAtt": [
                            "MountTargetVPC",
                            "DefaultSecurityGroup"
                        ]
                    }
                ]
            }
        },
        "AccessPointResource": {
            "Type": "AWS::EFS::AccessPoint",
            "Properties": {
                "FileSystemId": {
                    "Ref": "FileSystemResource"
                },
                "PosixUser": {
                    "Uid": "13234",
                    "Gid": "1322",
                    "SecondaryGids": [
                        "1344",
                        "1452"
                    ]
                },
                "RootDirectory": {
                    "CreationInfo": {
                        "OwnerGid": "708798",
                        "OwnerUid": "7987987",
                        "Permissions": "0755"
                    },
                    "Path": "/testcfn/abc"
                }
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
  --type-name AWSSamples::EFSEncrypt::Hook
```
