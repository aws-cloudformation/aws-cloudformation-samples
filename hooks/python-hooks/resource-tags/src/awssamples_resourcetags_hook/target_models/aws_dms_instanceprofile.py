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
class AwsDmsInstanceprofile(BaseModel):
    InstanceProfileArn: Optional[str]
    InstanceProfileIdentifier: Optional[str]
    AvailabilityZone: Optional[str]
    Description: Optional[str]
    KmsKeyArn: Optional[str]
    PubliclyAccessible: Optional[bool]
    NetworkType: Optional[str]
    InstanceProfileName: Optional[str]
    InstanceProfileCreationTime: Optional[str]
    SubnetGroupIdentifier: Optional[str]
    VpcSecurityGroups: Optional[AbstractSet[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDmsInstanceprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDmsInstanceprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InstanceProfileArn=json_data.get("InstanceProfileArn"),
            InstanceProfileIdentifier=json_data.get("InstanceProfileIdentifier"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Description=json_data.get("Description"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            NetworkType=json_data.get("NetworkType"),
            InstanceProfileName=json_data.get("InstanceProfileName"),
            InstanceProfileCreationTime=json_data.get("InstanceProfileCreationTime"),
            SubnetGroupIdentifier=json_data.get("SubnetGroupIdentifier"),
            VpcSecurityGroups=set_or_none(json_data.get("VpcSecurityGroups")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDmsInstanceprofile = AwsDmsInstanceprofile


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


