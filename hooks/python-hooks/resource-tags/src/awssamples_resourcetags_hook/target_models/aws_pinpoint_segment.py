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
class AwsPinpointSegment(BaseModel):
    SegmentId: Optional[str]
    Arn: Optional[str]
    SegmentGroups: Optional["_SegmentGroups"]
    Dimensions: Optional["_SegmentDimensions"]
    ApplicationId: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPinpointSegment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPinpointSegment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SegmentId=json_data.get("SegmentId"),
            Arn=json_data.get("Arn"),
            SegmentGroups=SegmentGroups._deserialize(json_data.get("SegmentGroups")),
            Dimensions=SegmentDimensions._deserialize(json_data.get("Dimensions")),
            ApplicationId=json_data.get("ApplicationId"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPinpointSegment = AwsPinpointSegment


@dataclass
class SegmentGroups(BaseModel):
    Groups: Optional[Sequence["_Groups"]]
    Include: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SegmentGroups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SegmentGroups"]:
        if not json_data:
            return None
        return cls(
            Groups=deserialize_list(json_data.get("Groups"), Groups),
            Include=json_data.get("Include"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SegmentGroups = SegmentGroups


@dataclass
class Groups(BaseModel):
    Type: Optional[str]
    SourceType: Optional[str]
    Dimensions: Optional[Sequence["_SegmentDimensions"]]
    SourceSegments: Optional[Sequence["_SourceSegments"]]

    @classmethod
    def _deserialize(
        cls: Type["_Groups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Groups"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            SourceType=json_data.get("SourceType"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), SegmentDimensions),
            SourceSegments=deserialize_list(json_data.get("SourceSegments"), SourceSegments),
        )


# work around possible type aliasing issues when variable has same name as a model
_Groups = Groups


@dataclass
class SegmentDimensions(BaseModel):
    Demographic: Optional["_Demographic"]
    Metrics: Optional[MutableMapping[str, Any]]
    Attributes: Optional[MutableMapping[str, Any]]
    Behavior: Optional["_Behavior"]
    UserAttributes: Optional[MutableMapping[str, Any]]
    Location: Optional["_Location"]

    @classmethod
    def _deserialize(
        cls: Type["_SegmentDimensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SegmentDimensions"]:
        if not json_data:
            return None
        return cls(
            Demographic=Demographic._deserialize(json_data.get("Demographic")),
            Metrics=json_data.get("Metrics"),
            Attributes=json_data.get("Attributes"),
            Behavior=Behavior._deserialize(json_data.get("Behavior")),
            UserAttributes=json_data.get("UserAttributes"),
            Location=Location._deserialize(json_data.get("Location")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SegmentDimensions = SegmentDimensions


@dataclass
class Demographic(BaseModel):
    AppVersion: Optional["_SetDimension"]
    DeviceType: Optional["_SetDimension"]
    Platform: Optional["_SetDimension"]
    Channel: Optional["_SetDimension"]
    Model: Optional["_SetDimension"]
    Make: Optional["_SetDimension"]

    @classmethod
    def _deserialize(
        cls: Type["_Demographic"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Demographic"]:
        if not json_data:
            return None
        return cls(
            AppVersion=SetDimension._deserialize(json_data.get("AppVersion")),
            DeviceType=SetDimension._deserialize(json_data.get("DeviceType")),
            Platform=SetDimension._deserialize(json_data.get("Platform")),
            Channel=SetDimension._deserialize(json_data.get("Channel")),
            Model=SetDimension._deserialize(json_data.get("Model")),
            Make=SetDimension._deserialize(json_data.get("Make")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Demographic = Demographic


@dataclass
class SetDimension(BaseModel):
    DimensionType: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SetDimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetDimension"]:
        if not json_data:
            return None
        return cls(
            DimensionType=json_data.get("DimensionType"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetDimension = SetDimension


@dataclass
class Behavior(BaseModel):
    Recency: Optional["_Recency"]

    @classmethod
    def _deserialize(
        cls: Type["_Behavior"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Behavior"]:
        if not json_data:
            return None
        return cls(
            Recency=Recency._deserialize(json_data.get("Recency")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Behavior = Behavior


@dataclass
class Recency(BaseModel):
    Duration: Optional[str]
    RecencyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Recency"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Recency"]:
        if not json_data:
            return None
        return cls(
            Duration=json_data.get("Duration"),
            RecencyType=json_data.get("RecencyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Recency = Recency


@dataclass
class Location(BaseModel):
    GPSPoint: Optional["_GPSPoint"]
    Country: Optional["_SetDimension"]

    @classmethod
    def _deserialize(
        cls: Type["_Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Location"]:
        if not json_data:
            return None
        return cls(
            GPSPoint=GPSPoint._deserialize(json_data.get("GPSPoint")),
            Country=SetDimension._deserialize(json_data.get("Country")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Location = Location


@dataclass
class GPSPoint(BaseModel):
    RangeInKilometers: Optional[float]
    Coordinates: Optional["_Coordinates"]

    @classmethod
    def _deserialize(
        cls: Type["_GPSPoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GPSPoint"]:
        if not json_data:
            return None
        return cls(
            RangeInKilometers=json_data.get("RangeInKilometers"),
            Coordinates=Coordinates._deserialize(json_data.get("Coordinates")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GPSPoint = GPSPoint


@dataclass
class Coordinates(BaseModel):
    Latitude: Optional[float]
    Longitude: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Coordinates"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Coordinates"]:
        if not json_data:
            return None
        return cls(
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Coordinates = Coordinates


@dataclass
class SourceSegments(BaseModel):
    Version: Optional[int]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceSegments"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceSegments"]:
        if not json_data:
            return None
        return cls(
            Version=json_data.get("Version"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceSegments = SourceSegments


