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
class AwsEc2Volume(BaseModel):
    MultiAttachEnabled: Optional[bool]
    KmsKeyId: Optional[str]
    Encrypted: Optional[bool]
    Size: Optional[int]
    AutoEnableIO: Optional[bool]
    OutpostArn: Optional[str]
    AvailabilityZone: Optional[str]
    Throughput: Optional[int]
    Iops: Optional[int]
    SnapshotId: Optional[str]
    VolumeType: Optional[str]
    VolumeId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Volume"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MultiAttachEnabled=json_data.get("MultiAttachEnabled"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Encrypted=json_data.get("Encrypted"),
            Size=json_data.get("Size"),
            AutoEnableIO=json_data.get("AutoEnableIO"),
            OutpostArn=json_data.get("OutpostArn"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Throughput=json_data.get("Throughput"),
            Iops=json_data.get("Iops"),
            SnapshotId=json_data.get("SnapshotId"),
            VolumeType=json_data.get("VolumeType"),
            VolumeId=json_data.get("VolumeId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Volume = AwsEc2Volume


@dataclass
class Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


