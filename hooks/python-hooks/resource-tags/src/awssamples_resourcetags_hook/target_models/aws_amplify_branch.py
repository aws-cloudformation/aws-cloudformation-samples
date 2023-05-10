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
class AwsAmplifyBranch(BaseModel):
    AppId: Optional[str]
    Arn: Optional[str]
    BasicAuthConfig: Optional["_BasicAuthConfig"]
    BranchName: Optional[str]
    BuildSpec: Optional[str]
    Description: Optional[str]
    EnableAutoBuild: Optional[bool]
    EnablePerformanceMode: Optional[bool]
    EnablePullRequestPreview: Optional[bool]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariable"]]
    Framework: Optional[str]
    PullRequestEnvironmentName: Optional[str]
    Stage: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAmplifyBranch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAmplifyBranch"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AppId=json_data.get("AppId"),
            Arn=json_data.get("Arn"),
            BasicAuthConfig=BasicAuthConfig._deserialize(json_data.get("BasicAuthConfig")),
            BranchName=json_data.get("BranchName"),
            BuildSpec=json_data.get("BuildSpec"),
            Description=json_data.get("Description"),
            EnableAutoBuild=json_data.get("EnableAutoBuild"),
            EnablePerformanceMode=json_data.get("EnablePerformanceMode"),
            EnablePullRequestPreview=json_data.get("EnablePullRequestPreview"),
            EnvironmentVariables=deserialize_list(json_data.get("EnvironmentVariables"), EnvironmentVariable),
            Framework=json_data.get("Framework"),
            PullRequestEnvironmentName=json_data.get("PullRequestEnvironmentName"),
            Stage=json_data.get("Stage"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAmplifyBranch = AwsAmplifyBranch


@dataclass
class BasicAuthConfig(BaseModel):
    EnableBasicAuth: Optional[bool]
    Username: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BasicAuthConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicAuthConfig"]:
        if not json_data:
            return None
        return cls(
            EnableBasicAuth=json_data.get("EnableBasicAuth"),
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicAuthConfig = BasicAuthConfig


@dataclass
class EnvironmentVariable(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariable"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariable = EnvironmentVariable


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


