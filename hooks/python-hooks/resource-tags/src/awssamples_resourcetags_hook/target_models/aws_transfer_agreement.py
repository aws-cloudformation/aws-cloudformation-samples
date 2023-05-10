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
class AwsTransferAgreement(BaseModel):
    Description: Optional[str]
    ServerId: Optional[str]
    LocalProfileId: Optional[str]
    PartnerProfileId: Optional[str]
    BaseDirectory: Optional[str]
    AccessRole: Optional[str]
    Status: Optional[str]
    Tags: Optional[Any]
    AgreementId: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsTransferAgreement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsTransferAgreement"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            ServerId=json_data.get("ServerId"),
            LocalProfileId=json_data.get("LocalProfileId"),
            PartnerProfileId=json_data.get("PartnerProfileId"),
            BaseDirectory=json_data.get("BaseDirectory"),
            AccessRole=json_data.get("AccessRole"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            AgreementId=json_data.get("AgreementId"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsTransferAgreement = AwsTransferAgreement


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


