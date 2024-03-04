"""Unit tests mocks for contract_test_inputs_generator."""


from datetime import datetime
from typing import (
    Any,
    Dict,
)
from unittest.mock import MagicMock


LIST_TYPES_PAGINATOR_RESPONSE_MOCK_RESOURCE_TYPE = [
    {
        "TypeSummaries": [
            {
                "Type": "RESOURCE",
                "TypeName": "AWS::MockResourceName::ForUnitTests",
                "DefaultVersionId": MagicMock(),
                "TypeArn": MagicMock(),
                "LastUpdated": datetime.now(),
                "Description": MagicMock(),
                "PublisherId": MagicMock(),
                "OriginalTypeName": MagicMock(),
                "PublicVersionNumber": MagicMock(),
                "LatestPublicVersion": MagicMock(),
                "PublisherIdentity": MagicMock(),
                "PublisherName": MagicMock(),
                "IsActivated": True,
            },
        ],
    },
]

VALID_1_PRE_CREATE_INPUTS: Dict[str, Any] = {
    "resourceProperties": {},
}

VALID_1_PRE_UPDATE_INPUTS: Dict[str, Any] = {
    "resourceProperties": {},
}

VALID_1_PRE_DELETE_INPUTS: Dict[str, Any] = {
    "resourceProperties": {},
}

INVALID_1_PRE_CREATE_INPUTS: Dict[str, Any] = {
    "resourceProperties": {
        "InvalidPropertyKey": "invalid_property_value",
    }
}

INVALID_1_PRE_UPDATE_INPUTS: Dict[str, Any] = {
    "resourceProperties": {
        "InvalidPropertyKey": "invalid_property_value",
    }
}

INVALID_1_PRE_DELETE_INPUTS: Dict[str, Any] = {
    "resourceProperties": {
        "InvalidPropertyKey": "invalid_property_value",
    }
}

VALID_1_PRE_CREATE_FILE_CONTENT: Dict[str, Any] = {
    "AWS::S3::Bucket": {"resourceProperties": {}},
    "AWS::S3::BucketPolicy": {"resourceProperties": {}},
}

VALID_1_PRE_UPDATE_FILE_CONTENT: Dict[str, Any] = {
    "AWS::S3::Bucket": {"resourceProperties": {}},
    "AWS::S3::BucketPolicy": {"resourceProperties": {}},
}

VALID_1_PRE_DELETE_FILE_CONTENT: Dict[str, Any] = {
    "AWS::S3::Bucket": {"resourceProperties": {}},
    "AWS::S3::BucketPolicy": {"resourceProperties": {}},
}

INVALID_1_PRE_CREATE_FILE_CONTENT: Dict[str, Any] = {
    "AWS::S3::Bucket": {
        "resourceProperties": {"InvalidPropertyKey": "invalid_property_value"}
    },
    "AWS::S3::BucketPolicy": {
        "resourceProperties": {"InvalidPropertyKey": "invalid_property_value"}
    },
}

INVALID_1_PRE_UPDATE_FILE_CONTENT: Dict[str, Any] = {
    "AWS::S3::Bucket": {
        "resourceProperties": {"InvalidPropertyKey": "invalid_property_value"}
    },
    "AWS::S3::BucketPolicy": {
        "resourceProperties": {"InvalidPropertyKey": "invalid_property_value"}
    },
}

INVALID_1_PRE_DELETE_FILE_CONTENT: Dict[str, Any] = {
    "AWS::S3::Bucket": {
        "resourceProperties": {"InvalidPropertyKey": "invalid_property_value"}
    },
    "AWS::S3::BucketPolicy": {
        "resourceProperties": {"InvalidPropertyKey": "invalid_property_value"}
    },
}
