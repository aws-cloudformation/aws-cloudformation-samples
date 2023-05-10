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
class AwsEc2Launchtemplate(BaseModel):
    LaunchTemplateName: Optional[str]
    LaunchTemplateData: Optional["_LaunchTemplateData"]
    VersionDescription: Optional[str]
    TagSpecifications: Optional[Sequence["_LaunchTemplateTagSpecification"]]
    LatestVersionNumber: Optional[str]
    Id: Optional[str]
    DefaultVersionNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Launchtemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Launchtemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            LaunchTemplateData=LaunchTemplateData._deserialize(json_data.get("LaunchTemplateData")),
            VersionDescription=json_data.get("VersionDescription"),
            TagSpecifications=deserialize_list(json_data.get("TagSpecifications"), LaunchTemplateTagSpecification),
            LatestVersionNumber=json_data.get("LatestVersionNumber"),
            Id=json_data.get("Id"),
            DefaultVersionNumber=json_data.get("DefaultVersionNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Launchtemplate = AwsEc2Launchtemplate


@dataclass
class LaunchTemplateData(BaseModel):
    SecurityGroups: Optional[Sequence[str]]
    TagSpecifications: Optional[Sequence["_TagSpecification"]]
    UserData: Optional[str]
    BlockDeviceMappings: Optional[Sequence["_BlockDeviceMapping"]]
    MaintenanceOptions: Optional["_MaintenanceOptions"]
    IamInstanceProfile: Optional["_IamInstanceProfile"]
    KernelId: Optional[str]
    EbsOptimized: Optional[bool]
    ElasticGpuSpecifications: Optional[Sequence["_ElasticGpuSpecification"]]
    ElasticInferenceAccelerators: Optional[Sequence["_LaunchTemplateElasticInferenceAccelerator"]]
    Placement: Optional["_Placement"]
    NetworkInterfaces: Optional[Sequence["_NetworkInterface"]]
    EnclaveOptions: Optional["_EnclaveOptions"]
    ImageId: Optional[str]
    InstanceType: Optional[str]
    Monitoring: Optional["_Monitoring"]
    HibernationOptions: Optional["_HibernationOptions"]
    MetadataOptions: Optional["_MetadataOptions"]
    LicenseSpecifications: Optional[Sequence["_LicenseSpecification"]]
    InstanceInitiatedShutdownBehavior: Optional[str]
    DisableApiStop: Optional[bool]
    CpuOptions: Optional["_CpuOptions"]
    PrivateDnsNameOptions: Optional["_PrivateDnsNameOptions"]
    SecurityGroupIds: Optional[Sequence[str]]
    KeyName: Optional[str]
    DisableApiTermination: Optional[bool]
    InstanceMarketOptions: Optional["_InstanceMarketOptions"]
    InstanceRequirements: Optional["_InstanceRequirements"]
    RamDiskId: Optional[str]
    CapacityReservationSpecification: Optional["_CapacityReservationSpecification"]
    CreditSpecification: Optional["_CreditSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateData"]:
        if not json_data:
            return None
        return cls(
            SecurityGroups=json_data.get("SecurityGroups"),
            TagSpecifications=deserialize_list(json_data.get("TagSpecifications"), TagSpecification),
            UserData=json_data.get("UserData"),
            BlockDeviceMappings=deserialize_list(json_data.get("BlockDeviceMappings"), BlockDeviceMapping),
            MaintenanceOptions=MaintenanceOptions._deserialize(json_data.get("MaintenanceOptions")),
            IamInstanceProfile=IamInstanceProfile._deserialize(json_data.get("IamInstanceProfile")),
            KernelId=json_data.get("KernelId"),
            EbsOptimized=json_data.get("EbsOptimized"),
            ElasticGpuSpecifications=deserialize_list(json_data.get("ElasticGpuSpecifications"), ElasticGpuSpecification),
            ElasticInferenceAccelerators=deserialize_list(json_data.get("ElasticInferenceAccelerators"), LaunchTemplateElasticInferenceAccelerator),
            Placement=Placement._deserialize(json_data.get("Placement")),
            NetworkInterfaces=deserialize_list(json_data.get("NetworkInterfaces"), NetworkInterface),
            EnclaveOptions=EnclaveOptions._deserialize(json_data.get("EnclaveOptions")),
            ImageId=json_data.get("ImageId"),
            InstanceType=json_data.get("InstanceType"),
            Monitoring=Monitoring._deserialize(json_data.get("Monitoring")),
            HibernationOptions=HibernationOptions._deserialize(json_data.get("HibernationOptions")),
            MetadataOptions=MetadataOptions._deserialize(json_data.get("MetadataOptions")),
            LicenseSpecifications=deserialize_list(json_data.get("LicenseSpecifications"), LicenseSpecification),
            InstanceInitiatedShutdownBehavior=json_data.get("InstanceInitiatedShutdownBehavior"),
            DisableApiStop=json_data.get("DisableApiStop"),
            CpuOptions=CpuOptions._deserialize(json_data.get("CpuOptions")),
            PrivateDnsNameOptions=PrivateDnsNameOptions._deserialize(json_data.get("PrivateDnsNameOptions")),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            KeyName=json_data.get("KeyName"),
            DisableApiTermination=json_data.get("DisableApiTermination"),
            InstanceMarketOptions=InstanceMarketOptions._deserialize(json_data.get("InstanceMarketOptions")),
            InstanceRequirements=InstanceRequirements._deserialize(json_data.get("InstanceRequirements")),
            RamDiskId=json_data.get("RamDiskId"),
            CapacityReservationSpecification=CapacityReservationSpecification._deserialize(json_data.get("CapacityReservationSpecification")),
            CreditSpecification=CreditSpecification._deserialize(json_data.get("CreditSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateData = LaunchTemplateData


@dataclass
class TagSpecification(BaseModel):
    ResourceType: Optional[str]
    Tags: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagSpecification"]:
        if not json_data:
            return None
        return cls(
            ResourceType=json_data.get("ResourceType"),
            Tags=deserialize_list(json_data.get("Tags"), Tag),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagSpecification = TagSpecification


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


@dataclass
class BlockDeviceMapping(BaseModel):
    NoDevice: Optional[str]
    VirtualName: Optional[str]
    Ebs: Optional["_Ebs"]
    DeviceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDeviceMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDeviceMapping"]:
        if not json_data:
            return None
        return cls(
            NoDevice=json_data.get("NoDevice"),
            VirtualName=json_data.get("VirtualName"),
            Ebs=Ebs._deserialize(json_data.get("Ebs")),
            DeviceName=json_data.get("DeviceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDeviceMapping = BlockDeviceMapping


@dataclass
class Ebs(BaseModel):
    SnapshotId: Optional[str]
    VolumeType: Optional[str]
    KmsKeyId: Optional[str]
    Encrypted: Optional[bool]
    Throughput: Optional[int]
    Iops: Optional[int]
    VolumeSize: Optional[int]
    DeleteOnTermination: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Ebs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ebs"]:
        if not json_data:
            return None
        return cls(
            SnapshotId=json_data.get("SnapshotId"),
            VolumeType=json_data.get("VolumeType"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Encrypted=json_data.get("Encrypted"),
            Throughput=json_data.get("Throughput"),
            Iops=json_data.get("Iops"),
            VolumeSize=json_data.get("VolumeSize"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ebs = Ebs


@dataclass
class MaintenanceOptions(BaseModel):
    AutoRecovery: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceOptions"]:
        if not json_data:
            return None
        return cls(
            AutoRecovery=json_data.get("AutoRecovery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceOptions = MaintenanceOptions


@dataclass
class IamInstanceProfile(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IamInstanceProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamInstanceProfile"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamInstanceProfile = IamInstanceProfile


@dataclass
class ElasticGpuSpecification(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticGpuSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticGpuSpecification"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticGpuSpecification = ElasticGpuSpecification


@dataclass
class LaunchTemplateElasticInferenceAccelerator(BaseModel):
    Type: Optional[str]
    Count: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateElasticInferenceAccelerator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateElasticInferenceAccelerator"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Count=json_data.get("Count"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateElasticInferenceAccelerator = LaunchTemplateElasticInferenceAccelerator


@dataclass
class Placement(BaseModel):
    GroupName: Optional[str]
    Tenancy: Optional[str]
    SpreadDomain: Optional[str]
    PartitionNumber: Optional[int]
    AvailabilityZone: Optional[str]
    Affinity: Optional[str]
    HostId: Optional[str]
    HostResourceGroupArn: Optional[str]
    GroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Placement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Placement"]:
        if not json_data:
            return None
        return cls(
            GroupName=json_data.get("GroupName"),
            Tenancy=json_data.get("Tenancy"),
            SpreadDomain=json_data.get("SpreadDomain"),
            PartitionNumber=json_data.get("PartitionNumber"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Affinity=json_data.get("Affinity"),
            HostId=json_data.get("HostId"),
            HostResourceGroupArn=json_data.get("HostResourceGroupArn"),
            GroupId=json_data.get("GroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Placement = Placement


@dataclass
class NetworkInterface(BaseModel):
    Description: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddresses: Optional[Sequence["_PrivateIpAdd"]]
    SecondaryPrivateIpAddressCount: Optional[int]
    Ipv6PrefixCount: Optional[int]
    Ipv4Prefixes: Optional[Sequence["_Ipv4PrefixSpecification"]]
    DeviceIndex: Optional[int]
    Ipv4PrefixCount: Optional[int]
    Ipv6Prefixes: Optional[Sequence["_Ipv6PrefixSpecification"]]
    SubnetId: Optional[str]
    Ipv6Addresses: Optional[Sequence["_Ipv6Add"]]
    AssociatePublicIpAddress: Optional[bool]
    NetworkInterfaceId: Optional[str]
    NetworkCardIndex: Optional[int]
    InterfaceType: Optional[str]
    AssociateCarrierIpAddress: Optional[bool]
    Ipv6AddressCount: Optional[int]
    Groups: Optional[Sequence[str]]
    DeleteOnTermination: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PrivateIpAddresses=deserialize_list(json_data.get("PrivateIpAddresses"), PrivateIpAdd),
            SecondaryPrivateIpAddressCount=json_data.get("SecondaryPrivateIpAddressCount"),
            Ipv6PrefixCount=json_data.get("Ipv6PrefixCount"),
            Ipv4Prefixes=deserialize_list(json_data.get("Ipv4Prefixes"), Ipv4PrefixSpecification),
            DeviceIndex=json_data.get("DeviceIndex"),
            Ipv4PrefixCount=json_data.get("Ipv4PrefixCount"),
            Ipv6Prefixes=deserialize_list(json_data.get("Ipv6Prefixes"), Ipv6PrefixSpecification),
            SubnetId=json_data.get("SubnetId"),
            Ipv6Addresses=deserialize_list(json_data.get("Ipv6Addresses"), Ipv6Add),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            NetworkCardIndex=json_data.get("NetworkCardIndex"),
            InterfaceType=json_data.get("InterfaceType"),
            AssociateCarrierIpAddress=json_data.get("AssociateCarrierIpAddress"),
            Ipv6AddressCount=json_data.get("Ipv6AddressCount"),
            Groups=json_data.get("Groups"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


@dataclass
class PrivateIpAdd(BaseModel):
    PrivateIpAddress: Optional[str]
    Primary: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateIpAdd"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateIpAdd"]:
        if not json_data:
            return None
        return cls(
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            Primary=json_data.get("Primary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateIpAdd = PrivateIpAdd


@dataclass
class Ipv4PrefixSpecification(BaseModel):
    Ipv4Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4PrefixSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4PrefixSpecification"]:
        if not json_data:
            return None
        return cls(
            Ipv4Prefix=json_data.get("Ipv4Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4PrefixSpecification = Ipv4PrefixSpecification


@dataclass
class Ipv6PrefixSpecification(BaseModel):
    Ipv6Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6PrefixSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6PrefixSpecification"]:
        if not json_data:
            return None
        return cls(
            Ipv6Prefix=json_data.get("Ipv6Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6PrefixSpecification = Ipv6PrefixSpecification


@dataclass
class Ipv6Add(BaseModel):
    Ipv6Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6Add"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6Add"]:
        if not json_data:
            return None
        return cls(
            Ipv6Address=json_data.get("Ipv6Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6Add = Ipv6Add


@dataclass
class EnclaveOptions(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EnclaveOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnclaveOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnclaveOptions = EnclaveOptions


@dataclass
class Monitoring(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Monitoring"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Monitoring"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Monitoring = Monitoring


@dataclass
class HibernationOptions(BaseModel):
    Configured: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HibernationOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HibernationOptions"]:
        if not json_data:
            return None
        return cls(
            Configured=json_data.get("Configured"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HibernationOptions = HibernationOptions


@dataclass
class MetadataOptions(BaseModel):
    HttpPutResponseHopLimit: Optional[int]
    HttpTokens: Optional[str]
    HttpProtocolIpv6: Optional[str]
    InstanceMetadataTags: Optional[str]
    HttpEndpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataOptions"]:
        if not json_data:
            return None
        return cls(
            HttpPutResponseHopLimit=json_data.get("HttpPutResponseHopLimit"),
            HttpTokens=json_data.get("HttpTokens"),
            HttpProtocolIpv6=json_data.get("HttpProtocolIpv6"),
            InstanceMetadataTags=json_data.get("InstanceMetadataTags"),
            HttpEndpoint=json_data.get("HttpEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataOptions = MetadataOptions


@dataclass
class LicenseSpecification(BaseModel):
    LicenseConfigurationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LicenseSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LicenseSpecification"]:
        if not json_data:
            return None
        return cls(
            LicenseConfigurationArn=json_data.get("LicenseConfigurationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LicenseSpecification = LicenseSpecification


@dataclass
class CpuOptions(BaseModel):
    ThreadsPerCore: Optional[int]
    AmdSevSnp: Optional[str]
    CoreCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CpuOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CpuOptions"]:
        if not json_data:
            return None
        return cls(
            ThreadsPerCore=json_data.get("ThreadsPerCore"),
            AmdSevSnp=json_data.get("AmdSevSnp"),
            CoreCount=json_data.get("CoreCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CpuOptions = CpuOptions


@dataclass
class PrivateDnsNameOptions(BaseModel):
    HostnameType: Optional[str]
    EnableResourceNameDnsAAAARecord: Optional[bool]
    EnableResourceNameDnsARecord: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateDnsNameOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateDnsNameOptions"]:
        if not json_data:
            return None
        return cls(
            HostnameType=json_data.get("HostnameType"),
            EnableResourceNameDnsAAAARecord=json_data.get("EnableResourceNameDnsAAAARecord"),
            EnableResourceNameDnsARecord=json_data.get("EnableResourceNameDnsARecord"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateDnsNameOptions = PrivateDnsNameOptions


@dataclass
class InstanceMarketOptions(BaseModel):
    SpotOptions: Optional["_SpotOptions"]
    MarketType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceMarketOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceMarketOptions"]:
        if not json_data:
            return None
        return cls(
            SpotOptions=SpotOptions._deserialize(json_data.get("SpotOptions")),
            MarketType=json_data.get("MarketType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceMarketOptions = InstanceMarketOptions


@dataclass
class SpotOptions(BaseModel):
    InstanceInterruptionBehavior: Optional[str]
    MaxPrice: Optional[str]
    SpotInstanceType: Optional[str]
    BlockDurationMinutes: Optional[int]
    ValidUntil: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpotOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotOptions"]:
        if not json_data:
            return None
        return cls(
            InstanceInterruptionBehavior=json_data.get("InstanceInterruptionBehavior"),
            MaxPrice=json_data.get("MaxPrice"),
            SpotInstanceType=json_data.get("SpotInstanceType"),
            BlockDurationMinutes=json_data.get("BlockDurationMinutes"),
            ValidUntil=json_data.get("ValidUntil"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotOptions = SpotOptions


@dataclass
class InstanceRequirements(BaseModel):
    LocalStorageTypes: Optional[Sequence[str]]
    InstanceGenerations: Optional[Sequence[str]]
    NetworkInterfaceCount: Optional["_NetworkInterfaceCount"]
    MemoryGiBPerVCpu: Optional["_MemoryGiBPerVCpu"]
    AcceleratorTypes: Optional[Sequence[str]]
    VCpuCount: Optional["_VCpuCount"]
    ExcludedInstanceTypes: Optional[Sequence[str]]
    AcceleratorManufacturers: Optional[Sequence[str]]
    AllowedInstanceTypes: Optional[Sequence[str]]
    LocalStorage: Optional[str]
    CpuManufacturers: Optional[Sequence[str]]
    AcceleratorCount: Optional["_AcceleratorCount"]
    NetworkBandwidthGbps: Optional["_NetworkBandwidthGbps"]
    BareMetal: Optional[str]
    RequireHibernateSupport: Optional[bool]
    SpotMaxPricePercentageOverLowestPrice: Optional[int]
    BaselineEbsBandwidthMbps: Optional["_BaselineEbsBandwidthMbps"]
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int]
    AcceleratorNames: Optional[Sequence[str]]
    AcceleratorTotalMemoryMiB: Optional["_AcceleratorTotalMemoryMiB"]
    BurstablePerformance: Optional[str]
    MemoryMiB: Optional["_MemoryMiB"]
    TotalLocalStorageGB: Optional["_TotalLocalStorageGB"]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceRequirements"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceRequirements"]:
        if not json_data:
            return None
        return cls(
            LocalStorageTypes=json_data.get("LocalStorageTypes"),
            InstanceGenerations=json_data.get("InstanceGenerations"),
            NetworkInterfaceCount=NetworkInterfaceCount._deserialize(json_data.get("NetworkInterfaceCount")),
            MemoryGiBPerVCpu=MemoryGiBPerVCpu._deserialize(json_data.get("MemoryGiBPerVCpu")),
            AcceleratorTypes=json_data.get("AcceleratorTypes"),
            VCpuCount=VCpuCount._deserialize(json_data.get("VCpuCount")),
            ExcludedInstanceTypes=json_data.get("ExcludedInstanceTypes"),
            AcceleratorManufacturers=json_data.get("AcceleratorManufacturers"),
            AllowedInstanceTypes=json_data.get("AllowedInstanceTypes"),
            LocalStorage=json_data.get("LocalStorage"),
            CpuManufacturers=json_data.get("CpuManufacturers"),
            AcceleratorCount=AcceleratorCount._deserialize(json_data.get("AcceleratorCount")),
            NetworkBandwidthGbps=NetworkBandwidthGbps._deserialize(json_data.get("NetworkBandwidthGbps")),
            BareMetal=json_data.get("BareMetal"),
            RequireHibernateSupport=json_data.get("RequireHibernateSupport"),
            SpotMaxPricePercentageOverLowestPrice=json_data.get("SpotMaxPricePercentageOverLowestPrice"),
            BaselineEbsBandwidthMbps=BaselineEbsBandwidthMbps._deserialize(json_data.get("BaselineEbsBandwidthMbps")),
            OnDemandMaxPricePercentageOverLowestPrice=json_data.get("OnDemandMaxPricePercentageOverLowestPrice"),
            AcceleratorNames=json_data.get("AcceleratorNames"),
            AcceleratorTotalMemoryMiB=AcceleratorTotalMemoryMiB._deserialize(json_data.get("AcceleratorTotalMemoryMiB")),
            BurstablePerformance=json_data.get("BurstablePerformance"),
            MemoryMiB=MemoryMiB._deserialize(json_data.get("MemoryMiB")),
            TotalLocalStorageGB=TotalLocalStorageGB._deserialize(json_data.get("TotalLocalStorageGB")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceRequirements = InstanceRequirements


@dataclass
class NetworkInterfaceCount(BaseModel):
    Max: Optional[int]
    Min: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceCount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceCount"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceCount = NetworkInterfaceCount


@dataclass
class MemoryGiBPerVCpu(BaseModel):
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MemoryGiBPerVCpu"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemoryGiBPerVCpu"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemoryGiBPerVCpu = MemoryGiBPerVCpu


@dataclass
class VCpuCount(BaseModel):
    Max: Optional[int]
    Min: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VCpuCount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VCpuCount"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VCpuCount = VCpuCount


@dataclass
class AcceleratorCount(BaseModel):
    Max: Optional[int]
    Min: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AcceleratorCount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcceleratorCount"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcceleratorCount = AcceleratorCount


@dataclass
class NetworkBandwidthGbps(BaseModel):
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkBandwidthGbps"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkBandwidthGbps"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkBandwidthGbps = NetworkBandwidthGbps


@dataclass
class BaselineEbsBandwidthMbps(BaseModel):
    Max: Optional[int]
    Min: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_BaselineEbsBandwidthMbps"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BaselineEbsBandwidthMbps"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BaselineEbsBandwidthMbps = BaselineEbsBandwidthMbps


@dataclass
class AcceleratorTotalMemoryMiB(BaseModel):
    Max: Optional[int]
    Min: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AcceleratorTotalMemoryMiB"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcceleratorTotalMemoryMiB"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcceleratorTotalMemoryMiB = AcceleratorTotalMemoryMiB


@dataclass
class MemoryMiB(BaseModel):
    Max: Optional[int]
    Min: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MemoryMiB"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemoryMiB"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemoryMiB = MemoryMiB


@dataclass
class TotalLocalStorageGB(BaseModel):
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TotalLocalStorageGB"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TotalLocalStorageGB"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TotalLocalStorageGB = TotalLocalStorageGB


@dataclass
class CapacityReservationSpecification(BaseModel):
    CapacityReservationTarget: Optional["_CapacityReservationTarget"]
    CapacityReservationPreference: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityReservationSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityReservationSpecification"]:
        if not json_data:
            return None
        return cls(
            CapacityReservationTarget=CapacityReservationTarget._deserialize(json_data.get("CapacityReservationTarget")),
            CapacityReservationPreference=json_data.get("CapacityReservationPreference"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityReservationSpecification = CapacityReservationSpecification


@dataclass
class CapacityReservationTarget(BaseModel):
    CapacityReservationResourceGroupArn: Optional[str]
    CapacityReservationId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityReservationTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityReservationTarget"]:
        if not json_data:
            return None
        return cls(
            CapacityReservationResourceGroupArn=json_data.get("CapacityReservationResourceGroupArn"),
            CapacityReservationId=json_data.get("CapacityReservationId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityReservationTarget = CapacityReservationTarget


@dataclass
class CreditSpecification(BaseModel):
    CpuCredits: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreditSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreditSpecification"]:
        if not json_data:
            return None
        return cls(
            CpuCredits=json_data.get("CpuCredits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreditSpecification = CreditSpecification


@dataclass
class LaunchTemplateTagSpecification(BaseModel):
    ResourceType: Optional[str]
    Tags: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateTagSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateTagSpecification"]:
        if not json_data:
            return None
        return cls(
            ResourceType=json_data.get("ResourceType"),
            Tags=deserialize_list(json_data.get("Tags"), Tag),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateTagSpecification = LaunchTemplateTagSpecification


