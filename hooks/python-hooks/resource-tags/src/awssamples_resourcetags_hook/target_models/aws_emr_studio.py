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
class AwsEmrStudio(BaseModel):
    Arn: Optional[str]
    AuthMode: Optional[str]
    DefaultS3Location: Optional[str]
    Description: Optional[str]
    EngineSecurityGroupId: Optional[str]
    Name: Optional[str]
    ServiceRole: Optional[str]
    StudioId: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Any]
    Url: Optional[str]
    UserRole: Optional[str]
    VpcId: Optional[str]
    WorkspaceSecurityGroupId: Optional[str]
    IdpAuthUrl: Optional[str]
    IdpRelayStateParameterName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEmrStudio"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEmrStudio"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AuthMode=json_data.get("AuthMode"),
            DefaultS3Location=json_data.get("DefaultS3Location"),
            Description=json_data.get("Description"),
            EngineSecurityGroupId=json_data.get("EngineSecurityGroupId"),
            Name=json_data.get("Name"),
            ServiceRole=json_data.get("ServiceRole"),
            StudioId=json_data.get("StudioId"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            Url=json_data.get("Url"),
            UserRole=json_data.get("UserRole"),
            VpcId=json_data.get("VpcId"),
            WorkspaceSecurityGroupId=json_data.get("WorkspaceSecurityGroupId"),
            IdpAuthUrl=json_data.get("IdpAuthUrl"),
            IdpRelayStateParameterName=json_data.get("IdpRelayStateParameterName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEmrStudio = AwsEmrStudio


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


