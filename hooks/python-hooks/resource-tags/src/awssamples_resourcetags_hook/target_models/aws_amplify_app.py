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
class AwsAmplifyApp(BaseModel):
    AccessToken: Optional[str]
    AppId: Optional[str]
    AppName: Optional[str]
    Arn: Optional[str]
    AutoBranchCreationConfig: Optional["_AutoBranchCreationConfig"]
    BasicAuthConfig: Optional["_BasicAuthConfig"]
    BuildSpec: Optional[str]
    CustomHeaders: Optional[str]
    CustomRules: Optional[Sequence["_CustomRule"]]
    DefaultDomain: Optional[str]
    Description: Optional[str]
    EnableBranchAutoDeletion: Optional[bool]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariable"]]
    IAMServiceRole: Optional[str]
    Name: Optional[str]
    OauthToken: Optional[str]
    Platform: Optional[str]
    Repository: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAmplifyApp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAmplifyApp"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccessToken=json_data.get("AccessToken"),
            AppId=json_data.get("AppId"),
            AppName=json_data.get("AppName"),
            Arn=json_data.get("Arn"),
            AutoBranchCreationConfig=AutoBranchCreationConfig._deserialize(json_data.get("AutoBranchCreationConfig")),
            BasicAuthConfig=BasicAuthConfig._deserialize(json_data.get("BasicAuthConfig")),
            BuildSpec=json_data.get("BuildSpec"),
            CustomHeaders=json_data.get("CustomHeaders"),
            CustomRules=deserialize_list(json_data.get("CustomRules"), CustomRule),
            DefaultDomain=json_data.get("DefaultDomain"),
            Description=json_data.get("Description"),
            EnableBranchAutoDeletion=json_data.get("EnableBranchAutoDeletion"),
            EnvironmentVariables=deserialize_list(json_data.get("EnvironmentVariables"), EnvironmentVariable),
            IAMServiceRole=json_data.get("IAMServiceRole"),
            Name=json_data.get("Name"),
            OauthToken=json_data.get("OauthToken"),
            Platform=json_data.get("Platform"),
            Repository=json_data.get("Repository"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAmplifyApp = AwsAmplifyApp


@dataclass
class AutoBranchCreationConfig(BaseModel):
    AutoBranchCreationPatterns: Optional[Sequence[str]]
    BasicAuthConfig: Optional["_BasicAuthConfig"]
    BuildSpec: Optional[str]
    EnableAutoBranchCreation: Optional[bool]
    EnableAutoBuild: Optional[bool]
    EnablePerformanceMode: Optional[bool]
    EnablePullRequestPreview: Optional[bool]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariable"]]
    Framework: Optional[str]
    PullRequestEnvironmentName: Optional[str]
    Stage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoBranchCreationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoBranchCreationConfig"]:
        if not json_data:
            return None
        return cls(
            AutoBranchCreationPatterns=json_data.get("AutoBranchCreationPatterns"),
            BasicAuthConfig=BasicAuthConfig._deserialize(json_data.get("BasicAuthConfig")),
            BuildSpec=json_data.get("BuildSpec"),
            EnableAutoBranchCreation=json_data.get("EnableAutoBranchCreation"),
            EnableAutoBuild=json_data.get("EnableAutoBuild"),
            EnablePerformanceMode=json_data.get("EnablePerformanceMode"),
            EnablePullRequestPreview=json_data.get("EnablePullRequestPreview"),
            EnvironmentVariables=deserialize_list(json_data.get("EnvironmentVariables"), EnvironmentVariable),
            Framework=json_data.get("Framework"),
            PullRequestEnvironmentName=json_data.get("PullRequestEnvironmentName"),
            Stage=json_data.get("Stage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoBranchCreationConfig = AutoBranchCreationConfig


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
class CustomRule(BaseModel):
    Condition: Optional[str]
    Status: Optional[str]
    Target: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomRule"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Status=json_data.get("Status"),
            Target=json_data.get("Target"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomRule = CustomRule


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


