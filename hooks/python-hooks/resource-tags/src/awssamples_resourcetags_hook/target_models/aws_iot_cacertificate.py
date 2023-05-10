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
class AwsIotCacertificate(BaseModel):
    CACertificatePem: Optional[str]
    VerificationCertificatePem: Optional[str]
    Status: Optional[str]
    CertificateMode: Optional[str]
    AutoRegistrationStatus: Optional[str]
    RemoveAutoRegistration: Optional[bool]
    RegistrationConfig: Optional["_RegistrationConfig"]
    Id: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotCacertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotCacertificate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CACertificatePem=json_data.get("CACertificatePem"),
            VerificationCertificatePem=json_data.get("VerificationCertificatePem"),
            Status=json_data.get("Status"),
            CertificateMode=json_data.get("CertificateMode"),
            AutoRegistrationStatus=json_data.get("AutoRegistrationStatus"),
            RemoveAutoRegistration=json_data.get("RemoveAutoRegistration"),
            RegistrationConfig=RegistrationConfig._deserialize(json_data.get("RegistrationConfig")),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotCacertificate = AwsIotCacertificate


@dataclass
class RegistrationConfig(BaseModel):
    TemplateBody: Optional[str]
    RoleArn: Optional[str]
    TemplateName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegistrationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegistrationConfig"]:
        if not json_data:
            return None
        return cls(
            TemplateBody=json_data.get("TemplateBody"),
            RoleArn=json_data.get("RoleArn"),
            TemplateName=json_data.get("TemplateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegistrationConfig = RegistrationConfig


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


