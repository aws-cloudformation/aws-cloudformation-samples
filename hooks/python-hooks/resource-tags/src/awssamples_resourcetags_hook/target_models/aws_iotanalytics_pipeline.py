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
class AwsIotanalyticsPipeline(BaseModel):
    Id: Optional[str]
    PipelineName: Optional[str]
    Tags: Optional[Any]
    PipelineActivities: Optional[Sequence["_Activity"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotanalyticsPipeline"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotanalyticsPipeline"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            PipelineName=json_data.get("PipelineName"),
            Tags=json_data.get("Tags"),
            PipelineActivities=deserialize_list(json_data.get("PipelineActivities"), Activity),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotanalyticsPipeline = AwsIotanalyticsPipeline


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
class Activity(BaseModel):
    SelectAttributes: Optional["_SelectAttributes"]
    Datastore: Optional["_Datastore"]
    Filter: Optional["_Filter"]
    AddAttributes: Optional["_AddAttributes"]
    Channel: Optional["_Channel"]
    DeviceShadowEnrich: Optional["_DeviceShadowEnrich"]
    Math: Optional["_Math"]
    Lambda: Optional["_Lambda"]
    DeviceRegistryEnrich: Optional["_DeviceRegistryEnrich"]
    RemoveAttributes: Optional["_RemoveAttributes"]

    @classmethod
    def _deserialize(
        cls: Type["_Activity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Activity"]:
        if not json_data:
            return None
        return cls(
            SelectAttributes=SelectAttributes._deserialize(json_data.get("SelectAttributes")),
            Datastore=Datastore._deserialize(json_data.get("Datastore")),
            Filter=Filter._deserialize(json_data.get("Filter")),
            AddAttributes=AddAttributes._deserialize(json_data.get("AddAttributes")),
            Channel=Channel._deserialize(json_data.get("Channel")),
            DeviceShadowEnrich=DeviceShadowEnrich._deserialize(json_data.get("DeviceShadowEnrich")),
            Math=Math._deserialize(json_data.get("Math")),
            Lambda=Lambda._deserialize(json_data.get("Lambda")),
            DeviceRegistryEnrich=DeviceRegistryEnrich._deserialize(json_data.get("DeviceRegistryEnrich")),
            RemoveAttributes=RemoveAttributes._deserialize(json_data.get("RemoveAttributes")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Activity = Activity


@dataclass
class SelectAttributes(BaseModel):
    Next: Optional[str]
    Attributes: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelectAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectAttributes"]:
        if not json_data:
            return None
        return cls(
            Next=json_data.get("Next"),
            Attributes=json_data.get("Attributes"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectAttributes = SelectAttributes


@dataclass
class Datastore(BaseModel):
    DatastoreName: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Datastore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Datastore"]:
        if not json_data:
            return None
        return cls(
            DatastoreName=json_data.get("DatastoreName"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Datastore = Datastore


@dataclass
class Filter(BaseModel):
    Filter: Optional[str]
    Next: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Filter=json_data.get("Filter"),
            Next=json_data.get("Next"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class AddAttributes(BaseModel):
    Next: Optional[str]
    Attributes: Optional[MutableMapping[str, str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddAttributes"]:
        if not json_data:
            return None
        return cls(
            Next=json_data.get("Next"),
            Attributes=json_data.get("Attributes"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddAttributes = AddAttributes


@dataclass
class Channel(BaseModel):
    ChannelName: Optional[str]
    Next: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Channel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Channel"]:
        if not json_data:
            return None
        return cls(
            ChannelName=json_data.get("ChannelName"),
            Next=json_data.get("Next"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Channel = Channel


@dataclass
class DeviceShadowEnrich(BaseModel):
    Attribute: Optional[str]
    Next: Optional[str]
    ThingName: Optional[str]
    RoleArn: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceShadowEnrich"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceShadowEnrich"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Next=json_data.get("Next"),
            ThingName=json_data.get("ThingName"),
            RoleArn=json_data.get("RoleArn"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceShadowEnrich = DeviceShadowEnrich


@dataclass
class Math(BaseModel):
    Attribute: Optional[str]
    Next: Optional[str]
    Math: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Math"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Math"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Next=json_data.get("Next"),
            Math=json_data.get("Math"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Math = Math


@dataclass
class Lambda(BaseModel):
    BatchSize: Optional[int]
    Next: Optional[str]
    LambdaName: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Lambda"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Lambda"]:
        if not json_data:
            return None
        return cls(
            BatchSize=json_data.get("BatchSize"),
            Next=json_data.get("Next"),
            LambdaName=json_data.get("LambdaName"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Lambda = Lambda


@dataclass
class DeviceRegistryEnrich(BaseModel):
    Attribute: Optional[str]
    Next: Optional[str]
    ThingName: Optional[str]
    RoleArn: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceRegistryEnrich"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceRegistryEnrich"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Next=json_data.get("Next"),
            ThingName=json_data.get("ThingName"),
            RoleArn=json_data.get("RoleArn"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceRegistryEnrich = DeviceRegistryEnrich


@dataclass
class RemoveAttributes(BaseModel):
    Next: Optional[str]
    Attributes: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemoveAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoveAttributes"]:
        if not json_data:
            return None
        return cls(
            Next=json_data.get("Next"),
            Attributes=json_data.get("Attributes"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoveAttributes = RemoveAttributes


