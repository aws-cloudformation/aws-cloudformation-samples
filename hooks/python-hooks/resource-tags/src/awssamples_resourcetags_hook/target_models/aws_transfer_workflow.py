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
class AwsTransferWorkflow(BaseModel):
    OnExceptionSteps: Optional[Sequence["_WorkflowStep"]]
    Steps: Optional[Sequence["_WorkflowStep"]]
    Tags: Optional[Any]
    Description: Optional[str]
    WorkflowId: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsTransferWorkflow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsTransferWorkflow"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OnExceptionSteps=deserialize_list(json_data.get("OnExceptionSteps"), WorkflowStep),
            Steps=deserialize_list(json_data.get("Steps"), WorkflowStep),
            Tags=json_data.get("Tags"),
            Description=json_data.get("Description"),
            WorkflowId=json_data.get("WorkflowId"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsTransferWorkflow = AwsTransferWorkflow


@dataclass
class WorkflowStep(BaseModel):
    CopyStepDetails: Optional["_CopyStepDetails"]
    CustomStepDetails: Optional["_CustomStepDetails"]
    DecryptStepDetails: Optional["_DecryptStepDetails"]
    DeleteStepDetails: Optional["_DeleteStepDetails"]
    TagStepDetails: Optional["_TagStepDetails"]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowStep"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowStep"]:
        if not json_data:
            return None
        return cls(
            CopyStepDetails=CopyStepDetails._deserialize(json_data.get("CopyStepDetails")),
            CustomStepDetails=CustomStepDetails._deserialize(json_data.get("CustomStepDetails")),
            DecryptStepDetails=DecryptStepDetails._deserialize(json_data.get("DecryptStepDetails")),
            DeleteStepDetails=DeleteStepDetails._deserialize(json_data.get("DeleteStepDetails")),
            TagStepDetails=TagStepDetails._deserialize(json_data.get("TagStepDetails")),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowStep = WorkflowStep


@dataclass
class CopyStepDetails(BaseModel):
    DestinationFileLocation: Optional["_S3FileLocation"]
    Name: Optional[str]
    OverwriteExisting: Optional[str]
    SourceFileLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CopyStepDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CopyStepDetails"]:
        if not json_data:
            return None
        return cls(
            DestinationFileLocation=S3FileLocation._deserialize(json_data.get("DestinationFileLocation")),
            Name=json_data.get("Name"),
            OverwriteExisting=json_data.get("OverwriteExisting"),
            SourceFileLocation=json_data.get("SourceFileLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CopyStepDetails = CopyStepDetails


@dataclass
class S3FileLocation(BaseModel):
    S3FileLocation: Optional["_S3InputFileLocation"]

    @classmethod
    def _deserialize(
        cls: Type["_S3FileLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3FileLocation"]:
        if not json_data:
            return None
        return cls(
            S3FileLocation=S3InputFileLocation._deserialize(json_data.get("S3FileLocation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3FileLocation = S3FileLocation


@dataclass
class S3InputFileLocation(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3InputFileLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3InputFileLocation"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3InputFileLocation = S3InputFileLocation


@dataclass
class CustomStepDetails(BaseModel):
    Name: Optional[str]
    Target: Optional[str]
    TimeoutSeconds: Optional[int]
    SourceFileLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomStepDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomStepDetails"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Target=json_data.get("Target"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            SourceFileLocation=json_data.get("SourceFileLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomStepDetails = CustomStepDetails


@dataclass
class DecryptStepDetails(BaseModel):
    DestinationFileLocation: Optional["_InputFileLocation"]
    Name: Optional[str]
    Type: Optional[str]
    OverwriteExisting: Optional[str]
    SourceFileLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DecryptStepDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DecryptStepDetails"]:
        if not json_data:
            return None
        return cls(
            DestinationFileLocation=InputFileLocation._deserialize(json_data.get("DestinationFileLocation")),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            OverwriteExisting=json_data.get("OverwriteExisting"),
            SourceFileLocation=json_data.get("SourceFileLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DecryptStepDetails = DecryptStepDetails


@dataclass
class InputFileLocation(BaseModel):
    S3FileLocation: Optional["_S3InputFileLocation"]
    EfsFileLocation: Optional["_EfsInputFileLocation"]

    @classmethod
    def _deserialize(
        cls: Type["_InputFileLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputFileLocation"]:
        if not json_data:
            return None
        return cls(
            S3FileLocation=S3InputFileLocation._deserialize(json_data.get("S3FileLocation")),
            EfsFileLocation=EfsInputFileLocation._deserialize(json_data.get("EfsFileLocation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputFileLocation = InputFileLocation


@dataclass
class EfsInputFileLocation(BaseModel):
    FileSystemId: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EfsInputFileLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EfsInputFileLocation"]:
        if not json_data:
            return None
        return cls(
            FileSystemId=json_data.get("FileSystemId"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EfsInputFileLocation = EfsInputFileLocation


@dataclass
class DeleteStepDetails(BaseModel):
    Name: Optional[str]
    SourceFileLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeleteStepDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeleteStepDetails"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SourceFileLocation=json_data.get("SourceFileLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeleteStepDetails = DeleteStepDetails


@dataclass
class TagStepDetails(BaseModel):
    Name: Optional[str]
    Tags: Optional[AbstractSet["_S3Tag"]]
    SourceFileLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagStepDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagStepDetails"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Tags=set_or_none(json_data.get("Tags")),
            SourceFileLocation=json_data.get("SourceFileLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagStepDetails = TagStepDetails


@dataclass
class S3Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Tag = S3Tag


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


