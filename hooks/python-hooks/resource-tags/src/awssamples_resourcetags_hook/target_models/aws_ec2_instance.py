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
class AwsEc2Instance(BaseModel):
    Tenancy: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    PrivateDnsName: Optional[str]
    PrivateIpAddress: Optional[str]
    UserData: Optional[str]
    BlockDeviceMappings: Optional[Sequence["_BlockDeviceMapping"]]
    IamInstanceProfile: Optional[str]
    Ipv6Addresses: Optional[Sequence["_InstanceIpv6Address"]]
    KernelId: Optional[str]
    SubnetId: Optional[str]
    EbsOptimized: Optional[bool]
    PropagateTagsToVolumeOnCreation: Optional[bool]
    ElasticGpuSpecifications: Optional[Sequence["_ElasticGpuSpecification"]]
    ElasticInferenceAccelerators: Optional[Sequence["_ElasticInferenceAccelerator"]]
    Volumes: Optional[Sequence["_Volume"]]
    PrivateIp: Optional[str]
    Ipv6AddressCount: Optional[int]
    LaunchTemplate: Optional["_LaunchTemplateSpecification"]
    EnclaveOptions: Optional["_EnclaveOptions"]
    NetworkInterfaces: Optional[Sequence["_NetworkInterface"]]
    ImageId: Optional[str]
    InstanceType: Optional[str]
    Monitoring: Optional[bool]
    Tags: Optional[Any]
    AdditionalInfo: Optional[str]
    HibernationOptions: Optional["_HibernationOptions"]
    LicenseSpecifications: Optional[Sequence["_LicenseSpecification"]]
    PublicIp: Optional[str]
    InstanceInitiatedShutdownBehavior: Optional[str]
    CpuOptions: Optional["_CpuOptions"]
    AvailabilityZone: Optional[str]
    PrivateDnsNameOptions: Optional["_PrivateDnsNameOptions"]
    HostId: Optional[str]
    HostResourceGroupArn: Optional[str]
    PublicDnsName: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    DisableApiTermination: Optional[bool]
    KeyName: Optional[str]
    RamdiskId: Optional[str]
    SourceDestCheck: Optional[bool]
    PlacementGroupName: Optional[str]
    SsmAssociations: Optional[Sequence["_SsmAssociation"]]
    Affinity: Optional[str]
    Id: Optional[str]
    CreditSpecification: Optional["_CreditSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Instance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Instance"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Tenancy=json_data.get("Tenancy"),
            SecurityGroups=json_data.get("SecurityGroups"),
            PrivateDnsName=json_data.get("PrivateDnsName"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            UserData=json_data.get("UserData"),
            BlockDeviceMappings=deserialize_list(json_data.get("BlockDeviceMappings"), BlockDeviceMapping),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            Ipv6Addresses=deserialize_list(json_data.get("Ipv6Addresses"), InstanceIpv6Address),
            KernelId=json_data.get("KernelId"),
            SubnetId=json_data.get("SubnetId"),
            EbsOptimized=json_data.get("EbsOptimized"),
            PropagateTagsToVolumeOnCreation=json_data.get("PropagateTagsToVolumeOnCreation"),
            ElasticGpuSpecifications=deserialize_list(json_data.get("ElasticGpuSpecifications"), ElasticGpuSpecification),
            ElasticInferenceAccelerators=deserialize_list(json_data.get("ElasticInferenceAccelerators"), ElasticInferenceAccelerator),
            Volumes=deserialize_list(json_data.get("Volumes"), Volume),
            PrivateIp=json_data.get("PrivateIp"),
            Ipv6AddressCount=json_data.get("Ipv6AddressCount"),
            LaunchTemplate=LaunchTemplateSpecification._deserialize(json_data.get("LaunchTemplate")),
            EnclaveOptions=EnclaveOptions._deserialize(json_data.get("EnclaveOptions")),
            NetworkInterfaces=deserialize_list(json_data.get("NetworkInterfaces"), NetworkInterface),
            ImageId=json_data.get("ImageId"),
            InstanceType=json_data.get("InstanceType"),
            Monitoring=json_data.get("Monitoring"),
            Tags=json_data.get("Tags"),
            AdditionalInfo=json_data.get("AdditionalInfo"),
            HibernationOptions=HibernationOptions._deserialize(json_data.get("HibernationOptions")),
            LicenseSpecifications=deserialize_list(json_data.get("LicenseSpecifications"), LicenseSpecification),
            PublicIp=json_data.get("PublicIp"),
            InstanceInitiatedShutdownBehavior=json_data.get("InstanceInitiatedShutdownBehavior"),
            CpuOptions=CpuOptions._deserialize(json_data.get("CpuOptions")),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            PrivateDnsNameOptions=PrivateDnsNameOptions._deserialize(json_data.get("PrivateDnsNameOptions")),
            HostId=json_data.get("HostId"),
            HostResourceGroupArn=json_data.get("HostResourceGroupArn"),
            PublicDnsName=json_data.get("PublicDnsName"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            DisableApiTermination=json_data.get("DisableApiTermination"),
            KeyName=json_data.get("KeyName"),
            RamdiskId=json_data.get("RamdiskId"),
            SourceDestCheck=json_data.get("SourceDestCheck"),
            PlacementGroupName=json_data.get("PlacementGroupName"),
            SsmAssociations=deserialize_list(json_data.get("SsmAssociations"), SsmAssociation),
            Affinity=json_data.get("Affinity"),
            Id=json_data.get("Id"),
            CreditSpecification=CreditSpecification._deserialize(json_data.get("CreditSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Instance = AwsEc2Instance


@dataclass
class BlockDeviceMapping(BaseModel):
    NoDevice: Optional[MutableMapping[str, Any]]
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
            Iops=json_data.get("Iops"),
            VolumeSize=json_data.get("VolumeSize"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ebs = Ebs


@dataclass
class InstanceIpv6Address(BaseModel):
    Ipv6Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceIpv6Address"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceIpv6Address"]:
        if not json_data:
            return None
        return cls(
            Ipv6Address=json_data.get("Ipv6Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceIpv6Address = InstanceIpv6Address


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
class ElasticInferenceAccelerator(BaseModel):
    Type: Optional[str]
    Count: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticInferenceAccelerator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticInferenceAccelerator"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Count=json_data.get("Count"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticInferenceAccelerator = ElasticInferenceAccelerator


@dataclass
class Volume(BaseModel):
    VolumeId: Optional[str]
    Device: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            VolumeId=json_data.get("VolumeId"),
            Device=json_data.get("Device"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


@dataclass
class LaunchTemplateSpecification(BaseModel):
    LaunchTemplateName: Optional[str]
    LaunchTemplateId: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateSpecification"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateSpecification = LaunchTemplateSpecification


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
class NetworkInterface(BaseModel):
    Description: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddresses: Optional[Sequence["_PrivateIpAddressSpecification"]]
    SecondaryPrivateIpAddressCount: Optional[int]
    DeviceIndex: Optional[str]
    GroupSet: Optional[Sequence[str]]
    Ipv6Addresses: Optional[Sequence["_InstanceIpv6Address"]]
    SubnetId: Optional[str]
    AssociatePublicIpAddress: Optional[bool]
    NetworkInterfaceId: Optional[str]
    AssociateCarrierIpAddress: Optional[bool]
    Ipv6AddressCount: Optional[int]
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
            PrivateIpAddresses=deserialize_list(json_data.get("PrivateIpAddresses"), PrivateIpAddressSpecification),
            SecondaryPrivateIpAddressCount=json_data.get("SecondaryPrivateIpAddressCount"),
            DeviceIndex=json_data.get("DeviceIndex"),
            GroupSet=json_data.get("GroupSet"),
            Ipv6Addresses=deserialize_list(json_data.get("Ipv6Addresses"), InstanceIpv6Address),
            SubnetId=json_data.get("SubnetId"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            AssociateCarrierIpAddress=json_data.get("AssociateCarrierIpAddress"),
            Ipv6AddressCount=json_data.get("Ipv6AddressCount"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


@dataclass
class PrivateIpAddressSpecification(BaseModel):
    PrivateIpAddress: Optional[str]
    Primary: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateIpAddressSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateIpAddressSpecification"]:
        if not json_data:
            return None
        return cls(
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            Primary=json_data.get("Primary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateIpAddressSpecification = PrivateIpAddressSpecification


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
class SsmAssociation(BaseModel):
    AssociationParameters: Optional[Sequence["_AssociationParameter"]]
    DocumentName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SsmAssociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SsmAssociation"]:
        if not json_data:
            return None
        return cls(
            AssociationParameters=deserialize_list(json_data.get("AssociationParameters"), AssociationParameter),
            DocumentName=json_data.get("DocumentName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SsmAssociation = SsmAssociation


@dataclass
class AssociationParameter(BaseModel):
    Value: Optional[Sequence[str]]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssociationParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssociationParameter"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssociationParameter = AssociationParameter


@dataclass
class CreditSpecification(BaseModel):
    CPUCredits: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreditSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreditSpecification"]:
        if not json_data:
            return None
        return cls(
            CPUCredits=json_data.get("CPUCredits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreditSpecification = CreditSpecification


