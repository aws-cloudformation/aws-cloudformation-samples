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
class AwsCodedeployDeploymentgroup(BaseModel):
    OnPremisesTagSet: Optional["_OnPremisesTagSet"]
    ApplicationName: Optional[str]
    DeploymentStyle: Optional["_DeploymentStyle"]
    ServiceRoleArn: Optional[str]
    BlueGreenDeploymentConfiguration: Optional["_BlueGreenDeploymentConfiguration"]
    AutoScalingGroups: Optional[Sequence[str]]
    Ec2TagSet: Optional["_EC2TagSet"]
    OutdatedInstancesStrategy: Optional[str]
    TriggerConfigurations: Optional[Sequence["_TriggerConfig"]]
    Deployment: Optional["_Deployment"]
    DeploymentConfigName: Optional[str]
    AlarmConfiguration: Optional["_AlarmConfiguration"]
    Ec2TagFilters: Optional[Sequence["_EC2TagFilter"]]
    ECSServices: Optional[Sequence["_ECSService"]]
    AutoRollbackConfiguration: Optional["_AutoRollbackConfiguration"]
    LoadBalancerInfo: Optional["_LoadBalancerInfo"]
    Id: Optional[str]
    DeploymentGroupName: Optional[str]
    Tags: Optional[Any]
    OnPremisesInstanceTagFilters: Optional[Sequence["_TagFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodedeployDeploymentgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodedeployDeploymentgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OnPremisesTagSet=OnPremisesTagSet._deserialize(json_data.get("OnPremisesTagSet")),
            ApplicationName=json_data.get("ApplicationName"),
            DeploymentStyle=DeploymentStyle._deserialize(json_data.get("DeploymentStyle")),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            BlueGreenDeploymentConfiguration=BlueGreenDeploymentConfiguration._deserialize(json_data.get("BlueGreenDeploymentConfiguration")),
            AutoScalingGroups=json_data.get("AutoScalingGroups"),
            Ec2TagSet=EC2TagSet._deserialize(json_data.get("Ec2TagSet")),
            OutdatedInstancesStrategy=json_data.get("OutdatedInstancesStrategy"),
            TriggerConfigurations=deserialize_list(json_data.get("TriggerConfigurations"), TriggerConfig),
            Deployment=Deployment._deserialize(json_data.get("Deployment")),
            DeploymentConfigName=json_data.get("DeploymentConfigName"),
            AlarmConfiguration=AlarmConfiguration._deserialize(json_data.get("AlarmConfiguration")),
            Ec2TagFilters=deserialize_list(json_data.get("Ec2TagFilters"), EC2TagFilter),
            ECSServices=deserialize_list(json_data.get("ECSServices"), ECSService),
            AutoRollbackConfiguration=AutoRollbackConfiguration._deserialize(json_data.get("AutoRollbackConfiguration")),
            LoadBalancerInfo=LoadBalancerInfo._deserialize(json_data.get("LoadBalancerInfo")),
            Id=json_data.get("Id"),
            DeploymentGroupName=json_data.get("DeploymentGroupName"),
            Tags=json_data.get("Tags"),
            OnPremisesInstanceTagFilters=deserialize_list(json_data.get("OnPremisesInstanceTagFilters"), TagFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodedeployDeploymentgroup = AwsCodedeployDeploymentgroup


@dataclass
class OnPremisesTagSet(BaseModel):
    OnPremisesTagSetList: Optional[Sequence["_OnPremisesTagSetListObject"]]

    @classmethod
    def _deserialize(
        cls: Type["_OnPremisesTagSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnPremisesTagSet"]:
        if not json_data:
            return None
        return cls(
            OnPremisesTagSetList=deserialize_list(json_data.get("OnPremisesTagSetList"), OnPremisesTagSetListObject),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnPremisesTagSet = OnPremisesTagSet


@dataclass
class OnPremisesTagSetListObject(BaseModel):
    OnPremisesTagGroup: Optional[Sequence["_TagFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_OnPremisesTagSetListObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnPremisesTagSetListObject"]:
        if not json_data:
            return None
        return cls(
            OnPremisesTagGroup=deserialize_list(json_data.get("OnPremisesTagGroup"), TagFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnPremisesTagSetListObject = OnPremisesTagSetListObject


@dataclass
class TagFilter(BaseModel):
    Value: Optional[str]
    Type: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagFilter"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagFilter = TagFilter


@dataclass
class DeploymentStyle(BaseModel):
    DeploymentOption: Optional[str]
    DeploymentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentStyle"]:
        if not json_data:
            return None
        return cls(
            DeploymentOption=json_data.get("DeploymentOption"),
            DeploymentType=json_data.get("DeploymentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentStyle = DeploymentStyle


@dataclass
class BlueGreenDeploymentConfiguration(BaseModel):
    GreenFleetProvisioningOption: Optional["_GreenFleetProvisioningOption"]
    DeploymentReadyOption: Optional["_DeploymentReadyOption"]
    TerminateBlueInstancesOnDeploymentSuccess: Optional["_BlueInstanceTerminationOption"]

    @classmethod
    def _deserialize(
        cls: Type["_BlueGreenDeploymentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlueGreenDeploymentConfiguration"]:
        if not json_data:
            return None
        return cls(
            GreenFleetProvisioningOption=GreenFleetProvisioningOption._deserialize(json_data.get("GreenFleetProvisioningOption")),
            DeploymentReadyOption=DeploymentReadyOption._deserialize(json_data.get("DeploymentReadyOption")),
            TerminateBlueInstancesOnDeploymentSuccess=BlueInstanceTerminationOption._deserialize(json_data.get("TerminateBlueInstancesOnDeploymentSuccess")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlueGreenDeploymentConfiguration = BlueGreenDeploymentConfiguration


@dataclass
class GreenFleetProvisioningOption(BaseModel):
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GreenFleetProvisioningOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GreenFleetProvisioningOption"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GreenFleetProvisioningOption = GreenFleetProvisioningOption


@dataclass
class DeploymentReadyOption(BaseModel):
    WaitTimeInMinutes: Optional[int]
    ActionOnTimeout: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentReadyOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentReadyOption"]:
        if not json_data:
            return None
        return cls(
            WaitTimeInMinutes=json_data.get("WaitTimeInMinutes"),
            ActionOnTimeout=json_data.get("ActionOnTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentReadyOption = DeploymentReadyOption


@dataclass
class BlueInstanceTerminationOption(BaseModel):
    TerminationWaitTimeInMinutes: Optional[int]
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlueInstanceTerminationOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlueInstanceTerminationOption"]:
        if not json_data:
            return None
        return cls(
            TerminationWaitTimeInMinutes=json_data.get("TerminationWaitTimeInMinutes"),
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlueInstanceTerminationOption = BlueInstanceTerminationOption


@dataclass
class EC2TagSet(BaseModel):
    Ec2TagSetList: Optional[Sequence["_EC2TagSetListObject"]]

    @classmethod
    def _deserialize(
        cls: Type["_EC2TagSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EC2TagSet"]:
        if not json_data:
            return None
        return cls(
            Ec2TagSetList=deserialize_list(json_data.get("Ec2TagSetList"), EC2TagSetListObject),
        )


# work around possible type aliasing issues when variable has same name as a model
_EC2TagSet = EC2TagSet


@dataclass
class EC2TagSetListObject(BaseModel):
    Ec2TagGroup: Optional[Sequence["_EC2TagFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_EC2TagSetListObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EC2TagSetListObject"]:
        if not json_data:
            return None
        return cls(
            Ec2TagGroup=deserialize_list(json_data.get("Ec2TagGroup"), EC2TagFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_EC2TagSetListObject = EC2TagSetListObject


@dataclass
class EC2TagFilter(BaseModel):
    Value: Optional[str]
    Type: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EC2TagFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EC2TagFilter"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EC2TagFilter = EC2TagFilter


@dataclass
class TriggerConfig(BaseModel):
    TriggerTargetArn: Optional[str]
    TriggerName: Optional[str]
    TriggerEvents: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerConfig"]:
        if not json_data:
            return None
        return cls(
            TriggerTargetArn=json_data.get("TriggerTargetArn"),
            TriggerName=json_data.get("TriggerName"),
            TriggerEvents=json_data.get("TriggerEvents"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerConfig = TriggerConfig


@dataclass
class Deployment(BaseModel):
    Description: Optional[str]
    Revision: Optional["_RevisionLocation"]
    IgnoreApplicationStopFailures: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Deployment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Deployment"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Revision=RevisionLocation._deserialize(json_data.get("Revision")),
            IgnoreApplicationStopFailures=json_data.get("IgnoreApplicationStopFailures"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Deployment = Deployment


@dataclass
class RevisionLocation(BaseModel):
    S3Location: Optional["_S3Location"]
    GitHubLocation: Optional["_GitHubLocation"]
    RevisionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RevisionLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevisionLocation"]:
        if not json_data:
            return None
        return cls(
            S3Location=S3Location._deserialize(json_data.get("S3Location")),
            GitHubLocation=GitHubLocation._deserialize(json_data.get("GitHubLocation")),
            RevisionType=json_data.get("RevisionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevisionLocation = RevisionLocation


@dataclass
class S3Location(BaseModel):
    BundleType: Optional[str]
    Bucket: Optional[str]
    ETag: Optional[str]
    Version: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Location"]:
        if not json_data:
            return None
        return cls(
            BundleType=json_data.get("BundleType"),
            Bucket=json_data.get("Bucket"),
            ETag=json_data.get("ETag"),
            Version=json_data.get("Version"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


@dataclass
class GitHubLocation(BaseModel):
    Repository: Optional[str]
    CommitId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GitHubLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitHubLocation"]:
        if not json_data:
            return None
        return cls(
            Repository=json_data.get("Repository"),
            CommitId=json_data.get("CommitId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitHubLocation = GitHubLocation


@dataclass
class AlarmConfiguration(BaseModel):
    Alarms: Optional[Sequence["_Alarm"]]
    IgnorePollAlarmFailure: Optional[bool]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AlarmConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlarmConfiguration"]:
        if not json_data:
            return None
        return cls(
            Alarms=deserialize_list(json_data.get("Alarms"), Alarm),
            IgnorePollAlarmFailure=json_data.get("IgnorePollAlarmFailure"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlarmConfiguration = AlarmConfiguration


@dataclass
class Alarm(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Alarm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Alarm"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Alarm = Alarm


@dataclass
class ECSService(BaseModel):
    ServiceName: Optional[str]
    ClusterName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ECSService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ECSService"]:
        if not json_data:
            return None
        return cls(
            ServiceName=json_data.get("ServiceName"),
            ClusterName=json_data.get("ClusterName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ECSService = ECSService


@dataclass
class AutoRollbackConfiguration(BaseModel):
    Events: Optional[Sequence[str]]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AutoRollbackConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoRollbackConfiguration"]:
        if not json_data:
            return None
        return cls(
            Events=json_data.get("Events"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoRollbackConfiguration = AutoRollbackConfiguration


@dataclass
class LoadBalancerInfo(BaseModel):
    TargetGroupInfoList: Optional[Sequence["_TargetGroupInfo"]]
    ElbInfoList: Optional[Sequence["_ELBInfo"]]
    TargetGroupPairInfoList: Optional[Sequence["_TargetGroupPairInfo"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerInfo"]:
        if not json_data:
            return None
        return cls(
            TargetGroupInfoList=deserialize_list(json_data.get("TargetGroupInfoList"), TargetGroupInfo),
            ElbInfoList=deserialize_list(json_data.get("ElbInfoList"), ELBInfo),
            TargetGroupPairInfoList=deserialize_list(json_data.get("TargetGroupPairInfoList"), TargetGroupPairInfo),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerInfo = LoadBalancerInfo


@dataclass
class TargetGroupInfo(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupInfo"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupInfo = TargetGroupInfo


@dataclass
class ELBInfo(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ELBInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ELBInfo"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ELBInfo = ELBInfo


@dataclass
class TargetGroupPairInfo(BaseModel):
    ProdTrafficRoute: Optional["_TrafficRoute"]
    TestTrafficRoute: Optional["_TrafficRoute"]
    TargetGroups: Optional[Sequence["_TargetGroupInfo"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupPairInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupPairInfo"]:
        if not json_data:
            return None
        return cls(
            ProdTrafficRoute=TrafficRoute._deserialize(json_data.get("ProdTrafficRoute")),
            TestTrafficRoute=TrafficRoute._deserialize(json_data.get("TestTrafficRoute")),
            TargetGroups=deserialize_list(json_data.get("TargetGroups"), TargetGroupInfo),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupPairInfo = TargetGroupPairInfo


@dataclass
class TrafficRoute(BaseModel):
    ListenerArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficRoute"]:
        if not json_data:
            return None
        return cls(
            ListenerArns=json_data.get("ListenerArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficRoute = TrafficRoute


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


