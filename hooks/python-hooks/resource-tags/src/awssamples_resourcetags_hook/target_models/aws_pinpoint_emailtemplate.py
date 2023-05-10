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
class AwsPinpointEmailtemplate(BaseModel):
    HtmlPart: Optional[str]
    TextPart: Optional[str]
    TemplateName: Optional[str]
    TemplateDescription: Optional[str]
    DefaultSubstitutions: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Subject: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPinpointEmailtemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPinpointEmailtemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            HtmlPart=json_data.get("HtmlPart"),
            TextPart=json_data.get("TextPart"),
            TemplateName=json_data.get("TemplateName"),
            TemplateDescription=json_data.get("TemplateDescription"),
            DefaultSubstitutions=json_data.get("DefaultSubstitutions"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Subject=json_data.get("Subject"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPinpointEmailtemplate = AwsPinpointEmailtemplate


