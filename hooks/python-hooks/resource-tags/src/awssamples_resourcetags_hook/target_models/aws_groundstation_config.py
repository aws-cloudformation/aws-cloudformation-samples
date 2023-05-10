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
class AwsGroundstationConfig(BaseModel):
    Name: Optional[str]
    Tags: Optional[Any]
    Type: Optional[str]
    ConfigData: Optional["_ConfigData"]
    Arn: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGroundstationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGroundstationConfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            ConfigData=ConfigData._deserialize(json_data.get("ConfigData")),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGroundstationConfig = AwsGroundstationConfig


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
class ConfigData(BaseModel):
    AntennaDownlinkConfig: Optional["_AntennaDownlinkConfig"]
    TrackingConfig: Optional["_TrackingConfig"]
    DataflowEndpointConfig: Optional["_DataflowEndpointConfig"]
    AntennaDownlinkDemodDecodeConfig: Optional["_AntennaDownlinkDemodDecodeConfig"]
    AntennaUplinkConfig: Optional["_AntennaUplinkConfig"]
    UplinkEchoConfig: Optional["_UplinkEchoConfig"]
    S3RecordingConfig: Optional["_S3RecordingConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigData"]:
        if not json_data:
            return None
        return cls(
            AntennaDownlinkConfig=AntennaDownlinkConfig._deserialize(json_data.get("AntennaDownlinkConfig")),
            TrackingConfig=TrackingConfig._deserialize(json_data.get("TrackingConfig")),
            DataflowEndpointConfig=DataflowEndpointConfig._deserialize(json_data.get("DataflowEndpointConfig")),
            AntennaDownlinkDemodDecodeConfig=AntennaDownlinkDemodDecodeConfig._deserialize(json_data.get("AntennaDownlinkDemodDecodeConfig")),
            AntennaUplinkConfig=AntennaUplinkConfig._deserialize(json_data.get("AntennaUplinkConfig")),
            UplinkEchoConfig=UplinkEchoConfig._deserialize(json_data.get("UplinkEchoConfig")),
            S3RecordingConfig=S3RecordingConfig._deserialize(json_data.get("S3RecordingConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigData = ConfigData


@dataclass
class AntennaDownlinkConfig(BaseModel):
    SpectrumConfig: Optional["_SpectrumConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AntennaDownlinkConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AntennaDownlinkConfig"]:
        if not json_data:
            return None
        return cls(
            SpectrumConfig=SpectrumConfig._deserialize(json_data.get("SpectrumConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AntennaDownlinkConfig = AntennaDownlinkConfig


@dataclass
class SpectrumConfig(BaseModel):
    CenterFrequency: Optional["_Frequency"]
    Bandwidth: Optional["_FrequencyBandwidth"]
    Polarization: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpectrumConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpectrumConfig"]:
        if not json_data:
            return None
        return cls(
            CenterFrequency=Frequency._deserialize(json_data.get("CenterFrequency")),
            Bandwidth=FrequencyBandwidth._deserialize(json_data.get("Bandwidth")),
            Polarization=json_data.get("Polarization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpectrumConfig = SpectrumConfig


@dataclass
class Frequency(BaseModel):
    Value: Optional[float]
    Units: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Frequency"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Frequency"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Units=json_data.get("Units"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Frequency = Frequency


@dataclass
class FrequencyBandwidth(BaseModel):
    Value: Optional[float]
    Units: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FrequencyBandwidth"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrequencyBandwidth"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Units=json_data.get("Units"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrequencyBandwidth = FrequencyBandwidth


@dataclass
class TrackingConfig(BaseModel):
    Autotrack: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrackingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrackingConfig"]:
        if not json_data:
            return None
        return cls(
            Autotrack=json_data.get("Autotrack"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrackingConfig = TrackingConfig


@dataclass
class DataflowEndpointConfig(BaseModel):
    DataflowEndpointName: Optional[str]
    DataflowEndpointRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataflowEndpointConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataflowEndpointConfig"]:
        if not json_data:
            return None
        return cls(
            DataflowEndpointName=json_data.get("DataflowEndpointName"),
            DataflowEndpointRegion=json_data.get("DataflowEndpointRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataflowEndpointConfig = DataflowEndpointConfig


@dataclass
class AntennaDownlinkDemodDecodeConfig(BaseModel):
    SpectrumConfig: Optional["_SpectrumConfig"]
    DemodulationConfig: Optional["_DemodulationConfig"]
    DecodeConfig: Optional["_DecodeConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AntennaDownlinkDemodDecodeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AntennaDownlinkDemodDecodeConfig"]:
        if not json_data:
            return None
        return cls(
            SpectrumConfig=SpectrumConfig._deserialize(json_data.get("SpectrumConfig")),
            DemodulationConfig=DemodulationConfig._deserialize(json_data.get("DemodulationConfig")),
            DecodeConfig=DecodeConfig._deserialize(json_data.get("DecodeConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AntennaDownlinkDemodDecodeConfig = AntennaDownlinkDemodDecodeConfig


@dataclass
class DemodulationConfig(BaseModel):
    UnvalidatedJSON: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DemodulationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DemodulationConfig"]:
        if not json_data:
            return None
        return cls(
            UnvalidatedJSON=json_data.get("UnvalidatedJSON"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DemodulationConfig = DemodulationConfig


@dataclass
class DecodeConfig(BaseModel):
    UnvalidatedJSON: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DecodeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DecodeConfig"]:
        if not json_data:
            return None
        return cls(
            UnvalidatedJSON=json_data.get("UnvalidatedJSON"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DecodeConfig = DecodeConfig


@dataclass
class AntennaUplinkConfig(BaseModel):
    SpectrumConfig: Optional["_UplinkSpectrumConfig"]
    TargetEirp: Optional["_Eirp"]
    TransmitDisabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AntennaUplinkConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AntennaUplinkConfig"]:
        if not json_data:
            return None
        return cls(
            SpectrumConfig=UplinkSpectrumConfig._deserialize(json_data.get("SpectrumConfig")),
            TargetEirp=Eirp._deserialize(json_data.get("TargetEirp")),
            TransmitDisabled=json_data.get("TransmitDisabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AntennaUplinkConfig = AntennaUplinkConfig


@dataclass
class UplinkSpectrumConfig(BaseModel):
    CenterFrequency: Optional["_Frequency"]
    Polarization: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UplinkSpectrumConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UplinkSpectrumConfig"]:
        if not json_data:
            return None
        return cls(
            CenterFrequency=Frequency._deserialize(json_data.get("CenterFrequency")),
            Polarization=json_data.get("Polarization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UplinkSpectrumConfig = UplinkSpectrumConfig


@dataclass
class Eirp(BaseModel):
    Value: Optional[float]
    Units: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Eirp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Eirp"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Units=json_data.get("Units"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Eirp = Eirp


@dataclass
class UplinkEchoConfig(BaseModel):
    Enabled: Optional[bool]
    AntennaUplinkConfigArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UplinkEchoConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UplinkEchoConfig"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            AntennaUplinkConfigArn=json_data.get("AntennaUplinkConfigArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UplinkEchoConfig = UplinkEchoConfig


@dataclass
class S3RecordingConfig(BaseModel):
    BucketArn: Optional[str]
    RoleArn: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3RecordingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3RecordingConfig"]:
        if not json_data:
            return None
        return cls(
            BucketArn=json_data.get("BucketArn"),
            RoleArn=json_data.get("RoleArn"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3RecordingConfig = S3RecordingConfig


