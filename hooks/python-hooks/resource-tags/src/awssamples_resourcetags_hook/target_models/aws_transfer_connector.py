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
class AwsTransferConnector(BaseModel):
    AccessRole: Optional[str]
    As2Config: Optional["_As2Config"]
    Arn: Optional[str]
    ConnectorId: Optional[str]
    LoggingRole: Optional[str]
    Tags: Optional[Any]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsTransferConnector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsTransferConnector"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccessRole=json_data.get("AccessRole"),
            As2Config=As2Config._deserialize(json_data.get("As2Config")),
            Arn=json_data.get("Arn"),
            ConnectorId=json_data.get("ConnectorId"),
            LoggingRole=json_data.get("LoggingRole"),
            Tags=json_data.get("Tags"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsTransferConnector = AwsTransferConnector


@dataclass
class As2Config(BaseModel):
    LocalProfileId: Optional[str]
    PartnerProfileId: Optional[str]
    MessageSubject: Optional[str]
    Compression: Optional[str]
    EncryptionAlgorithm: Optional[str]
    SigningAlgorithm: Optional[str]
    MdnSigningAlgorithm: Optional[str]
    MdnResponse: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_As2Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_As2Config"]:
        if not json_data:
            return None
        return cls(
            LocalProfileId=json_data.get("LocalProfileId"),
            PartnerProfileId=json_data.get("PartnerProfileId"),
            MessageSubject=json_data.get("MessageSubject"),
            Compression=json_data.get("Compression"),
            EncryptionAlgorithm=json_data.get("EncryptionAlgorithm"),
            SigningAlgorithm=json_data.get("SigningAlgorithm"),
            MdnSigningAlgorithm=json_data.get("MdnSigningAlgorithm"),
            MdnResponse=json_data.get("MdnResponse"),
        )


# work around possible type aliasing issues when variable has same name as a model
_As2Config = As2Config


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


