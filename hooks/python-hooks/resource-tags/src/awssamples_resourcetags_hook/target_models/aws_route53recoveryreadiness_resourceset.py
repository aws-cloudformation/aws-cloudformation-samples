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
class AwsRoute53recoveryreadinessResourceset(BaseModel):
    ResourceSetName: Optional[str]
    Resources: Optional[Sequence["_Resource"]]
    ResourceSetArn: Optional[str]
    ResourceSetType: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53recoveryreadinessResourceset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53recoveryreadinessResourceset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ResourceSetName=json_data.get("ResourceSetName"),
            Resources=deserialize_list(json_data.get("Resources"), Resource),
            ResourceSetArn=json_data.get("ResourceSetArn"),
            ResourceSetType=json_data.get("ResourceSetType"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53recoveryreadinessResourceset = AwsRoute53recoveryreadinessResourceset


@dataclass
class Resource(BaseModel):
    ResourceArn: Optional[str]
    ComponentId: Optional[str]
    DnsTargetResource: Optional["_DNSTargetResource"]
    ReadinessScopes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Resource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Resource"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
            ComponentId=json_data.get("ComponentId"),
            DnsTargetResource=DNSTargetResource._deserialize(json_data.get("DnsTargetResource")),
            ReadinessScopes=json_data.get("ReadinessScopes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Resource = Resource


@dataclass
class DNSTargetResource(BaseModel):
    DomainName: Optional[str]
    RecordSetId: Optional[str]
    HostedZoneArn: Optional[str]
    RecordType: Optional[str]
    TargetResource: Optional["_TargetResource"]

    @classmethod
    def _deserialize(
        cls: Type["_DNSTargetResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DNSTargetResource"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            RecordSetId=json_data.get("RecordSetId"),
            HostedZoneArn=json_data.get("HostedZoneArn"),
            RecordType=json_data.get("RecordType"),
            TargetResource=TargetResource._deserialize(json_data.get("TargetResource")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DNSTargetResource = DNSTargetResource


@dataclass
class TargetResource(BaseModel):
    NLBResource: Optional["_NLBResource"]
    R53Resource: Optional["_R53ResourceRecord"]

    @classmethod
    def _deserialize(
        cls: Type["_TargetResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetResource"]:
        if not json_data:
            return None
        return cls(
            NLBResource=NLBResource._deserialize(json_data.get("NLBResource")),
            R53Resource=R53ResourceRecord._deserialize(json_data.get("R53Resource")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetResource = TargetResource


@dataclass
class NLBResource(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NLBResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NLBResource"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NLBResource = NLBResource


@dataclass
class R53ResourceRecord(BaseModel):
    DomainName: Optional[str]
    RecordSetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_R53ResourceRecord"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_R53ResourceRecord"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            RecordSetId=json_data.get("RecordSetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_R53ResourceRecord = R53ResourceRecord


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


