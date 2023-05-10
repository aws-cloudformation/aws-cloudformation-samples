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
class AwsEc2Networkinsightsanalysis(BaseModel):
    Status: Optional[str]
    ReturnPathComponents: Optional[Sequence["_PathComponent"]]
    NetworkInsightsAnalysisId: Optional[str]
    NetworkInsightsPathId: Optional[str]
    NetworkPathFound: Optional[bool]
    SuggestedAccounts: Optional[Sequence[str]]
    FilterInArns: Optional[Sequence[str]]
    NetworkInsightsAnalysisArn: Optional[str]
    StatusMessage: Optional[str]
    StartDate: Optional[str]
    AlternatePathHints: Optional[Sequence["_AlternatePathHint"]]
    Explanations: Optional[Sequence["_Explanation"]]
    ForwardPathComponents: Optional[Sequence["_PathComponent"]]
    AdditionalAccounts: Optional[Sequence[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Networkinsightsanalysis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Networkinsightsanalysis"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Status=json_data.get("Status"),
            ReturnPathComponents=deserialize_list(json_data.get("ReturnPathComponents"), PathComponent),
            NetworkInsightsAnalysisId=json_data.get("NetworkInsightsAnalysisId"),
            NetworkInsightsPathId=json_data.get("NetworkInsightsPathId"),
            NetworkPathFound=json_data.get("NetworkPathFound"),
            SuggestedAccounts=json_data.get("SuggestedAccounts"),
            FilterInArns=json_data.get("FilterInArns"),
            NetworkInsightsAnalysisArn=json_data.get("NetworkInsightsAnalysisArn"),
            StatusMessage=json_data.get("StatusMessage"),
            StartDate=json_data.get("StartDate"),
            AlternatePathHints=deserialize_list(json_data.get("AlternatePathHints"), AlternatePathHint),
            Explanations=deserialize_list(json_data.get("Explanations"), Explanation),
            ForwardPathComponents=deserialize_list(json_data.get("ForwardPathComponents"), PathComponent),
            AdditionalAccounts=json_data.get("AdditionalAccounts"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Networkinsightsanalysis = AwsEc2Networkinsightsanalysis


@dataclass
class PathComponent(BaseModel):
    AdditionalDetails: Optional[Sequence["_AdditionalDetail"]]
    InboundHeader: Optional["_AnalysisPacketHeader"]
    Vpc: Optional["_AnalysisComponent"]
    DestinationVpc: Optional["_AnalysisComponent"]
    SecurityGroupRule: Optional["_AnalysisSecurityGroupRule"]
    TransitGateway: Optional["_AnalysisComponent"]
    ElasticLoadBalancerListener: Optional["_AnalysisComponent"]
    Explanations: Optional[Sequence["_Explanation"]]
    ServiceName: Optional[str]
    SequenceNumber: Optional[int]
    SourceVpc: Optional["_AnalysisComponent"]
    OutboundHeader: Optional["_AnalysisPacketHeader"]
    AclRule: Optional["_AnalysisAclRule"]
    TransitGatewayRouteTableRoute: Optional["_TransitGatewayRouteTableRoute"]
    Component: Optional["_AnalysisComponent"]
    Subnet: Optional["_AnalysisComponent"]
    RouteTableRoute: Optional["_AnalysisRouteTableRoute"]

    @classmethod
    def _deserialize(
        cls: Type["_PathComponent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathComponent"]:
        if not json_data:
            return None
        return cls(
            AdditionalDetails=deserialize_list(json_data.get("AdditionalDetails"), AdditionalDetail),
            InboundHeader=AnalysisPacketHeader._deserialize(json_data.get("InboundHeader")),
            Vpc=AnalysisComponent._deserialize(json_data.get("Vpc")),
            DestinationVpc=AnalysisComponent._deserialize(json_data.get("DestinationVpc")),
            SecurityGroupRule=AnalysisSecurityGroupRule._deserialize(json_data.get("SecurityGroupRule")),
            TransitGateway=AnalysisComponent._deserialize(json_data.get("TransitGateway")),
            ElasticLoadBalancerListener=AnalysisComponent._deserialize(json_data.get("ElasticLoadBalancerListener")),
            Explanations=deserialize_list(json_data.get("Explanations"), Explanation),
            ServiceName=json_data.get("ServiceName"),
            SequenceNumber=json_data.get("SequenceNumber"),
            SourceVpc=AnalysisComponent._deserialize(json_data.get("SourceVpc")),
            OutboundHeader=AnalysisPacketHeader._deserialize(json_data.get("OutboundHeader")),
            AclRule=AnalysisAclRule._deserialize(json_data.get("AclRule")),
            TransitGatewayRouteTableRoute=TransitGatewayRouteTableRoute._deserialize(json_data.get("TransitGatewayRouteTableRoute")),
            Component=AnalysisComponent._deserialize(json_data.get("Component")),
            Subnet=AnalysisComponent._deserialize(json_data.get("Subnet")),
            RouteTableRoute=AnalysisRouteTableRoute._deserialize(json_data.get("RouteTableRoute")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathComponent = PathComponent


@dataclass
class AdditionalDetail(BaseModel):
    ServiceName: Optional[str]
    AdditionalDetailType: Optional[str]
    LoadBalancers: Optional[Sequence["_AnalysisComponent"]]
    Component: Optional["_AnalysisComponent"]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalDetail"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalDetail"]:
        if not json_data:
            return None
        return cls(
            ServiceName=json_data.get("ServiceName"),
            AdditionalDetailType=json_data.get("AdditionalDetailType"),
            LoadBalancers=deserialize_list(json_data.get("LoadBalancers"), AnalysisComponent),
            Component=AnalysisComponent._deserialize(json_data.get("Component")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalDetail = AdditionalDetail


@dataclass
class AnalysisComponent(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisComponent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisComponent"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisComponent = AnalysisComponent


@dataclass
class AnalysisPacketHeader(BaseModel):
    DestinationPortRanges: Optional[Sequence["_PortRange"]]
    SourcePortRanges: Optional[Sequence["_PortRange"]]
    DestinationAddresses: Optional[Sequence[str]]
    Protocol: Optional[str]
    SourceAddresses: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisPacketHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisPacketHeader"]:
        if not json_data:
            return None
        return cls(
            DestinationPortRanges=deserialize_list(json_data.get("DestinationPortRanges"), PortRange),
            SourcePortRanges=deserialize_list(json_data.get("SourcePortRanges"), PortRange),
            DestinationAddresses=json_data.get("DestinationAddresses"),
            Protocol=json_data.get("Protocol"),
            SourceAddresses=json_data.get("SourceAddresses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisPacketHeader = AnalysisPacketHeader


@dataclass
class PortRange(BaseModel):
    From: Optional[int]
    To: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PortRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortRange"]:
        if not json_data:
            return None
        return cls(
            From=json_data.get("From"),
            To=json_data.get("To"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortRange = PortRange


@dataclass
class AnalysisSecurityGroupRule(BaseModel):
    PortRange: Optional["_PortRange"]
    Cidr: Optional[str]
    PrefixListId: Optional[str]
    SecurityGroupId: Optional[str]
    Protocol: Optional[str]
    Direction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisSecurityGroupRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisSecurityGroupRule"]:
        if not json_data:
            return None
        return cls(
            PortRange=PortRange._deserialize(json_data.get("PortRange")),
            Cidr=json_data.get("Cidr"),
            PrefixListId=json_data.get("PrefixListId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Protocol=json_data.get("Protocol"),
            Direction=json_data.get("Direction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisSecurityGroupRule = AnalysisSecurityGroupRule


@dataclass
class Explanation(BaseModel):
    VpnGateway: Optional["_AnalysisComponent"]
    PacketField: Optional[str]
    TransitGatewayAttachment: Optional["_AnalysisComponent"]
    Protocols: Optional[Sequence[str]]
    IngressRouteTable: Optional["_AnalysisComponent"]
    ClassicLoadBalancerListener: Optional["_AnalysisLoadBalancerListener"]
    VpcPeeringConnection: Optional["_AnalysisComponent"]
    Address: Optional[str]
    Port: Optional[int]
    Addresses: Optional[Sequence[str]]
    ElasticLoadBalancerListener: Optional["_AnalysisComponent"]
    TransitGatewayRouteTable: Optional["_AnalysisComponent"]
    ExplanationCode: Optional[str]
    InternetGateway: Optional["_AnalysisComponent"]
    SourceVpc: Optional["_AnalysisComponent"]
    AttachedTo: Optional["_AnalysisComponent"]
    PrefixList: Optional["_AnalysisComponent"]
    TransitGatewayRouteTableRoute: Optional["_TransitGatewayRouteTableRoute"]
    ComponentRegion: Optional[str]
    LoadBalancerTargetGroup: Optional["_AnalysisComponent"]
    NetworkInterface: Optional["_AnalysisComponent"]
    CustomerGateway: Optional["_AnalysisComponent"]
    DestinationVpc: Optional["_AnalysisComponent"]
    SecurityGroup: Optional["_AnalysisComponent"]
    TransitGateway: Optional["_AnalysisComponent"]
    RouteTable: Optional["_AnalysisComponent"]
    State: Optional[str]
    LoadBalancerListenerPort: Optional[int]
    vpcEndpoint: Optional["_AnalysisComponent"]
    Subnet: Optional["_AnalysisComponent"]
    Cidrs: Optional[Sequence[str]]
    Destination: Optional["_AnalysisComponent"]
    SecurityGroups: Optional[Sequence["_AnalysisComponent"]]
    ComponentAccount: Optional[str]
    VpnConnection: Optional["_AnalysisComponent"]
    Vpc: Optional["_AnalysisComponent"]
    NatGateway: Optional["_AnalysisComponent"]
    Direction: Optional[str]
    LoadBalancerTargetPort: Optional[int]
    LoadBalancerTarget: Optional["_AnalysisLoadBalancerTarget"]
    LoadBalancerTargetGroups: Optional[Sequence["_AnalysisComponent"]]
    Component: Optional["_AnalysisComponent"]
    MissingComponent: Optional[str]
    RouteTableRoute: Optional["_AnalysisRouteTableRoute"]
    AvailabilityZones: Optional[Sequence[str]]
    PortRanges: Optional[Sequence["_PortRange"]]
    Acl: Optional["_AnalysisComponent"]
    SecurityGroupRule: Optional["_AnalysisSecurityGroupRule"]
    SubnetRouteTable: Optional["_AnalysisComponent"]
    LoadBalancerArn: Optional[str]
    AclRule: Optional["_AnalysisAclRule"]

    @classmethod
    def _deserialize(
        cls: Type["_Explanation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Explanation"]:
        if not json_data:
            return None
        return cls(
            VpnGateway=AnalysisComponent._deserialize(json_data.get("VpnGateway")),
            PacketField=json_data.get("PacketField"),
            TransitGatewayAttachment=AnalysisComponent._deserialize(json_data.get("TransitGatewayAttachment")),
            Protocols=json_data.get("Protocols"),
            IngressRouteTable=AnalysisComponent._deserialize(json_data.get("IngressRouteTable")),
            ClassicLoadBalancerListener=AnalysisLoadBalancerListener._deserialize(json_data.get("ClassicLoadBalancerListener")),
            VpcPeeringConnection=AnalysisComponent._deserialize(json_data.get("VpcPeeringConnection")),
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
            Addresses=json_data.get("Addresses"),
            ElasticLoadBalancerListener=AnalysisComponent._deserialize(json_data.get("ElasticLoadBalancerListener")),
            TransitGatewayRouteTable=AnalysisComponent._deserialize(json_data.get("TransitGatewayRouteTable")),
            ExplanationCode=json_data.get("ExplanationCode"),
            InternetGateway=AnalysisComponent._deserialize(json_data.get("InternetGateway")),
            SourceVpc=AnalysisComponent._deserialize(json_data.get("SourceVpc")),
            AttachedTo=AnalysisComponent._deserialize(json_data.get("AttachedTo")),
            PrefixList=AnalysisComponent._deserialize(json_data.get("PrefixList")),
            TransitGatewayRouteTableRoute=TransitGatewayRouteTableRoute._deserialize(json_data.get("TransitGatewayRouteTableRoute")),
            ComponentRegion=json_data.get("ComponentRegion"),
            LoadBalancerTargetGroup=AnalysisComponent._deserialize(json_data.get("LoadBalancerTargetGroup")),
            NetworkInterface=AnalysisComponent._deserialize(json_data.get("NetworkInterface")),
            CustomerGateway=AnalysisComponent._deserialize(json_data.get("CustomerGateway")),
            DestinationVpc=AnalysisComponent._deserialize(json_data.get("DestinationVpc")),
            SecurityGroup=AnalysisComponent._deserialize(json_data.get("SecurityGroup")),
            TransitGateway=AnalysisComponent._deserialize(json_data.get("TransitGateway")),
            RouteTable=AnalysisComponent._deserialize(json_data.get("RouteTable")),
            State=json_data.get("State"),
            LoadBalancerListenerPort=json_data.get("LoadBalancerListenerPort"),
            vpcEndpoint=AnalysisComponent._deserialize(json_data.get("vpcEndpoint")),
            Subnet=AnalysisComponent._deserialize(json_data.get("Subnet")),
            Cidrs=json_data.get("Cidrs"),
            Destination=AnalysisComponent._deserialize(json_data.get("Destination")),
            SecurityGroups=deserialize_list(json_data.get("SecurityGroups"), AnalysisComponent),
            ComponentAccount=json_data.get("ComponentAccount"),
            VpnConnection=AnalysisComponent._deserialize(json_data.get("VpnConnection")),
            Vpc=AnalysisComponent._deserialize(json_data.get("Vpc")),
            NatGateway=AnalysisComponent._deserialize(json_data.get("NatGateway")),
            Direction=json_data.get("Direction"),
            LoadBalancerTargetPort=json_data.get("LoadBalancerTargetPort"),
            LoadBalancerTarget=AnalysisLoadBalancerTarget._deserialize(json_data.get("LoadBalancerTarget")),
            LoadBalancerTargetGroups=deserialize_list(json_data.get("LoadBalancerTargetGroups"), AnalysisComponent),
            Component=AnalysisComponent._deserialize(json_data.get("Component")),
            MissingComponent=json_data.get("MissingComponent"),
            RouteTableRoute=AnalysisRouteTableRoute._deserialize(json_data.get("RouteTableRoute")),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            PortRanges=deserialize_list(json_data.get("PortRanges"), PortRange),
            Acl=AnalysisComponent._deserialize(json_data.get("Acl")),
            SecurityGroupRule=AnalysisSecurityGroupRule._deserialize(json_data.get("SecurityGroupRule")),
            SubnetRouteTable=AnalysisComponent._deserialize(json_data.get("SubnetRouteTable")),
            LoadBalancerArn=json_data.get("LoadBalancerArn"),
            AclRule=AnalysisAclRule._deserialize(json_data.get("AclRule")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Explanation = Explanation


@dataclass
class AnalysisLoadBalancerListener(BaseModel):
    InstancePort: Optional[int]
    LoadBalancerPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisLoadBalancerListener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisLoadBalancerListener"]:
        if not json_data:
            return None
        return cls(
            InstancePort=json_data.get("InstancePort"),
            LoadBalancerPort=json_data.get("LoadBalancerPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisLoadBalancerListener = AnalysisLoadBalancerListener


@dataclass
class TransitGatewayRouteTableRoute(BaseModel):
    PrefixListId: Optional[str]
    ResourceId: Optional[str]
    State: Optional[str]
    ResourceType: Optional[str]
    RouteOrigin: Optional[str]
    DestinationCidr: Optional[str]
    AttachmentId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TransitGatewayRouteTableRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransitGatewayRouteTableRoute"]:
        if not json_data:
            return None
        return cls(
            PrefixListId=json_data.get("PrefixListId"),
            ResourceId=json_data.get("ResourceId"),
            State=json_data.get("State"),
            ResourceType=json_data.get("ResourceType"),
            RouteOrigin=json_data.get("RouteOrigin"),
            DestinationCidr=json_data.get("DestinationCidr"),
            AttachmentId=json_data.get("AttachmentId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransitGatewayRouteTableRoute = TransitGatewayRouteTableRoute


@dataclass
class AnalysisLoadBalancerTarget(BaseModel):
    Address: Optional[str]
    Instance: Optional["_AnalysisComponent"]
    Port: Optional[int]
    AvailabilityZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisLoadBalancerTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisLoadBalancerTarget"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Instance=AnalysisComponent._deserialize(json_data.get("Instance")),
            Port=json_data.get("Port"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisLoadBalancerTarget = AnalysisLoadBalancerTarget


@dataclass
class AnalysisRouteTableRoute(BaseModel):
    Origin: Optional[str]
    destinationPrefixListId: Optional[str]
    destinationCidr: Optional[str]
    NetworkInterfaceId: Optional[str]
    TransitGatewayId: Optional[str]
    VpcPeeringConnectionId: Optional[str]
    instanceId: Optional[str]
    State: Optional[str]
    egressOnlyInternetGatewayId: Optional[str]
    NatGatewayId: Optional[str]
    gatewayId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisRouteTableRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisRouteTableRoute"]:
        if not json_data:
            return None
        return cls(
            Origin=json_data.get("Origin"),
            destinationPrefixListId=json_data.get("destinationPrefixListId"),
            destinationCidr=json_data.get("destinationCidr"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            VpcPeeringConnectionId=json_data.get("VpcPeeringConnectionId"),
            instanceId=json_data.get("instanceId"),
            State=json_data.get("State"),
            egressOnlyInternetGatewayId=json_data.get("egressOnlyInternetGatewayId"),
            NatGatewayId=json_data.get("NatGatewayId"),
            gatewayId=json_data.get("gatewayId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisRouteTableRoute = AnalysisRouteTableRoute


@dataclass
class AnalysisAclRule(BaseModel):
    PortRange: Optional["_PortRange"]
    Cidr: Optional[str]
    RuleAction: Optional[str]
    Egress: Optional[bool]
    RuleNumber: Optional[int]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisAclRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisAclRule"]:
        if not json_data:
            return None
        return cls(
            PortRange=PortRange._deserialize(json_data.get("PortRange")),
            Cidr=json_data.get("Cidr"),
            RuleAction=json_data.get("RuleAction"),
            Egress=json_data.get("Egress"),
            RuleNumber=json_data.get("RuleNumber"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisAclRule = AnalysisAclRule


@dataclass
class AlternatePathHint(BaseModel):
    ComponentArn: Optional[str]
    ComponentId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlternatePathHint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlternatePathHint"]:
        if not json_data:
            return None
        return cls(
            ComponentArn=json_data.get("ComponentArn"),
            ComponentId=json_data.get("ComponentId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlternatePathHint = AlternatePathHint


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


