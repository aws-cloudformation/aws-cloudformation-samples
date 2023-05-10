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
class AwsKinesisfirehoseDeliverystream(BaseModel):
    Arn: Optional[str]
    DeliveryStreamEncryptionConfigurationInput: Optional["_DeliveryStreamEncryptionConfigurationInput"]
    DeliveryStreamName: Optional[str]
    DeliveryStreamType: Optional[str]
    ElasticsearchDestinationConfiguration: Optional["_ElasticsearchDestinationConfiguration"]
    AmazonopensearchserviceDestinationConfiguration: Optional["_AmazonopensearchserviceDestinationConfiguration"]
    AmazonOpenSearchServerlessDestinationConfiguration: Optional["_AmazonOpenSearchServerlessDestinationConfiguration"]
    ExtendedS3DestinationConfiguration: Optional["_ExtendedS3DestinationConfiguration"]
    KinesisStreamSourceConfiguration: Optional["_KinesisStreamSourceConfiguration"]
    RedshiftDestinationConfiguration: Optional["_RedshiftDestinationConfiguration"]
    S3DestinationConfiguration: Optional["_S3DestinationConfiguration"]
    SplunkDestinationConfiguration: Optional["_SplunkDestinationConfiguration"]
    HttpEndpointDestinationConfiguration: Optional["_HttpEndpointDestinationConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKinesisfirehoseDeliverystream"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKinesisfirehoseDeliverystream"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            DeliveryStreamEncryptionConfigurationInput=DeliveryStreamEncryptionConfigurationInput._deserialize(json_data.get("DeliveryStreamEncryptionConfigurationInput")),
            DeliveryStreamName=json_data.get("DeliveryStreamName"),
            DeliveryStreamType=json_data.get("DeliveryStreamType"),
            ElasticsearchDestinationConfiguration=ElasticsearchDestinationConfiguration._deserialize(json_data.get("ElasticsearchDestinationConfiguration")),
            AmazonopensearchserviceDestinationConfiguration=AmazonopensearchserviceDestinationConfiguration._deserialize(json_data.get("AmazonopensearchserviceDestinationConfiguration")),
            AmazonOpenSearchServerlessDestinationConfiguration=AmazonOpenSearchServerlessDestinationConfiguration._deserialize(json_data.get("AmazonOpenSearchServerlessDestinationConfiguration")),
            ExtendedS3DestinationConfiguration=ExtendedS3DestinationConfiguration._deserialize(json_data.get("ExtendedS3DestinationConfiguration")),
            KinesisStreamSourceConfiguration=KinesisStreamSourceConfiguration._deserialize(json_data.get("KinesisStreamSourceConfiguration")),
            RedshiftDestinationConfiguration=RedshiftDestinationConfiguration._deserialize(json_data.get("RedshiftDestinationConfiguration")),
            S3DestinationConfiguration=S3DestinationConfiguration._deserialize(json_data.get("S3DestinationConfiguration")),
            SplunkDestinationConfiguration=SplunkDestinationConfiguration._deserialize(json_data.get("SplunkDestinationConfiguration")),
            HttpEndpointDestinationConfiguration=HttpEndpointDestinationConfiguration._deserialize(json_data.get("HttpEndpointDestinationConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKinesisfirehoseDeliverystream = AwsKinesisfirehoseDeliverystream


@dataclass
class DeliveryStreamEncryptionConfigurationInput(BaseModel):
    KeyARN: Optional[str]
    KeyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeliveryStreamEncryptionConfigurationInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeliveryStreamEncryptionConfigurationInput"]:
        if not json_data:
            return None
        return cls(
            KeyARN=json_data.get("KeyARN"),
            KeyType=json_data.get("KeyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeliveryStreamEncryptionConfigurationInput = DeliveryStreamEncryptionConfigurationInput


@dataclass
class ElasticsearchDestinationConfiguration(BaseModel):
    BufferingHints: Optional["_ElasticsearchBufferingHints"]
    CloudWatchLoggingOptions: Optional["_CloudWatchLoggingOptions"]
    DomainARN: Optional[str]
    IndexName: Optional[str]
    IndexRotationPeriod: Optional[str]
    ProcessingConfiguration: Optional["_ProcessingConfiguration"]
    RetryOptions: Optional["_ElasticsearchRetryOptions"]
    RoleARN: Optional[str]
    S3BackupMode: Optional[str]
    S3Configuration: Optional["_S3DestinationConfiguration"]
    ClusterEndpoint: Optional[str]
    TypeName: Optional[str]
    VpcConfiguration: Optional["_VpcConfiguration"]
    DocumentIdOptions: Optional["_DocumentIdOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchDestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchDestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            BufferingHints=ElasticsearchBufferingHints._deserialize(json_data.get("BufferingHints")),
            CloudWatchLoggingOptions=CloudWatchLoggingOptions._deserialize(json_data.get("CloudWatchLoggingOptions")),
            DomainARN=json_data.get("DomainARN"),
            IndexName=json_data.get("IndexName"),
            IndexRotationPeriod=json_data.get("IndexRotationPeriod"),
            ProcessingConfiguration=ProcessingConfiguration._deserialize(json_data.get("ProcessingConfiguration")),
            RetryOptions=ElasticsearchRetryOptions._deserialize(json_data.get("RetryOptions")),
            RoleARN=json_data.get("RoleARN"),
            S3BackupMode=json_data.get("S3BackupMode"),
            S3Configuration=S3DestinationConfiguration._deserialize(json_data.get("S3Configuration")),
            ClusterEndpoint=json_data.get("ClusterEndpoint"),
            TypeName=json_data.get("TypeName"),
            VpcConfiguration=VpcConfiguration._deserialize(json_data.get("VpcConfiguration")),
            DocumentIdOptions=DocumentIdOptions._deserialize(json_data.get("DocumentIdOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchDestinationConfiguration = ElasticsearchDestinationConfiguration


@dataclass
class ElasticsearchBufferingHints(BaseModel):
    IntervalInSeconds: Optional[int]
    SizeInMBs: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchBufferingHints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchBufferingHints"]:
        if not json_data:
            return None
        return cls(
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            SizeInMBs=json_data.get("SizeInMBs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchBufferingHints = ElasticsearchBufferingHints


@dataclass
class CloudWatchLoggingOptions(BaseModel):
    Enabled: Optional[bool]
    LogGroupName: Optional[str]
    LogStreamName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLoggingOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLoggingOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogGroupName=json_data.get("LogGroupName"),
            LogStreamName=json_data.get("LogStreamName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLoggingOptions = CloudWatchLoggingOptions


@dataclass
class ProcessingConfiguration(BaseModel):
    Enabled: Optional[bool]
    Processors: Optional[Sequence["_Processor"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessingConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Processors=deserialize_list(json_data.get("Processors"), Processor),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessingConfiguration = ProcessingConfiguration


@dataclass
class Processor(BaseModel):
    Parameters: Optional[Sequence["_ProcessorParameter"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Processor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Processor"]:
        if not json_data:
            return None
        return cls(
            Parameters=deserialize_list(json_data.get("Parameters"), ProcessorParameter),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Processor = Processor


@dataclass
class ProcessorParameter(BaseModel):
    ParameterName: Optional[str]
    ParameterValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessorParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessorParameter"]:
        if not json_data:
            return None
        return cls(
            ParameterName=json_data.get("ParameterName"),
            ParameterValue=json_data.get("ParameterValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessorParameter = ProcessorParameter


@dataclass
class ElasticsearchRetryOptions(BaseModel):
    DurationInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchRetryOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchRetryOptions"]:
        if not json_data:
            return None
        return cls(
            DurationInSeconds=json_data.get("DurationInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchRetryOptions = ElasticsearchRetryOptions


@dataclass
class S3DestinationConfiguration(BaseModel):
    BucketARN: Optional[str]
    BufferingHints: Optional["_BufferingHints"]
    CloudWatchLoggingOptions: Optional["_CloudWatchLoggingOptions"]
    CompressionFormat: Optional[str]
    EncryptionConfiguration: Optional["_EncryptionConfiguration"]
    ErrorOutputPrefix: Optional[str]
    Prefix: Optional[str]
    RoleARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3DestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3DestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            BucketARN=json_data.get("BucketARN"),
            BufferingHints=BufferingHints._deserialize(json_data.get("BufferingHints")),
            CloudWatchLoggingOptions=CloudWatchLoggingOptions._deserialize(json_data.get("CloudWatchLoggingOptions")),
            CompressionFormat=json_data.get("CompressionFormat"),
            EncryptionConfiguration=EncryptionConfiguration._deserialize(json_data.get("EncryptionConfiguration")),
            ErrorOutputPrefix=json_data.get("ErrorOutputPrefix"),
            Prefix=json_data.get("Prefix"),
            RoleARN=json_data.get("RoleARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3DestinationConfiguration = S3DestinationConfiguration


@dataclass
class BufferingHints(BaseModel):
    IntervalInSeconds: Optional[int]
    SizeInMBs: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_BufferingHints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BufferingHints"]:
        if not json_data:
            return None
        return cls(
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            SizeInMBs=json_data.get("SizeInMBs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BufferingHints = BufferingHints


@dataclass
class EncryptionConfiguration(BaseModel):
    KMSEncryptionConfig: Optional["_KMSEncryptionConfig"]
    NoEncryptionConfig: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            KMSEncryptionConfig=KMSEncryptionConfig._deserialize(json_data.get("KMSEncryptionConfig")),
            NoEncryptionConfig=json_data.get("NoEncryptionConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfiguration = EncryptionConfiguration


@dataclass
class KMSEncryptionConfig(BaseModel):
    AWSKMSKeyARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KMSEncryptionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KMSEncryptionConfig"]:
        if not json_data:
            return None
        return cls(
            AWSKMSKeyARN=json_data.get("AWSKMSKeyARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KMSEncryptionConfig = KMSEncryptionConfig


@dataclass
class VpcConfiguration(BaseModel):
    RoleARN: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            RoleARN=json_data.get("RoleARN"),
            SubnetIds=json_data.get("SubnetIds"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfiguration = VpcConfiguration


@dataclass
class DocumentIdOptions(BaseModel):
    DefaultDocumentIdFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentIdOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentIdOptions"]:
        if not json_data:
            return None
        return cls(
            DefaultDocumentIdFormat=json_data.get("DefaultDocumentIdFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentIdOptions = DocumentIdOptions


@dataclass
class AmazonopensearchserviceDestinationConfiguration(BaseModel):
    BufferingHints: Optional["_AmazonopensearchserviceBufferingHints"]
    CloudWatchLoggingOptions: Optional["_CloudWatchLoggingOptions"]
    DomainARN: Optional[str]
    IndexName: Optional[str]
    IndexRotationPeriod: Optional[str]
    ProcessingConfiguration: Optional["_ProcessingConfiguration"]
    RetryOptions: Optional["_AmazonopensearchserviceRetryOptions"]
    RoleARN: Optional[str]
    S3BackupMode: Optional[str]
    S3Configuration: Optional["_S3DestinationConfiguration"]
    ClusterEndpoint: Optional[str]
    TypeName: Optional[str]
    VpcConfiguration: Optional["_VpcConfiguration"]
    DocumentIdOptions: Optional["_DocumentIdOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonopensearchserviceDestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonopensearchserviceDestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            BufferingHints=AmazonopensearchserviceBufferingHints._deserialize(json_data.get("BufferingHints")),
            CloudWatchLoggingOptions=CloudWatchLoggingOptions._deserialize(json_data.get("CloudWatchLoggingOptions")),
            DomainARN=json_data.get("DomainARN"),
            IndexName=json_data.get("IndexName"),
            IndexRotationPeriod=json_data.get("IndexRotationPeriod"),
            ProcessingConfiguration=ProcessingConfiguration._deserialize(json_data.get("ProcessingConfiguration")),
            RetryOptions=AmazonopensearchserviceRetryOptions._deserialize(json_data.get("RetryOptions")),
            RoleARN=json_data.get("RoleARN"),
            S3BackupMode=json_data.get("S3BackupMode"),
            S3Configuration=S3DestinationConfiguration._deserialize(json_data.get("S3Configuration")),
            ClusterEndpoint=json_data.get("ClusterEndpoint"),
            TypeName=json_data.get("TypeName"),
            VpcConfiguration=VpcConfiguration._deserialize(json_data.get("VpcConfiguration")),
            DocumentIdOptions=DocumentIdOptions._deserialize(json_data.get("DocumentIdOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonopensearchserviceDestinationConfiguration = AmazonopensearchserviceDestinationConfiguration


@dataclass
class AmazonopensearchserviceBufferingHints(BaseModel):
    IntervalInSeconds: Optional[int]
    SizeInMBs: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonopensearchserviceBufferingHints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonopensearchserviceBufferingHints"]:
        if not json_data:
            return None
        return cls(
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            SizeInMBs=json_data.get("SizeInMBs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonopensearchserviceBufferingHints = AmazonopensearchserviceBufferingHints


@dataclass
class AmazonopensearchserviceRetryOptions(BaseModel):
    DurationInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonopensearchserviceRetryOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonopensearchserviceRetryOptions"]:
        if not json_data:
            return None
        return cls(
            DurationInSeconds=json_data.get("DurationInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonopensearchserviceRetryOptions = AmazonopensearchserviceRetryOptions


@dataclass
class AmazonOpenSearchServerlessDestinationConfiguration(BaseModel):
    BufferingHints: Optional["_AmazonOpenSearchServerlessBufferingHints"]
    CloudWatchLoggingOptions: Optional["_CloudWatchLoggingOptions"]
    IndexName: Optional[str]
    ProcessingConfiguration: Optional["_ProcessingConfiguration"]
    RetryOptions: Optional["_AmazonOpenSearchServerlessRetryOptions"]
    RoleARN: Optional[str]
    S3BackupMode: Optional[str]
    S3Configuration: Optional["_S3DestinationConfiguration"]
    CollectionEndpoint: Optional[str]
    VpcConfiguration: Optional["_VpcConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonOpenSearchServerlessDestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonOpenSearchServerlessDestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            BufferingHints=AmazonOpenSearchServerlessBufferingHints._deserialize(json_data.get("BufferingHints")),
            CloudWatchLoggingOptions=CloudWatchLoggingOptions._deserialize(json_data.get("CloudWatchLoggingOptions")),
            IndexName=json_data.get("IndexName"),
            ProcessingConfiguration=ProcessingConfiguration._deserialize(json_data.get("ProcessingConfiguration")),
            RetryOptions=AmazonOpenSearchServerlessRetryOptions._deserialize(json_data.get("RetryOptions")),
            RoleARN=json_data.get("RoleARN"),
            S3BackupMode=json_data.get("S3BackupMode"),
            S3Configuration=S3DestinationConfiguration._deserialize(json_data.get("S3Configuration")),
            CollectionEndpoint=json_data.get("CollectionEndpoint"),
            VpcConfiguration=VpcConfiguration._deserialize(json_data.get("VpcConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonOpenSearchServerlessDestinationConfiguration = AmazonOpenSearchServerlessDestinationConfiguration


@dataclass
class AmazonOpenSearchServerlessBufferingHints(BaseModel):
    IntervalInSeconds: Optional[int]
    SizeInMBs: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonOpenSearchServerlessBufferingHints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonOpenSearchServerlessBufferingHints"]:
        if not json_data:
            return None
        return cls(
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            SizeInMBs=json_data.get("SizeInMBs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonOpenSearchServerlessBufferingHints = AmazonOpenSearchServerlessBufferingHints


@dataclass
class AmazonOpenSearchServerlessRetryOptions(BaseModel):
    DurationInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonOpenSearchServerlessRetryOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonOpenSearchServerlessRetryOptions"]:
        if not json_data:
            return None
        return cls(
            DurationInSeconds=json_data.get("DurationInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonOpenSearchServerlessRetryOptions = AmazonOpenSearchServerlessRetryOptions


@dataclass
class ExtendedS3DestinationConfiguration(BaseModel):
    BucketARN: Optional[str]
    BufferingHints: Optional["_BufferingHints"]
    CloudWatchLoggingOptions: Optional["_CloudWatchLoggingOptions"]
    CompressionFormat: Optional[str]
    DataFormatConversionConfiguration: Optional["_DataFormatConversionConfiguration"]
    DynamicPartitioningConfiguration: Optional["_DynamicPartitioningConfiguration"]
    EncryptionConfiguration: Optional["_EncryptionConfiguration"]
    ErrorOutputPrefix: Optional[str]
    Prefix: Optional[str]
    ProcessingConfiguration: Optional["_ProcessingConfiguration"]
    RoleARN: Optional[str]
    S3BackupConfiguration: Optional["_S3DestinationConfiguration"]
    S3BackupMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtendedS3DestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtendedS3DestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            BucketARN=json_data.get("BucketARN"),
            BufferingHints=BufferingHints._deserialize(json_data.get("BufferingHints")),
            CloudWatchLoggingOptions=CloudWatchLoggingOptions._deserialize(json_data.get("CloudWatchLoggingOptions")),
            CompressionFormat=json_data.get("CompressionFormat"),
            DataFormatConversionConfiguration=DataFormatConversionConfiguration._deserialize(json_data.get("DataFormatConversionConfiguration")),
            DynamicPartitioningConfiguration=DynamicPartitioningConfiguration._deserialize(json_data.get("DynamicPartitioningConfiguration")),
            EncryptionConfiguration=EncryptionConfiguration._deserialize(json_data.get("EncryptionConfiguration")),
            ErrorOutputPrefix=json_data.get("ErrorOutputPrefix"),
            Prefix=json_data.get("Prefix"),
            ProcessingConfiguration=ProcessingConfiguration._deserialize(json_data.get("ProcessingConfiguration")),
            RoleARN=json_data.get("RoleARN"),
            S3BackupConfiguration=S3DestinationConfiguration._deserialize(json_data.get("S3BackupConfiguration")),
            S3BackupMode=json_data.get("S3BackupMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtendedS3DestinationConfiguration = ExtendedS3DestinationConfiguration


@dataclass
class DataFormatConversionConfiguration(BaseModel):
    Enabled: Optional[bool]
    InputFormatConfiguration: Optional["_InputFormatConfiguration"]
    OutputFormatConfiguration: Optional["_OutputFormatConfiguration"]
    SchemaConfiguration: Optional["_SchemaConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DataFormatConversionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataFormatConversionConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            InputFormatConfiguration=InputFormatConfiguration._deserialize(json_data.get("InputFormatConfiguration")),
            OutputFormatConfiguration=OutputFormatConfiguration._deserialize(json_data.get("OutputFormatConfiguration")),
            SchemaConfiguration=SchemaConfiguration._deserialize(json_data.get("SchemaConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataFormatConversionConfiguration = DataFormatConversionConfiguration


@dataclass
class InputFormatConfiguration(BaseModel):
    Deserializer: Optional["_Deserializer"]

    @classmethod
    def _deserialize(
        cls: Type["_InputFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            Deserializer=Deserializer._deserialize(json_data.get("Deserializer")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputFormatConfiguration = InputFormatConfiguration


@dataclass
class Deserializer(BaseModel):
    HiveJsonSerDe: Optional["_HiveJsonSerDe"]
    OpenXJsonSerDe: Optional["_OpenXJsonSerDe"]

    @classmethod
    def _deserialize(
        cls: Type["_Deserializer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Deserializer"]:
        if not json_data:
            return None
        return cls(
            HiveJsonSerDe=HiveJsonSerDe._deserialize(json_data.get("HiveJsonSerDe")),
            OpenXJsonSerDe=OpenXJsonSerDe._deserialize(json_data.get("OpenXJsonSerDe")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Deserializer = Deserializer


@dataclass
class HiveJsonSerDe(BaseModel):
    TimestampFormats: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HiveJsonSerDe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HiveJsonSerDe"]:
        if not json_data:
            return None
        return cls(
            TimestampFormats=json_data.get("TimestampFormats"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HiveJsonSerDe = HiveJsonSerDe


@dataclass
class OpenXJsonSerDe(BaseModel):
    CaseInsensitive: Optional[bool]
    ColumnToJsonKeyMappings: Optional[MutableMapping[str, str]]
    ConvertDotsInJsonKeysToUnderscores: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_OpenXJsonSerDe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenXJsonSerDe"]:
        if not json_data:
            return None
        return cls(
            CaseInsensitive=json_data.get("CaseInsensitive"),
            ColumnToJsonKeyMappings=json_data.get("ColumnToJsonKeyMappings"),
            ConvertDotsInJsonKeysToUnderscores=json_data.get("ConvertDotsInJsonKeysToUnderscores"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenXJsonSerDe = OpenXJsonSerDe


@dataclass
class OutputFormatConfiguration(BaseModel):
    Serializer: Optional["_Serializer"]

    @classmethod
    def _deserialize(
        cls: Type["_OutputFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            Serializer=Serializer._deserialize(json_data.get("Serializer")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputFormatConfiguration = OutputFormatConfiguration


@dataclass
class Serializer(BaseModel):
    OrcSerDe: Optional["_OrcSerDe"]
    ParquetSerDe: Optional["_ParquetSerDe"]

    @classmethod
    def _deserialize(
        cls: Type["_Serializer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Serializer"]:
        if not json_data:
            return None
        return cls(
            OrcSerDe=OrcSerDe._deserialize(json_data.get("OrcSerDe")),
            ParquetSerDe=ParquetSerDe._deserialize(json_data.get("ParquetSerDe")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Serializer = Serializer


@dataclass
class OrcSerDe(BaseModel):
    BlockSizeBytes: Optional[int]
    BloomFilterColumns: Optional[Sequence[str]]
    BloomFilterFalsePositiveProbability: Optional[float]
    Compression: Optional[str]
    DictionaryKeyThreshold: Optional[float]
    EnablePadding: Optional[bool]
    FormatVersion: Optional[str]
    PaddingTolerance: Optional[float]
    RowIndexStride: Optional[int]
    StripeSizeBytes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_OrcSerDe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrcSerDe"]:
        if not json_data:
            return None
        return cls(
            BlockSizeBytes=json_data.get("BlockSizeBytes"),
            BloomFilterColumns=json_data.get("BloomFilterColumns"),
            BloomFilterFalsePositiveProbability=json_data.get("BloomFilterFalsePositiveProbability"),
            Compression=json_data.get("Compression"),
            DictionaryKeyThreshold=json_data.get("DictionaryKeyThreshold"),
            EnablePadding=json_data.get("EnablePadding"),
            FormatVersion=json_data.get("FormatVersion"),
            PaddingTolerance=json_data.get("PaddingTolerance"),
            RowIndexStride=json_data.get("RowIndexStride"),
            StripeSizeBytes=json_data.get("StripeSizeBytes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrcSerDe = OrcSerDe


@dataclass
class ParquetSerDe(BaseModel):
    BlockSizeBytes: Optional[int]
    Compression: Optional[str]
    EnableDictionaryCompression: Optional[bool]
    MaxPaddingBytes: Optional[int]
    PageSizeBytes: Optional[int]
    WriterVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParquetSerDe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParquetSerDe"]:
        if not json_data:
            return None
        return cls(
            BlockSizeBytes=json_data.get("BlockSizeBytes"),
            Compression=json_data.get("Compression"),
            EnableDictionaryCompression=json_data.get("EnableDictionaryCompression"),
            MaxPaddingBytes=json_data.get("MaxPaddingBytes"),
            PageSizeBytes=json_data.get("PageSizeBytes"),
            WriterVersion=json_data.get("WriterVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParquetSerDe = ParquetSerDe


@dataclass
class SchemaConfiguration(BaseModel):
    CatalogId: Optional[str]
    DatabaseName: Optional[str]
    Region: Optional[str]
    RoleARN: Optional[str]
    TableName: Optional[str]
    VersionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaConfiguration"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            Region=json_data.get("Region"),
            RoleARN=json_data.get("RoleARN"),
            TableName=json_data.get("TableName"),
            VersionId=json_data.get("VersionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaConfiguration = SchemaConfiguration


@dataclass
class DynamicPartitioningConfiguration(BaseModel):
    Enabled: Optional[bool]
    RetryOptions: Optional["_RetryOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicPartitioningConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicPartitioningConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            RetryOptions=RetryOptions._deserialize(json_data.get("RetryOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicPartitioningConfiguration = DynamicPartitioningConfiguration


@dataclass
class RetryOptions(BaseModel):
    DurationInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RetryOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryOptions"]:
        if not json_data:
            return None
        return cls(
            DurationInSeconds=json_data.get("DurationInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryOptions = RetryOptions


@dataclass
class KinesisStreamSourceConfiguration(BaseModel):
    KinesisStreamARN: Optional[str]
    RoleARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamSourceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamSourceConfiguration"]:
        if not json_data:
            return None
        return cls(
            KinesisStreamARN=json_data.get("KinesisStreamARN"),
            RoleARN=json_data.get("RoleARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamSourceConfiguration = KinesisStreamSourceConfiguration


@dataclass
class RedshiftDestinationConfiguration(BaseModel):
    CloudWatchLoggingOptions: Optional["_CloudWatchLoggingOptions"]
    ClusterJDBCURL: Optional[str]
    CopyCommand: Optional["_CopyCommand"]
    Password: Optional[str]
    ProcessingConfiguration: Optional["_ProcessingConfiguration"]
    RetryOptions: Optional["_RedshiftRetryOptions"]
    RoleARN: Optional[str]
    S3BackupConfiguration: Optional["_S3DestinationConfiguration"]
    S3BackupMode: Optional[str]
    S3Configuration: Optional["_S3DestinationConfiguration"]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftDestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftDestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLoggingOptions=CloudWatchLoggingOptions._deserialize(json_data.get("CloudWatchLoggingOptions")),
            ClusterJDBCURL=json_data.get("ClusterJDBCURL"),
            CopyCommand=CopyCommand._deserialize(json_data.get("CopyCommand")),
            Password=json_data.get("Password"),
            ProcessingConfiguration=ProcessingConfiguration._deserialize(json_data.get("ProcessingConfiguration")),
            RetryOptions=RedshiftRetryOptions._deserialize(json_data.get("RetryOptions")),
            RoleARN=json_data.get("RoleARN"),
            S3BackupConfiguration=S3DestinationConfiguration._deserialize(json_data.get("S3BackupConfiguration")),
            S3BackupMode=json_data.get("S3BackupMode"),
            S3Configuration=S3DestinationConfiguration._deserialize(json_data.get("S3Configuration")),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftDestinationConfiguration = RedshiftDestinationConfiguration


@dataclass
class CopyCommand(BaseModel):
    CopyOptions: Optional[str]
    DataTableColumns: Optional[str]
    DataTableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CopyCommand"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CopyCommand"]:
        if not json_data:
            return None
        return cls(
            CopyOptions=json_data.get("CopyOptions"),
            DataTableColumns=json_data.get("DataTableColumns"),
            DataTableName=json_data.get("DataTableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CopyCommand = CopyCommand


@dataclass
class RedshiftRetryOptions(BaseModel):
    DurationInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftRetryOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftRetryOptions"]:
        if not json_data:
            return None
        return cls(
            DurationInSeconds=json_data.get("DurationInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftRetryOptions = RedshiftRetryOptions


@dataclass
class SplunkDestinationConfiguration(BaseModel):
    CloudWatchLoggingOptions: Optional["_CloudWatchLoggingOptions"]
    HECAcknowledgmentTimeoutInSeconds: Optional[int]
    HECEndpoint: Optional[str]
    HECEndpointType: Optional[str]
    HECToken: Optional[str]
    ProcessingConfiguration: Optional["_ProcessingConfiguration"]
    RetryOptions: Optional["_SplunkRetryOptions"]
    S3BackupMode: Optional[str]
    S3Configuration: Optional["_S3DestinationConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_SplunkDestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplunkDestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLoggingOptions=CloudWatchLoggingOptions._deserialize(json_data.get("CloudWatchLoggingOptions")),
            HECAcknowledgmentTimeoutInSeconds=json_data.get("HECAcknowledgmentTimeoutInSeconds"),
            HECEndpoint=json_data.get("HECEndpoint"),
            HECEndpointType=json_data.get("HECEndpointType"),
            HECToken=json_data.get("HECToken"),
            ProcessingConfiguration=ProcessingConfiguration._deserialize(json_data.get("ProcessingConfiguration")),
            RetryOptions=SplunkRetryOptions._deserialize(json_data.get("RetryOptions")),
            S3BackupMode=json_data.get("S3BackupMode"),
            S3Configuration=S3DestinationConfiguration._deserialize(json_data.get("S3Configuration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplunkDestinationConfiguration = SplunkDestinationConfiguration


@dataclass
class SplunkRetryOptions(BaseModel):
    DurationInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SplunkRetryOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplunkRetryOptions"]:
        if not json_data:
            return None
        return cls(
            DurationInSeconds=json_data.get("DurationInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplunkRetryOptions = SplunkRetryOptions


@dataclass
class HttpEndpointDestinationConfiguration(BaseModel):
    RoleARN: Optional[str]
    EndpointConfiguration: Optional["_HttpEndpointConfiguration"]
    RequestConfiguration: Optional["_HttpEndpointRequestConfiguration"]
    BufferingHints: Optional["_BufferingHints"]
    CloudWatchLoggingOptions: Optional["_CloudWatchLoggingOptions"]
    ProcessingConfiguration: Optional["_ProcessingConfiguration"]
    RetryOptions: Optional["_RetryOptions"]
    S3BackupMode: Optional[str]
    S3Configuration: Optional["_S3DestinationConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpEndpointDestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpEndpointDestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            RoleARN=json_data.get("RoleARN"),
            EndpointConfiguration=HttpEndpointConfiguration._deserialize(json_data.get("EndpointConfiguration")),
            RequestConfiguration=HttpEndpointRequestConfiguration._deserialize(json_data.get("RequestConfiguration")),
            BufferingHints=BufferingHints._deserialize(json_data.get("BufferingHints")),
            CloudWatchLoggingOptions=CloudWatchLoggingOptions._deserialize(json_data.get("CloudWatchLoggingOptions")),
            ProcessingConfiguration=ProcessingConfiguration._deserialize(json_data.get("ProcessingConfiguration")),
            RetryOptions=RetryOptions._deserialize(json_data.get("RetryOptions")),
            S3BackupMode=json_data.get("S3BackupMode"),
            S3Configuration=S3DestinationConfiguration._deserialize(json_data.get("S3Configuration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpEndpointDestinationConfiguration = HttpEndpointDestinationConfiguration


@dataclass
class HttpEndpointConfiguration(BaseModel):
    Url: Optional[str]
    AccessKey: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpEndpointConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpEndpointConfiguration"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
            AccessKey=json_data.get("AccessKey"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpEndpointConfiguration = HttpEndpointConfiguration


@dataclass
class HttpEndpointRequestConfiguration(BaseModel):
    ContentEncoding: Optional[str]
    CommonAttributes: Optional[Sequence["_HttpEndpointCommonAttribute"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpEndpointRequestConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpEndpointRequestConfiguration"]:
        if not json_data:
            return None
        return cls(
            ContentEncoding=json_data.get("ContentEncoding"),
            CommonAttributes=deserialize_list(json_data.get("CommonAttributes"), HttpEndpointCommonAttribute),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpEndpointRequestConfiguration = HttpEndpointRequestConfiguration


@dataclass
class HttpEndpointCommonAttribute(BaseModel):
    AttributeName: Optional[str]
    AttributeValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpEndpointCommonAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpEndpointCommonAttribute"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            AttributeValue=json_data.get("AttributeValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpEndpointCommonAttribute = HttpEndpointCommonAttribute


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


