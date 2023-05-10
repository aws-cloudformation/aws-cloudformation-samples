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
class AwsWisdomAssistantassociation(BaseModel):
    AssistantAssociationArn: Optional[str]
    AssistantArn: Optional[str]
    AssistantAssociationId: Optional[str]
    AssistantId: Optional[str]
    Association: Optional["_AssociationData"]
    AssociationType: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWisdomAssistantassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWisdomAssistantassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AssistantAssociationArn=json_data.get("AssistantAssociationArn"),
            AssistantArn=json_data.get("AssistantArn"),
            AssistantAssociationId=json_data.get("AssistantAssociationId"),
            AssistantId=json_data.get("AssistantId"),
            Association=AssociationData._deserialize(json_data.get("Association")),
            AssociationType=json_data.get("AssociationType"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWisdomAssistantassociation = AwsWisdomAssistantassociation


@dataclass
class AssociationData(BaseModel):
    KnowledgeBaseId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssociationData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssociationData"]:
        if not json_data:
            return None
        return cls(
            KnowledgeBaseId=json_data.get("KnowledgeBaseId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssociationData = AssociationData


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


