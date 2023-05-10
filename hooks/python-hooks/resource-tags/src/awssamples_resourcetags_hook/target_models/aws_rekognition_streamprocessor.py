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
class AwsRekognitionStreamprocessor(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    KmsKeyId: Optional[str]
    RoleArn: Optional[str]
    KinesisVideoStream: Optional["_KinesisVideoStream"]
    FaceSearchSettings: Optional["_FaceSearchSettings"]
    ConnectedHomeSettings: Optional["_ConnectedHomeSettings"]
    KinesisDataStream: Optional["_KinesisDataStream"]
    S3Destination: Optional["_S3Destination"]
    NotificationChannel: Optional["_NotificationChannel"]
    DataSharingPreference: Optional["_DataSharingPreference"]
    PolygonRegionsOfInterest: Optional[AbstractSet[Sequence["_Point"]]]
    BoundingBoxRegionsOfInterest: Optional[AbstractSet["_BoundingBox"]]
    Status: Optional[str]
    StatusMessage: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRekognitionStreamprocessor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRekognitionStreamprocessor"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            KmsKeyId=json_data.get("KmsKeyId"),
            RoleArn=json_data.get("RoleArn"),
            KinesisVideoStream=KinesisVideoStream._deserialize(json_data.get("KinesisVideoStream")),
            FaceSearchSettings=FaceSearchSettings._deserialize(json_data.get("FaceSearchSettings")),
            ConnectedHomeSettings=ConnectedHomeSettings._deserialize(json_data.get("ConnectedHomeSettings")),
            KinesisDataStream=KinesisDataStream._deserialize(json_data.get("KinesisDataStream")),
            S3Destination=S3Destination._deserialize(json_data.get("S3Destination")),
            NotificationChannel=NotificationChannel._deserialize(json_data.get("NotificationChannel")),
            DataSharingPreference=DataSharingPreference._deserialize(json_data.get("DataSharingPreference")),
            PolygonRegionsOfInterest=set_or_none(json_data.get("PolygonRegionsOfInterest")),
            BoundingBoxRegionsOfInterest=set_or_none(json_data.get("BoundingBoxRegionsOfInterest")),
            Status=json_data.get("Status"),
            StatusMessage=json_data.get("StatusMessage"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRekognitionStreamprocessor = AwsRekognitionStreamprocessor


@dataclass
class KinesisVideoStream(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisVideoStream"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisVideoStream"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisVideoStream = KinesisVideoStream


@dataclass
class FaceSearchSettings(BaseModel):
    CollectionId: Optional[str]
    FaceMatchThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FaceSearchSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FaceSearchSettings"]:
        if not json_data:
            return None
        return cls(
            CollectionId=json_data.get("CollectionId"),
            FaceMatchThreshold=json_data.get("FaceMatchThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FaceSearchSettings = FaceSearchSettings


@dataclass
class ConnectedHomeSettings(BaseModel):
    Labels: Optional[AbstractSet[str]]
    MinConfidence: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectedHomeSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectedHomeSettings"]:
        if not json_data:
            return None
        return cls(
            Labels=set_or_none(json_data.get("Labels")),
            MinConfidence=json_data.get("MinConfidence"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectedHomeSettings = ConnectedHomeSettings


@dataclass
class KinesisDataStream(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisDataStream"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisDataStream"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisDataStream = KinesisDataStream


@dataclass
class S3Destination(BaseModel):
    BucketName: Optional[str]
    ObjectKeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Destination"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            ObjectKeyPrefix=json_data.get("ObjectKeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Destination = S3Destination


@dataclass
class NotificationChannel(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationChannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationChannel"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationChannel = NotificationChannel


@dataclass
class DataSharingPreference(BaseModel):
    OptIn: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DataSharingPreference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSharingPreference"]:
        if not json_data:
            return None
        return cls(
            OptIn=json_data.get("OptIn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSharingPreference = DataSharingPreference


@dataclass
class Point(BaseModel):
    X: Optional[float]
    Y: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Point"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Point"]:
        if not json_data:
            return None
        return cls(
            X=json_data.get("X"),
            Y=json_data.get("Y"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Point = Point


@dataclass
class BoundingBox(BaseModel):
    Height: Optional[float]
    Width: Optional[float]
    Left: Optional[float]
    Top: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BoundingBox"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoundingBox"]:
        if not json_data:
            return None
        return cls(
            Height=json_data.get("Height"),
            Width=json_data.get("Width"),
            Left=json_data.get("Left"),
            Top=json_data.get("Top"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoundingBox = BoundingBox


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


