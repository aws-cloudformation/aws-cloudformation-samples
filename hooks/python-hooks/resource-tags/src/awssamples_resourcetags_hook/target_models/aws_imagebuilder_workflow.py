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
class AwsImagebuilderWorkflow(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Version: Optional[str]
    Description: Optional[str]
    ChangeDescription: Optional[str]
    Type: Optional[str]
    Data: Optional[str]
    Uri: Optional[str]
    KmsKeyId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsImagebuilderWorkflow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsImagebuilderWorkflow"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
            Description=json_data.get("Description"),
            ChangeDescription=json_data.get("ChangeDescription"),
            Type=json_data.get("Type"),
            Data=json_data.get("Data"),
            Uri=json_data.get("Uri"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsImagebuilderWorkflow = AwsImagebuilderWorkflow


