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
class AwsOmicsWorkflow(BaseModel):
    Arn: Optional[str]
    CreationTime: Optional[str]
    DefinitionUri: Optional[str]
    Description: Optional[str]
    Engine: Optional[str]
    Id: Optional[str]
    Main: Optional[str]
    Name: Optional[str]
    ParameterTemplate: Optional[MutableMapping[str, "_WorkflowParameter"]]
    Status: Optional[str]
    StorageCapacity: Optional[float]
    Tags: Optional[Any]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOmicsWorkflow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOmicsWorkflow"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CreationTime=json_data.get("CreationTime"),
            DefinitionUri=json_data.get("DefinitionUri"),
            Description=json_data.get("Description"),
            Engine=json_data.get("Engine"),
            Id=json_data.get("Id"),
            Main=json_data.get("Main"),
            Name=json_data.get("Name"),
            ParameterTemplate=json_data.get("ParameterTemplate"),
            Status=json_data.get("Status"),
            StorageCapacity=json_data.get("StorageCapacity"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOmicsWorkflow = AwsOmicsWorkflow


@dataclass
class WorkflowParameter(BaseModel):
    Description: Optional[str]
    Optional: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowParameter"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Optional=json_data.get("Optional"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowParameter = WorkflowParameter


