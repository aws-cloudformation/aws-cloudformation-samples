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
class AwsMskCluster(BaseModel):
    BrokerNodeGroupInfo: Optional["_BrokerNodeGroupInfo"]
    EnhancedMonitoring: Optional[str]
    KafkaVersion: Optional[str]
    NumberOfBrokerNodes: Optional[int]
    EncryptionInfo: Optional["_EncryptionInfo"]
    OpenMonitoring: Optional["_OpenMonitoring"]
    ClusterName: Optional[str]
    Arn: Optional[str]
    CurrentVersion: Optional[str]
    ClientAuthentication: Optional["_ClientAuthentication"]
    LoggingInfo: Optional["_LoggingInfo"]
    Tags: Optional[Any]
    ConfigurationInfo: Optional["_ConfigurationInfo"]
    StorageMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMskCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMskCluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            BrokerNodeGroupInfo=BrokerNodeGroupInfo._deserialize(json_data.get("BrokerNodeGroupInfo")),
            EnhancedMonitoring=json_data.get("EnhancedMonitoring"),
            KafkaVersion=json_data.get("KafkaVersion"),
            NumberOfBrokerNodes=json_data.get("NumberOfBrokerNodes"),
            EncryptionInfo=EncryptionInfo._deserialize(json_data.get("EncryptionInfo")),
            OpenMonitoring=OpenMonitoring._deserialize(json_data.get("OpenMonitoring")),
            ClusterName=json_data.get("ClusterName"),
            Arn=json_data.get("Arn"),
            CurrentVersion=json_data.get("CurrentVersion"),
            ClientAuthentication=ClientAuthentication._deserialize(json_data.get("ClientAuthentication")),
            LoggingInfo=LoggingInfo._deserialize(json_data.get("LoggingInfo")),
            Tags=json_data.get("Tags"),
            ConfigurationInfo=ConfigurationInfo._deserialize(json_data.get("ConfigurationInfo")),
            StorageMode=json_data.get("StorageMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMskCluster = AwsMskCluster


@dataclass
class BrokerNodeGroupInfo(BaseModel):
    StorageInfo: Optional["_StorageInfo"]
    ConnectivityInfo: Optional["_ConnectivityInfo"]
    SecurityGroups: Optional[Sequence[str]]
    BrokerAZDistribution: Optional[str]
    ClientSubnets: Optional[Sequence[str]]
    InstanceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BrokerNodeGroupInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BrokerNodeGroupInfo"]:
        if not json_data:
            return None
        return cls(
            StorageInfo=StorageInfo._deserialize(json_data.get("StorageInfo")),
            ConnectivityInfo=ConnectivityInfo._deserialize(json_data.get("ConnectivityInfo")),
            SecurityGroups=json_data.get("SecurityGroups"),
            BrokerAZDistribution=json_data.get("BrokerAZDistribution"),
            ClientSubnets=json_data.get("ClientSubnets"),
            InstanceType=json_data.get("InstanceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BrokerNodeGroupInfo = BrokerNodeGroupInfo


@dataclass
class StorageInfo(BaseModel):
    EBSStorageInfo: Optional["_EBSStorageInfo"]

    @classmethod
    def _deserialize(
        cls: Type["_StorageInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageInfo"]:
        if not json_data:
            return None
        return cls(
            EBSStorageInfo=EBSStorageInfo._deserialize(json_data.get("EBSStorageInfo")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageInfo = StorageInfo


@dataclass
class EBSStorageInfo(BaseModel):
    VolumeSize: Optional[int]
    ProvisionedThroughput: Optional["_ProvisionedThroughput"]

    @classmethod
    def _deserialize(
        cls: Type["_EBSStorageInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EBSStorageInfo"]:
        if not json_data:
            return None
        return cls(
            VolumeSize=json_data.get("VolumeSize"),
            ProvisionedThroughput=ProvisionedThroughput._deserialize(json_data.get("ProvisionedThroughput")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EBSStorageInfo = EBSStorageInfo


@dataclass
class ProvisionedThroughput(BaseModel):
    Enabled: Optional[bool]
    VolumeThroughput: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisionedThroughput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisionedThroughput"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            VolumeThroughput=json_data.get("VolumeThroughput"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisionedThroughput = ProvisionedThroughput


@dataclass
class ConnectivityInfo(BaseModel):
    PublicAccess: Optional["_PublicAccess"]
    VpcConnectivity: Optional["_VpcConnectivity"]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectivityInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectivityInfo"]:
        if not json_data:
            return None
        return cls(
            PublicAccess=PublicAccess._deserialize(json_data.get("PublicAccess")),
            VpcConnectivity=VpcConnectivity._deserialize(json_data.get("VpcConnectivity")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectivityInfo = ConnectivityInfo


@dataclass
class PublicAccess(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicAccess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicAccess"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicAccess = PublicAccess


@dataclass
class VpcConnectivity(BaseModel):
    ClientAuthentication: Optional["_VpcConnectivityClientAuthentication"]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConnectivity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConnectivity"]:
        if not json_data:
            return None
        return cls(
            ClientAuthentication=VpcConnectivityClientAuthentication._deserialize(json_data.get("ClientAuthentication")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConnectivity = VpcConnectivity


@dataclass
class VpcConnectivityClientAuthentication(BaseModel):
    Tls: Optional["_VpcConnectivityTls"]
    Sasl: Optional["_VpcConnectivitySasl"]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConnectivityClientAuthentication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConnectivityClientAuthentication"]:
        if not json_data:
            return None
        return cls(
            Tls=VpcConnectivityTls._deserialize(json_data.get("Tls")),
            Sasl=VpcConnectivitySasl._deserialize(json_data.get("Sasl")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConnectivityClientAuthentication = VpcConnectivityClientAuthentication


@dataclass
class VpcConnectivityTls(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConnectivityTls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConnectivityTls"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConnectivityTls = VpcConnectivityTls


@dataclass
class VpcConnectivitySasl(BaseModel):
    Scram: Optional["_VpcConnectivityScram"]
    Iam: Optional["_VpcConnectivityIam"]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConnectivitySasl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConnectivitySasl"]:
        if not json_data:
            return None
        return cls(
            Scram=VpcConnectivityScram._deserialize(json_data.get("Scram")),
            Iam=VpcConnectivityIam._deserialize(json_data.get("Iam")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConnectivitySasl = VpcConnectivitySasl


@dataclass
class VpcConnectivityScram(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConnectivityScram"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConnectivityScram"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConnectivityScram = VpcConnectivityScram


@dataclass
class VpcConnectivityIam(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConnectivityIam"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConnectivityIam"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConnectivityIam = VpcConnectivityIam


@dataclass
class EncryptionInfo(BaseModel):
    EncryptionAtRest: Optional["_EncryptionAtRest"]
    EncryptionInTransit: Optional["_EncryptionInTransit"]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionInfo"]:
        if not json_data:
            return None
        return cls(
            EncryptionAtRest=EncryptionAtRest._deserialize(json_data.get("EncryptionAtRest")),
            EncryptionInTransit=EncryptionInTransit._deserialize(json_data.get("EncryptionInTransit")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionInfo = EncryptionInfo


@dataclass
class EncryptionAtRest(BaseModel):
    DataVolumeKMSKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionAtRest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionAtRest"]:
        if not json_data:
            return None
        return cls(
            DataVolumeKMSKeyId=json_data.get("DataVolumeKMSKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionAtRest = EncryptionAtRest


@dataclass
class EncryptionInTransit(BaseModel):
    InCluster: Optional[bool]
    ClientBroker: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionInTransit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionInTransit"]:
        if not json_data:
            return None
        return cls(
            InCluster=json_data.get("InCluster"),
            ClientBroker=json_data.get("ClientBroker"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionInTransit = EncryptionInTransit


@dataclass
class OpenMonitoring(BaseModel):
    Prometheus: Optional["_Prometheus"]

    @classmethod
    def _deserialize(
        cls: Type["_OpenMonitoring"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenMonitoring"]:
        if not json_data:
            return None
        return cls(
            Prometheus=Prometheus._deserialize(json_data.get("Prometheus")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenMonitoring = OpenMonitoring


@dataclass
class Prometheus(BaseModel):
    JmxExporter: Optional["_JmxExporter"]
    NodeExporter: Optional["_NodeExporter"]

    @classmethod
    def _deserialize(
        cls: Type["_Prometheus"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Prometheus"]:
        if not json_data:
            return None
        return cls(
            JmxExporter=JmxExporter._deserialize(json_data.get("JmxExporter")),
            NodeExporter=NodeExporter._deserialize(json_data.get("NodeExporter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Prometheus = Prometheus


@dataclass
class JmxExporter(BaseModel):
    EnabledInBroker: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_JmxExporter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JmxExporter"]:
        if not json_data:
            return None
        return cls(
            EnabledInBroker=json_data.get("EnabledInBroker"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JmxExporter = JmxExporter


@dataclass
class NodeExporter(BaseModel):
    EnabledInBroker: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NodeExporter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeExporter"]:
        if not json_data:
            return None
        return cls(
            EnabledInBroker=json_data.get("EnabledInBroker"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeExporter = NodeExporter


@dataclass
class ClientAuthentication(BaseModel):
    Tls: Optional["_Tls"]
    Sasl: Optional["_Sasl"]
    Unauthenticated: Optional["_Unauthenticated"]

    @classmethod
    def _deserialize(
        cls: Type["_ClientAuthentication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientAuthentication"]:
        if not json_data:
            return None
        return cls(
            Tls=Tls._deserialize(json_data.get("Tls")),
            Sasl=Sasl._deserialize(json_data.get("Sasl")),
            Unauthenticated=Unauthenticated._deserialize(json_data.get("Unauthenticated")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientAuthentication = ClientAuthentication


@dataclass
class Tls(BaseModel):
    CertificateAuthorityArnList: Optional[Sequence[str]]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Tls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tls"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthorityArnList=json_data.get("CertificateAuthorityArnList"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tls = Tls


@dataclass
class Sasl(BaseModel):
    Scram: Optional["_Scram"]
    Iam: Optional["_Iam"]

    @classmethod
    def _deserialize(
        cls: Type["_Sasl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sasl"]:
        if not json_data:
            return None
        return cls(
            Scram=Scram._deserialize(json_data.get("Scram")),
            Iam=Iam._deserialize(json_data.get("Iam")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sasl = Sasl


@dataclass
class Scram(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Scram"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scram"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scram = Scram


@dataclass
class Iam(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Iam"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Iam"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Iam = Iam


@dataclass
class Unauthenticated(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Unauthenticated"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Unauthenticated"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Unauthenticated = Unauthenticated


@dataclass
class LoggingInfo(BaseModel):
    BrokerLogs: Optional["_BrokerLogs"]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingInfo"]:
        if not json_data:
            return None
        return cls(
            BrokerLogs=BrokerLogs._deserialize(json_data.get("BrokerLogs")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingInfo = LoggingInfo


@dataclass
class BrokerLogs(BaseModel):
    S3: Optional["_S3"]
    CloudWatchLogs: Optional["_CloudWatchLogs"]
    Firehose: Optional["_Firehose"]

    @classmethod
    def _deserialize(
        cls: Type["_BrokerLogs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BrokerLogs"]:
        if not json_data:
            return None
        return cls(
            S3=S3._deserialize(json_data.get("S3")),
            CloudWatchLogs=CloudWatchLogs._deserialize(json_data.get("CloudWatchLogs")),
            Firehose=Firehose._deserialize(json_data.get("Firehose")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BrokerLogs = BrokerLogs


@dataclass
class S3(BaseModel):
    Enabled: Optional[bool]
    Prefix: Optional[str]
    Bucket: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Prefix=json_data.get("Prefix"),
            Bucket=json_data.get("Bucket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3 = S3


@dataclass
class CloudWatchLogs(BaseModel):
    LogGroup: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLogs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLogs"]:
        if not json_data:
            return None
        return cls(
            LogGroup=json_data.get("LogGroup"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLogs = CloudWatchLogs


@dataclass
class Firehose(BaseModel):
    Enabled: Optional[bool]
    DeliveryStream: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Firehose"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Firehose"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            DeliveryStream=json_data.get("DeliveryStream"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Firehose = Firehose


@dataclass
class ConfigurationInfo(BaseModel):
    Revision: Optional[int]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationInfo"]:
        if not json_data:
            return None
        return cls(
            Revision=json_data.get("Revision"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationInfo = ConfigurationInfo


