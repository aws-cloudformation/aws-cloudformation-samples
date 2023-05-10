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
    UserPoolTags: Optional[MutableMapping[str, Any]]
    Policies: Optional["_Policies"]
    Schema: Optional[Sequence["_SchemaAttribute"]]
    AdminCreateUserConfig: Optional["_AdminCreateUserConfig"]
    UsernameConfiguration: Optional["_UsernameConfiguration"]
    UserPoolName: Optional[str]
    SmsVerificationMessage: Optional[str]
    UserAttributeUpdateSettings: Optional["_UserAttributeUpdateSettings"]
    EmailConfiguration: Optional["_EmailConfiguration"]
    SmsConfiguration: Optional["_SmsConfiguration"]
    EmailVerificationSubject: Optional[str]
    AccountRecoverySetting: Optional["_AccountRecoverySetting"]
    VerificationMessageTemplate: Optional["_VerificationMessageTemplate"]
    ProviderURL: Optional[str]
    MfaConfiguration: Optional[str]
    DeletionProtection: Optional[str]
    SmsAuthenticationMessage: Optional[str]
    ProviderName: Optional[str]
    UserPoolAddOns: Optional["_UserPoolAddOns"]
    AliasAttributes: Optional[Sequence[str]]
    EnabledMfas: Optional[Sequence[str]]
    LambdaConfig: Optional["_LambdaConfig"]
    Id: Optional[str]
    Arn: Optional[str]
    UsernameAttributes: Optional[Sequence[str]]
    AutoVerifiedAttributes: Optional[Sequence[str]]
    DeviceConfiguration: Optional["_DeviceConfiguration"]
    EmailVerificationMessage: Optional[str]

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
            UserPoolTags=json_data.get("UserPoolTags"),
            Policies=Policies._deserialize(json_data.get("Policies")),
            Schema=deserialize_list(json_data.get("Schema"), SchemaAttribute),
            AdminCreateUserConfig=AdminCreateUserConfig._deserialize(json_data.get("AdminCreateUserConfig")),
            UsernameConfiguration=UsernameConfiguration._deserialize(json_data.get("UsernameConfiguration")),
            UserPoolName=json_data.get("UserPoolName"),
            SmsVerificationMessage=json_data.get("SmsVerificationMessage"),
            UserAttributeUpdateSettings=UserAttributeUpdateSettings._deserialize(json_data.get("UserAttributeUpdateSettings")),
            EmailConfiguration=EmailConfiguration._deserialize(json_data.get("EmailConfiguration")),
            SmsConfiguration=SmsConfiguration._deserialize(json_data.get("SmsConfiguration")),
            EmailVerificationSubject=json_data.get("EmailVerificationSubject"),
            AccountRecoverySetting=AccountRecoverySetting._deserialize(json_data.get("AccountRecoverySetting")),
            VerificationMessageTemplate=VerificationMessageTemplate._deserialize(json_data.get("VerificationMessageTemplate")),
            ProviderURL=json_data.get("ProviderURL"),
            MfaConfiguration=json_data.get("MfaConfiguration"),
            DeletionProtection=json_data.get("DeletionProtection"),
            SmsAuthenticationMessage=json_data.get("SmsAuthenticationMessage"),
            ProviderName=json_data.get("ProviderName"),
            UserPoolAddOns=UserPoolAddOns._deserialize(json_data.get("UserPoolAddOns")),
            AliasAttributes=json_data.get("AliasAttributes"),
            EnabledMfas=json_data.get("EnabledMfas"),
            LambdaConfig=LambdaConfig._deserialize(json_data.get("LambdaConfig")),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            UsernameAttributes=json_data.get("UsernameAttributes"),
            AutoVerifiedAttributes=json_data.get("AutoVerifiedAttributes"),
            DeviceConfiguration=DeviceConfiguration._deserialize(json_data.get("DeviceConfiguration")),
            EmailVerificationMessage=json_data.get("EmailVerificationMessage"),
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
    RequireNumbers: Optional[bool]
    MinimumLength: Optional[int]
    TemporaryPasswordValidityDays: Optional[int]
    RequireUppercase: Optional[bool]
    RequireLowercase: Optional[bool]
    RequireSymbols: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PasswordPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PasswordPolicy"]:
        if not json_data:
            return None
        return cls(
            RequireNumbers=json_data.get("RequireNumbers"),
            MinimumLength=json_data.get("MinimumLength"),
            TemporaryPasswordValidityDays=json_data.get("TemporaryPasswordValidityDays"),
            RequireUppercase=json_data.get("RequireUppercase"),
            RequireLowercase=json_data.get("RequireLowercase"),
            RequireSymbols=json_data.get("RequireSymbols"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PasswordPolicy = PasswordPolicy


@dataclass
class SchemaAttribute(BaseModel):
    DeveloperOnlyAttribute: Optional[bool]
    Mutable: Optional[bool]
    AttributeDataType: Optional[str]
    StringAttributeConstraints: Optional["_StringAttributeConstraints"]
    Required: Optional[bool]
    NumberAttributeConstraints: Optional["_NumberAttributeConstraints"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaAttribute"]:
        if not json_data:
            return None
        return cls(
            DeveloperOnlyAttribute=json_data.get("DeveloperOnlyAttribute"),
            Mutable=json_data.get("Mutable"),
            AttributeDataType=json_data.get("AttributeDataType"),
            StringAttributeConstraints=StringAttributeConstraints._deserialize(json_data.get("StringAttributeConstraints")),
            Required=json_data.get("Required"),
            NumberAttributeConstraints=NumberAttributeConstraints._deserialize(json_data.get("NumberAttributeConstraints")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaAttribute = SchemaAttribute


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
class NumberAttributeConstraints(BaseModel):
    MinValue: Optional[str]
    MaxValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NumberAttributeConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberAttributeConstraints"]:
        if not json_data:
            return None
        return cls(
            MinValue=json_data.get("MinValue"),
            MaxValue=json_data.get("MaxValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberAttributeConstraints = NumberAttributeConstraints


@dataclass
class AdminCreateUserConfig(BaseModel):
    InviteMessageTemplate: Optional["_InviteMessageTemplate"]
    UnusedAccountValidityDays: Optional[int]
    AllowAdminCreateUserOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AdminCreateUserConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminCreateUserConfig"]:
        if not json_data:
            return None
        return cls(
            InviteMessageTemplate=InviteMessageTemplate._deserialize(json_data.get("InviteMessageTemplate")),
            UnusedAccountValidityDays=json_data.get("UnusedAccountValidityDays"),
            AllowAdminCreateUserOnly=json_data.get("AllowAdminCreateUserOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminCreateUserConfig = AdminCreateUserConfig


@dataclass
class InviteMessageTemplate(BaseModel):
    EmailSubject: Optional[str]
    EmailMessage: Optional[str]
    SMSMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InviteMessageTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InviteMessageTemplate"]:
        if not json_data:
            return None
        return cls(
            EmailSubject=json_data.get("EmailSubject"),
            EmailMessage=json_data.get("EmailMessage"),
            SMSMessage=json_data.get("SMSMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InviteMessageTemplate = InviteMessageTemplate


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
class EmailConfiguration(BaseModel):
    ReplyToEmailAddress: Optional[str]
    ConfigurationSet: Optional[str]
    EmailSendingAccount: Optional[str]
    From: Optional[str]
    SourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailConfiguration"]:
        if not json_data:
            return None
        return cls(
            ReplyToEmailAddress=json_data.get("ReplyToEmailAddress"),
            ConfigurationSet=json_data.get("ConfigurationSet"),
            EmailSendingAccount=json_data.get("EmailSendingAccount"),
            From=json_data.get("From"),
            SourceArn=json_data.get("SourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailConfiguration = EmailConfiguration


@dataclass
class SmsConfiguration(BaseModel):
    SnsCallerArn: Optional[str]
    SnsRegion: Optional[str]
    ExternalId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmsConfiguration"]:
        if not json_data:
            return None
        return cls(
            SnsCallerArn=json_data.get("SnsCallerArn"),
            SnsRegion=json_data.get("SnsRegion"),
            ExternalId=json_data.get("ExternalId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmsConfiguration = SmsConfiguration


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
    Priority: Optional[int]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecoveryOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecoveryOption"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecoveryOption = RecoveryOption


@dataclass
class VerificationMessageTemplate(BaseModel):
    EmailMessageByLink: Optional[str]
    EmailMessage: Optional[str]
    SmsMessage: Optional[str]
    EmailSubject: Optional[str]
    DefaultEmailOption: Optional[str]
    EmailSubjectByLink: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VerificationMessageTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VerificationMessageTemplate"]:
        if not json_data:
            return None
        return cls(
            EmailMessageByLink=json_data.get("EmailMessageByLink"),
            EmailMessage=json_data.get("EmailMessage"),
            SmsMessage=json_data.get("SmsMessage"),
            EmailSubject=json_data.get("EmailSubject"),
            DefaultEmailOption=json_data.get("DefaultEmailOption"),
            EmailSubjectByLink=json_data.get("EmailSubjectByLink"),
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


@dataclass
class LambdaConfig(BaseModel):
    CreateAuthChallenge: Optional[str]
    PreSignUp: Optional[str]
    KMSKeyID: Optional[str]
    UserMigration: Optional[str]
    PostAuthentication: Optional[str]
    VerifyAuthChallengeResponse: Optional[str]
    PreAuthentication: Optional[str]
    DefineAuthChallenge: Optional[str]
    PreTokenGeneration: Optional[str]
    CustomSMSSender: Optional["_CustomSMSSender"]
    PostConfirmation: Optional[str]
    CustomMessage: Optional[str]
    CustomEmailSender: Optional["_CustomEmailSender"]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConfig"]:
        if not json_data:
            return None
        return cls(
            CreateAuthChallenge=json_data.get("CreateAuthChallenge"),
            PreSignUp=json_data.get("PreSignUp"),
            KMSKeyID=json_data.get("KMSKeyID"),
            UserMigration=json_data.get("UserMigration"),
            PostAuthentication=json_data.get("PostAuthentication"),
            VerifyAuthChallengeResponse=json_data.get("VerifyAuthChallengeResponse"),
            PreAuthentication=json_data.get("PreAuthentication"),
            DefineAuthChallenge=json_data.get("DefineAuthChallenge"),
            PreTokenGeneration=json_data.get("PreTokenGeneration"),
            CustomSMSSender=CustomSMSSender._deserialize(json_data.get("CustomSMSSender")),
            PostConfirmation=json_data.get("PostConfirmation"),
            CustomMessage=json_data.get("CustomMessage"),
            CustomEmailSender=CustomEmailSender._deserialize(json_data.get("CustomEmailSender")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConfig = LambdaConfig


@dataclass
class CustomSMSSender(BaseModel):
    LambdaArn: Optional[str]
    LambdaVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSMSSender"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSMSSender"]:
        if not json_data:
            return None
        return cls(
            LambdaArn=json_data.get("LambdaArn"),
            LambdaVersion=json_data.get("LambdaVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSMSSender = CustomSMSSender


@dataclass
class CustomEmailSender(BaseModel):
    LambdaArn: Optional[str]
    LambdaVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomEmailSender"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomEmailSender"]:
        if not json_data:
            return None
        return cls(
            LambdaArn=json_data.get("LambdaArn"),
            LambdaVersion=json_data.get("LambdaVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomEmailSender = CustomEmailSender


@dataclass
class DeviceConfiguration(BaseModel):
    DeviceOnlyRememberedOnUserPrompt: Optional[bool]
    ChallengeRequiredOnNewDevice: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceConfiguration"]:
        if not json_data:
            return None
        return cls(
            DeviceOnlyRememberedOnUserPrompt=json_data.get("DeviceOnlyRememberedOnUserPrompt"),
            ChallengeRequiredOnNewDevice=json_data.get("ChallengeRequiredOnNewDevice"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceConfiguration = DeviceConfiguration


