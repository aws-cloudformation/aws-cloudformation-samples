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
class AwsPcaconnectoradConnector(BaseModel):
    CertificateAuthorityArn: Optional[str]
    ConnectorArn: Optional[str]
    DirectoryId: Optional[str]
    Tags: Optional[Any]
    VpcInformation: Optional["_VpcInformation"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPcaconnectoradConnector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPcaconnectoradConnector"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CertificateAuthorityArn=json_data.get("CertificateAuthorityArn"),
            ConnectorArn=json_data.get("ConnectorArn"),
            DirectoryId=json_data.get("DirectoryId"),
            Tags=json_data.get("Tags"),
            VpcInformation=VpcInformation._deserialize(json_data.get("VpcInformation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPcaconnectoradConnector = AwsPcaconnectoradConnector


@dataclass
class VpcInformation(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcInformation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcInformation"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcInformation = VpcInformation


