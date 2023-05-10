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
class AwsIotfleetwiseDecodermanifest(BaseModel):
    Arn: Optional[str]
    CreationTime: Optional[str]
    Description: Optional[str]
    LastModificationTime: Optional[str]
    ModelManifestArn: Optional[str]
    Name: Optional[str]
    NetworkInterfaces: Optional[Sequence[Any]]
    SignalDecoders: Optional[Sequence[Any]]
    Status: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotfleetwiseDecodermanifest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotfleetwiseDecodermanifest"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CreationTime=json_data.get("CreationTime"),
            Description=json_data.get("Description"),
            LastModificationTime=json_data.get("LastModificationTime"),
            ModelManifestArn=json_data.get("ModelManifestArn"),
            Name=json_data.get("Name"),
            NetworkInterfaces=json_data.get("NetworkInterfaces"),
            SignalDecoders=json_data.get("SignalDecoders"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotfleetwiseDecodermanifest = AwsIotfleetwiseDecodermanifest


@dataclass
class CanNetworkInterface(BaseModel):
    InterfaceId: Optional[str]
    Type: Optional[str]
    CanInterface: Optional["_CanInterface"]

    @classmethod
    def _deserialize(
        cls: Type["_CanNetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CanNetworkInterface"]:
        if not json_data:
            return None
        return cls(
            InterfaceId=json_data.get("InterfaceId"),
            Type=json_data.get("Type"),
            CanInterface=CanInterface._deserialize(json_data.get("CanInterface")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CanNetworkInterface = CanNetworkInterface


@dataclass
class CanInterface(BaseModel):
    Name: Optional[str]
    ProtocolName: Optional[str]
    ProtocolVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CanInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CanInterface"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ProtocolName=json_data.get("ProtocolName"),
            ProtocolVersion=json_data.get("ProtocolVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CanInterface = CanInterface


@dataclass
class ObdNetworkInterface(BaseModel):
    InterfaceId: Optional[str]
    Type: Optional[str]
    ObdInterface: Optional["_ObdInterface"]

    @classmethod
    def _deserialize(
        cls: Type["_ObdNetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObdNetworkInterface"]:
        if not json_data:
            return None
        return cls(
            InterfaceId=json_data.get("InterfaceId"),
            Type=json_data.get("Type"),
            ObdInterface=ObdInterface._deserialize(json_data.get("ObdInterface")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObdNetworkInterface = ObdNetworkInterface


@dataclass
class ObdInterface(BaseModel):
    Name: Optional[str]
    RequestMessageId: Optional[Any]
    ObdStandard: Optional[str]
    PidRequestIntervalSeconds: Optional[Any]
    DtcRequestIntervalSeconds: Optional[Any]
    UseExtendedIds: Optional[Any]
    HasTransmissionEcu: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_ObdInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObdInterface"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RequestMessageId=json_data.get("RequestMessageId"),
            ObdStandard=json_data.get("ObdStandard"),
            PidRequestIntervalSeconds=json_data.get("PidRequestIntervalSeconds"),
            DtcRequestIntervalSeconds=json_data.get("DtcRequestIntervalSeconds"),
            UseExtendedIds=json_data.get("UseExtendedIds"),
            HasTransmissionEcu=json_data.get("HasTransmissionEcu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObdInterface = ObdInterface


@dataclass
class CanSignalDecoder(BaseModel):
    FullyQualifiedName: Optional[str]
    Type: Optional[str]
    InterfaceId: Optional[str]
    CanSignal: Optional["_CanSignal"]

    @classmethod
    def _deserialize(
        cls: Type["_CanSignalDecoder"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CanSignalDecoder"]:
        if not json_data:
            return None
        return cls(
            FullyQualifiedName=json_data.get("FullyQualifiedName"),
            Type=json_data.get("Type"),
            InterfaceId=json_data.get("InterfaceId"),
            CanSignal=CanSignal._deserialize(json_data.get("CanSignal")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CanSignalDecoder = CanSignalDecoder


@dataclass
class CanSignal(BaseModel):
    MessageId: Optional[Any]
    IsBigEndian: Optional[Any]
    IsSigned: Optional[Any]
    StartBit: Optional[Any]
    Offset: Optional[Any]
    Factor: Optional[Any]
    Length: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CanSignal"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CanSignal"]:
        if not json_data:
            return None
        return cls(
            MessageId=json_data.get("MessageId"),
            IsBigEndian=json_data.get("IsBigEndian"),
            IsSigned=json_data.get("IsSigned"),
            StartBit=json_data.get("StartBit"),
            Offset=json_data.get("Offset"),
            Factor=json_data.get("Factor"),
            Length=json_data.get("Length"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CanSignal = CanSignal


@dataclass
class ObdSignalDecoder(BaseModel):
    FullyQualifiedName: Optional[str]
    Type: Optional[str]
    InterfaceId: Optional[str]
    ObdSignal: Optional["_ObdSignal"]

    @classmethod
    def _deserialize(
        cls: Type["_ObdSignalDecoder"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObdSignalDecoder"]:
        if not json_data:
            return None
        return cls(
            FullyQualifiedName=json_data.get("FullyQualifiedName"),
            Type=json_data.get("Type"),
            InterfaceId=json_data.get("InterfaceId"),
            ObdSignal=ObdSignal._deserialize(json_data.get("ObdSignal")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObdSignalDecoder = ObdSignalDecoder


@dataclass
class ObdSignal(BaseModel):
    PidResponseLength: Optional[Any]
    ServiceMode: Optional[Any]
    Pid: Optional[Any]
    Scaling: Optional[Any]
    Offset: Optional[Any]
    StartByte: Optional[Any]
    ByteLength: Optional[Any]
    BitRightShift: Optional[Any]
    BitMaskLength: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_ObdSignal"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObdSignal"]:
        if not json_data:
            return None
        return cls(
            PidResponseLength=json_data.get("PidResponseLength"),
            ServiceMode=json_data.get("ServiceMode"),
            Pid=json_data.get("Pid"),
            Scaling=json_data.get("Scaling"),
            Offset=json_data.get("Offset"),
            StartByte=json_data.get("StartByte"),
            ByteLength=json_data.get("ByteLength"),
            BitRightShift=json_data.get("BitRightShift"),
            BitMaskLength=json_data.get("BitMaskLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObdSignal = ObdSignal


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


