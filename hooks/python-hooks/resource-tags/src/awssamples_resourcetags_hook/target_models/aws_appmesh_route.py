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
class AwsAppmeshRoute(BaseModel):
    Uid: Optional[str]
    MeshName: Optional[str]
    VirtualRouterName: Optional[str]
    MeshOwner: Optional[str]
    ResourceOwner: Optional[str]
    RouteName: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Spec: Optional["_RouteSpec"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppmeshRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppmeshRoute"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Uid=json_data.get("Uid"),
            MeshName=json_data.get("MeshName"),
            VirtualRouterName=json_data.get("VirtualRouterName"),
            MeshOwner=json_data.get("MeshOwner"),
            ResourceOwner=json_data.get("ResourceOwner"),
            RouteName=json_data.get("RouteName"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Spec=RouteSpec._deserialize(json_data.get("Spec")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppmeshRoute = AwsAppmeshRoute


@dataclass
class RouteSpec(BaseModel):
    HttpRoute: Optional["_HttpRoute"]
    Http2Route: Optional["_HttpRoute"]
    GrpcRoute: Optional["_GrpcRoute"]
    TcpRoute: Optional["_TcpRoute"]
    Priority: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RouteSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteSpec"]:
        if not json_data:
            return None
        return cls(
            HttpRoute=HttpRoute._deserialize(json_data.get("HttpRoute")),
            Http2Route=HttpRoute._deserialize(json_data.get("Http2Route")),
            GrpcRoute=GrpcRoute._deserialize(json_data.get("GrpcRoute")),
            TcpRoute=TcpRoute._deserialize(json_data.get("TcpRoute")),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteSpec = RouteSpec


@dataclass
class HttpRoute(BaseModel):
    Action: Optional["_HttpRouteAction"]
    RetryPolicy: Optional["_HttpRetryPolicy"]
    Timeout: Optional["_HttpTimeout"]
    Match: Optional["_HttpRouteMatch"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRoute"]:
        if not json_data:
            return None
        return cls(
            Action=HttpRouteAction._deserialize(json_data.get("Action")),
            RetryPolicy=HttpRetryPolicy._deserialize(json_data.get("RetryPolicy")),
            Timeout=HttpTimeout._deserialize(json_data.get("Timeout")),
            Match=HttpRouteMatch._deserialize(json_data.get("Match")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRoute = HttpRoute


@dataclass
class HttpRouteAction(BaseModel):
    WeightedTargets: Optional[Sequence["_WeightedTarget"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRouteAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRouteAction"]:
        if not json_data:
            return None
        return cls(
            WeightedTargets=deserialize_list(json_data.get("WeightedTargets"), WeightedTarget),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRouteAction = HttpRouteAction


@dataclass
class WeightedTarget(BaseModel):
    VirtualNode: Optional[str]
    Weight: Optional[int]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_WeightedTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeightedTarget"]:
        if not json_data:
            return None
        return cls(
            VirtualNode=json_data.get("VirtualNode"),
            Weight=json_data.get("Weight"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeightedTarget = WeightedTarget


@dataclass
class HttpRetryPolicy(BaseModel):
    MaxRetries: Optional[int]
    TcpRetryEvents: Optional[Sequence[str]]
    PerRetryTimeout: Optional["_Duration"]
    HttpRetryEvents: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRetryPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRetryPolicy"]:
        if not json_data:
            return None
        return cls(
            MaxRetries=json_data.get("MaxRetries"),
            TcpRetryEvents=json_data.get("TcpRetryEvents"),
            PerRetryTimeout=Duration._deserialize(json_data.get("PerRetryTimeout")),
            HttpRetryEvents=json_data.get("HttpRetryEvents"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRetryPolicy = HttpRetryPolicy


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
class HttpRouteMatch(BaseModel):
    Path: Optional["_HttpPathMatch"]
    Scheme: Optional[str]
    Headers: Optional[Sequence["_HttpRouteHeader"]]
    Port: Optional[int]
    Prefix: Optional[str]
    Method: Optional[str]
    QueryParameters: Optional[Sequence["_QueryParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRouteMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRouteMatch"]:
        if not json_data:
            return None
        return cls(
            Path=HttpPathMatch._deserialize(json_data.get("Path")),
            Scheme=json_data.get("Scheme"),
            Headers=deserialize_list(json_data.get("Headers"), HttpRouteHeader),
            Port=json_data.get("Port"),
            Prefix=json_data.get("Prefix"),
            Method=json_data.get("Method"),
            QueryParameters=deserialize_list(json_data.get("QueryParameters"), QueryParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRouteMatch = HttpRouteMatch


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
class HttpRouteHeader(BaseModel):
    Invert: Optional[bool]
    Name: Optional[str]
    Match: Optional["_HeaderMatchMethod"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRouteHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRouteHeader"]:
        if not json_data:
            return None
        return cls(
            Invert=json_data.get("Invert"),
            Name=json_data.get("Name"),
            Match=HeaderMatchMethod._deserialize(json_data.get("Match")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRouteHeader = HttpRouteHeader


@dataclass
class HeaderMatchMethod(BaseModel):
    Suffix: Optional[str]
    Exact: Optional[str]
    Prefix: Optional[str]
    Regex: Optional[str]
    Range: Optional["_MatchRange"]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderMatchMethod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderMatchMethod"]:
        if not json_data:
            return None
        return cls(
            Suffix=json_data.get("Suffix"),
            Exact=json_data.get("Exact"),
            Prefix=json_data.get("Prefix"),
            Regex=json_data.get("Regex"),
            Range=MatchRange._deserialize(json_data.get("Range")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderMatchMethod = HeaderMatchMethod


@dataclass
class MatchRange(BaseModel):
    Start: Optional[int]
    End: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MatchRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchRange"]:
        if not json_data:
            return None
        return cls(
            Start=json_data.get("Start"),
            End=json_data.get("End"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchRange = MatchRange


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
class GrpcRoute(BaseModel):
    Action: Optional["_GrpcRouteAction"]
    RetryPolicy: Optional["_GrpcRetryPolicy"]
    Timeout: Optional["_GrpcTimeout"]
    Match: Optional["_GrpcRouteMatch"]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcRoute"]:
        if not json_data:
            return None
        return cls(
            Action=GrpcRouteAction._deserialize(json_data.get("Action")),
            RetryPolicy=GrpcRetryPolicy._deserialize(json_data.get("RetryPolicy")),
            Timeout=GrpcTimeout._deserialize(json_data.get("Timeout")),
            Match=GrpcRouteMatch._deserialize(json_data.get("Match")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcRoute = GrpcRoute


@dataclass
class GrpcRouteAction(BaseModel):
    WeightedTargets: Optional[Sequence["_WeightedTarget"]]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcRouteAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcRouteAction"]:
        if not json_data:
            return None
        return cls(
            WeightedTargets=deserialize_list(json_data.get("WeightedTargets"), WeightedTarget),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcRouteAction = GrpcRouteAction


@dataclass
class GrpcRetryPolicy(BaseModel):
    MaxRetries: Optional[int]
    TcpRetryEvents: Optional[Sequence[str]]
    PerRetryTimeout: Optional["_Duration"]
    GrpcRetryEvents: Optional[Sequence[str]]
    HttpRetryEvents: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcRetryPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcRetryPolicy"]:
        if not json_data:
            return None
        return cls(
            MaxRetries=json_data.get("MaxRetries"),
            TcpRetryEvents=json_data.get("TcpRetryEvents"),
            PerRetryTimeout=Duration._deserialize(json_data.get("PerRetryTimeout")),
            GrpcRetryEvents=json_data.get("GrpcRetryEvents"),
            HttpRetryEvents=json_data.get("HttpRetryEvents"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcRetryPolicy = GrpcRetryPolicy


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
class GrpcRouteMatch(BaseModel):
    Metadata: Optional[Sequence["_GrpcRouteMetadata"]]
    MethodName: Optional[str]
    ServiceName: Optional[str]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcRouteMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcRouteMatch"]:
        if not json_data:
            return None
        return cls(
            Metadata=deserialize_list(json_data.get("Metadata"), GrpcRouteMetadata),
            MethodName=json_data.get("MethodName"),
            ServiceName=json_data.get("ServiceName"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcRouteMatch = GrpcRouteMatch


@dataclass
class GrpcRouteMetadata(BaseModel):
    Invert: Optional[bool]
    Name: Optional[str]
    Match: Optional["_GrpcRouteMetadataMatchMethod"]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcRouteMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcRouteMetadata"]:
        if not json_data:
            return None
        return cls(
            Invert=json_data.get("Invert"),
            Name=json_data.get("Name"),
            Match=GrpcRouteMetadataMatchMethod._deserialize(json_data.get("Match")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcRouteMetadata = GrpcRouteMetadata


@dataclass
class GrpcRouteMetadataMatchMethod(BaseModel):
    Suffix: Optional[str]
    Exact: Optional[str]
    Prefix: Optional[str]
    Regex: Optional[str]
    Range: Optional["_MatchRange"]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcRouteMetadataMatchMethod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcRouteMetadataMatchMethod"]:
        if not json_data:
            return None
        return cls(
            Suffix=json_data.get("Suffix"),
            Exact=json_data.get("Exact"),
            Prefix=json_data.get("Prefix"),
            Regex=json_data.get("Regex"),
            Range=MatchRange._deserialize(json_data.get("Range")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcRouteMetadataMatchMethod = GrpcRouteMetadataMatchMethod


@dataclass
class TcpRoute(BaseModel):
    Action: Optional["_TcpRouteAction"]
    Timeout: Optional["_TcpTimeout"]
    Match: Optional["_TcpRouteMatch"]

    @classmethod
    def _deserialize(
        cls: Type["_TcpRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpRoute"]:
        if not json_data:
            return None
        return cls(
            Action=TcpRouteAction._deserialize(json_data.get("Action")),
            Timeout=TcpTimeout._deserialize(json_data.get("Timeout")),
            Match=TcpRouteMatch._deserialize(json_data.get("Match")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpRoute = TcpRoute


@dataclass
class TcpRouteAction(BaseModel):
    WeightedTargets: Optional[Sequence["_WeightedTarget"]]

    @classmethod
    def _deserialize(
        cls: Type["_TcpRouteAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpRouteAction"]:
        if not json_data:
            return None
        return cls(
            WeightedTargets=deserialize_list(json_data.get("WeightedTargets"), WeightedTarget),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpRouteAction = TcpRouteAction


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
class TcpRouteMatch(BaseModel):
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TcpRouteMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpRouteMatch"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpRouteMatch = TcpRouteMatch


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


