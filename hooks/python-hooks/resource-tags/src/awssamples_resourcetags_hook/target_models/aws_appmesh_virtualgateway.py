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
class AwsAppmeshVirtualgateway(BaseModel):
    Uid: Optional[str]
    VirtualGatewayName: Optional[str]
    MeshName: Optional[str]
    MeshOwner: Optional[str]
    ResourceOwner: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Spec: Optional["_VirtualGatewaySpec"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppmeshVirtualgateway"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppmeshVirtualgateway"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Uid=json_data.get("Uid"),
            VirtualGatewayName=json_data.get("VirtualGatewayName"),
            MeshName=json_data.get("MeshName"),
            MeshOwner=json_data.get("MeshOwner"),
            ResourceOwner=json_data.get("ResourceOwner"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Spec=VirtualGatewaySpec._deserialize(json_data.get("Spec")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppmeshVirtualgateway = AwsAppmeshVirtualgateway


@dataclass
class VirtualGatewaySpec(BaseModel):
    Logging: Optional["_VirtualGatewayLogging"]
    Listeners: Optional[Sequence["_VirtualGatewayListener"]]
    BackendDefaults: Optional["_VirtualGatewayBackendDefaults"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewaySpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewaySpec"]:
        if not json_data:
            return None
        return cls(
            Logging=VirtualGatewayLogging._deserialize(json_data.get("Logging")),
            Listeners=deserialize_list(json_data.get("Listeners"), VirtualGatewayListener),
            BackendDefaults=VirtualGatewayBackendDefaults._deserialize(json_data.get("BackendDefaults")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewaySpec = VirtualGatewaySpec


@dataclass
class VirtualGatewayLogging(BaseModel):
    AccessLog: Optional["_VirtualGatewayAccessLog"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayLogging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayLogging"]:
        if not json_data:
            return None
        return cls(
            AccessLog=VirtualGatewayAccessLog._deserialize(json_data.get("AccessLog")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayLogging = VirtualGatewayLogging


@dataclass
class VirtualGatewayAccessLog(BaseModel):
    File: Optional["_VirtualGatewayFileAccessLog"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayAccessLog"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayAccessLog"]:
        if not json_data:
            return None
        return cls(
            File=VirtualGatewayFileAccessLog._deserialize(json_data.get("File")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayAccessLog = VirtualGatewayAccessLog


@dataclass
class VirtualGatewayFileAccessLog(BaseModel):
    Path: Optional[str]
    Format: Optional["_LoggingFormat"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayFileAccessLog"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayFileAccessLog"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Format=LoggingFormat._deserialize(json_data.get("Format")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayFileAccessLog = VirtualGatewayFileAccessLog


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
class VirtualGatewayListener(BaseModel):
    ConnectionPool: Optional["_VirtualGatewayConnectionPool"]
    HealthCheck: Optional["_VirtualGatewayHealthCheckPolicy"]
    TLS: Optional["_VirtualGatewayListenerTls"]
    PortMapping: Optional["_VirtualGatewayPortMapping"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayListener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayListener"]:
        if not json_data:
            return None
        return cls(
            ConnectionPool=VirtualGatewayConnectionPool._deserialize(json_data.get("ConnectionPool")),
            HealthCheck=VirtualGatewayHealthCheckPolicy._deserialize(json_data.get("HealthCheck")),
            TLS=VirtualGatewayListenerTls._deserialize(json_data.get("TLS")),
            PortMapping=VirtualGatewayPortMapping._deserialize(json_data.get("PortMapping")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayListener = VirtualGatewayListener


@dataclass
class VirtualGatewayConnectionPool(BaseModel):
    HTTP: Optional["_VirtualGatewayHttpConnectionPool"]
    HTTP2: Optional["_VirtualGatewayHttp2ConnectionPool"]
    GRPC: Optional["_VirtualGatewayGrpcConnectionPool"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayConnectionPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayConnectionPool"]:
        if not json_data:
            return None
        return cls(
            HTTP=VirtualGatewayHttpConnectionPool._deserialize(json_data.get("HTTP")),
            HTTP2=VirtualGatewayHttp2ConnectionPool._deserialize(json_data.get("HTTP2")),
            GRPC=VirtualGatewayGrpcConnectionPool._deserialize(json_data.get("GRPC")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayConnectionPool = VirtualGatewayConnectionPool


@dataclass
class VirtualGatewayHttpConnectionPool(BaseModel):
    MaxConnections: Optional[int]
    MaxPendingRequests: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayHttpConnectionPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayHttpConnectionPool"]:
        if not json_data:
            return None
        return cls(
            MaxConnections=json_data.get("MaxConnections"),
            MaxPendingRequests=json_data.get("MaxPendingRequests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayHttpConnectionPool = VirtualGatewayHttpConnectionPool


@dataclass
class VirtualGatewayHttp2ConnectionPool(BaseModel):
    MaxRequests: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayHttp2ConnectionPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayHttp2ConnectionPool"]:
        if not json_data:
            return None
        return cls(
            MaxRequests=json_data.get("MaxRequests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayHttp2ConnectionPool = VirtualGatewayHttp2ConnectionPool


@dataclass
class VirtualGatewayGrpcConnectionPool(BaseModel):
    MaxRequests: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayGrpcConnectionPool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayGrpcConnectionPool"]:
        if not json_data:
            return None
        return cls(
            MaxRequests=json_data.get("MaxRequests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayGrpcConnectionPool = VirtualGatewayGrpcConnectionPool


@dataclass
class VirtualGatewayHealthCheckPolicy(BaseModel):
    Path: Optional[str]
    UnhealthyThreshold: Optional[int]
    Port: Optional[int]
    HealthyThreshold: Optional[int]
    TimeoutMillis: Optional[int]
    Protocol: Optional[str]
    IntervalMillis: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayHealthCheckPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayHealthCheckPolicy"]:
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
_VirtualGatewayHealthCheckPolicy = VirtualGatewayHealthCheckPolicy


@dataclass
class VirtualGatewayListenerTls(BaseModel):
    Validation: Optional["_VirtualGatewayListenerTlsValidationContext"]
    Mode: Optional[str]
    Certificate: Optional["_VirtualGatewayListenerTlsCertificate"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayListenerTls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayListenerTls"]:
        if not json_data:
            return None
        return cls(
            Validation=VirtualGatewayListenerTlsValidationContext._deserialize(json_data.get("Validation")),
            Mode=json_data.get("Mode"),
            Certificate=VirtualGatewayListenerTlsCertificate._deserialize(json_data.get("Certificate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayListenerTls = VirtualGatewayListenerTls


@dataclass
class VirtualGatewayListenerTlsValidationContext(BaseModel):
    SubjectAlternativeNames: Optional["_SubjectAlternativeNames"]
    Trust: Optional["_VirtualGatewayListenerTlsValidationContextTrust"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayListenerTlsValidationContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayListenerTlsValidationContext"]:
        if not json_data:
            return None
        return cls(
            SubjectAlternativeNames=SubjectAlternativeNames._deserialize(json_data.get("SubjectAlternativeNames")),
            Trust=VirtualGatewayListenerTlsValidationContextTrust._deserialize(json_data.get("Trust")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayListenerTlsValidationContext = VirtualGatewayListenerTlsValidationContext


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
class VirtualGatewayListenerTlsValidationContextTrust(BaseModel):
    File: Optional["_VirtualGatewayTlsValidationContextFileTrust"]
    SDS: Optional["_VirtualGatewayTlsValidationContextSdsTrust"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayListenerTlsValidationContextTrust"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayListenerTlsValidationContextTrust"]:
        if not json_data:
            return None
        return cls(
            File=VirtualGatewayTlsValidationContextFileTrust._deserialize(json_data.get("File")),
            SDS=VirtualGatewayTlsValidationContextSdsTrust._deserialize(json_data.get("SDS")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayListenerTlsValidationContextTrust = VirtualGatewayListenerTlsValidationContextTrust


@dataclass
class VirtualGatewayTlsValidationContextFileTrust(BaseModel):
    CertificateChain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayTlsValidationContextFileTrust"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayTlsValidationContextFileTrust"]:
        if not json_data:
            return None
        return cls(
            CertificateChain=json_data.get("CertificateChain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayTlsValidationContextFileTrust = VirtualGatewayTlsValidationContextFileTrust


@dataclass
class VirtualGatewayTlsValidationContextSdsTrust(BaseModel):
    SecretName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayTlsValidationContextSdsTrust"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayTlsValidationContextSdsTrust"]:
        if not json_data:
            return None
        return cls(
            SecretName=json_data.get("SecretName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayTlsValidationContextSdsTrust = VirtualGatewayTlsValidationContextSdsTrust


@dataclass
class VirtualGatewayListenerTlsCertificate(BaseModel):
    SDS: Optional["_VirtualGatewayListenerTlsSdsCertificate"]
    ACM: Optional["_VirtualGatewayListenerTlsAcmCertificate"]
    File: Optional["_VirtualGatewayListenerTlsFileCertificate"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayListenerTlsCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayListenerTlsCertificate"]:
        if not json_data:
            return None
        return cls(
            SDS=VirtualGatewayListenerTlsSdsCertificate._deserialize(json_data.get("SDS")),
            ACM=VirtualGatewayListenerTlsAcmCertificate._deserialize(json_data.get("ACM")),
            File=VirtualGatewayListenerTlsFileCertificate._deserialize(json_data.get("File")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayListenerTlsCertificate = VirtualGatewayListenerTlsCertificate


@dataclass
class VirtualGatewayListenerTlsSdsCertificate(BaseModel):
    SecretName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayListenerTlsSdsCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayListenerTlsSdsCertificate"]:
        if not json_data:
            return None
        return cls(
            SecretName=json_data.get("SecretName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayListenerTlsSdsCertificate = VirtualGatewayListenerTlsSdsCertificate


@dataclass
class VirtualGatewayListenerTlsAcmCertificate(BaseModel):
    CertificateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayListenerTlsAcmCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayListenerTlsAcmCertificate"]:
        if not json_data:
            return None
        return cls(
            CertificateArn=json_data.get("CertificateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayListenerTlsAcmCertificate = VirtualGatewayListenerTlsAcmCertificate


@dataclass
class VirtualGatewayListenerTlsFileCertificate(BaseModel):
    CertificateChain: Optional[str]
    PrivateKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayListenerTlsFileCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayListenerTlsFileCertificate"]:
        if not json_data:
            return None
        return cls(
            CertificateChain=json_data.get("CertificateChain"),
            PrivateKey=json_data.get("PrivateKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayListenerTlsFileCertificate = VirtualGatewayListenerTlsFileCertificate


@dataclass
class VirtualGatewayPortMapping(BaseModel):
    Protocol: Optional[str]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayPortMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayPortMapping"]:
        if not json_data:
            return None
        return cls(
            Protocol=json_data.get("Protocol"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayPortMapping = VirtualGatewayPortMapping


@dataclass
class VirtualGatewayBackendDefaults(BaseModel):
    ClientPolicy: Optional["_VirtualGatewayClientPolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayBackendDefaults"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayBackendDefaults"]:
        if not json_data:
            return None
        return cls(
            ClientPolicy=VirtualGatewayClientPolicy._deserialize(json_data.get("ClientPolicy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayBackendDefaults = VirtualGatewayBackendDefaults


@dataclass
class VirtualGatewayClientPolicy(BaseModel):
    TLS: Optional["_VirtualGatewayClientPolicyTls"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayClientPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayClientPolicy"]:
        if not json_data:
            return None
        return cls(
            TLS=VirtualGatewayClientPolicyTls._deserialize(json_data.get("TLS")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayClientPolicy = VirtualGatewayClientPolicy


@dataclass
class VirtualGatewayClientPolicyTls(BaseModel):
    Validation: Optional["_VirtualGatewayTlsValidationContext"]
    Ports: Optional[Sequence[int]]
    Enforce: Optional[bool]
    Certificate: Optional["_VirtualGatewayClientTlsCertificate"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayClientPolicyTls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayClientPolicyTls"]:
        if not json_data:
            return None
        return cls(
            Validation=VirtualGatewayTlsValidationContext._deserialize(json_data.get("Validation")),
            Ports=json_data.get("Ports"),
            Enforce=json_data.get("Enforce"),
            Certificate=VirtualGatewayClientTlsCertificate._deserialize(json_data.get("Certificate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayClientPolicyTls = VirtualGatewayClientPolicyTls


@dataclass
class VirtualGatewayTlsValidationContext(BaseModel):
    SubjectAlternativeNames: Optional["_SubjectAlternativeNames"]
    Trust: Optional["_VirtualGatewayTlsValidationContextTrust"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayTlsValidationContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayTlsValidationContext"]:
        if not json_data:
            return None
        return cls(
            SubjectAlternativeNames=SubjectAlternativeNames._deserialize(json_data.get("SubjectAlternativeNames")),
            Trust=VirtualGatewayTlsValidationContextTrust._deserialize(json_data.get("Trust")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayTlsValidationContext = VirtualGatewayTlsValidationContext


@dataclass
class VirtualGatewayTlsValidationContextTrust(BaseModel):
    SDS: Optional["_VirtualGatewayTlsValidationContextSdsTrust"]
    ACM: Optional["_VirtualGatewayTlsValidationContextAcmTrust"]
    File: Optional["_VirtualGatewayTlsValidationContextFileTrust"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayTlsValidationContextTrust"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayTlsValidationContextTrust"]:
        if not json_data:
            return None
        return cls(
            SDS=VirtualGatewayTlsValidationContextSdsTrust._deserialize(json_data.get("SDS")),
            ACM=VirtualGatewayTlsValidationContextAcmTrust._deserialize(json_data.get("ACM")),
            File=VirtualGatewayTlsValidationContextFileTrust._deserialize(json_data.get("File")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayTlsValidationContextTrust = VirtualGatewayTlsValidationContextTrust


@dataclass
class VirtualGatewayTlsValidationContextAcmTrust(BaseModel):
    CertificateAuthorityArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayTlsValidationContextAcmTrust"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayTlsValidationContextAcmTrust"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthorityArns=json_data.get("CertificateAuthorityArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayTlsValidationContextAcmTrust = VirtualGatewayTlsValidationContextAcmTrust


@dataclass
class VirtualGatewayClientTlsCertificate(BaseModel):
    File: Optional["_VirtualGatewayListenerTlsFileCertificate"]
    SDS: Optional["_VirtualGatewayListenerTlsSdsCertificate"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualGatewayClientTlsCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualGatewayClientTlsCertificate"]:
        if not json_data:
            return None
        return cls(
            File=VirtualGatewayListenerTlsFileCertificate._deserialize(json_data.get("File")),
            SDS=VirtualGatewayListenerTlsSdsCertificate._deserialize(json_data.get("SDS")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualGatewayClientTlsCertificate = VirtualGatewayClientTlsCertificate


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


