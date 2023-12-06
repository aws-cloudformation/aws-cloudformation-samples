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
class AwsElasticacheServerlesscache(BaseModel):
    ServerlessCacheName: Optional[str]
    Description: Optional[str]
    Engine: Optional[str]
    MajorEngineVersion: Optional[str]
    FullEngineVersion: Optional[str]
    CacheUsageLimits: Optional["_CacheUsageLimits"]
    KmsKeyId: Optional[str]
    SecurityGroupIds: Optional[AbstractSet[str]]
    SnapshotArnsToRestore: Optional[AbstractSet[str]]
    Tags: Optional[Any]
    UserGroupId: Optional[str]
    SubnetIds: Optional[AbstractSet[str]]
    SnapshotRetentionLimit: Optional[int]
    DailySnapshotTime: Optional[str]
    CreateTime: Optional[str]
    Status: Optional[str]
    Endpoint: Optional["_Endpoint"]
    ReaderEndpoint: Optional["_Endpoint"]
    ARN: Optional[str]
    FinalSnapshotName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticacheServerlesscache"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticacheServerlesscache"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ServerlessCacheName=json_data.get("ServerlessCacheName"),
            Description=json_data.get("Description"),
            Engine=json_data.get("Engine"),
            MajorEngineVersion=json_data.get("MajorEngineVersion"),
            FullEngineVersion=json_data.get("FullEngineVersion"),
            CacheUsageLimits=CacheUsageLimits._deserialize(json_data.get("CacheUsageLimits")),
            KmsKeyId=json_data.get("KmsKeyId"),
            SecurityGroupIds=set_or_none(json_data.get("SecurityGroupIds")),
            SnapshotArnsToRestore=set_or_none(json_data.get("SnapshotArnsToRestore")),
            Tags=json_data.get("Tags"),
            UserGroupId=json_data.get("UserGroupId"),
            SubnetIds=set_or_none(json_data.get("SubnetIds")),
            SnapshotRetentionLimit=json_data.get("SnapshotRetentionLimit"),
            DailySnapshotTime=json_data.get("DailySnapshotTime"),
            CreateTime=json_data.get("CreateTime"),
            Status=json_data.get("Status"),
            Endpoint=Endpoint._deserialize(json_data.get("Endpoint")),
            ReaderEndpoint=Endpoint._deserialize(json_data.get("ReaderEndpoint")),
            ARN=json_data.get("ARN"),
            FinalSnapshotName=json_data.get("FinalSnapshotName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticacheServerlesscache = AwsElasticacheServerlesscache


@dataclass
class CacheUsageLimits(BaseModel):
    DataStorage: Optional["_DataStorage"]
    ECPUPerSecond: Optional["_ECPUPerSecond"]

    @classmethod
    def _deserialize(
        cls: Type["_CacheUsageLimits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheUsageLimits"]:
        if not json_data:
            return None
        return cls(
            DataStorage=DataStorage._deserialize(json_data.get("DataStorage")),
            ECPUPerSecond=ECPUPerSecond._deserialize(json_data.get("ECPUPerSecond")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheUsageLimits = CacheUsageLimits


@dataclass
class DataStorage(BaseModel):
    Maximum: Optional[int]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataStorage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataStorage"]:
        if not json_data:
            return None
        return cls(
            Maximum=json_data.get("Maximum"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataStorage = DataStorage


@dataclass
class ECPUPerSecond(BaseModel):
    Maximum: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ECPUPerSecond"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ECPUPerSecond"]:
        if not json_data:
            return None
        return cls(
            Maximum=json_data.get("Maximum"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ECPUPerSecond = ECPUPerSecond


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


@dataclass
class Endpoint(BaseModel):
    Address: Optional[str]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Endpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Endpoint"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Endpoint = Endpoint


