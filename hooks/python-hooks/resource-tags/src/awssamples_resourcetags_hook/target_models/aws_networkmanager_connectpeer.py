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
class AwsNetworkmanagerConnectpeer(BaseModel):
    ConnectAttachmentId: Optional[str]
    CoreNetworkId: Optional[str]
    Configuration: Optional["_ConnectPeerConfiguration"]
    CreatedAt: Optional[str]
    CoreNetworkAddress: Optional[str]
    BgpOptions: Optional["_BgpOptions"]
    ConnectPeerId: Optional[str]
    PeerAddress: Optional[str]
    State: Optional[str]
    InsideCidrBlocks: Optional[Sequence[str]]
    Tags: Optional[Any]
    EdgeLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNetworkmanagerConnectpeer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNetworkmanagerConnectpeer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ConnectAttachmentId=json_data.get("ConnectAttachmentId"),
            CoreNetworkId=json_data.get("CoreNetworkId"),
            Configuration=ConnectPeerConfiguration._deserialize(json_data.get("Configuration")),
            CreatedAt=json_data.get("CreatedAt"),
            CoreNetworkAddress=json_data.get("CoreNetworkAddress"),
            BgpOptions=BgpOptions._deserialize(json_data.get("BgpOptions")),
            ConnectPeerId=json_data.get("ConnectPeerId"),
            PeerAddress=json_data.get("PeerAddress"),
            State=json_data.get("State"),
            InsideCidrBlocks=json_data.get("InsideCidrBlocks"),
            Tags=json_data.get("Tags"),
            EdgeLocation=json_data.get("EdgeLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkmanagerConnectpeer = AwsNetworkmanagerConnectpeer


@dataclass
class ConnectPeerConfiguration(BaseModel):
    BgpConfigurations: Optional[Sequence["_ConnectPeerBgpConfiguration"]]
    PeerAddress: Optional[str]
    CoreNetworkAddress: Optional[str]
    InsideCidrBlocks: Optional[Sequence[str]]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectPeerConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectPeerConfiguration"]:
        if not json_data:
            return None
        return cls(
            BgpConfigurations=deserialize_list(json_data.get("BgpConfigurations"), ConnectPeerBgpConfiguration),
            PeerAddress=json_data.get("PeerAddress"),
            CoreNetworkAddress=json_data.get("CoreNetworkAddress"),
            InsideCidrBlocks=json_data.get("InsideCidrBlocks"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectPeerConfiguration = ConnectPeerConfiguration


@dataclass
class ConnectPeerBgpConfiguration(BaseModel):
    PeerAddress: Optional[str]
    CoreNetworkAddress: Optional[str]
    PeerAsn: Optional[float]
    CoreNetworkAsn: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectPeerBgpConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectPeerBgpConfiguration"]:
        if not json_data:
            return None
        return cls(
            PeerAddress=json_data.get("PeerAddress"),
            CoreNetworkAddress=json_data.get("CoreNetworkAddress"),
            PeerAsn=json_data.get("PeerAsn"),
            CoreNetworkAsn=json_data.get("CoreNetworkAsn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectPeerBgpConfiguration = ConnectPeerBgpConfiguration


@dataclass
class BgpOptions(BaseModel):
    PeerAsn: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BgpOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BgpOptions"]:
        if not json_data:
            return None
        return cls(
            PeerAsn=json_data.get("PeerAsn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BgpOptions = BgpOptions


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


