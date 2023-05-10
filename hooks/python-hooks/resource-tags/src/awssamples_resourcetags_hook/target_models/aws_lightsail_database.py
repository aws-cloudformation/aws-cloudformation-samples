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
class AwsLightsailDatabase(BaseModel):
    RelationalDatabaseName: Optional[str]
    DatabaseArn: Optional[str]
    AvailabilityZone: Optional[str]
    RelationalDatabaseBlueprintId: Optional[str]
    RelationalDatabaseBundleId: Optional[str]
    MasterDatabaseName: Optional[str]
    MasterUsername: Optional[str]
    MasterUserPassword: Optional[str]
    PreferredBackupWindow: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    PubliclyAccessible: Optional[bool]
    CaCertificateIdentifier: Optional[str]
    BackupRetention: Optional[bool]
    RotateMasterUserPassword: Optional[bool]
    RelationalDatabaseParameters: Optional[AbstractSet["_RelationalDatabaseParameter"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLightsailDatabase"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLightsailDatabase"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RelationalDatabaseName=json_data.get("RelationalDatabaseName"),
            DatabaseArn=json_data.get("DatabaseArn"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            RelationalDatabaseBlueprintId=json_data.get("RelationalDatabaseBlueprintId"),
            RelationalDatabaseBundleId=json_data.get("RelationalDatabaseBundleId"),
            MasterDatabaseName=json_data.get("MasterDatabaseName"),
            MasterUsername=json_data.get("MasterUsername"),
            MasterUserPassword=json_data.get("MasterUserPassword"),
            PreferredBackupWindow=json_data.get("PreferredBackupWindow"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            CaCertificateIdentifier=json_data.get("CaCertificateIdentifier"),
            BackupRetention=json_data.get("BackupRetention"),
            RotateMasterUserPassword=json_data.get("RotateMasterUserPassword"),
            RelationalDatabaseParameters=set_or_none(json_data.get("RelationalDatabaseParameters")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLightsailDatabase = AwsLightsailDatabase


@dataclass
class RelationalDatabaseParameter(BaseModel):
    AllowedValues: Optional[str]
    ApplyMethod: Optional[str]
    ApplyType: Optional[str]
    DataType: Optional[str]
    Description: Optional[str]
    IsModifiable: Optional[bool]
    ParameterName: Optional[str]
    ParameterValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationalDatabaseParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationalDatabaseParameter"]:
        if not json_data:
            return None
        return cls(
            AllowedValues=json_data.get("AllowedValues"),
            ApplyMethod=json_data.get("ApplyMethod"),
            ApplyType=json_data.get("ApplyType"),
            DataType=json_data.get("DataType"),
            Description=json_data.get("Description"),
            IsModifiable=json_data.get("IsModifiable"),
            ParameterName=json_data.get("ParameterName"),
            ParameterValue=json_data.get("ParameterValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationalDatabaseParameter = RelationalDatabaseParameter


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


