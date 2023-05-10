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
    PeerAddress: Optional[str]
    CoreNetworkAddress: Optional[str]
    BgpOptions: Optional["_BgpOptions"]
    InsideCidrBlocks: Optional[Sequence[str]]
    CoreNetworkId: Optional[str]
    ConnectAttachmentId: Optional[str]
    ConnectPeerId: Optional[str]
    EdgeLocation: Optional[str]
    State: Optional[str]
    CreatedAt: Optional[str]
    Configuration: Optional["_ConnectPeerConfiguration"]
    Tags: Optional[Any]

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
            PeerAddress=json_data.get("PeerAddress"),
            CoreNetworkAddress=json_data.get("CoreNetworkAddress"),
            BgpOptions=BgpOptions._deserialize(json_data.get("BgpOptions")),
            InsideCidrBlocks=json_data.get("InsideCidrBlocks"),
            CoreNetworkId=json_data.get("CoreNetworkId"),
            ConnectAttachmentId=json_data.get("ConnectAttachmentId"),
            ConnectPeerId=json_data.get("ConnectPeerId"),
            EdgeLocation=json_data.get("EdgeLocation"),
            State=json_data.get("State"),
            CreatedAt=json_data.get("CreatedAt"),
            Configuration=ConnectPeerConfiguration._deserialize(json_data.get("Configuration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkmanagerConnectpeer = AwsNetworkmanagerConnectpeer


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
class ConnectPeerConfiguration(BaseModel):
    CoreNetworkAddress: Optional[str]
    PeerAddress: Optional[str]
    InsideCidrBlocks: Optional[Sequence[str]]
    Protocol: Optional[str]
    BgpConfigurations: Optional[Sequence["_ConnectPeerBgpConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectPeerConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectPeerConfiguration"]:
        if not json_data:
            return None
        return cls(
            CoreNetworkAddress=json_data.get("CoreNetworkAddress"),
            PeerAddress=json_data.get("PeerAddress"),
            InsideCidrBlocks=json_data.get("InsideCidrBlocks"),
            Protocol=json_data.get("Protocol"),
            BgpConfigurations=deserialize_list(json_data.get("BgpConfigurations"), ConnectPeerBgpConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectPeerConfiguration = ConnectPeerConfiguration


@dataclass
class ConnectPeerBgpConfiguration(BaseModel):
    CoreNetworkAsn: Optional[float]
    PeerAsn: Optional[float]
    CoreNetworkAddress: Optional[str]
    PeerAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectPeerBgpConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectPeerBgpConfiguration"]:
        if not json_data:
            return None
        return cls(
            CoreNetworkAsn=json_data.get("CoreNetworkAsn"),
            PeerAsn=json_data.get("PeerAsn"),
            CoreNetworkAddress=json_data.get("CoreNetworkAddress"),
            PeerAddress=json_data.get("PeerAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectPeerBgpConfiguration = ConnectPeerBgpConfiguration


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


