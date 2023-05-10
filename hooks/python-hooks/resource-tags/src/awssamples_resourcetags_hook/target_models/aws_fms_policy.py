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
class AwsFmsPolicy(BaseModel):
    ExcludeMap: Optional["_IEMap"]
    ExcludeResourceTags: Optional[bool]
    IncludeMap: Optional["_IEMap"]
    Id: Optional[str]
    PolicyName: Optional[str]
    PolicyDescription: Optional[str]
    RemediationEnabled: Optional[bool]
    ResourceTags: Optional[Sequence["_ResourceTag"]]
    ResourceType: Optional[str]
    ResourceTypeList: Optional[Sequence[str]]
    ResourceSetIds: Optional[Sequence[str]]
    SecurityServicePolicyData: Optional["_SecurityServicePolicyData"]
    Arn: Optional[str]
    DeleteAllPolicyResources: Optional[bool]
    ResourcesCleanUp: Optional[bool]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsFmsPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsFmsPolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ExcludeMap=IEMap._deserialize(json_data.get("ExcludeMap")),
            ExcludeResourceTags=json_data.get("ExcludeResourceTags"),
            IncludeMap=IEMap._deserialize(json_data.get("IncludeMap")),
            Id=json_data.get("Id"),
            PolicyName=json_data.get("PolicyName"),
            PolicyDescription=json_data.get("PolicyDescription"),
            RemediationEnabled=json_data.get("RemediationEnabled"),
            ResourceTags=deserialize_list(json_data.get("ResourceTags"), ResourceTag),
            ResourceType=json_data.get("ResourceType"),
            ResourceTypeList=json_data.get("ResourceTypeList"),
            ResourceSetIds=json_data.get("ResourceSetIds"),
            SecurityServicePolicyData=SecurityServicePolicyData._deserialize(json_data.get("SecurityServicePolicyData")),
            Arn=json_data.get("Arn"),
            DeleteAllPolicyResources=json_data.get("DeleteAllPolicyResources"),
            ResourcesCleanUp=json_data.get("ResourcesCleanUp"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsFmsPolicy = AwsFmsPolicy


@dataclass
class IEMap(BaseModel):
    ACCOUNT: Optional[Sequence[str]]
    ORGUNIT: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IEMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IEMap"]:
        if not json_data:
            return None
        return cls(
            ACCOUNT=json_data.get("ACCOUNT"),
            ORGUNIT=json_data.get("ORGUNIT"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IEMap = IEMap


@dataclass
class ResourceTag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceTag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceTag = ResourceTag


@dataclass
class SecurityServicePolicyData(BaseModel):
    ManagedServiceData: Optional[str]
    Type: Optional[str]
    PolicyOption: Optional["_PolicyOption"]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityServicePolicyData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityServicePolicyData"]:
        if not json_data:
            return None
        return cls(
            ManagedServiceData=json_data.get("ManagedServiceData"),
            Type=json_data.get("Type"),
            PolicyOption=PolicyOption._deserialize(json_data.get("PolicyOption")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityServicePolicyData = SecurityServicePolicyData


@dataclass
class PolicyOption(BaseModel):
    NetworkFirewallPolicy: Optional["_NetworkFirewallPolicy"]
    ThirdPartyFirewallPolicy: Optional["_ThirdPartyFirewallPolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyOption"]:
        if not json_data:
            return None
        return cls(
            NetworkFirewallPolicy=NetworkFirewallPolicy._deserialize(json_data.get("NetworkFirewallPolicy")),
            ThirdPartyFirewallPolicy=ThirdPartyFirewallPolicy._deserialize(json_data.get("ThirdPartyFirewallPolicy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyOption = PolicyOption


@dataclass
class NetworkFirewallPolicy(BaseModel):
    FirewallDeploymentModel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFirewallPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFirewallPolicy"]:
        if not json_data:
            return None
        return cls(
            FirewallDeploymentModel=json_data.get("FirewallDeploymentModel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFirewallPolicy = NetworkFirewallPolicy


@dataclass
class ThirdPartyFirewallPolicy(BaseModel):
    FirewallDeploymentModel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThirdPartyFirewallPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThirdPartyFirewallPolicy"]:
        if not json_data:
            return None
        return cls(
            FirewallDeploymentModel=json_data.get("FirewallDeploymentModel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThirdPartyFirewallPolicy = ThirdPartyFirewallPolicy


@dataclass
class PolicyTag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyTag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyTag = PolicyTag


