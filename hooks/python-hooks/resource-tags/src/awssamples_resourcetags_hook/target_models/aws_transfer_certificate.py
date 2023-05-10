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
class AwsTransferCertificate(BaseModel):
    Usage: Optional[str]
    Certificate: Optional[str]
    CertificateChain: Optional[str]
    PrivateKey: Optional[str]
    ActiveDate: Optional[str]
    InactiveDate: Optional[str]
    Description: Optional[str]
    Tags: Optional[Any]
    Arn: Optional[str]
    CertificateId: Optional[str]
    Status: Optional[str]
    Type: Optional[str]
    Serial: Optional[str]
    NotBeforeDate: Optional[str]
    NotAfterDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsTransferCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsTransferCertificate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Usage=json_data.get("Usage"),
            Certificate=json_data.get("Certificate"),
            CertificateChain=json_data.get("CertificateChain"),
            PrivateKey=json_data.get("PrivateKey"),
            ActiveDate=json_data.get("ActiveDate"),
            InactiveDate=json_data.get("InactiveDate"),
            Description=json_data.get("Description"),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
            CertificateId=json_data.get("CertificateId"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            Serial=json_data.get("Serial"),
            NotBeforeDate=json_data.get("NotBeforeDate"),
            NotAfterDate=json_data.get("NotAfterDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsTransferCertificate = AwsTransferCertificate


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


