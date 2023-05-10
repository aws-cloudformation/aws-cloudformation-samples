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
class AwsElasticbeanstalkEnvironment(BaseModel):
    PlatformArn: Optional[str]
    ApplicationName: Optional[str]
    Description: Optional[str]
    EnvironmentName: Optional[str]
    OperationsRole: Optional[str]
    Tier: Optional["_Tier"]
    VersionLabel: Optional[str]
    EndpointURL: Optional[str]
    OptionSettings: Optional[Sequence["_OptionSetting"]]
    TemplateName: Optional[str]
    SolutionStackName: Optional[str]
    CNAMEPrefix: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticbeanstalkEnvironment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticbeanstalkEnvironment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PlatformArn=json_data.get("PlatformArn"),
            ApplicationName=json_data.get("ApplicationName"),
            Description=json_data.get("Description"),
            EnvironmentName=json_data.get("EnvironmentName"),
            OperationsRole=json_data.get("OperationsRole"),
            Tier=Tier._deserialize(json_data.get("Tier")),
            VersionLabel=json_data.get("VersionLabel"),
            EndpointURL=json_data.get("EndpointURL"),
            OptionSettings=deserialize_list(json_data.get("OptionSettings"), OptionSetting),
            TemplateName=json_data.get("TemplateName"),
            SolutionStackName=json_data.get("SolutionStackName"),
            CNAMEPrefix=json_data.get("CNAMEPrefix"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticbeanstalkEnvironment = AwsElasticbeanstalkEnvironment


@dataclass
class Tier(BaseModel):
    Type: Optional[str]
    Version: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tier"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tier = Tier


@dataclass
class OptionSetting(BaseModel):
    ResourceName: Optional[str]
    Value: Optional[str]
    Namespace: Optional[str]
    OptionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionSetting"]:
        if not json_data:
            return None
        return cls(
            ResourceName=json_data.get("ResourceName"),
            Value=json_data.get("Value"),
            Namespace=json_data.get("Namespace"),
            OptionName=json_data.get("OptionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionSetting = OptionSetting


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


