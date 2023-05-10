# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass

from cloudformation_cli_python_lib.interface import BaseModel
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

import sys
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class AwsNimblestudioStreamingimage(BaseModel):
    Description: Optional[str]
    Ec2ImageId: Optional[str]
    EncryptionConfiguration: Optional["_StreamingImageEncryptionConfiguration"]
    EulaIds: Optional[Sequence[str]]
    Name: Optional[str]
    Owner: Optional[str]
    Platform: Optional[str]
    StreamingImageId: Optional[str]
    StudioId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNimblestudioStreamingimage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNimblestudioStreamingimage"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            Ec2ImageId=json_data.get("Ec2ImageId"),
            EncryptionConfiguration=StreamingImageEncryptionConfiguration._deserialize(json_data.get("EncryptionConfiguration")),
            EulaIds=json_data.get("EulaIds"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            Platform=json_data.get("Platform"),
            StreamingImageId=json_data.get("StreamingImageId"),
            StudioId=json_data.get("StudioId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNimblestudioStreamingimage = AwsNimblestudioStreamingimage


@dataclass
class StreamingImageEncryptionConfiguration(BaseModel):
    KeyType: Optional[str]
    KeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StreamingImageEncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamingImageEncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            KeyType=json_data.get("KeyType"),
            KeyArn=json_data.get("KeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamingImageEncryptionConfiguration = StreamingImageEncryptionConfiguration


