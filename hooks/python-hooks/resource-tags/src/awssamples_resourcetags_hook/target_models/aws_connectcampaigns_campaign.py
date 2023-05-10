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
class AwsConnectcampaignsCampaign(BaseModel):
    ConnectInstanceArn: Optional[str]
    DialerConfig: Optional["_DialerConfig"]
    Arn: Optional[str]
    Name: Optional[str]
    OutboundCallConfig: Optional["_OutboundCallConfig"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectcampaignsCampaign"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectcampaignsCampaign"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ConnectInstanceArn=json_data.get("ConnectInstanceArn"),
            DialerConfig=DialerConfig._deserialize(json_data.get("DialerConfig")),
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            OutboundCallConfig=OutboundCallConfig._deserialize(json_data.get("OutboundCallConfig")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectcampaignsCampaign = AwsConnectcampaignsCampaign


@dataclass
class DialerConfig(BaseModel):
    ProgressiveDialerConfig: Optional["_ProgressiveDialerConfig"]
    PredictiveDialerConfig: Optional["_PredictiveDialerConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_DialerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DialerConfig"]:
        if not json_data:
            return None
        return cls(
            ProgressiveDialerConfig=ProgressiveDialerConfig._deserialize(json_data.get("ProgressiveDialerConfig")),
            PredictiveDialerConfig=PredictiveDialerConfig._deserialize(json_data.get("PredictiveDialerConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DialerConfig = DialerConfig


@dataclass
class ProgressiveDialerConfig(BaseModel):
    BandwidthAllocation: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ProgressiveDialerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProgressiveDialerConfig"]:
        if not json_data:
            return None
        return cls(
            BandwidthAllocation=json_data.get("BandwidthAllocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProgressiveDialerConfig = ProgressiveDialerConfig


@dataclass
class PredictiveDialerConfig(BaseModel):
    BandwidthAllocation: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PredictiveDialerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredictiveDialerConfig"]:
        if not json_data:
            return None
        return cls(
            BandwidthAllocation=json_data.get("BandwidthAllocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredictiveDialerConfig = PredictiveDialerConfig


@dataclass
class OutboundCallConfig(BaseModel):
    ConnectContactFlowArn: Optional[str]
    ConnectSourcePhoneNumber: Optional[str]
    ConnectQueueArn: Optional[str]
    AnswerMachineDetectionConfig: Optional["_AnswerMachineDetectionConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_OutboundCallConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutboundCallConfig"]:
        if not json_data:
            return None
        return cls(
            ConnectContactFlowArn=json_data.get("ConnectContactFlowArn"),
            ConnectSourcePhoneNumber=json_data.get("ConnectSourcePhoneNumber"),
            ConnectQueueArn=json_data.get("ConnectQueueArn"),
            AnswerMachineDetectionConfig=AnswerMachineDetectionConfig._deserialize(json_data.get("AnswerMachineDetectionConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutboundCallConfig = OutboundCallConfig


@dataclass
class AnswerMachineDetectionConfig(BaseModel):
    EnableAnswerMachineDetection: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AnswerMachineDetectionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnswerMachineDetectionConfig"]:
        if not json_data:
            return None
        return cls(
            EnableAnswerMachineDetection=json_data.get("EnableAnswerMachineDetection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnswerMachineDetectionConfig = AnswerMachineDetectionConfig


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


