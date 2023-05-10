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
class AwsKendraDatasource(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    Name: Optional[str]
    IndexId: Optional[str]
    Type: Optional[str]
    DataSourceConfiguration: Optional["_DataSourceConfiguration"]
    Description: Optional[str]
    Schedule: Optional[str]
    RoleArn: Optional[str]
    Tags: Optional[Any]
    CustomDocumentEnrichmentConfiguration: Optional["_CustomDocumentEnrichmentConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKendraDatasource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKendraDatasource"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            IndexId=json_data.get("IndexId"),
            Type=json_data.get("Type"),
            DataSourceConfiguration=DataSourceConfiguration._deserialize(json_data.get("DataSourceConfiguration")),
            Description=json_data.get("Description"),
            Schedule=json_data.get("Schedule"),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
            CustomDocumentEnrichmentConfiguration=CustomDocumentEnrichmentConfiguration._deserialize(json_data.get("CustomDocumentEnrichmentConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKendraDatasource = AwsKendraDatasource


@dataclass
class DataSourceConfiguration(BaseModel):
    S3Configuration: Optional["_S3DataSourceConfiguration"]
    SharePointConfiguration: Optional["_SharePointConfiguration"]
    SalesforceConfiguration: Optional["_SalesforceConfiguration"]
    OneDriveConfiguration: Optional["_OneDriveConfiguration"]
    ServiceNowConfiguration: Optional["_ServiceNowConfiguration"]
    DatabaseConfiguration: Optional["_DatabaseConfiguration"]
    ConfluenceConfiguration: Optional["_ConfluenceConfiguration"]
    GoogleDriveConfiguration: Optional["_GoogleDriveConfiguration"]
    WebCrawlerConfiguration: Optional["_WebCrawlerConfiguration"]
    WorkDocsConfiguration: Optional["_WorkDocsConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DataSourceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSourceConfiguration"]:
        if not json_data:
            return None
        return cls(
            S3Configuration=S3DataSourceConfiguration._deserialize(json_data.get("S3Configuration")),
            SharePointConfiguration=SharePointConfiguration._deserialize(json_data.get("SharePointConfiguration")),
            SalesforceConfiguration=SalesforceConfiguration._deserialize(json_data.get("SalesforceConfiguration")),
            OneDriveConfiguration=OneDriveConfiguration._deserialize(json_data.get("OneDriveConfiguration")),
            ServiceNowConfiguration=ServiceNowConfiguration._deserialize(json_data.get("ServiceNowConfiguration")),
            DatabaseConfiguration=DatabaseConfiguration._deserialize(json_data.get("DatabaseConfiguration")),
            ConfluenceConfiguration=ConfluenceConfiguration._deserialize(json_data.get("ConfluenceConfiguration")),
            GoogleDriveConfiguration=GoogleDriveConfiguration._deserialize(json_data.get("GoogleDriveConfiguration")),
            WebCrawlerConfiguration=WebCrawlerConfiguration._deserialize(json_data.get("WebCrawlerConfiguration")),
            WorkDocsConfiguration=WorkDocsConfiguration._deserialize(json_data.get("WorkDocsConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSourceConfiguration = DataSourceConfiguration


@dataclass
class S3DataSourceConfiguration(BaseModel):
    BucketName: Optional[str]
    InclusionPrefixes: Optional[Sequence[str]]
    InclusionPatterns: Optional[Sequence[str]]
    ExclusionPatterns: Optional[Sequence[str]]
    DocumentsMetadataConfiguration: Optional["_DocumentsMetadataConfiguration"]
    AccessControlListConfiguration: Optional["_AccessControlListConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_S3DataSourceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3DataSourceConfiguration"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            InclusionPrefixes=json_data.get("InclusionPrefixes"),
            InclusionPatterns=json_data.get("InclusionPatterns"),
            ExclusionPatterns=json_data.get("ExclusionPatterns"),
            DocumentsMetadataConfiguration=DocumentsMetadataConfiguration._deserialize(json_data.get("DocumentsMetadataConfiguration")),
            AccessControlListConfiguration=AccessControlListConfiguration._deserialize(json_data.get("AccessControlListConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3DataSourceConfiguration = S3DataSourceConfiguration


@dataclass
class DocumentsMetadataConfiguration(BaseModel):
    S3Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentsMetadataConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentsMetadataConfiguration"]:
        if not json_data:
            return None
        return cls(
            S3Prefix=json_data.get("S3Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentsMetadataConfiguration = DocumentsMetadataConfiguration


@dataclass
class AccessControlListConfiguration(BaseModel):
    KeyPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlListConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlListConfiguration"]:
        if not json_data:
            return None
        return cls(
            KeyPath=json_data.get("KeyPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlListConfiguration = AccessControlListConfiguration


@dataclass
class SharePointConfiguration(BaseModel):
    SharePointVersion: Optional[str]
    Urls: Optional[Sequence[str]]
    SecretArn: Optional[str]
    CrawlAttachments: Optional[bool]
    UseChangeLog: Optional[bool]
    InclusionPatterns: Optional[Sequence[str]]
    ExclusionPatterns: Optional[Sequence[str]]
    VpcConfiguration: Optional["_DataSourceVpcConfiguration"]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]
    DocumentTitleFieldName: Optional[str]
    DisableLocalGroups: Optional[bool]
    SslCertificateS3Path: Optional["_S3Path"]

    @classmethod
    def _deserialize(
        cls: Type["_SharePointConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SharePointConfiguration"]:
        if not json_data:
            return None
        return cls(
            SharePointVersion=json_data.get("SharePointVersion"),
            Urls=json_data.get("Urls"),
            SecretArn=json_data.get("SecretArn"),
            CrawlAttachments=json_data.get("CrawlAttachments"),
            UseChangeLog=json_data.get("UseChangeLog"),
            InclusionPatterns=json_data.get("InclusionPatterns"),
            ExclusionPatterns=json_data.get("ExclusionPatterns"),
            VpcConfiguration=DataSourceVpcConfiguration._deserialize(json_data.get("VpcConfiguration")),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
            DocumentTitleFieldName=json_data.get("DocumentTitleFieldName"),
            DisableLocalGroups=json_data.get("DisableLocalGroups"),
            SslCertificateS3Path=S3Path._deserialize(json_data.get("SslCertificateS3Path")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SharePointConfiguration = SharePointConfiguration


@dataclass
class DataSourceVpcConfiguration(BaseModel):
    SubnetIds: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DataSourceVpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSourceVpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            SubnetIds=json_data.get("SubnetIds"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSourceVpcConfiguration = DataSourceVpcConfiguration


@dataclass
class DataSourceToIndexFieldMapping(BaseModel):
    DataSourceFieldName: Optional[str]
    DateFieldFormat: Optional[str]
    IndexFieldName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataSourceToIndexFieldMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSourceToIndexFieldMapping"]:
        if not json_data:
            return None
        return cls(
            DataSourceFieldName=json_data.get("DataSourceFieldName"),
            DateFieldFormat=json_data.get("DateFieldFormat"),
            IndexFieldName=json_data.get("IndexFieldName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSourceToIndexFieldMapping = DataSourceToIndexFieldMapping


@dataclass
class S3Path(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Path"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Path"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Path = S3Path


@dataclass
class SalesforceConfiguration(BaseModel):
    ServerUrl: Optional[str]
    SecretArn: Optional[str]
    StandardObjectConfigurations: Optional[Sequence["_SalesforceStandardObjectConfiguration"]]
    KnowledgeArticleConfiguration: Optional["_SalesforceKnowledgeArticleConfiguration"]
    ChatterFeedConfiguration: Optional["_SalesforceChatterFeedConfiguration"]
    CrawlAttachments: Optional[bool]
    StandardObjectAttachmentConfiguration: Optional["_SalesforceStandardObjectAttachmentConfiguration"]
    IncludeAttachmentFilePatterns: Optional[Sequence[str]]
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SalesforceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SalesforceConfiguration"]:
        if not json_data:
            return None
        return cls(
            ServerUrl=json_data.get("ServerUrl"),
            SecretArn=json_data.get("SecretArn"),
            StandardObjectConfigurations=deserialize_list(json_data.get("StandardObjectConfigurations"), SalesforceStandardObjectConfiguration),
            KnowledgeArticleConfiguration=SalesforceKnowledgeArticleConfiguration._deserialize(json_data.get("KnowledgeArticleConfiguration")),
            ChatterFeedConfiguration=SalesforceChatterFeedConfiguration._deserialize(json_data.get("ChatterFeedConfiguration")),
            CrawlAttachments=json_data.get("CrawlAttachments"),
            StandardObjectAttachmentConfiguration=SalesforceStandardObjectAttachmentConfiguration._deserialize(json_data.get("StandardObjectAttachmentConfiguration")),
            IncludeAttachmentFilePatterns=json_data.get("IncludeAttachmentFilePatterns"),
            ExcludeAttachmentFilePatterns=json_data.get("ExcludeAttachmentFilePatterns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceConfiguration = SalesforceConfiguration


@dataclass
class SalesforceStandardObjectConfiguration(BaseModel):
    Name: Optional[str]
    DocumentDataFieldName: Optional[str]
    DocumentTitleFieldName: Optional[str]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_SalesforceStandardObjectConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SalesforceStandardObjectConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            DocumentDataFieldName=json_data.get("DocumentDataFieldName"),
            DocumentTitleFieldName=json_data.get("DocumentTitleFieldName"),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceStandardObjectConfiguration = SalesforceStandardObjectConfiguration


@dataclass
class SalesforceKnowledgeArticleConfiguration(BaseModel):
    IncludedStates: Optional[Sequence[str]]
    StandardKnowledgeArticleTypeConfiguration: Optional["_SalesforceStandardKnowledgeArticleTypeConfiguration"]
    CustomKnowledgeArticleTypeConfigurations: Optional[Sequence["_SalesforceCustomKnowledgeArticleTypeConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_SalesforceKnowledgeArticleConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SalesforceKnowledgeArticleConfiguration"]:
        if not json_data:
            return None
        return cls(
            IncludedStates=json_data.get("IncludedStates"),
            StandardKnowledgeArticleTypeConfiguration=SalesforceStandardKnowledgeArticleTypeConfiguration._deserialize(json_data.get("StandardKnowledgeArticleTypeConfiguration")),
            CustomKnowledgeArticleTypeConfigurations=deserialize_list(json_data.get("CustomKnowledgeArticleTypeConfigurations"), SalesforceCustomKnowledgeArticleTypeConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceKnowledgeArticleConfiguration = SalesforceKnowledgeArticleConfiguration


@dataclass
class SalesforceStandardKnowledgeArticleTypeConfiguration(BaseModel):
    DocumentDataFieldName: Optional[str]
    DocumentTitleFieldName: Optional[str]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_SalesforceStandardKnowledgeArticleTypeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SalesforceStandardKnowledgeArticleTypeConfiguration"]:
        if not json_data:
            return None
        return cls(
            DocumentDataFieldName=json_data.get("DocumentDataFieldName"),
            DocumentTitleFieldName=json_data.get("DocumentTitleFieldName"),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceStandardKnowledgeArticleTypeConfiguration = SalesforceStandardKnowledgeArticleTypeConfiguration


@dataclass
class SalesforceCustomKnowledgeArticleTypeConfiguration(BaseModel):
    Name: Optional[str]
    DocumentDataFieldName: Optional[str]
    DocumentTitleFieldName: Optional[str]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_SalesforceCustomKnowledgeArticleTypeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SalesforceCustomKnowledgeArticleTypeConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            DocumentDataFieldName=json_data.get("DocumentDataFieldName"),
            DocumentTitleFieldName=json_data.get("DocumentTitleFieldName"),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceCustomKnowledgeArticleTypeConfiguration = SalesforceCustomKnowledgeArticleTypeConfiguration


@dataclass
class SalesforceChatterFeedConfiguration(BaseModel):
    DocumentDataFieldName: Optional[str]
    DocumentTitleFieldName: Optional[str]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]
    IncludeFilterTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SalesforceChatterFeedConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SalesforceChatterFeedConfiguration"]:
        if not json_data:
            return None
        return cls(
            DocumentDataFieldName=json_data.get("DocumentDataFieldName"),
            DocumentTitleFieldName=json_data.get("DocumentTitleFieldName"),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
            IncludeFilterTypes=json_data.get("IncludeFilterTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceChatterFeedConfiguration = SalesforceChatterFeedConfiguration


@dataclass
class SalesforceStandardObjectAttachmentConfiguration(BaseModel):
    DocumentTitleFieldName: Optional[str]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_SalesforceStandardObjectAttachmentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SalesforceStandardObjectAttachmentConfiguration"]:
        if not json_data:
            return None
        return cls(
            DocumentTitleFieldName=json_data.get("DocumentTitleFieldName"),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceStandardObjectAttachmentConfiguration = SalesforceStandardObjectAttachmentConfiguration


@dataclass
class OneDriveConfiguration(BaseModel):
    TenantDomain: Optional[str]
    SecretArn: Optional[str]
    OneDriveUsers: Optional["_OneDriveUsers"]
    InclusionPatterns: Optional[Sequence[str]]
    ExclusionPatterns: Optional[Sequence[str]]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]
    DisableLocalGroups: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_OneDriveConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OneDriveConfiguration"]:
        if not json_data:
            return None
        return cls(
            TenantDomain=json_data.get("TenantDomain"),
            SecretArn=json_data.get("SecretArn"),
            OneDriveUsers=OneDriveUsers._deserialize(json_data.get("OneDriveUsers")),
            InclusionPatterns=json_data.get("InclusionPatterns"),
            ExclusionPatterns=json_data.get("ExclusionPatterns"),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
            DisableLocalGroups=json_data.get("DisableLocalGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OneDriveConfiguration = OneDriveConfiguration


@dataclass
class OneDriveUsers(BaseModel):
    OneDriveUserList: Optional[Sequence[str]]
    OneDriveUserS3Path: Optional["_S3Path"]

    @classmethod
    def _deserialize(
        cls: Type["_OneDriveUsers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OneDriveUsers"]:
        if not json_data:
            return None
        return cls(
            OneDriveUserList=json_data.get("OneDriveUserList"),
            OneDriveUserS3Path=S3Path._deserialize(json_data.get("OneDriveUserS3Path")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OneDriveUsers = OneDriveUsers


@dataclass
class ServiceNowConfiguration(BaseModel):
    HostUrl: Optional[str]
    SecretArn: Optional[str]
    ServiceNowBuildVersion: Optional[str]
    AuthenticationType: Optional[str]
    KnowledgeArticleConfiguration: Optional["_ServiceNowKnowledgeArticleConfiguration"]
    ServiceCatalogConfiguration: Optional["_ServiceNowServiceCatalogConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceNowConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceNowConfiguration"]:
        if not json_data:
            return None
        return cls(
            HostUrl=json_data.get("HostUrl"),
            SecretArn=json_data.get("SecretArn"),
            ServiceNowBuildVersion=json_data.get("ServiceNowBuildVersion"),
            AuthenticationType=json_data.get("AuthenticationType"),
            KnowledgeArticleConfiguration=ServiceNowKnowledgeArticleConfiguration._deserialize(json_data.get("KnowledgeArticleConfiguration")),
            ServiceCatalogConfiguration=ServiceNowServiceCatalogConfiguration._deserialize(json_data.get("ServiceCatalogConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceNowConfiguration = ServiceNowConfiguration


@dataclass
class ServiceNowKnowledgeArticleConfiguration(BaseModel):
    CrawlAttachments: Optional[bool]
    IncludeAttachmentFilePatterns: Optional[Sequence[str]]
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]]
    DocumentDataFieldName: Optional[str]
    DocumentTitleFieldName: Optional[str]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]
    FilterQuery: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceNowKnowledgeArticleConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceNowKnowledgeArticleConfiguration"]:
        if not json_data:
            return None
        return cls(
            CrawlAttachments=json_data.get("CrawlAttachments"),
            IncludeAttachmentFilePatterns=json_data.get("IncludeAttachmentFilePatterns"),
            ExcludeAttachmentFilePatterns=json_data.get("ExcludeAttachmentFilePatterns"),
            DocumentDataFieldName=json_data.get("DocumentDataFieldName"),
            DocumentTitleFieldName=json_data.get("DocumentTitleFieldName"),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
            FilterQuery=json_data.get("FilterQuery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceNowKnowledgeArticleConfiguration = ServiceNowKnowledgeArticleConfiguration


@dataclass
class ServiceNowServiceCatalogConfiguration(BaseModel):
    CrawlAttachments: Optional[bool]
    IncludeAttachmentFilePatterns: Optional[Sequence[str]]
    ExcludeAttachmentFilePatterns: Optional[Sequence[str]]
    DocumentDataFieldName: Optional[str]
    DocumentTitleFieldName: Optional[str]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceNowServiceCatalogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceNowServiceCatalogConfiguration"]:
        if not json_data:
            return None
        return cls(
            CrawlAttachments=json_data.get("CrawlAttachments"),
            IncludeAttachmentFilePatterns=json_data.get("IncludeAttachmentFilePatterns"),
            ExcludeAttachmentFilePatterns=json_data.get("ExcludeAttachmentFilePatterns"),
            DocumentDataFieldName=json_data.get("DocumentDataFieldName"),
            DocumentTitleFieldName=json_data.get("DocumentTitleFieldName"),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceNowServiceCatalogConfiguration = ServiceNowServiceCatalogConfiguration


@dataclass
class DatabaseConfiguration(BaseModel):
    DatabaseEngineType: Optional[str]
    ConnectionConfiguration: Optional["_ConnectionConfiguration"]
    VpcConfiguration: Optional["_DataSourceVpcConfiguration"]
    ColumnConfiguration: Optional["_ColumnConfiguration"]
    AclConfiguration: Optional["_AclConfiguration"]
    SqlConfiguration: Optional["_SqlConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseConfiguration"]:
        if not json_data:
            return None
        return cls(
            DatabaseEngineType=json_data.get("DatabaseEngineType"),
            ConnectionConfiguration=ConnectionConfiguration._deserialize(json_data.get("ConnectionConfiguration")),
            VpcConfiguration=DataSourceVpcConfiguration._deserialize(json_data.get("VpcConfiguration")),
            ColumnConfiguration=ColumnConfiguration._deserialize(json_data.get("ColumnConfiguration")),
            AclConfiguration=AclConfiguration._deserialize(json_data.get("AclConfiguration")),
            SqlConfiguration=SqlConfiguration._deserialize(json_data.get("SqlConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseConfiguration = DatabaseConfiguration


@dataclass
class ConnectionConfiguration(BaseModel):
    DatabaseHost: Optional[str]
    DatabasePort: Optional[int]
    DatabaseName: Optional[str]
    TableName: Optional[str]
    SecretArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionConfiguration"]:
        if not json_data:
            return None
        return cls(
            DatabaseHost=json_data.get("DatabaseHost"),
            DatabasePort=json_data.get("DatabasePort"),
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            SecretArn=json_data.get("SecretArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionConfiguration = ConnectionConfiguration


@dataclass
class ColumnConfiguration(BaseModel):
    DocumentIdColumnName: Optional[str]
    DocumentDataColumnName: Optional[str]
    DocumentTitleColumnName: Optional[str]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]
    ChangeDetectingColumns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnConfiguration"]:
        if not json_data:
            return None
        return cls(
            DocumentIdColumnName=json_data.get("DocumentIdColumnName"),
            DocumentDataColumnName=json_data.get("DocumentDataColumnName"),
            DocumentTitleColumnName=json_data.get("DocumentTitleColumnName"),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
            ChangeDetectingColumns=json_data.get("ChangeDetectingColumns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnConfiguration = ColumnConfiguration


@dataclass
class AclConfiguration(BaseModel):
    AllowedGroupsColumnName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AclConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AclConfiguration"]:
        if not json_data:
            return None
        return cls(
            AllowedGroupsColumnName=json_data.get("AllowedGroupsColumnName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AclConfiguration = AclConfiguration


@dataclass
class SqlConfiguration(BaseModel):
    QueryIdentifiersEnclosingOption: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SqlConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqlConfiguration"]:
        if not json_data:
            return None
        return cls(
            QueryIdentifiersEnclosingOption=json_data.get("QueryIdentifiersEnclosingOption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqlConfiguration = SqlConfiguration


@dataclass
class ConfluenceConfiguration(BaseModel):
    ServerUrl: Optional[str]
    SecretArn: Optional[str]
    Version: Optional[str]
    SpaceConfiguration: Optional["_ConfluenceSpaceConfiguration"]
    PageConfiguration: Optional["_ConfluencePageConfiguration"]
    BlogConfiguration: Optional["_ConfluenceBlogConfiguration"]
    AttachmentConfiguration: Optional["_ConfluenceAttachmentConfiguration"]
    VpcConfiguration: Optional["_DataSourceVpcConfiguration"]
    InclusionPatterns: Optional[Sequence[str]]
    ExclusionPatterns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfluenceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfluenceConfiguration"]:
        if not json_data:
            return None
        return cls(
            ServerUrl=json_data.get("ServerUrl"),
            SecretArn=json_data.get("SecretArn"),
            Version=json_data.get("Version"),
            SpaceConfiguration=ConfluenceSpaceConfiguration._deserialize(json_data.get("SpaceConfiguration")),
            PageConfiguration=ConfluencePageConfiguration._deserialize(json_data.get("PageConfiguration")),
            BlogConfiguration=ConfluenceBlogConfiguration._deserialize(json_data.get("BlogConfiguration")),
            AttachmentConfiguration=ConfluenceAttachmentConfiguration._deserialize(json_data.get("AttachmentConfiguration")),
            VpcConfiguration=DataSourceVpcConfiguration._deserialize(json_data.get("VpcConfiguration")),
            InclusionPatterns=json_data.get("InclusionPatterns"),
            ExclusionPatterns=json_data.get("ExclusionPatterns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfluenceConfiguration = ConfluenceConfiguration


@dataclass
class ConfluenceSpaceConfiguration(BaseModel):
    CrawlPersonalSpaces: Optional[bool]
    CrawlArchivedSpaces: Optional[bool]
    IncludeSpaces: Optional[Sequence[str]]
    ExcludeSpaces: Optional[Sequence[str]]
    SpaceFieldMappings: Optional[Sequence["_ConfluenceSpaceToIndexFieldMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfluenceSpaceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfluenceSpaceConfiguration"]:
        if not json_data:
            return None
        return cls(
            CrawlPersonalSpaces=json_data.get("CrawlPersonalSpaces"),
            CrawlArchivedSpaces=json_data.get("CrawlArchivedSpaces"),
            IncludeSpaces=json_data.get("IncludeSpaces"),
            ExcludeSpaces=json_data.get("ExcludeSpaces"),
            SpaceFieldMappings=deserialize_list(json_data.get("SpaceFieldMappings"), ConfluenceSpaceToIndexFieldMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfluenceSpaceConfiguration = ConfluenceSpaceConfiguration


@dataclass
class ConfluenceSpaceToIndexFieldMapping(BaseModel):
    DataSourceFieldName: Optional[str]
    DateFieldFormat: Optional[str]
    IndexFieldName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfluenceSpaceToIndexFieldMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfluenceSpaceToIndexFieldMapping"]:
        if not json_data:
            return None
        return cls(
            DataSourceFieldName=json_data.get("DataSourceFieldName"),
            DateFieldFormat=json_data.get("DateFieldFormat"),
            IndexFieldName=json_data.get("IndexFieldName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfluenceSpaceToIndexFieldMapping = ConfluenceSpaceToIndexFieldMapping


@dataclass
class ConfluencePageConfiguration(BaseModel):
    PageFieldMappings: Optional[Sequence["_ConfluencePageToIndexFieldMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfluencePageConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfluencePageConfiguration"]:
        if not json_data:
            return None
        return cls(
            PageFieldMappings=deserialize_list(json_data.get("PageFieldMappings"), ConfluencePageToIndexFieldMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfluencePageConfiguration = ConfluencePageConfiguration


@dataclass
class ConfluencePageToIndexFieldMapping(BaseModel):
    DataSourceFieldName: Optional[str]
    DateFieldFormat: Optional[str]
    IndexFieldName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfluencePageToIndexFieldMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfluencePageToIndexFieldMapping"]:
        if not json_data:
            return None
        return cls(
            DataSourceFieldName=json_data.get("DataSourceFieldName"),
            DateFieldFormat=json_data.get("DateFieldFormat"),
            IndexFieldName=json_data.get("IndexFieldName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfluencePageToIndexFieldMapping = ConfluencePageToIndexFieldMapping


@dataclass
class ConfluenceBlogConfiguration(BaseModel):
    BlogFieldMappings: Optional[Sequence["_ConfluenceBlogToIndexFieldMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfluenceBlogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfluenceBlogConfiguration"]:
        if not json_data:
            return None
        return cls(
            BlogFieldMappings=deserialize_list(json_data.get("BlogFieldMappings"), ConfluenceBlogToIndexFieldMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfluenceBlogConfiguration = ConfluenceBlogConfiguration


@dataclass
class ConfluenceBlogToIndexFieldMapping(BaseModel):
    DataSourceFieldName: Optional[str]
    DateFieldFormat: Optional[str]
    IndexFieldName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfluenceBlogToIndexFieldMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfluenceBlogToIndexFieldMapping"]:
        if not json_data:
            return None
        return cls(
            DataSourceFieldName=json_data.get("DataSourceFieldName"),
            DateFieldFormat=json_data.get("DateFieldFormat"),
            IndexFieldName=json_data.get("IndexFieldName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfluenceBlogToIndexFieldMapping = ConfluenceBlogToIndexFieldMapping


@dataclass
class ConfluenceAttachmentConfiguration(BaseModel):
    CrawlAttachments: Optional[bool]
    AttachmentFieldMappings: Optional[Sequence["_ConfluenceAttachmentToIndexFieldMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfluenceAttachmentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfluenceAttachmentConfiguration"]:
        if not json_data:
            return None
        return cls(
            CrawlAttachments=json_data.get("CrawlAttachments"),
            AttachmentFieldMappings=deserialize_list(json_data.get("AttachmentFieldMappings"), ConfluenceAttachmentToIndexFieldMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfluenceAttachmentConfiguration = ConfluenceAttachmentConfiguration


@dataclass
class ConfluenceAttachmentToIndexFieldMapping(BaseModel):
    DataSourceFieldName: Optional[str]
    DateFieldFormat: Optional[str]
    IndexFieldName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfluenceAttachmentToIndexFieldMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfluenceAttachmentToIndexFieldMapping"]:
        if not json_data:
            return None
        return cls(
            DataSourceFieldName=json_data.get("DataSourceFieldName"),
            DateFieldFormat=json_data.get("DateFieldFormat"),
            IndexFieldName=json_data.get("IndexFieldName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfluenceAttachmentToIndexFieldMapping = ConfluenceAttachmentToIndexFieldMapping


@dataclass
class GoogleDriveConfiguration(BaseModel):
    SecretArn: Optional[str]
    InclusionPatterns: Optional[Sequence[str]]
    ExclusionPatterns: Optional[Sequence[str]]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]
    ExcludeMimeTypes: Optional[Sequence[str]]
    ExcludeUserAccounts: Optional[Sequence[str]]
    ExcludeSharedDrives: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleDriveConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleDriveConfiguration"]:
        if not json_data:
            return None
        return cls(
            SecretArn=json_data.get("SecretArn"),
            InclusionPatterns=json_data.get("InclusionPatterns"),
            ExclusionPatterns=json_data.get("ExclusionPatterns"),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
            ExcludeMimeTypes=json_data.get("ExcludeMimeTypes"),
            ExcludeUserAccounts=json_data.get("ExcludeUserAccounts"),
            ExcludeSharedDrives=json_data.get("ExcludeSharedDrives"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleDriveConfiguration = GoogleDriveConfiguration


@dataclass
class WebCrawlerConfiguration(BaseModel):
    Urls: Optional["_WebCrawlerUrls"]
    CrawlDepth: Optional[int]
    MaxLinksPerPage: Optional[int]
    MaxContentSizePerPageInMegaBytes: Optional[float]
    MaxUrlsPerMinuteCrawlRate: Optional[int]
    UrlInclusionPatterns: Optional[Sequence[str]]
    UrlExclusionPatterns: Optional[Sequence[str]]
    ProxyConfiguration: Optional["_ProxyConfiguration"]
    AuthenticationConfiguration: Optional["_WebCrawlerAuthenticationConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_WebCrawlerConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebCrawlerConfiguration"]:
        if not json_data:
            return None
        return cls(
            Urls=WebCrawlerUrls._deserialize(json_data.get("Urls")),
            CrawlDepth=json_data.get("CrawlDepth"),
            MaxLinksPerPage=json_data.get("MaxLinksPerPage"),
            MaxContentSizePerPageInMegaBytes=json_data.get("MaxContentSizePerPageInMegaBytes"),
            MaxUrlsPerMinuteCrawlRate=json_data.get("MaxUrlsPerMinuteCrawlRate"),
            UrlInclusionPatterns=json_data.get("UrlInclusionPatterns"),
            UrlExclusionPatterns=json_data.get("UrlExclusionPatterns"),
            ProxyConfiguration=ProxyConfiguration._deserialize(json_data.get("ProxyConfiguration")),
            AuthenticationConfiguration=WebCrawlerAuthenticationConfiguration._deserialize(json_data.get("AuthenticationConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebCrawlerConfiguration = WebCrawlerConfiguration


@dataclass
class WebCrawlerUrls(BaseModel):
    SeedUrlConfiguration: Optional["_WebCrawlerSeedUrlConfiguration"]
    SiteMapsConfiguration: Optional["_WebCrawlerSiteMapsConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_WebCrawlerUrls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebCrawlerUrls"]:
        if not json_data:
            return None
        return cls(
            SeedUrlConfiguration=WebCrawlerSeedUrlConfiguration._deserialize(json_data.get("SeedUrlConfiguration")),
            SiteMapsConfiguration=WebCrawlerSiteMapsConfiguration._deserialize(json_data.get("SiteMapsConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebCrawlerUrls = WebCrawlerUrls


@dataclass
class WebCrawlerSeedUrlConfiguration(BaseModel):
    SeedUrls: Optional[Sequence[str]]
    WebCrawlerMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebCrawlerSeedUrlConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebCrawlerSeedUrlConfiguration"]:
        if not json_data:
            return None
        return cls(
            SeedUrls=json_data.get("SeedUrls"),
            WebCrawlerMode=json_data.get("WebCrawlerMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebCrawlerSeedUrlConfiguration = WebCrawlerSeedUrlConfiguration


@dataclass
class WebCrawlerSiteMapsConfiguration(BaseModel):
    SiteMaps: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_WebCrawlerSiteMapsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebCrawlerSiteMapsConfiguration"]:
        if not json_data:
            return None
        return cls(
            SiteMaps=json_data.get("SiteMaps"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebCrawlerSiteMapsConfiguration = WebCrawlerSiteMapsConfiguration


@dataclass
class ProxyConfiguration(BaseModel):
    Host: Optional[str]
    Port: Optional[int]
    Credentials: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyConfiguration"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Port=json_data.get("Port"),
            Credentials=json_data.get("Credentials"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyConfiguration = ProxyConfiguration


@dataclass
class WebCrawlerAuthenticationConfiguration(BaseModel):
    BasicAuthentication: Optional[Sequence["_WebCrawlerBasicAuthentication"]]

    @classmethod
    def _deserialize(
        cls: Type["_WebCrawlerAuthenticationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebCrawlerAuthenticationConfiguration"]:
        if not json_data:
            return None
        return cls(
            BasicAuthentication=deserialize_list(json_data.get("BasicAuthentication"), WebCrawlerBasicAuthentication),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebCrawlerAuthenticationConfiguration = WebCrawlerAuthenticationConfiguration


@dataclass
class WebCrawlerBasicAuthentication(BaseModel):
    Host: Optional[str]
    Port: Optional[int]
    Credentials: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebCrawlerBasicAuthentication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebCrawlerBasicAuthentication"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Port=json_data.get("Port"),
            Credentials=json_data.get("Credentials"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebCrawlerBasicAuthentication = WebCrawlerBasicAuthentication


@dataclass
class WorkDocsConfiguration(BaseModel):
    OrganizationId: Optional[str]
    CrawlComments: Optional[bool]
    UseChangeLog: Optional[bool]
    InclusionPatterns: Optional[Sequence[str]]
    ExclusionPatterns: Optional[Sequence[str]]
    FieldMappings: Optional[Sequence["_DataSourceToIndexFieldMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkDocsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkDocsConfiguration"]:
        if not json_data:
            return None
        return cls(
            OrganizationId=json_data.get("OrganizationId"),
            CrawlComments=json_data.get("CrawlComments"),
            UseChangeLog=json_data.get("UseChangeLog"),
            InclusionPatterns=json_data.get("InclusionPatterns"),
            ExclusionPatterns=json_data.get("ExclusionPatterns"),
            FieldMappings=deserialize_list(json_data.get("FieldMappings"), DataSourceToIndexFieldMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkDocsConfiguration = WorkDocsConfiguration


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


@dataclass
class CustomDocumentEnrichmentConfiguration(BaseModel):
    InlineConfigurations: Optional[Sequence["_InlineCustomDocumentEnrichmentConfiguration"]]
    PreExtractionHookConfiguration: Optional["_HookConfiguration"]
    PostExtractionHookConfiguration: Optional["_HookConfiguration"]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDocumentEnrichmentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDocumentEnrichmentConfiguration"]:
        if not json_data:
            return None
        return cls(
            InlineConfigurations=deserialize_list(json_data.get("InlineConfigurations"), InlineCustomDocumentEnrichmentConfiguration),
            PreExtractionHookConfiguration=HookConfiguration._deserialize(json_data.get("PreExtractionHookConfiguration")),
            PostExtractionHookConfiguration=HookConfiguration._deserialize(json_data.get("PostExtractionHookConfiguration")),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDocumentEnrichmentConfiguration = CustomDocumentEnrichmentConfiguration


@dataclass
class InlineCustomDocumentEnrichmentConfiguration(BaseModel):
    Condition: Optional["_DocumentAttributeCondition"]
    Target: Optional["_DocumentAttributeTarget"]
    DocumentContentDeletion: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_InlineCustomDocumentEnrichmentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InlineCustomDocumentEnrichmentConfiguration"]:
        if not json_data:
            return None
        return cls(
            Condition=DocumentAttributeCondition._deserialize(json_data.get("Condition")),
            Target=DocumentAttributeTarget._deserialize(json_data.get("Target")),
            DocumentContentDeletion=json_data.get("DocumentContentDeletion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InlineCustomDocumentEnrichmentConfiguration = InlineCustomDocumentEnrichmentConfiguration


@dataclass
class DocumentAttributeCondition(BaseModel):
    ConditionDocumentAttributeKey: Optional[str]
    Operator: Optional[str]
    ConditionOnValue: Optional["_DocumentAttributeValue"]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentAttributeCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentAttributeCondition"]:
        if not json_data:
            return None
        return cls(
            ConditionDocumentAttributeKey=json_data.get("ConditionDocumentAttributeKey"),
            Operator=json_data.get("Operator"),
            ConditionOnValue=DocumentAttributeValue._deserialize(json_data.get("ConditionOnValue")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentAttributeCondition = DocumentAttributeCondition


@dataclass
class DocumentAttributeValue(BaseModel):
    StringValue: Optional[str]
    StringListValue: Optional[Sequence[str]]
    LongValue: Optional[int]
    DateValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentAttributeValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentAttributeValue"]:
        if not json_data:
            return None
        return cls(
            StringValue=json_data.get("StringValue"),
            StringListValue=json_data.get("StringListValue"),
            LongValue=json_data.get("LongValue"),
            DateValue=json_data.get("DateValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentAttributeValue = DocumentAttributeValue


@dataclass
class DocumentAttributeTarget(BaseModel):
    TargetDocumentAttributeKey: Optional[str]
    TargetDocumentAttributeValueDeletion: Optional[bool]
    TargetDocumentAttributeValue: Optional["_DocumentAttributeValue"]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentAttributeTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentAttributeTarget"]:
        if not json_data:
            return None
        return cls(
            TargetDocumentAttributeKey=json_data.get("TargetDocumentAttributeKey"),
            TargetDocumentAttributeValueDeletion=json_data.get("TargetDocumentAttributeValueDeletion"),
            TargetDocumentAttributeValue=DocumentAttributeValue._deserialize(json_data.get("TargetDocumentAttributeValue")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentAttributeTarget = DocumentAttributeTarget


@dataclass
class HookConfiguration(BaseModel):
    InvocationCondition: Optional["_DocumentAttributeCondition"]
    LambdaArn: Optional[str]
    S3Bucket: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HookConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HookConfiguration"]:
        if not json_data:
            return None
        return cls(
            InvocationCondition=DocumentAttributeCondition._deserialize(json_data.get("InvocationCondition")),
            LambdaArn=json_data.get("LambdaArn"),
            S3Bucket=json_data.get("S3Bucket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HookConfiguration = HookConfiguration


