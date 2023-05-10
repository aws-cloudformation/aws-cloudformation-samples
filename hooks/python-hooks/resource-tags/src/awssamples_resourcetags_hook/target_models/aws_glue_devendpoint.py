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
class AwsGlueDevendpoint(BaseModel):
    ExtraJarsS3Path: Optional[str]
    PublicKey: Optional[str]
    NumberOfNodes: Optional[int]
    Arguments: Optional[MutableMapping[str, Any]]
    SubnetId: Optional[str]
    PublicKeys: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]
    RoleArn: Optional[str]
    WorkerType: Optional[str]
    EndpointName: Optional[str]
    GlueVersion: Optional[str]
    ExtraPythonLibsS3Path: Optional[str]
    SecurityConfiguration: Optional[str]
    Id: Optional[str]
    NumberOfWorkers: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueDevendpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueDevendpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ExtraJarsS3Path=json_data.get("ExtraJarsS3Path"),
            PublicKey=json_data.get("PublicKey"),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            Arguments=json_data.get("Arguments"),
            SubnetId=json_data.get("SubnetId"),
            PublicKeys=json_data.get("PublicKeys"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            RoleArn=json_data.get("RoleArn"),
            WorkerType=json_data.get("WorkerType"),
            EndpointName=json_data.get("EndpointName"),
            GlueVersion=json_data.get("GlueVersion"),
            ExtraPythonLibsS3Path=json_data.get("ExtraPythonLibsS3Path"),
            SecurityConfiguration=json_data.get("SecurityConfiguration"),
            Id=json_data.get("Id"),
            NumberOfWorkers=json_data.get("NumberOfWorkers"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueDevendpoint = AwsGlueDevendpoint


