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
class AwsLexBotalias(BaseModel):
    BotAliasId: Optional[str]
    BotId: Optional[str]
    Arn: Optional[str]
    BotAliasStatus: Optional[str]
    BotAliasLocaleSettings: Optional[AbstractSet["_BotAliasLocaleSettingsItem"]]
    BotAliasName: Optional[str]
    BotVersion: Optional[str]
    ConversationLogSettings: Optional["_ConversationLogSettings"]
    Description: Optional[str]
    SentimentAnalysisSettings: Optional["_SentimentAnalysisSettings"]
    BotAliasTags: Optional[AbstractSet["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLexBotalias"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLexBotalias"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            BotAliasId=json_data.get("BotAliasId"),
            BotId=json_data.get("BotId"),
            Arn=json_data.get("Arn"),
            BotAliasStatus=json_data.get("BotAliasStatus"),
            BotAliasLocaleSettings=set_or_none(json_data.get("BotAliasLocaleSettings")),
            BotAliasName=json_data.get("BotAliasName"),
            BotVersion=json_data.get("BotVersion"),
            ConversationLogSettings=ConversationLogSettings._deserialize(json_data.get("ConversationLogSettings")),
            Description=json_data.get("Description"),
            SentimentAnalysisSettings=SentimentAnalysisSettings._deserialize(json_data.get("SentimentAnalysisSettings")),
            BotAliasTags=set_or_none(json_data.get("BotAliasTags")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLexBotalias = AwsLexBotalias


@dataclass
class BotAliasLocaleSettingsItem(BaseModel):
    LocaleId: Optional[str]
    BotAliasLocaleSetting: Optional["_BotAliasLocaleSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_BotAliasLocaleSettingsItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BotAliasLocaleSettingsItem"]:
        if not json_data:
            return None
        return cls(
            LocaleId=json_data.get("LocaleId"),
            BotAliasLocaleSetting=BotAliasLocaleSettings._deserialize(json_data.get("BotAliasLocaleSetting")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BotAliasLocaleSettingsItem = BotAliasLocaleSettingsItem


@dataclass
class BotAliasLocaleSettings(BaseModel):
    CodeHookSpecification: Optional["_CodeHookSpecification"]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BotAliasLocaleSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BotAliasLocaleSettings"]:
        if not json_data:
            return None
        return cls(
            CodeHookSpecification=CodeHookSpecification._deserialize(json_data.get("CodeHookSpecification")),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BotAliasLocaleSettings = BotAliasLocaleSettings


@dataclass
class CodeHookSpecification(BaseModel):
    LambdaCodeHook: Optional["_LambdaCodeHook"]

    @classmethod
    def _deserialize(
        cls: Type["_CodeHookSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeHookSpecification"]:
        if not json_data:
            return None
        return cls(
            LambdaCodeHook=LambdaCodeHook._deserialize(json_data.get("LambdaCodeHook")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeHookSpecification = CodeHookSpecification


@dataclass
class LambdaCodeHook(BaseModel):
    CodeHookInterfaceVersion: Optional[str]
    LambdaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaCodeHook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaCodeHook"]:
        if not json_data:
            return None
        return cls(
            CodeHookInterfaceVersion=json_data.get("CodeHookInterfaceVersion"),
            LambdaArn=json_data.get("LambdaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaCodeHook = LambdaCodeHook


@dataclass
class ConversationLogSettings(BaseModel):
    AudioLogSettings: Optional[AbstractSet["_AudioLogSetting"]]
    TextLogSettings: Optional[AbstractSet["_TextLogSetting"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConversationLogSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConversationLogSettings"]:
        if not json_data:
            return None
        return cls(
            AudioLogSettings=set_or_none(json_data.get("AudioLogSettings")),
            TextLogSettings=set_or_none(json_data.get("TextLogSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConversationLogSettings = ConversationLogSettings


@dataclass
class AudioLogSetting(BaseModel):
    Destination: Optional["_AudioLogDestination"]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AudioLogSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioLogSetting"]:
        if not json_data:
            return None
        return cls(
            Destination=AudioLogDestination._deserialize(json_data.get("Destination")),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioLogSetting = AudioLogSetting


@dataclass
class AudioLogDestination(BaseModel):
    S3Bucket: Optional["_S3BucketLogDestination"]

    @classmethod
    def _deserialize(
        cls: Type["_AudioLogDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioLogDestination"]:
        if not json_data:
            return None
        return cls(
            S3Bucket=S3BucketLogDestination._deserialize(json_data.get("S3Bucket")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioLogDestination = AudioLogDestination


@dataclass
class S3BucketLogDestination(BaseModel):
    S3BucketArn: Optional[str]
    LogPrefix: Optional[str]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3BucketLogDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3BucketLogDestination"]:
        if not json_data:
            return None
        return cls(
            S3BucketArn=json_data.get("S3BucketArn"),
            LogPrefix=json_data.get("LogPrefix"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3BucketLogDestination = S3BucketLogDestination


@dataclass
class TextLogSetting(BaseModel):
    Destination: Optional["_TextLogDestination"]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TextLogSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextLogSetting"]:
        if not json_data:
            return None
        return cls(
            Destination=TextLogDestination._deserialize(json_data.get("Destination")),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextLogSetting = TextLogSetting


@dataclass
class TextLogDestination(BaseModel):
    CloudWatch: Optional["_CloudWatchLogGroupLogDestination"]

    @classmethod
    def _deserialize(
        cls: Type["_TextLogDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextLogDestination"]:
        if not json_data:
            return None
        return cls(
            CloudWatch=CloudWatchLogGroupLogDestination._deserialize(json_data.get("CloudWatch")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextLogDestination = TextLogDestination


@dataclass
class CloudWatchLogGroupLogDestination(BaseModel):
    CloudWatchLogGroupArn: Optional[str]
    LogPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLogGroupLogDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLogGroupLogDestination"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogGroupArn=json_data.get("CloudWatchLogGroupArn"),
            LogPrefix=json_data.get("LogPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLogGroupLogDestination = CloudWatchLogGroupLogDestination


@dataclass
class SentimentAnalysisSettings(BaseModel):
    DetectSentiment: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SentimentAnalysisSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SentimentAnalysisSettings"]:
        if not json_data:
            return None
        return cls(
            DetectSentiment=json_data.get("DetectSentiment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SentimentAnalysisSettings = SentimentAnalysisSettings


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


