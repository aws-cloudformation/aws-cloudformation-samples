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
class AwsAppmeshVirtualnode(BaseModel):
    Uid: Optional[str]
    MeshName: Optional[str]
    MeshOwner: Optional[str]
    ResourceOwner: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Spec: Optional["_VirtualNodeSpec"]
    VirtualNodeName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppmeshVirtualnode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppmeshVirtualnode"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Uid=json_data.get("Uid"),
            MeshName=json_data.get("MeshName"),
            MeshOwner=json_data.get("MeshOwner"),
            ResourceOwner=json_data.get("ResourceOwner"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Spec=VirtualNodeSpec._deserialize(json_data.get("Spec")),
            VirtualNodeName=json_data.get("VirtualNodeName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppmeshVirtualnode = AwsAppmeshVirtualnode


@dataclass
class VirtualNodeSpec(BaseModel):
    Logging: Optional["_Logging"]
    Backends: Optional[Sequence["_Backend"]]
    Listeners: Optional[Sequence["_Listener"]]
    BackendDefaults: Optional["_BackendDefaults"]
    ServiceDiscovery: Optional["_ServiceDiscovery"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNodeSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNodeSpec"]:
        if not json_data:
            return None
        return cls(
            Logging=Logging._deserialize(json_data.get("Logging")),
            Backends=deserialize_list(json_data.get("Backends"), Backend),
            Listeners=deserialize_list(json_data.get("Listeners"), Listener),
            BackendDefaults=BackendDefaults._deserialize(json_data.get("BackendDefaults")),
            ServiceDiscovery=ServiceDiscovery._deserialize(json_data.get("ServiceDiscovery")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNodeSpec = VirtualNodeSpec


@dataclass
class Logging(BaseModel):
    AccessLog: Optional["_AccessLog"]

    @classmethod
    def _deserialize(
        cls: Type["_Logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logging"]:
        if not json_data:
            return None
        return cls(
            AccessLog=AccessLog._deserialize(json_data.get("AccessLog")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logging = Logging


@dataclass
class AccessLog(BaseModel):
    File: Optional["_FileAccessLog"]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLog"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLog"]:
        if not json_data:
            return None
        return cls(
            File=FileAccessLog._deserialize(json_data.get("File")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLog = AccessLog


@dataclass
class FileAccessLog(BaseModel):
    Path: Optional[str]
    Format: Optional["_LoggingFormat"]

    @classmethod
    def _deserialize(
        cls: Type["_FileAccessLog"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileAccessLog"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Format=LoggingFormat._deserialize(json_data.get("Format")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileAccessLog = FileAccessLog


@dataclass
class LoggingFormat(BaseModel):
    Text: Optional[str]
    Json: Optional[Sequence["_JsonFormatRef"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingFormat"]:
        if not json_data:
            return None
        return cls(
            Text=json_data.get("Text"),
            Json=deserialize_list(json_data.get("Json"), JsonFormatRef),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingFormat = LoggingFormat


@dataclass
class JsonFormatRef(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonFormatRef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonFormatRef"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonFormatRef = JsonFormatRef


@dataclass
class Backend(BaseModel):
    VirtualService: Optional["_VirtualServiceBackend"]

    @classmethod
    def _deserialize(
        cls: Type["_Backend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backend"]:
        if not json_data:
            return None
        return cls(
            VirtualService=VirtualServiceBackend._deserialize(json_data.get("VirtualService")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backend = Backend


@dataclass
class VirtualServiceBackend(BaseModel):
    VirtualServiceName: Optional[str]
    ClientPolicy: Optional["_ClientPolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualServiceBackend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualServiceBackend"]:
        if not json_data:
            return None
        return cls(
            VirtualServiceName=json_data.get("VirtualServiceName"),
            ClientPolicy=ClientPolicy._deserialize(json_data.get("ClientPolicy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualServiceBackend = VirtualServiceBackend


@dataclass
class ClientPolicy(BaseModel):
    TLS: Optional["_ClientPolicyTls"]

    @classmethod
    def _deserialize(
        cls: Type["_ClientPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientPolicy"]:
        if not json_data:
            return None
        return cls(
            TLS=ClientPolicyTls._deserialize(json_data.get("TLS")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientPolicy = ClientPolicy


@dataclass
class ClientPolicyTls(BaseModel):
    Validation: Optional["_TlsValidationContext"]
    Ports: Optional[Sequence[int]]
    Enforce: Optional[bool]
    Certificate: Optional["_ClientTlsCertificate"]

    @classmethod
    def _deserialize(
        cls: Type["_ClientPolicyTls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientPolicyTls"]:
        if not json_data:
            return None
        return cls(
            Validation=TlsValidationContext._deserialize(json_data.get("Validation")),
            Ports=json_data.get("Ports"),
            Enforce=json_data.get("Enforce"),
            Certificate=ClientTlsCertificate._deserialize(json_data.get("Certificate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientPolicyTls = ClientPolicyTls


@dataclass
class TlsValidationContext(BaseModel):
    SubjectAlternativeNames: Optional["_SubjectAlternativeNames"]
    Trust: Optional["_TlsValidationContextTrust"]

    @classmethod
    def _deserialize(
        cls: Type["_TlsValidationContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsValidationContext"]:
        if not json_data:
            return None
        return cls(
            SubjectAlternativeNames=SubjectAlternativeNames._deserialize(json_data.get("SubjectAlternativeNames")),
            Trust=TlsValidationContextTrust._deserialize(json_data.get("Trust")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsValidationContext = TlsValidationContext


@dataclass
class SubjectAlternativeNames(BaseModel):
    Match: Optional["_SubjectAlternativeNameMatchers"]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectAlternativeNames"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectAlternativeNames"]:
        if not json_data:
            return None
        return cls(
            Match=SubjectAlternativeNameMatchers._deserialize(json_data.get("Match")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectAlternativeNames = SubjectAlternativeNames


@dataclass
class SubjectAlternativeNameMatchers(BaseModel):
    Exact: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectAlternativeNameMatchers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectAlternativeNameMatchers"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectAlternativeNameMatchers = SubjectAlternativeNameMatchers


@dataclass
class TlsValidationContextTrust(BaseModel):
    SDS: Optional["_TlsValidationContextSdsTrust"]
    ACM: Optional["_TlsValidationContextAcmTrust"]
    File: Optional["_TlsValidationContextFileTrust"]

    @classmethod
    def _deserialize(
        cls: Type["_TlsValidationContextTrust"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsValidationContextTrust"]:
        if not json_data:
            return None
        return cls(
            SDS=TlsValidationContextSdsTrust._deserialize(json_data.get("SDS")),
            ACM=TlsValidationContextAcmTrust._deserialize(json_data.get("ACM")),
            File=TlsValidationContextFileTrust._deserialize(json_data.get("File")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsValidationContextTrust = TlsValidationContextTrust


@dataclass
class TlsValidationContextSdsTrust(BaseModel):
    SecretName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TlsValidationContextSdsTrust"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsValidationContextSdsTrust"]:
        if not json_data:
            return None
        return cls(
            SecretName=json_data.get("SecretName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsValidationContextSdsTrust = TlsValidationContextSdsTrust


@dataclass
class TlsValidationContextAcmTrust(BaseModel):
    CertificateAuthorityArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsValidationContextAcmTrust"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsValidationContextAcmTrust"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthorityArns=json_data.get("CertificateAuthorityArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsValidationContextAcmTrust = TlsValidationContextAcmTrust


@dataclass
class TlsValidationContextFileTrust(BaseModel):
    CertificateChain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TlsValidationContextFileTrust"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsValidationContextFileTrust"]:
        if not json_data:
            return None
        return cls(
            CertificateChain=json_data.get("CertificateChain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsValidationContextFileTrust = TlsValidationContextFileTrust


@dataclass
class ClientTlsCertificate(BaseModel):
    File: Optional["_ListenerTlsFileCertificate"]
    SDS: Optional["_ListenerTlsSdsCertificate"]

    @classmethod
    def _deserialize(
        cls: Type["_ClientTlsCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientTlsCertificate"]:
        if not json_data:
            return None
        return cls(
            File=ListenerTlsFileCertificate._deserialize(json_data.get("File")),
            SDS=ListenerTlsSdsCertificate._deserialize(json_data.get("SDS")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientTlsCertificate = ClientTlsCertificate


@dataclass
class ListenerTlsFileCertificate(BaseModel):
    CertificateChain: Optional[str]
    PrivateKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerTlsFileCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerTlsFileCertificate"]:
        if not json_data:
            return None
        return cls(
            CertificateChain=json_data.get("CertificateChain"),
            PrivateKey=json_data.get("PrivateKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerTlsFileCertificate = ListenerTlsFileCertificate


@dataclass
class ListenerTlsSdsCertificate(BaseModel):
    SecretName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerTlsSdsCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerTlsSdsCertificate"]:
        if not json_data:
            return None
        return cls(
            SecretName=json_data.get("SecretName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerTlsSdsCertificate = ListenerTlsSdsCertificate


@dataclass
class Listener(BaseModel):
    ConnectionPool: Optional["_VirtualNodeConnectionPool"]
    Timeout: Optional["_ListenerTimeout"]
    HealthCheck: Optional["_HealthCheck"]
    TLS: Optional["_ListenerTls"]
    PortMapping: Optional["_PortMapping"]
    OutlierDetection: Optional["_OutlierDetection"]

    @classmethod
    def _deserialize(
        cls: Type["_Listener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Listener"]:
        if not json_data:
            return None
        return cls(
            ConnectionPool=VirtualNodeConnectionPool._deserialize(json_data.get("ConnectionPool")),
            Timeout=ListenerTimeout._deserialize(json_data.get("Timeout")),
            HealthCheck=HealthCheck._deserialize(json_data.get("HealthCheck")),
            TLS=ListenerTls._deserialize(json_data.get("TLS")),
            PortMapping=PortMapping._deserialize(json_data.get("PortMapping")),
            OutlierDetection=OutlierDetection._deserialize(json_data.get("OutlierDetection")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Listener = Listener


@dataclass
class VirtualNodeConnectionPool(BaseModel):
    TCP: Optional["_VirtualNodeTcpConnectionPool"]
    HTTP: Optional["_VirtualNodeHttpConnectionPool"]
    HTTP2: Optional["_VirtualNodeHttp2ConnectionPool"]
    GRPC: Optional["_VirtualNodeGrpcConnectionPool"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNodeConnectionPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNodeConnectionPool"]:
        if not json_data:
            return None
        return cls(
            TCP=VirtualNodeTcpConnectionPool._deserialize(json_data.get("TCP")),
            HTTP=VirtualNodeHttpConnectionPool._deserialize(json_data.get("HTTP")),
            HTTP2=VirtualNodeHttp2ConnectionPool._deserialize(json_data.get("HTTP2")),
            GRPC=VirtualNodeGrpcConnectionPool._deserialize(json_data.get("GRPC")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNodeConnectionPool = VirtualNodeConnectionPool


@dataclass
class VirtualNodeTcpConnectionPool(BaseModel):
    MaxConnections: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNodeTcpConnectionPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNodeTcpConnectionPool"]:
        if not json_data:
            return None
        return cls(
            MaxConnections=json_data.get("MaxConnections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNodeTcpConnectionPool = VirtualNodeTcpConnectionPool


@dataclass
class VirtualNodeHttpConnectionPool(BaseModel):
    MaxConnections: Optional[int]
    MaxPendingRequests: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNodeHttpConnectionPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNodeHttpConnectionPool"]:
        if not json_data:
            return None
        return cls(
            MaxConnections=json_data.get("MaxConnections"),
            MaxPendingRequests=json_data.get("MaxPendingRequests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNodeHttpConnectionPool = VirtualNodeHttpConnectionPool


@dataclass
class VirtualNodeHttp2ConnectionPool(BaseModel):
    MaxRequests: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNodeHttp2ConnectionPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNodeHttp2ConnectionPool"]:
        if not json_data:
            return None
        return cls(
            MaxRequests=json_data.get("MaxRequests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNodeHttp2ConnectionPool = VirtualNodeHttp2ConnectionPool


@dataclass
class VirtualNodeGrpcConnectionPool(BaseModel):
    MaxRequests: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNodeGrpcConnectionPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNodeGrpcConnectionPool"]:
        if not json_data:
            return None
        return cls(
            MaxRequests=json_data.get("MaxRequests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNodeGrpcConnectionPool = VirtualNodeGrpcConnectionPool


@dataclass
class ListenerTimeout(BaseModel):
    TCP: Optional["_TcpTimeout"]
    HTTP: Optional["_HttpTimeout"]
    HTTP2: Optional["_HttpTimeout"]
    GRPC: Optional["_GrpcTimeout"]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerTimeout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerTimeout"]:
        if not json_data:
            return None
        return cls(
            TCP=TcpTimeout._deserialize(json_data.get("TCP")),
            HTTP=HttpTimeout._deserialize(json_data.get("HTTP")),
            HTTP2=HttpTimeout._deserialize(json_data.get("HTTP2")),
            GRPC=GrpcTimeout._deserialize(json_data.get("GRPC")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerTimeout = ListenerTimeout


@dataclass
class TcpTimeout(BaseModel):
    Idle: Optional["_Duration"]

    @classmethod
    def _deserialize(
        cls: Type["_TcpTimeout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpTimeout"]:
        if not json_data:
            return None
        return cls(
            Idle=Duration._deserialize(json_data.get("Idle")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpTimeout = TcpTimeout


@dataclass
class Duration(BaseModel):
    Value: Optional[int]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Duration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Duration"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Duration = Duration


@dataclass
class HttpTimeout(BaseModel):
    PerRequest: Optional["_Duration"]
    Idle: Optional["_Duration"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpTimeout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpTimeout"]:
        if not json_data:
            return None
        return cls(
            PerRequest=Duration._deserialize(json_data.get("PerRequest")),
            Idle=Duration._deserialize(json_data.get("Idle")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpTimeout = HttpTimeout


@dataclass
class GrpcTimeout(BaseModel):
    PerRequest: Optional["_Duration"]
    Idle: Optional["_Duration"]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcTimeout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcTimeout"]:
        if not json_data:
            return None
        return cls(
            PerRequest=Duration._deserialize(json_data.get("PerRequest")),
            Idle=Duration._deserialize(json_data.get("Idle")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcTimeout = GrpcTimeout


@dataclass
class HealthCheck(BaseModel):
    Path: Optional[str]
    UnhealthyThreshold: Optional[int]
    Port: Optional[int]
    HealthyThreshold: Optional[int]
    TimeoutMillis: Optional[int]
    Protocol: Optional[str]
    IntervalMillis: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheck"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
            Port=json_data.get("Port"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            TimeoutMillis=json_data.get("TimeoutMillis"),
            Protocol=json_data.get("Protocol"),
            IntervalMillis=json_data.get("IntervalMillis"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheck = HealthCheck


@dataclass
class ListenerTls(BaseModel):
    Validation: Optional["_ListenerTlsValidationContext"]
    Mode: Optional[str]
    Certificate: Optional["_ListenerTlsCertificate"]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerTls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerTls"]:
        if not json_data:
            return None
        return cls(
            Validation=ListenerTlsValidationContext._deserialize(json_data.get("Validation")),
            Mode=json_data.get("Mode"),
            Certificate=ListenerTlsCertificate._deserialize(json_data.get("Certificate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerTls = ListenerTls


@dataclass
class ListenerTlsValidationContext(BaseModel):
    SubjectAlternativeNames: Optional["_SubjectAlternativeNames"]
    Trust: Optional["_ListenerTlsValidationContextTrust"]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerTlsValidationContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerTlsValidationContext"]:
        if not json_data:
            return None
        return cls(
            SubjectAlternativeNames=SubjectAlternativeNames._deserialize(json_data.get("SubjectAlternativeNames")),
            Trust=ListenerTlsValidationContextTrust._deserialize(json_data.get("Trust")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerTlsValidationContext = ListenerTlsValidationContext


@dataclass
class ListenerTlsValidationContextTrust(BaseModel):
    File: Optional["_TlsValidationContextFileTrust"]
    SDS: Optional["_TlsValidationContextSdsTrust"]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerTlsValidationContextTrust"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerTlsValidationContextTrust"]:
        if not json_data:
            return None
        return cls(
            File=TlsValidationContextFileTrust._deserialize(json_data.get("File")),
            SDS=TlsValidationContextSdsTrust._deserialize(json_data.get("SDS")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerTlsValidationContextTrust = ListenerTlsValidationContextTrust


@dataclass
class ListenerTlsCertificate(BaseModel):
    SDS: Optional["_ListenerTlsSdsCertificate"]
    ACM: Optional["_ListenerTlsAcmCertificate"]
    File: Optional["_ListenerTlsFileCertificate"]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerTlsCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerTlsCertificate"]:
        if not json_data:
            return None
        return cls(
            SDS=ListenerTlsSdsCertificate._deserialize(json_data.get("SDS")),
            ACM=ListenerTlsAcmCertificate._deserialize(json_data.get("ACM")),
            File=ListenerTlsFileCertificate._deserialize(json_data.get("File")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerTlsCertificate = ListenerTlsCertificate


@dataclass
class ListenerTlsAcmCertificate(BaseModel):
    CertificateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerTlsAcmCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerTlsAcmCertificate"]:
        if not json_data:
            return None
        return cls(
            CertificateArn=json_data.get("CertificateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerTlsAcmCertificate = ListenerTlsAcmCertificate


@dataclass
class PortMapping(BaseModel):
    Protocol: Optional[str]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PortMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortMapping"]:
        if not json_data:
            return None
        return cls(
            Protocol=json_data.get("Protocol"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortMapping = PortMapping


@dataclass
class OutlierDetection(BaseModel):
    MaxEjectionPercent: Optional[int]
    BaseEjectionDuration: Optional["_Duration"]
    MaxServerErrors: Optional[int]
    Interval: Optional["_Duration"]

    @classmethod
    def _deserialize(
        cls: Type["_OutlierDetection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutlierDetection"]:
        if not json_data:
            return None
        return cls(
            MaxEjectionPercent=json_data.get("MaxEjectionPercent"),
            BaseEjectionDuration=Duration._deserialize(json_data.get("BaseEjectionDuration")),
            MaxServerErrors=json_data.get("MaxServerErrors"),
            Interval=Duration._deserialize(json_data.get("Interval")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutlierDetection = OutlierDetection


@dataclass
class BackendDefaults(BaseModel):
    ClientPolicy: Optional["_ClientPolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_BackendDefaults"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendDefaults"]:
        if not json_data:
            return None
        return cls(
            ClientPolicy=ClientPolicy._deserialize(json_data.get("ClientPolicy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendDefaults = BackendDefaults


@dataclass
class ServiceDiscovery(BaseModel):
    DNS: Optional["_DnsServiceDiscovery"]
    AWSCloudMap: Optional["_AwsCloudMapServiceDiscovery"]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDiscovery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDiscovery"]:
        if not json_data:
            return None
        return cls(
            DNS=DnsServiceDiscovery._deserialize(json_data.get("DNS")),
            AWSCloudMap=AwsCloudMapServiceDiscovery._deserialize(json_data.get("AWSCloudMap")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDiscovery = ServiceDiscovery


@dataclass
class DnsServiceDiscovery(BaseModel):
    Hostname: Optional[str]
    IpPreference: Optional[str]
    ResponseType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsServiceDiscovery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsServiceDiscovery"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            IpPreference=json_data.get("IpPreference"),
            ResponseType=json_data.get("ResponseType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsServiceDiscovery = DnsServiceDiscovery


@dataclass
class AwsCloudMapServiceDiscovery(BaseModel):
    Attributes: Optional[Sequence["_AwsCloudMapInstanceAttribute"]]
    NamespaceName: Optional[str]
    ServiceName: Optional[str]
    IpPreference: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudMapServiceDiscovery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudMapServiceDiscovery"]:
        if not json_data:
            return None
        return cls(
            Attributes=deserialize_list(json_data.get("Attributes"), AwsCloudMapInstanceAttribute),
            NamespaceName=json_data.get("NamespaceName"),
            ServiceName=json_data.get("ServiceName"),
            IpPreference=json_data.get("IpPreference"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudMapServiceDiscovery = AwsCloudMapServiceDiscovery


@dataclass
class AwsCloudMapInstanceAttribute(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudMapInstanceAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudMapInstanceAttribute"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudMapInstanceAttribute = AwsCloudMapInstanceAttribute


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


