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
class AwsAppmeshGatewayroute(BaseModel):
    Uid: Optional[str]
    MeshName: Optional[str]
    VirtualGatewayName: Optional[str]
    MeshOwner: Optional[str]
    ResourceOwner: Optional[str]
    GatewayRouteName: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Spec: Optional["_GatewayRouteSpec"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppmeshGatewayroute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppmeshGatewayroute"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Uid=json_data.get("Uid"),
            MeshName=json_data.get("MeshName"),
            VirtualGatewayName=json_data.get("VirtualGatewayName"),
            MeshOwner=json_data.get("MeshOwner"),
            ResourceOwner=json_data.get("ResourceOwner"),
            GatewayRouteName=json_data.get("GatewayRouteName"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Spec=GatewayRouteSpec._deserialize(json_data.get("Spec")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppmeshGatewayroute = AwsAppmeshGatewayroute


@dataclass
class GatewayRouteSpec(BaseModel):
    HttpRoute: Optional["_HttpGatewayRoute"]
    Http2Route: Optional["_HttpGatewayRoute"]
    GrpcRoute: Optional["_GrpcGatewayRoute"]
    Priority: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayRouteSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayRouteSpec"]:
        if not json_data:
            return None
        return cls(
            HttpRoute=HttpGatewayRoute._deserialize(json_data.get("HttpRoute")),
            Http2Route=HttpGatewayRoute._deserialize(json_data.get("Http2Route")),
            GrpcRoute=GrpcGatewayRoute._deserialize(json_data.get("GrpcRoute")),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayRouteSpec = GatewayRouteSpec


@dataclass
class HttpGatewayRoute(BaseModel):
    Action: Optional["_HttpGatewayRouteAction"]
    Match: Optional["_HttpGatewayRouteMatch"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGatewayRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGatewayRoute"]:
        if not json_data:
            return None
        return cls(
            Action=HttpGatewayRouteAction._deserialize(json_data.get("Action")),
            Match=HttpGatewayRouteMatch._deserialize(json_data.get("Match")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGatewayRoute = HttpGatewayRoute


@dataclass
class HttpGatewayRouteAction(BaseModel):
    Target: Optional["_GatewayRouteTarget"]
    Rewrite: Optional["_HttpGatewayRouteRewrite"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGatewayRouteAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGatewayRouteAction"]:
        if not json_data:
            return None
        return cls(
            Target=GatewayRouteTarget._deserialize(json_data.get("Target")),
            Rewrite=HttpGatewayRouteRewrite._deserialize(json_data.get("Rewrite")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGatewayRouteAction = HttpGatewayRouteAction


@dataclass
class GatewayRouteTarget(BaseModel):
    VirtualService: Optional["_GatewayRouteVirtualService"]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayRouteTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayRouteTarget"]:
        if not json_data:
            return None
        return cls(
            VirtualService=GatewayRouteVirtualService._deserialize(json_data.get("VirtualService")),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayRouteTarget = GatewayRouteTarget


@dataclass
class GatewayRouteVirtualService(BaseModel):
    VirtualServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayRouteVirtualService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayRouteVirtualService"]:
        if not json_data:
            return None
        return cls(
            VirtualServiceName=json_data.get("VirtualServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayRouteVirtualService = GatewayRouteVirtualService


@dataclass
class HttpGatewayRouteRewrite(BaseModel):
    Path: Optional["_HttpGatewayRoutePathRewrite"]
    Hostname: Optional["_GatewayRouteHostnameRewrite"]
    Prefix: Optional["_HttpGatewayRoutePrefixRewrite"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGatewayRouteRewrite"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGatewayRouteRewrite"]:
        if not json_data:
            return None
        return cls(
            Path=HttpGatewayRoutePathRewrite._deserialize(json_data.get("Path")),
            Hostname=GatewayRouteHostnameRewrite._deserialize(json_data.get("Hostname")),
            Prefix=HttpGatewayRoutePrefixRewrite._deserialize(json_data.get("Prefix")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGatewayRouteRewrite = HttpGatewayRouteRewrite


@dataclass
class HttpGatewayRoutePathRewrite(BaseModel):
    Exact: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGatewayRoutePathRewrite"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGatewayRoutePathRewrite"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGatewayRoutePathRewrite = HttpGatewayRoutePathRewrite


@dataclass
class GatewayRouteHostnameRewrite(BaseModel):
    DefaultTargetHostname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayRouteHostnameRewrite"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayRouteHostnameRewrite"]:
        if not json_data:
            return None
        return cls(
            DefaultTargetHostname=json_data.get("DefaultTargetHostname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayRouteHostnameRewrite = GatewayRouteHostnameRewrite


@dataclass
class HttpGatewayRoutePrefixRewrite(BaseModel):
    Value: Optional[str]
    DefaultPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGatewayRoutePrefixRewrite"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGatewayRoutePrefixRewrite"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            DefaultPrefix=json_data.get("DefaultPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGatewayRoutePrefixRewrite = HttpGatewayRoutePrefixRewrite


@dataclass
class HttpGatewayRouteMatch(BaseModel):
    Path: Optional["_HttpPathMatch"]
    Headers: Optional[Sequence["_HttpGatewayRouteHeader"]]
    Port: Optional[int]
    Hostname: Optional["_GatewayRouteHostnameMatch"]
    Prefix: Optional[str]
    Method: Optional[str]
    QueryParameters: Optional[Sequence["_QueryParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGatewayRouteMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGatewayRouteMatch"]:
        if not json_data:
            return None
        return cls(
            Path=HttpPathMatch._deserialize(json_data.get("Path")),
            Headers=deserialize_list(json_data.get("Headers"), HttpGatewayRouteHeader),
            Port=json_data.get("Port"),
            Hostname=GatewayRouteHostnameMatch._deserialize(json_data.get("Hostname")),
            Prefix=json_data.get("Prefix"),
            Method=json_data.get("Method"),
            QueryParameters=deserialize_list(json_data.get("QueryParameters"), QueryParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGatewayRouteMatch = HttpGatewayRouteMatch


@dataclass
class HttpPathMatch(BaseModel):
    Regex: Optional[str]
    Exact: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpPathMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpPathMatch"]:
        if not json_data:
            return None
        return cls(
            Regex=json_data.get("Regex"),
            Exact=json_data.get("Exact"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpPathMatch = HttpPathMatch


@dataclass
class HttpGatewayRouteHeader(BaseModel):
    Invert: Optional[bool]
    Name: Optional[str]
    Match: Optional["_HttpGatewayRouteHeaderMatch"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGatewayRouteHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGatewayRouteHeader"]:
        if not json_data:
            return None
        return cls(
            Invert=json_data.get("Invert"),
            Name=json_data.get("Name"),
            Match=HttpGatewayRouteHeaderMatch._deserialize(json_data.get("Match")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGatewayRouteHeader = HttpGatewayRouteHeader


@dataclass
class HttpGatewayRouteHeaderMatch(BaseModel):
    Suffix: Optional[str]
    Exact: Optional[str]
    Prefix: Optional[str]
    Regex: Optional[str]
    Range: Optional["_GatewayRouteRangeMatch"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpGatewayRouteHeaderMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpGatewayRouteHeaderMatch"]:
        if not json_data:
            return None
        return cls(
            Suffix=json_data.get("Suffix"),
            Exact=json_data.get("Exact"),
            Prefix=json_data.get("Prefix"),
            Regex=json_data.get("Regex"),
            Range=GatewayRouteRangeMatch._deserialize(json_data.get("Range")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpGatewayRouteHeaderMatch = HttpGatewayRouteHeaderMatch


@dataclass
class GatewayRouteRangeMatch(BaseModel):
    Start: Optional[int]
    End: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayRouteRangeMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayRouteRangeMatch"]:
        if not json_data:
            return None
        return cls(
            Start=json_data.get("Start"),
            End=json_data.get("End"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayRouteRangeMatch = GatewayRouteRangeMatch


@dataclass
class GatewayRouteHostnameMatch(BaseModel):
    Suffix: Optional[str]
    Exact: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayRouteHostnameMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayRouteHostnameMatch"]:
        if not json_data:
            return None
        return cls(
            Suffix=json_data.get("Suffix"),
            Exact=json_data.get("Exact"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayRouteHostnameMatch = GatewayRouteHostnameMatch


@dataclass
class QueryParameter(BaseModel):
    Name: Optional[str]
    Match: Optional["_HttpQueryParameterMatch"]

    @classmethod
    def _deserialize(
        cls: Type["_QueryParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryParameter"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Match=HttpQueryParameterMatch._deserialize(json_data.get("Match")),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryParameter = QueryParameter


@dataclass
class HttpQueryParameterMatch(BaseModel):
    Exact: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpQueryParameterMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpQueryParameterMatch"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpQueryParameterMatch = HttpQueryParameterMatch


@dataclass
class GrpcGatewayRoute(BaseModel):
    Action: Optional["_GrpcGatewayRouteAction"]
    Match: Optional["_GrpcGatewayRouteMatch"]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcGatewayRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcGatewayRoute"]:
        if not json_data:
            return None
        return cls(
            Action=GrpcGatewayRouteAction._deserialize(json_data.get("Action")),
            Match=GrpcGatewayRouteMatch._deserialize(json_data.get("Match")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcGatewayRoute = GrpcGatewayRoute


@dataclass
class GrpcGatewayRouteAction(BaseModel):
    Target: Optional["_GatewayRouteTarget"]
    Rewrite: Optional["_GrpcGatewayRouteRewrite"]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcGatewayRouteAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcGatewayRouteAction"]:
        if not json_data:
            return None
        return cls(
            Target=GatewayRouteTarget._deserialize(json_data.get("Target")),
            Rewrite=GrpcGatewayRouteRewrite._deserialize(json_data.get("Rewrite")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcGatewayRouteAction = GrpcGatewayRouteAction


@dataclass
class GrpcGatewayRouteRewrite(BaseModel):
    Hostname: Optional["_GatewayRouteHostnameRewrite"]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcGatewayRouteRewrite"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcGatewayRouteRewrite"]:
        if not json_data:
            return None
        return cls(
            Hostname=GatewayRouteHostnameRewrite._deserialize(json_data.get("Hostname")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcGatewayRouteRewrite = GrpcGatewayRouteRewrite


@dataclass
class GrpcGatewayRouteMatch(BaseModel):
    Hostname: Optional["_GatewayRouteHostnameMatch"]
    Metadata: Optional[Sequence["_GrpcGatewayRouteMetadata"]]
    ServiceName: Optional[str]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcGatewayRouteMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcGatewayRouteMatch"]:
        if not json_data:
            return None
        return cls(
            Hostname=GatewayRouteHostnameMatch._deserialize(json_data.get("Hostname")),
            Metadata=deserialize_list(json_data.get("Metadata"), GrpcGatewayRouteMetadata),
            ServiceName=json_data.get("ServiceName"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcGatewayRouteMatch = GrpcGatewayRouteMatch


@dataclass
class GrpcGatewayRouteMetadata(BaseModel):
    Invert: Optional[bool]
    Name: Optional[str]
    Match: Optional["_GatewayRouteMetadataMatch"]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcGatewayRouteMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcGatewayRouteMetadata"]:
        if not json_data:
            return None
        return cls(
            Invert=json_data.get("Invert"),
            Name=json_data.get("Name"),
            Match=GatewayRouteMetadataMatch._deserialize(json_data.get("Match")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcGatewayRouteMetadata = GrpcGatewayRouteMetadata


@dataclass
class GatewayRouteMetadataMatch(BaseModel):
    Suffix: Optional[str]
    Exact: Optional[str]
    Prefix: Optional[str]
    Regex: Optional[str]
    Range: Optional["_GatewayRouteRangeMatch"]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayRouteMetadataMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayRouteMetadataMatch"]:
        if not json_data:
            return None
        return cls(
            Suffix=json_data.get("Suffix"),
            Exact=json_data.get("Exact"),
            Prefix=json_data.get("Prefix"),
            Regex=json_data.get("Regex"),
            Range=GatewayRouteRangeMatch._deserialize(json_data.get("Range")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayRouteMetadataMatch = GatewayRouteMetadataMatch


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


