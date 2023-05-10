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
class AwsAppconfigDeployment(BaseModel):
    DeploymentStrategyId: Optional[str]
    ConfigurationProfileId: Optional[str]
    EnvironmentId: Optional[str]
    KmsKeyIdentifier: Optional[str]
    Description: Optional[str]
    ConfigurationVersion: Optional[str]
    Id: Optional[str]
    ApplicationId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppconfigDeployment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppconfigDeployment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DeploymentStrategyId=json_data.get("DeploymentStrategyId"),
            ConfigurationProfileId=json_data.get("ConfigurationProfileId"),
            EnvironmentId=json_data.get("EnvironmentId"),
            KmsKeyIdentifier=json_data.get("KmsKeyIdentifier"),
            Description=json_data.get("Description"),
            ConfigurationVersion=json_data.get("ConfigurationVersion"),
            Id=json_data.get("Id"),
            ApplicationId=json_data.get("ApplicationId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppconfigDeployment = AwsAppconfigDeployment


@dataclass
class Tags(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


