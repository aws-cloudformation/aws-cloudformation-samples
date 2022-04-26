"""Mocks for unit tests described in the test_handlers.py file."""

import datetime
from typing import (
    Any,
    Dict,
)
from unittest.mock import MagicMock

WITH_NO_PROPERTIES: Dict[str, Dict[Any, Any]] = {"resourceProperties": {}}

WITH_NO_TAGS = {
    "resourceProperties": {
        "BucketEncryption": {
            "ServerSideEncryptionConfiguration": [
                {"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}
            ]
        },
        "VersioningConfiguration": {"Status": "Enabled"},
    },
    "previousResourceProperties": None,
}

TARGET_NAME_NOT_SUPPORTED = "AWS::EC2::EIPAssociation"
TARGET_TYPE_NOT_SUPPORTED = "AWS::EC2::EIPAssociation"

TAGS_IS_ARRAY = {
    "resourceProperties": {
        "BucketEncryption": {
            "ServerSideEncryptionConfiguration": [
                {"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}
            ]
        },
        "VersioningConfiguration": {"Status": "Enabled"},
        "Tags": [
            {"Key": "Name", "Value": "ExampleName"},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
    },
    "previousResourceProperties": None,
}

TAGS_IS_OBJECT = {
    "resourceProperties": {
        "Type": "String",
        "Description": "Example SSM parameter.",
        "Value": "test",
        "Tags": {"Name": "ExampleName", "AppName": "ExampleAppName"},
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_MISSING_REQUIRED_KEY = {
    "resourceProperties": {
        "BucketEncryption": {
            "ServerSideEncryptionConfiguration": [
                {"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}
            ]
        },
        "VersioningConfiguration": {"Status": "Enabled"},
        "Tags": [
            {"Key": "MissingNameKey", "Value": "ExampleName"},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
    },
    "previousResourceProperties": None,
}

TAGS_IS_OBJECT_MISSING_REQUIRED_KEY = {
    "resourceProperties": {
        "Type": "String",
        "Description": "Example SSM parameter.",
        "Value": "test",
        "Tags": {"AppName": "ExampleAppName", "MissingNameKey": "ExampleName"},
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_MISSING_REQUIRED_KEYS = {
    "resourceProperties": {
        "BucketEncryption": {
            "ServerSideEncryptionConfiguration": [
                {"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}
            ]
        },
        "VersioningConfiguration": {"Status": "Enabled"},
        "Tags": [
            {"Key": "MissingNameKey", "Value": "ExampleName"},
            {"Key": "MissingAppNameKey", "Value": "ExampleAppName"},
        ],
    },
    "previousResourceProperties": None,
}

TAGS_IS_OBJECT_MISSING_REQUIRED_KEYS = {
    "resourceProperties": {
        "Type": "String",
        "Description": "Example SSM parameter.",
        "Value": "test",
        "Tags": {
            "MissingAppNamekey": "ExampleAppName",
            "MissingNameKey": "ExampleName",
        },
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_MISSING_VALUE = {
    "resourceProperties": {
        "BucketEncryption": {
            "ServerSideEncryptionConfiguration": [
                {"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}
            ]
        },
        "VersioningConfiguration": {"Status": "Enabled"},
        "Tags": [
            {"Key": "Name", "Value": "ExampleName"},
            {"Key": "AppName", "Value": ""},
        ],
    },
    "previousResourceProperties": None,
}

TAGS_IS_OBJECT_MISSING_VALUE = {
    "resourceProperties": {
        "Type": "String",
        "Description": "Example SSM parameter.",
        "Value": "test",
        "Tags": {"AppName": "", "Name": "ExampleName"},
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_MISSING_VALUES = {
    "resourceProperties": {
        "BucketEncryption": {
            "ServerSideEncryptionConfiguration": [
                {"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}
            ]
        },
        "VersioningConfiguration": {"Status": "Enabled"},
        "Tags": [
            {"Key": "Name", "Value": ""},
            {"Key": "AppName", "Value": ""},
        ],
    },
    "previousResourceProperties": None,
}

TAGS_IS_OBJECT_MISSING_VALUES = {
    "resourceProperties": {
        "Type": "String",
        "Description": "Example SSM parameter.",
        "Value": "test",
        "Tags": {"AppName": "", "Name": ""},
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_PROPERTIES = {
    "resourceProperties": {
        "DataPrivacy": MagicMock(),
        "IdleSessionTTLInSeconds": 60,
        "Name": "test",
        "RoleArn": MagicMock(),
        "BotTags": [
            {"Key": "Name", "Value": "ExampleName"},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
        "TestBotAliasTags": [
            {"Key": "Name", "Value": "ExampleName"},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_PROPERTIES_MISSING_REQUIRED_KEY = {
    "resourceProperties": {
        "DataPrivacy": MagicMock(),
        "IdleSessionTTLInSeconds": 60,
        "Name": "test",
        "RoleArn": MagicMock(),
        "BotTags": [
            {"Key": "Name", "Value": "ExampleName"},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
        "TestBotAliasTags": [
            {"Key": "MissingNameKey", "Value": "ExampleName"},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_PROPERTIES_MISSING_VALUE = {
    "resourceProperties": {
        "DataPrivacy": MagicMock(),
        "IdleSessionTTLInSeconds": 60,
        "Name": "test",
        "RoleArn": MagicMock(),
        "BotTags": [
            {"Key": "Name", "Value": ""},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
        "TestBotAliasTags": [
            {"Key": "Name", "Value": ""},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_PROPERTIES_MISSING_TAG_PROPERTIES = {
    "resourceProperties": {
        "DataPrivacy": MagicMock(),
        "IdleSessionTTLInSeconds": 60,
        "Name": "test",
        "RoleArn": MagicMock(),
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_PROPERTIES_MISSING_TAG_PROPERTY = {
    "resourceProperties": {
        "DataPrivacy": MagicMock(),
        "IdleSessionTTLInSeconds": 60,
        "Name": "test",
        "RoleArn": MagicMock(),
        "TestBotAliasTags": [
            {"Key": "Name", "Value": "ExampleName"},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
    },
    "previousResourceProperties": None,
}

TAGSPECIFICATIONS = {
    "resourceProperties": {
        "LaunchTemplateName": "ExampleLaunchTemplate",
        "LaunchTemplateData": {"InstanceType": "t2.micro"},
        "TagSpecifications": [
            {
                "ResourceType": "launch-template",
                "Tags": [
                    {"Key": "Name", "Value": "ExampleName"},
                    {"Key": "AppName", "Value": "ExampleAppName"},
                ],
            }
        ],
    },
    "previousResourceProperties": None,
}

TAGSPECIFICATIONS_MISSING_REQUIRED_KEY = {
    "resourceProperties": {
        "LaunchTemplateName": "ExampleLaunchTemplate",
        "LaunchTemplateData": {"InstanceType": "t2.micro"},
        "TagSpecifications": [
            {
                "ResourceType": "launch-template",
                "Tags": [
                    {"Key": "MissingNameKey", "Value": "ExampleName"},
                    {"Key": "AppName", "Value": "ExampleAppName"},
                ],
            }
        ],
    },
    "previousResourceProperties": None,
}

TAGSPECIFICATIONS_MISSING_VALUE = {
    "resourceProperties": {
        "LaunchTemplateName": "ExampleLaunchTemplate",
        "LaunchTemplateData": {"InstanceType": "t2.micro"},
        "TagSpecifications": [
            {
                "ResourceType": "launch-template",
                "Tags": [
                    {"Key": "Name", "Value": "ExampleName"},
                    {"Key": "AppName", "Value": ""},
                ],
            }
        ],
    },
    "previousResourceProperties": None,
}

TAGSPECIFICATIONS_MISSING_TAGS_PROPERTY = {
    "resourceProperties": {
        "LaunchTemplateName": "ExampleLaunchTemplate",
        "LaunchTemplateData": {"InstanceType": "t2.micro"},
        "TagSpecifications": [
            {
                "ResourceType": "launch-template",
            }
        ],
    },
    "previousResourceProperties": None,
}

TAGSPECIFICATIONS_MISSING_TAGSPECIFICATION = {
    "resourceProperties": {
        "LaunchTemplateName": "ExampleLaunchTemplate",
        "LaunchTemplateData": {"InstanceType": "t2.micro"},
        "TagSpecifications": [],
    },
    "previousResourceProperties": None,
}

STACK_TAGS_TEST_CASES = {
    "resourceProperties": {
        "BucketEncryption": {
            "ServerSideEncryptionConfiguration": [
                {"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}
            ]
        },
        "VersioningConfiguration": {"Status": "Enabled"},
    },
    "previousResourceProperties": None,
}

DESCRIBE_STACKS_API_MOCK = (
    "test-stack",
    {
        "Stacks": [
            {
                "StackName": "test-stack",
                "CreationTime": datetime.datetime(2022, 3, 18),
                "StackStatus": "CREATE_COMPLETE",
                "Tags": [{"Key": "Name", "Value": "string"}],
            },
        ],
    },
)

ALLOWED_TAG_VALUES_TESTS = {
    "resourceProperties": {
        "BucketEncryption": {
            "ServerSideEncryptionConfiguration": [
                {"ServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}
            ]
        },
        "VersioningConfiguration": {"Status": "Enabled"},
        "Tags": [
            {"Key": "Name", "Value": "ExampleName"},
            {"Key": "AppName", "Value": "ExampleAppName"},
            {"Key": "Env", "Value": "dev"},
            {"Key": "Team", "Value": "Team1"},
        ],
    },
    "previousResourceProperties": None,
}

RESOURCE_TAGS_ADD_CHAR_ESCAPE_TESTS = {
    "resourceProperties": {
        "LaunchTemplateName": "ExampleLaunchTemplate",
        "LaunchTemplateData": {"InstanceType": "t2.micro"},
        "TagSpecifications": [
            {
                "ResourceType": "launch-template",
                "Tags": [
                    {"Key": "K,1", "Value": "V,1"},
                    {"Key": "K=2", "Value": "V=2"},
                    {"Key": "K|3", "Value": "V|3"},
                ],
            }
        ],
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_AUTOSCALING_GROUP_PROPAGATE_AT_LAUNCH_TRUE = {
    "resourceProperties": {
        "MinSize": "0",
        "MaxSize": "1",
        "DesiredCapacity": "1",
        "LaunchTemplate": {
            "LaunchTemplateId": {"Ref": "ExampleLaunchTemplate"},
            "Version": {"Ref": "ExampleLaunchTemplateVersionNumber"},
        },
        "VPCZoneIdentifier": {"Ref": "ExampleSubnets"},
        "Tags": [
            {
                "Key": "Name",
                "Value": "ExampleName",
                "PropagateAtLaunch": "true",
            },
            {
                "Key": "AppName",
                "Value": "ExampleAppName",
                "PropagateAtLaunch": True,
            },
        ],
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_AUTOSCALING_GROUP_PROPAGATE_AT_LAUNCH_FALSE = {
    "resourceProperties": {
        "MinSize": "0",
        "MaxSize": "1",
        "DesiredCapacity": "1",
        "LaunchTemplate": {
            "LaunchTemplateId": {"Ref": "ExampleLaunchTemplate"},
            "Version": {"Ref": "ExampleLaunchTemplateVersionNumber"},
        },
        "VPCZoneIdentifier": {"Ref": "ExampleSubnets"},
        "Tags": [
            {
                "Key": "Name",
                "Value": "ExampleName",
                "PropagateAtLaunch": "false",
            },
            {
                "Key": "AppName",
                "Value": "ExampleAppName",
                "PropagateAtLaunch": False,
            },
        ],
    },
    "previousResourceProperties": None,
}

TAGS_IS_ARRAY_AUTOSCALING_GROUP_PROPAGATE_AT_LAUNCH_MISSING = {
    "resourceProperties": {
        "MinSize": "0",
        "MaxSize": "1",
        "DesiredCapacity": "1",
        "LaunchTemplate": {
            "LaunchTemplateId": {"Ref": "ExampleLaunchTemplate"},
            "Version": {"Ref": "ExampleLaunchTemplateVersionNumber"},
        },
        "VPCZoneIdentifier": {"Ref": "ExampleSubnets"},
        "Tags": [
            {"Key": "Name", "Value": "ExampleName"},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
    },
    "previousResourceProperties": None,
}

TAG_PROPAGATION_BOOLEAN_TRUE = {
    "resourceProperties": {
        "Type": "container",
        "JobDefinitionName": MagicMock(),
        "ContainerProperties": {
            "MountPoints": [
                {
                    "ReadOnly": False,
                    "SourceVolume": MagicMock(),
                    "ContainerPath": MagicMock(),
                }
            ],
            "Volumes": [
                {
                    "Host": {
                        "SourcePath": MagicMock(),
                    },
                    "Name": MagicMock(),
                }
            ],
            "Command": [
                MagicMock(),
            ],
            "Memory": 2000,
            "Privileged": True,
            "JobRoleArn": "String",
            "ReadonlyRootFilesystem": True,
            "Vcpus": 2,
            "Image": MagicMock(),
        },
        "Tags": {"Name": "ExampleName", "AppName": "ExampleAppName"},
        "PropagateTags": True,
    }
}

TAG_PROPAGATION_BOOLEAN_FALSE = {
    "resourceProperties": {
        "Type": "container",
        "JobDefinitionName": MagicMock(),
        "ContainerProperties": {
            "MountPoints": [
                {
                    "ReadOnly": False,
                    "SourceVolume": MagicMock(),
                    "ContainerPath": MagicMock(),
                }
            ],
            "Volumes": [
                {
                    "Host": {
                        "SourcePath": MagicMock(),
                    },
                    "Name": MagicMock(),
                }
            ],
            "Command": [
                MagicMock(),
            ],
            "Memory": 2000,
            "Privileged": True,
            "JobRoleArn": "String",
            "ReadonlyRootFilesystem": True,
            "Vcpus": 2,
            "Image": MagicMock(),
        },
        "Tags": {"Name": "ExampleName", "AppName": "ExampleAppName"},
        "PropagateTags": False,
    }
}

TAG_PROPAGATION_STRING_TRUE = {
    "resourceProperties": {
        "Type": "container",
        "JobDefinitionName": MagicMock(),
        "ContainerProperties": {
            "MountPoints": [
                {
                    "ReadOnly": False,
                    "SourceVolume": MagicMock(),
                    "ContainerPath": MagicMock(),
                }
            ],
            "Volumes": [
                {
                    "Host": {
                        "SourcePath": MagicMock(),
                    },
                    "Name": MagicMock(),
                }
            ],
            "Command": [
                MagicMock(),
            ],
            "Memory": 2000,
            "Privileged": True,
            "JobRoleArn": "String",
            "ReadonlyRootFilesystem": True,
            "Vcpus": 2,
            "Image": MagicMock(),
        },
        "Tags": {"Name": "ExampleName", "AppName": "ExampleAppName"},
        "PropagateTags": "true",
    }
}

TAG_PROPAGATION_STRING_FALSE = {
    "resourceProperties": {
        "Type": "container",
        "JobDefinitionName": MagicMock(),
        "ContainerProperties": {
            "MountPoints": [
                {
                    "ReadOnly": False,
                    "SourceVolume": MagicMock(),
                    "ContainerPath": MagicMock(),
                }
            ],
            "Volumes": [
                {
                    "Host": {
                        "SourcePath": MagicMock(),
                    },
                    "Name": MagicMock(),
                }
            ],
            "Command": [
                MagicMock(),
            ],
            "Memory": 2000,
            "Privileged": True,
            "JobRoleArn": "String",
            "ReadonlyRootFilesystem": True,
            "Vcpus": 2,
            "Image": MagicMock(),
        },
        "Tags": {"Name": "ExampleName", "AppName": "ExampleAppName"},
        "PropagateTags": "false",
    }
}

TAG_PROPAGATION_MISSING = {
    "resourceProperties": {
        "Type": "container",
        "JobDefinitionName": MagicMock(),
        "ContainerProperties": {
            "MountPoints": [
                {
                    "ReadOnly": False,
                    "SourceVolume": MagicMock(),
                    "ContainerPath": MagicMock(),
                }
            ],
            "Volumes": [
                {
                    "Host": {
                        "SourcePath": MagicMock(),
                    },
                    "Name": MagicMock(),
                }
            ],
            "Command": [
                MagicMock(),
            ],
            "Memory": 2000,
            "Privileged": True,
            "JobRoleArn": "String",
            "ReadonlyRootFilesystem": True,
            "Vcpus": 2,
            "Image": MagicMock(),
        },
        "Tags": {"Name": "ExampleName", "AppName": "ExampleAppName"},
    }
}

TAG_PROPAGATION_VALID_STRING = {
    "resourceProperties": {
        "Cluster": MagicMock(),
        "DesiredCount": 1,
        "TaskDefinition": MagicMock(),
        "Tags": [
            {"Key": "Name", "Value": "ExampleName"},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
        "PropagateTags": "SERVICE",
    }
}

TAG_PROPAGATION_INVALID_STRING = {
    "resourceProperties": {
        "Cluster": MagicMock(),
        "DesiredCount": 1,
        "TaskDefinition": MagicMock(),
        "Tags": [
            {"Key": "Name", "Value": "ExampleName"},
            {"Key": "AppName", "Value": "ExampleAppName"},
        ],
        "PropagateTags": "INVALID_VALUE",
    }
}
