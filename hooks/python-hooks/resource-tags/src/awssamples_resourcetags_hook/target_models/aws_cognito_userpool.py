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
class AwsCognitoUserpool(BaseModel):
    UserPoolName: Optional[str]
    Policies: Optional["_Policies"]
    AccountRecoverySetting: Optional["_AccountRecoverySetting"]
    AdminCreateUserConfig: Optional["_AdminCreateUserConfig"]
    AliasAttributes: Optional[Sequence[str]]
    UsernameAttributes: Optional[Sequence[str]]
    AutoVerifiedAttributes: Optional[Sequence[str]]
    DeviceConfiguration: Optional["_DeviceConfiguration"]
    EmailConfiguration: Optional["_EmailConfiguration"]
    EmailVerificationMessage: Optional[str]
    EmailVerificationSubject: Optional[str]
    DeletionProtection: Optional[str]
    LambdaConfig: Optional["_LambdaConfig"]
    MfaConfiguration: Optional[str]
    EnabledMfas: Optional[Sequence[str]]
    SmsAuthenticationMessage: Optional[str]
    SmsConfiguration: Optional["_SmsConfiguration"]
    SmsVerificationMessage: Optional[str]
    Schema: Optional[Sequence["_SchemaAttribute"]]
    UsernameConfiguration: Optional["_UsernameConfiguration"]
    UserAttributeUpdateSettings: Optional["_UserAttributeUpdateSettings"]
    UserPoolTags: Optional[MutableMapping[str, str]]
    VerificationMessageTemplate: Optional["_VerificationMessageTemplate"]
    UserPoolAddOns: Optional["_UserPoolAddOns"]
    ProviderName: Optional[str]
    ProviderURL: Optional[str]
    Arn: Optional[str]
    UserPoolId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCognitoUserpool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCognitoUserpool"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            UserPoolName=json_data.get("UserPoolName"),
            Policies=Policies._deserialize(json_data.get("Policies")),
            AccountRecoverySetting=AccountRecoverySetting._deserialize(json_data.get("AccountRecoverySetting")),
            AdminCreateUserConfig=AdminCreateUserConfig._deserialize(json_data.get("AdminCreateUserConfig")),
            AliasAttributes=json_data.get("AliasAttributes"),
            UsernameAttributes=json_data.get("UsernameAttributes"),
            AutoVerifiedAttributes=json_data.get("AutoVerifiedAttributes"),
            DeviceConfiguration=DeviceConfiguration._deserialize(json_data.get("DeviceConfiguration")),
            EmailConfiguration=EmailConfiguration._deserialize(json_data.get("EmailConfiguration")),
            EmailVerificationMessage=json_data.get("EmailVerificationMessage"),
            EmailVerificationSubject=json_data.get("EmailVerificationSubject"),
            DeletionProtection=json_data.get("DeletionProtection"),
            LambdaConfig=LambdaConfig._deserialize(json_data.get("LambdaConfig")),
            MfaConfiguration=json_data.get("MfaConfiguration"),
            EnabledMfas=json_data.get("EnabledMfas"),
            SmsAuthenticationMessage=json_data.get("SmsAuthenticationMessage"),
            SmsConfiguration=SmsConfiguration._deserialize(json_data.get("SmsConfiguration")),
            SmsVerificationMessage=json_data.get("SmsVerificationMessage"),
            Schema=deserialize_list(json_data.get("Schema"), SchemaAttribute),
            UsernameConfiguration=UsernameConfiguration._deserialize(json_data.get("UsernameConfiguration")),
            UserAttributeUpdateSettings=UserAttributeUpdateSettings._deserialize(json_data.get("UserAttributeUpdateSettings")),
            UserPoolTags=json_data.get("UserPoolTags"),
            VerificationMessageTemplate=VerificationMessageTemplate._deserialize(json_data.get("VerificationMessageTemplate")),
            UserPoolAddOns=UserPoolAddOns._deserialize(json_data.get("UserPoolAddOns")),
            ProviderName=json_data.get("ProviderName"),
            ProviderURL=json_data.get("ProviderURL"),
            Arn=json_data.get("Arn"),
            UserPoolId=json_data.get("UserPoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCognitoUserpool = AwsCognitoUserpool


@dataclass
class Policies(BaseModel):
    PasswordPolicy: Optional["_PasswordPolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_Policies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Policies"]:
        if not json_data:
            return None
        return cls(
            PasswordPolicy=PasswordPolicy._deserialize(json_data.get("PasswordPolicy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Policies = Policies


@dataclass
class PasswordPolicy(BaseModel):
    MinimumLength: Optional[int]
    RequireLowercase: Optional[bool]
    RequireNumbers: Optional[bool]
    RequireSymbols: Optional[bool]
    RequireUppercase: Optional[bool]
    TemporaryPasswordValidityDays: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordPolicy"]:
        if not json_data:
            return None
        return cls(
            MinimumLength=json_data.get("MinimumLength"),
            RequireLowercase=json_data.get("RequireLowercase"),
            RequireNumbers=json_data.get("RequireNumbers"),
            RequireSymbols=json_data.get("RequireSymbols"),
            RequireUppercase=json_data.get("RequireUppercase"),
            TemporaryPasswordValidityDays=json_data.get("TemporaryPasswordValidityDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PasswordPolicy = PasswordPolicy


@dataclass
class AccountRecoverySetting(BaseModel):
    RecoveryMechanisms: Optional[Sequence["_RecoveryOption"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccountRecoverySetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountRecoverySetting"]:
        if not json_data:
            return None
        return cls(
            RecoveryMechanisms=deserialize_list(json_data.get("RecoveryMechanisms"), RecoveryOption),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountRecoverySetting = AccountRecoverySetting


@dataclass
class RecoveryOption(BaseModel):
    Name: Optional[str]
    Priority: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RecoveryOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecoveryOption"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecoveryOption = RecoveryOption


@dataclass
class AdminCreateUserConfig(BaseModel):
    AllowAdminCreateUserOnly: Optional[bool]
    InviteMessageTemplate: Optional["_InviteMessageTemplate"]
    UnusedAccountValidityDays: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AdminCreateUserConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminCreateUserConfig"]:
        if not json_data:
            return None
        return cls(
            AllowAdminCreateUserOnly=json_data.get("AllowAdminCreateUserOnly"),
            InviteMessageTemplate=InviteMessageTemplate._deserialize(json_data.get("InviteMessageTemplate")),
            UnusedAccountValidityDays=json_data.get("UnusedAccountValidityDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminCreateUserConfig = AdminCreateUserConfig


@dataclass
class InviteMessageTemplate(BaseModel):
    EmailMessage: Optional[str]
    EmailSubject: Optional[str]
    SMSMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InviteMessageTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InviteMessageTemplate"]:
        if not json_data:
            return None
        return cls(
            EmailMessage=json_data.get("EmailMessage"),
            EmailSubject=json_data.get("EmailSubject"),
            SMSMessage=json_data.get("SMSMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InviteMessageTemplate = InviteMessageTemplate


@dataclass
class DeviceConfiguration(BaseModel):
    ChallengeRequiredOnNewDevice: Optional[bool]
    DeviceOnlyRememberedOnUserPrompt: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceConfiguration"]:
        if not json_data:
            return None
        return cls(
            ChallengeRequiredOnNewDevice=json_data.get("ChallengeRequiredOnNewDevice"),
            DeviceOnlyRememberedOnUserPrompt=json_data.get("DeviceOnlyRememberedOnUserPrompt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceConfiguration = DeviceConfiguration


@dataclass
class EmailConfiguration(BaseModel):
    ReplyToEmailAddress: Optional[str]
    SourceArn: Optional[str]
    From: Optional[str]
    ConfigurationSet: Optional[str]
    EmailSendingAccount: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailConfiguration"]:
        if not json_data:
            return None
        return cls(
            ReplyToEmailAddress=json_data.get("ReplyToEmailAddress"),
            SourceArn=json_data.get("SourceArn"),
            From=json_data.get("From"),
            ConfigurationSet=json_data.get("ConfigurationSet"),
            EmailSendingAccount=json_data.get("EmailSendingAccount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailConfiguration = EmailConfiguration


@dataclass
class LambdaConfig(BaseModel):
    CreateAuthChallenge: Optional[str]
    CustomMessage: Optional[str]
    DefineAuthChallenge: Optional[str]
    PostAuthentication: Optional[str]
    PostConfirmation: Optional[str]
    PreAuthentication: Optional[str]
    PreSignUp: Optional[str]
    VerifyAuthChallengeResponse: Optional[str]
    UserMigration: Optional[str]
    PreTokenGeneration: Optional[str]
    CustomEmailSender: Optional["_CustomEmailSender"]
    CustomSMSSender: Optional["_CustomSMSSender"]
    KMSKeyID: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConfig"]:
        if not json_data:
            return None
        return cls(
            CreateAuthChallenge=json_data.get("CreateAuthChallenge"),
            CustomMessage=json_data.get("CustomMessage"),
            DefineAuthChallenge=json_data.get("DefineAuthChallenge"),
            PostAuthentication=json_data.get("PostAuthentication"),
            PostConfirmation=json_data.get("PostConfirmation"),
            PreAuthentication=json_data.get("PreAuthentication"),
            PreSignUp=json_data.get("PreSignUp"),
            VerifyAuthChallengeResponse=json_data.get("VerifyAuthChallengeResponse"),
            UserMigration=json_data.get("UserMigration"),
            PreTokenGeneration=json_data.get("PreTokenGeneration"),
            CustomEmailSender=CustomEmailSender._deserialize(json_data.get("CustomEmailSender")),
            CustomSMSSender=CustomSMSSender._deserialize(json_data.get("CustomSMSSender")),
            KMSKeyID=json_data.get("KMSKeyID"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConfig = LambdaConfig


@dataclass
class CustomEmailSender(BaseModel):
    LambdaVersion: Optional[str]
    LambdaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomEmailSender"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomEmailSender"]:
        if not json_data:
            return None
        return cls(
            LambdaVersion=json_data.get("LambdaVersion"),
            LambdaArn=json_data.get("LambdaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomEmailSender = CustomEmailSender


@dataclass
class CustomSMSSender(BaseModel):
    LambdaVersion: Optional[str]
    LambdaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSMSSender"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSMSSender"]:
        if not json_data:
            return None
        return cls(
            LambdaVersion=json_data.get("LambdaVersion"),
            LambdaArn=json_data.get("LambdaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSMSSender = CustomSMSSender


@dataclass
class SmsConfiguration(BaseModel):
    ExternalId: Optional[str]
    SnsCallerArn: Optional[str]
    SnsRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmsConfiguration"]:
        if not json_data:
            return None
        return cls(
            ExternalId=json_data.get("ExternalId"),
            SnsCallerArn=json_data.get("SnsCallerArn"),
            SnsRegion=json_data.get("SnsRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmsConfiguration = SmsConfiguration


@dataclass
class SchemaAttribute(BaseModel):
    AttributeDataType: Optional[str]
    DeveloperOnlyAttribute: Optional[bool]
    Mutable: Optional[bool]
    Name: Optional[str]
    NumberAttributeConstraints: Optional["_NumberAttributeConstraints"]
    StringAttributeConstraints: Optional["_StringAttributeConstraints"]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaAttribute"]:
        if not json_data:
            return None
        return cls(
            AttributeDataType=json_data.get("AttributeDataType"),
            DeveloperOnlyAttribute=json_data.get("DeveloperOnlyAttribute"),
            Mutable=json_data.get("Mutable"),
            Name=json_data.get("Name"),
            NumberAttributeConstraints=NumberAttributeConstraints._deserialize(json_data.get("NumberAttributeConstraints")),
            StringAttributeConstraints=StringAttributeConstraints._deserialize(json_data.get("StringAttributeConstraints")),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaAttribute = SchemaAttribute


@dataclass
class NumberAttributeConstraints(BaseModel):
    MaxValue: Optional[str]
    MinValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NumberAttributeConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberAttributeConstraints"]:
        if not json_data:
            return None
        return cls(
            MaxValue=json_data.get("MaxValue"),
            MinValue=json_data.get("MinValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberAttributeConstraints = NumberAttributeConstraints


@dataclass
class StringAttributeConstraints(BaseModel):
    MaxLength: Optional[str]
    MinLength: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringAttributeConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringAttributeConstraints"]:
        if not json_data:
            return None
        return cls(
            MaxLength=json_data.get("MaxLength"),
            MinLength=json_data.get("MinLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringAttributeConstraints = StringAttributeConstraints


@dataclass
class UsernameConfiguration(BaseModel):
    CaseSensitive: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_UsernameConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsernameConfiguration"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsernameConfiguration = UsernameConfiguration


@dataclass
class UserAttributeUpdateSettings(BaseModel):
    AttributesRequireVerificationBeforeUpdate: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_UserAttributeUpdateSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserAttributeUpdateSettings"]:
        if not json_data:
            return None
        return cls(
            AttributesRequireVerificationBeforeUpdate=json_data.get("AttributesRequireVerificationBeforeUpdate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserAttributeUpdateSettings = UserAttributeUpdateSettings


@dataclass
class VerificationMessageTemplate(BaseModel):
    DefaultEmailOption: Optional[str]
    EmailMessage: Optional[str]
    EmailMessageByLink: Optional[str]
    EmailSubject: Optional[str]
    EmailSubjectByLink: Optional[str]
    SmsMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VerificationMessageTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VerificationMessageTemplate"]:
        if not json_data:
            return None
        return cls(
            DefaultEmailOption=json_data.get("DefaultEmailOption"),
            EmailMessage=json_data.get("EmailMessage"),
            EmailMessageByLink=json_data.get("EmailMessageByLink"),
            EmailSubject=json_data.get("EmailSubject"),
            EmailSubjectByLink=json_data.get("EmailSubjectByLink"),
            SmsMessage=json_data.get("SmsMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VerificationMessageTemplate = VerificationMessageTemplate


@dataclass
class UserPoolAddOns(BaseModel):
    AdvancedSecurityMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserPoolAddOns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserPoolAddOns"]:
        if not json_data:
            return None
        return cls(
            AdvancedSecurityMode=json_data.get("AdvancedSecurityMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserPoolAddOns = UserPoolAddOns


