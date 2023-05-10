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
class AwsEc2Verifiedaccessgroup(BaseModel):
    VerifiedAccessGroupId: Optional[str]
    VerifiedAccessInstanceId: Optional[str]
    VerifiedAccessGroupArn: Optional[str]
    Owner: Optional[str]
    CreationTime: Optional[str]
    LastUpdatedTime: Optional[str]
    Description: Optional[str]
    PolicyDocument: Optional[str]
    PolicyEnabled: Optional[bool]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Verifiedaccessgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Verifiedaccessgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            VerifiedAccessGroupId=json_data.get("VerifiedAccessGroupId"),
            VerifiedAccessInstanceId=json_data.get("VerifiedAccessInstanceId"),
            VerifiedAccessGroupArn=json_data.get("VerifiedAccessGroupArn"),
            Owner=json_data.get("Owner"),
            CreationTime=json_data.get("CreationTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            Description=json_data.get("Description"),
            PolicyDocument=json_data.get("PolicyDocument"),
            PolicyEnabled=json_data.get("PolicyEnabled"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Verifiedaccessgroup = AwsEc2Verifiedaccessgroup


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


