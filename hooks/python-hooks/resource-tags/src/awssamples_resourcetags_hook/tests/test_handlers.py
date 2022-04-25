"""Unit tests for the handlers.py module."""

import re
from typing import (
    Any,
    Dict,
)
from unittest.mock import (
    MagicMock,
    patch,
)

import botocore.session  # type: ignore
from botocore.stub import Stubber  # type: ignore
from cloudformation_cli_python_lib import (  # type: ignore
    BaseHookHandlerRequest,
    HandlerErrorCode,
    HookContext,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
)

from .. import handlers
from ..models import TypeConfigurationModel
from . import mock_data as mocks

# Determine the base module path name from TYPE_NAME; used with patch().
BASE_PATH = re.sub("::", "_", handlers.TYPE_NAME.lower())


def _get_session_client_mock() -> SessionProxy:
    """Return a mock session client."""
    # Mock session
    session = MagicMock(
        name="session",
    )
    # Mock session client
    session.client = MagicMock(
        name="client",
        return_value=MagicMock(
            name="client",
        ),
    )
    return SessionProxy(
        session,
    )


def _get_base_hook_handler_request_mock(
    target_name: str,
    target_type: str,
    target_model: Dict[str, Any],
    hook_type_name: str = handlers.TYPE_NAME,
) -> BaseHookHandlerRequest:
    """Return a mock BaseHookHandlerRequest for pre-provision."""
    return BaseHookHandlerRequest(
        clientRequestToken=MagicMock(),
        hookContext=HookContext(
            awsAccountId=MagicMock(),
            stackId="arn:aws:cloudformation:us-east-1:123456789012:stack/test/abcd0123-abcd-0123-abcd-0123456789ab",  # noqa: E501
            hookTypeName=hook_type_name,
            hookTypeVersion="00000001",
            invocationPoint=HookInvocationPoint.CREATE_PRE_PROVISION,
            targetName=target_name,
            targetType=target_type,
            targetLogicalId="test",
            targetModel=target_model,
        ),
    )


# Tests
def test_exception() -> None:
    """Inject a TypeError to test the handler's exception block."""
    with patch(
        f"{BASE_PATH}.handlers._validate_resource_properties",
        side_effect=TypeError(
            "Mock exception.",
        ),
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=None,
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.TAGS_IS_ARRAY,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys="Name,",
                ValidationStrategy="resource",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert return_value.message == "Mock exception."
        assert return_value.status == OperationStatus.FAILED
        assert return_value.errorCode == HandlerErrorCode.InternalFailure


def test_tags_object_to_list() -> None:
    """Test the conversion of a tagging structure from object to list."""
    tags_object = {"Name": "test"}
    return_value = handlers._tags_object_to_list(
        tags_object=tags_object,
    )
    assert return_value == [{"Key": "Name", "Value": "test"}]


def test_get_type_config_tag_keys() -> None:
    """Test tag keys retrieval from hook input."""
    type_config_tag_keys = " ,  Name, AppName,  EnvironmentName,"
    return_value = handlers._get_type_config_tag_keys(
        type_config_tag_keys=type_config_tag_keys,
    )
    assert return_value == [
        "Name",
        "AppName",
        "EnvironmentName",
    ]


def test_get_type_config_tag_keys_removes_allowed_tag_values() -> None:
    """Test removal of allowed tag values when getting tag keys."""
    type_config_tag_keys = "Name=test_allowed_value1, Env=dev|qa|prod,"
    return_value = handlers._get_type_config_tag_keys(
        type_config_tag_keys=type_config_tag_keys,
    )
    assert return_value == [
        "Name",
        "Env",
    ]


def test_get_type_config_tags_allowed_values() -> None:
    """Test to retrieve allowed values, if any, from the hook configuration."""
    type_config_tag_keys = "Name = value1, Team, Env = |dev  | qa|prod|,"
    return_value = handlers._get_type_config_tags_allowed_values(
        type_config_tag_keys=type_config_tag_keys,
    )
    assert return_value == [
        {"allowed_values": ["value1"], "name": "Name"},
        {"allowed_values": ["dev", "qa", "prod"], "name": "Env"},
    ]


def test_missing_type_config_tag_keys_property() -> None:
    """Failure: TagKeys hook configuration property missing."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.WITH_NO_PROPERTIES,
        ),
        callback_context=None,
        type_configuration=None,
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "No TagKeys hook configuration property."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.InvalidTypeConfiguration


def test_missing_type_config_tag_keys() -> None:
    """Failure: TagKeys hook configuration missing."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.WITH_NO_PROPERTIES,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Hook configuration for TagKeys missing."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.InvalidTypeConfiguration


def test_invalid_type_config_tag_keys() -> None:
    """Failure: TagKeys hook configuration not valid."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.WITH_NO_PROPERTIES,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys=",",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Invalid hook configuration: no keys for TagKeys."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.InvalidTypeConfiguration


def test_no_resource_properties() -> None:
    """Failure: no resource properties specified."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.WITH_NO_PROPERTIES,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "No resource properties specified."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_no_resource_tags() -> None:
    """Failure: no tag-related resource properties specified."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.WITH_NO_TAGS,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Resource property missing: Tags."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_resource_not_supported() -> None:
    """Failure: not supported resource type."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name=mocks.TARGET_NAME_NOT_SUPPORTED,
            target_type=mocks.TARGET_TYPE_NOT_SUPPORTED,
            target_model=MagicMock(),
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Resource or hook not supporting tags."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.InvalidRequest


def test_tagkeys_and_allowed_values_more_than_one_TAGKEYS_DELIM() -> None:
    """Failure: 1+ argument separator between tag keys and allowed values."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name=test,,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message == "Can't parse: adjacent ',' delimiters found."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode is HandlerErrorCode.InvalidTypeConfiguration


def test_tagkeys_and_allowed_values_more_than_one_TAGKEY_ARGS_DELIM() -> None:
    """Failure: 1+ argument separator between tag keys and allowed values."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name==test",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message == "Can't parse: adjacent '=' delimiters found."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode is HandlerErrorCode.InvalidTypeConfiguration


def test_tagkeys_and_allowed_values_more_than_one_TAGKEY_ALLOWED_VALUES_DELIM() -> None:  # noqa: E501
    """Failure: 1+ argument separator between tag keys and allowed values."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name=test||",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message == "Can't parse: adjacent '|' delimiters found."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode is HandlerErrorCode.InvalidTypeConfiguration


def test_tagkeys_and_allowed_values_delimiter_parsing() -> None:
    """Failure: tag keys and allowed values delimiter parsing in the config."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,=",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Can't parse: ',' around '='."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode is HandlerErrorCode.InvalidTypeConfiguration


def test_tags_is_array() -> None:
    """Success: tags as an array."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::S3::Bucket: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_tags_is_object() -> None:
    """Success: tags as an object."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::SSM::Parameter",
            target_type="AWS::SSM::Parameter",
            target_model=mocks.TAGS_IS_OBJECT,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::SSM::Parameter: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_tags_is_array_missing_required_key() -> None:
    """Failure: tags as array, and missing required tag key."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY_MISSING_REQUIRED_KEY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Required tag key(s) missing: ['Name']."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_object_missing_required_key() -> None:
    """Failure: tags as object, and missing required tag key."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::SSM::Parameter",
            target_type="AWS::SSM::Parameter",
            target_model=mocks.TAGS_IS_OBJECT_MISSING_REQUIRED_KEY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Required tag key(s) missing: ['Name']."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_array_missing_required_keys() -> None:
    """Failure: tags as array, and missing required tag keys."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY_MISSING_REQUIRED_KEYS,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Required tag key(s) missing: ['AppName', 'Name']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_object_missing_required_keys() -> None:
    """Failure: tags as object, and missing required tag keys."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::SSM::Parameter",
            target_type="AWS::SSM::Parameter",
            target_model=mocks.TAGS_IS_OBJECT_MISSING_REQUIRED_KEYS,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Required tag key(s) missing: ['AppName', 'Name']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_array_missing_value() -> None:
    """Failure: tags as array, and missing tag value."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY_MISSING_VALUE,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Empty value(s) for tag(s): ['AppName']."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_object_missing_value() -> None:
    """Failure: tags as object, and missing tag value."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::SSM::Parameter",
            target_type="AWS::SSM::Parameter",
            target_model=mocks.TAGS_IS_OBJECT_MISSING_VALUE,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Empty value(s) for tag(s): ['AppName']."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_array_missing_values() -> None:
    """Failure: tags as array, and missing tag values."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY_MISSING_VALUES,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Empty value(s) for tag(s): ['AppName', 'Name']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_object_missing_values() -> None:
    """Failure: tags as object, and missing tag values."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::SSM::Parameter",
            target_type="AWS::SSM::Parameter",
            target_model=mocks.TAGS_IS_OBJECT_MISSING_VALUES,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Empty value(s) for tag(s): ['AppName', 'Name']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_array_properties() -> None:
    """Success: required tag properties keys and non-empty values."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::Lex::Bot",
            target_type="AWS::Lex::Bot",
            target_model=mocks.TAGS_IS_ARRAY_PROPERTIES,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::Lex::Bot: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_tags_is_array_properties_missing_required_key() -> None:
    """Failure: missing required key on resource type with 1+ tag property."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::Lex::Bot",
            target_type="AWS::Lex::Bot",
            target_model=mocks.TAGS_IS_ARRAY_PROPERTIES_MISSING_REQUIRED_KEY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Required tag key(s) missing: ['Name']."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_array_properties_missing_values() -> None:
    """Failure: empty tag values on resource type with 1+ tag property."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::Lex::Bot",
            target_type="AWS::Lex::Bot",
            target_model=mocks.TAGS_IS_ARRAY_PROPERTIES_MISSING_VALUE,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Empty value(s) for tag(s): ['Name']."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_array_properties_missing_tag_properties() -> None:
    """Failure: missing tag properties on resource with 1+ tag property."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::Lex::Bot",
            target_type="AWS::Lex::Bot",
            target_model=mocks.TAGS_IS_ARRAY_PROPERTIES_MISSING_TAG_PROPERTIES,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Resource property missing: BotTags."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_array_properties_missing_tag_property() -> None:
    """Failure: missing tag property on resource with 1+ tag property."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::Lex::Bot",
            target_type="AWS::Lex::Bot",
            target_model=mocks.TAGS_IS_ARRAY_PROPERTIES_MISSING_TAG_PROPERTY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Resource property missing: BotTags."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tagspecifications() -> None:
    """Success: use case test with TagSpecifications."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::EC2::LaunchTemplate",
            target_type="AWS::EC2::LaunchTemplate",
            target_model=mocks.TAGSPECIFICATIONS,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::EC2::LaunchTemplate: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_tagspecifications_missing_required_key() -> None:
    """Failure: missing required tag keys for TagSpecifications."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::EC2::LaunchTemplate",
            target_type="AWS::EC2::LaunchTemplate",
            target_model=mocks.TAGSPECIFICATIONS_MISSING_REQUIRED_KEY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Required tag key(s) missing: ['Name']."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tagspecifications_missing_value() -> None:
    """Failure: missing tag value for TagSpecifications."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::EC2::LaunchTemplate",
            target_type="AWS::EC2::LaunchTemplate",
            target_model=mocks.TAGSPECIFICATIONS_MISSING_VALUE,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Empty value(s) for tag(s): ['AppName']."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tagspecifications_missing_tags_property() -> None:
    """Failure: missing Tags property for TagSpecifications."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::EC2::LaunchTemplate",
            target_type="AWS::EC2::LaunchTemplate",
            target_model=mocks.TAGSPECIFICATIONS_MISSING_TAGS_PROPERTY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "TagSpecifications: missing Tags property."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tagspecifications_missing_tagspecification() -> None:
    """Failure: missing TagSpecification for TagSpecifications."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::EC2::LaunchTemplate",
            target_type="AWS::EC2::LaunchTemplate",
            target_model=mocks.TAGSPECIFICATIONS_MISSING_TAGSPECIFICATION,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "TagSpecifications does not contain items."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_stack_required_key() -> None:
    """Success: required tag key specified for the stack."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[{"Key": "Name", "Value": "ExampleName"}],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=_get_session_client_mock(),
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys="Name,",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert (
            return_value.message
            == f"{handlers.TYPE_NAME} succeeded: stack: test."
        )
        assert return_value.status == OperationStatus.SUCCESS
        assert return_value.errorCode is None


def test_stack_missing_required_key() -> None:
    """Failure: required tag key not specified for the stack."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[{"Key": "MissingNameKey", "Value": "ExampleName"}],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=_get_session_client_mock(),
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys="Name,",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert (
            return_value.message
            == "Required tag key(s) missing: ['Name'] on stack."
        )
        assert return_value.status == OperationStatus.FAILED
        assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_stack_missing_required_keys() -> None:
    """Failure: required tag keys not specified for the stack."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[{"Key": "MissingNameKey", "Value": "ExampleName"}],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=_get_session_client_mock(),
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys="Name,AppName,",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert (
            return_value.message
            == "Required tag key(s) missing: ['AppName', 'Name'] on stack."
        )
        assert return_value.status == OperationStatus.FAILED
        assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_unknown_tag_validation_strategy() -> None:
    """Failure: unknown validation strategy specified."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=MagicMock(),
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,AppName,",
            ValidationStrategy="unknown_validation_strategy",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert return_value.message == "Unknown tag validation strategy."
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.InvalidTypeConfiguration


def test_empty_tag_validation_strategy_configuration() -> None:
    """Success: using default resource validation strategy."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name,AppName,",
            ValidationStrategy="",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::S3::Bucket: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_unable_to_create_cloudformation_client() -> None:
    """Failure test for client creation."""
    with patch(
        f"{BASE_PATH}.handlers._get_session_client",
        return_value=None,
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=_get_session_client_mock(),
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys="Name,",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert (
            return_value.message
            == "Unable to create a client for AWS CloudFormation."
        )
        assert return_value.status == OperationStatus.FAILED
        assert return_value.errorCode == HandlerErrorCode.InternalFailure


def test_get_stack_tags_returns_expected_tags() -> None:
    """Success: retrieving expected tags from the stack."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_info",
        return_value={
            "Stacks": [
                {
                    "Tags": [
                        {"Key": "Name", "Value": "string"},
                    ],
                },
            ],
        },
    ):
        return_value = handlers._get_stack_tags(
            session=_get_session_client_mock(),
            stack_id=MagicMock(),
        )
        assert isinstance(return_value, list)
        assert return_value == [{"Key": "Name", "Value": "string"}]


def test_get_session_client_returns_none() -> None:
    """Failure: non-SessionProxy object specified for session."""
    return_value = handlers._get_session_client(
        session=None,
        service_name="cloudformation",
    )
    assert return_value is None


def test_get_stack_info() -> None:
    """Test: expected output of _get_stack_info()."""
    stack_name = mocks.DESCRIBE_STACKS_API_MOCK[0]
    response = mocks.DESCRIBE_STACKS_API_MOCK[1]

    client = botocore.session.get_session().create_client(
        "cloudformation",
    )
    stubber = Stubber(client)

    expected_params = {"StackName": stack_name}
    stubber.add_response(
        method="describe_stacks",
        service_response=response,
        expected_params=expected_params,
    )
    stubber.add_response(
        method="describe_stacks",
        service_response=response,
        expected_params=expected_params,
    )
    stubber.activate()

    service_response = client.describe_stacks(
        StackName=stack_name,
    )

    return_value = handlers._get_stack_info(
        client=client,
        stack_id=stack_name,
    )
    assert service_response == response
    assert return_value == response


def test_expected_resource_tag_value_is_present() -> None:
    """Success: expect presence of an allowed tag value."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.ALLOWED_TAG_VALUES_TESTS,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Env = dev|qa|prod",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::S3::Bucket: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_expected_resource_tag_value_is_not_present() -> None:
    """Failure: expect presence of an allowed tag value."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.ALLOWED_TAG_VALUES_TESTS,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Env = test|qa|prod,Team",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message == "Tag(s) with invalid value: ['dev for Env']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_expected_resource_tag_values_are_not_present() -> None:
    """Failure: expect presence of allowed tag values."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.ALLOWED_TAG_VALUES_TESTS,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Env = test|qa|prod,Team=Team2",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Tag(s) with invalid value: ['dev for Env', 'Team1 for Team']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_expected_stack_tag_value_is_present() -> None:
    """Success: expect presence of an allowed tag value."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[{"Key": "Env", "Value": "dev"}],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=None,
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys="Env = dev|qa|prod",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert (
            return_value.message
            == f"{handlers.TYPE_NAME} succeeded: stack: test."
        )
        assert return_value.status == OperationStatus.SUCCESS
        assert return_value.errorCode is None


def test_expected_stack_tag_value_is_not_present() -> None:
    """Failure: expect presence of an allowed tag value."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[{"Key": "Env", "Value": "dev"}],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=None,
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys="Env = test|qa|prod",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert (
            return_value.message
            == "Tag(s) with invalid value: ['dev for Env']."
        )
        assert return_value.status == OperationStatus.FAILED
        assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_expected_stack_tag_values_are_not_present() -> None:
    """Failure: expect presence of an allowed tag value."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[
            {"Key": "Env", "Value": "dev"},
            {"Key": "Team", "Value": "Team1"},
        ],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=None,
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys="Env = test|qa|prod,Team=Team2",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert (
            return_value.message
            == "Tag(s) with invalid value: ['dev for Env', 'Team1 for Team']."
        )
        assert return_value.status == OperationStatus.FAILED
        assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_escape_TAGKEYS_DELIM_stack_level_tags() -> None:
    """Success: TAGKEYS_DELIM as a character for key/value."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[{"Key": "My,env", "Value": "dev,env"}],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=None,
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys=r"My\,env = dev\,env|qa|prod",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert (
            return_value.message
            == f"{handlers.TYPE_NAME} succeeded: stack: test."
        )
        assert return_value.status == OperationStatus.SUCCESS
        assert return_value.errorCode is None


def test_escape_TAGKEY_ARGS_DELIM_stack_level_tags() -> None:
    """Success: TAGKEY_ARGS_DELIM as a character for a key/value."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[{"Key": "My=env", "Value": "dev=env"}],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=None,
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys=r"My\=env = dev\=env|qa|prod",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert (
            return_value.message
            == f"{handlers.TYPE_NAME} succeeded: stack: test."
        )
        assert return_value.status == OperationStatus.SUCCESS
        assert return_value.errorCode is None


def test_escape_TAGKEY_ALLOWED_VALUES_DELIM_stack_level_tags() -> None:
    """Success: TAGKEY_ALLOWED_VALUES_DELIM as a character for a key/value."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[{"Key": "My|env", "Value": "dev|env"}],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=None,
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys=r"My\|env = dev\|env|qa|prod",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert (
            return_value.message
            == f"{handlers.TYPE_NAME} succeeded: stack: test."
        )
        assert return_value.status == OperationStatus.SUCCESS
        assert return_value.errorCode is None


def test_escape_characters_resource_level_tags() -> None:
    """Success: escape characters for delimiters for a key/value."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::EC2::LaunchTemplate",
            target_type="AWS::EC2::LaunchTemplate",
            target_model=mocks.RESOURCE_TAGS_ADD_CHAR_ESCAPE_TESTS,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys=r"K\,1=V\,1 ,K\=2=V\=2, K\|3=V\|3",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::EC2::LaunchTemplate: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_regexp_input_for_resource_target_success() -> None:
    """Success: regexp match for a given resource-level tag value."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name = regexp:^[a-zA-Z]+$",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::S3::Bucket: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_regexp_input_for_stack_target_success() -> None:
    """Success: regexp match for a given stack-level tag value."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[{"Key": "Name", "Value": "ExampleName"}],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=None,
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys="Name = regexp:^[a-zA-Z]+$",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
        assert (
            return_value.message
            == f"{handlers.TYPE_NAME} succeeded: stack: test."
        )
        assert return_value.status == OperationStatus.SUCCESS
        assert return_value.errorCode is None


def test_regexp_input_for_resource_target_failure() -> None:
    """Failure: regexp match for a given resource-level tag value."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name = regexp:^[a-z]+$",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Tag(s) with invalid value: ['ExampleName for Name']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_regexp_input_for_stack_target_failure() -> None:
    """Failure: regexp match for a given stack-level tag value."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[{"Key": "Name", "Value": "ExampleName"}],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=None,
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                TagKeys="Name = regexp:^[a-z]+$",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
    assert (
        return_value.message
        == "Tag(s) with invalid value: ['ExampleName for Name']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_regexp_input_error() -> None:
    """Failure: regexp provided as an input for the hook contains an error."""
    with patch(
        f"{BASE_PATH}.handlers._get_stack_tags",
        return_value=[{"Key": "Name", "Value": "ExampleName"}],
    ):
        return_value = handlers.pre_create_pre_update_handler(  # type: ignore
            session=None,
            request=_get_base_hook_handler_request_mock(
                target_name="AWS::S3::Bucket",
                target_type="AWS::S3::Bucket",
                target_model=mocks.STACK_TAGS_TEST_CASES,
            ),
            callback_context=None,
            type_configuration=TypeConfigurationModel(
                # Remove a square bracket to inject an error.
                TagKeys="Name = regexp:^[a-z+$",
                ValidationStrategy="stack",
            ),
        )
        assert isinstance(
            return_value,
            ProgressEvent,
        )
    assert (
        return_value.message
        == "Regular expression: ^[a-z+$: unterminated character set at position 1"  # noqa: E501
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.InvalidTypeConfiguration


def test_tags_is_array_autoscaling_group_propagate_at_launch_true() -> None:
    """Success: PropagateAtLaunch set to true for an Auto Scaling group."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::AutoScaling::AutoScalingGroup",
            target_type="AWS::AutoScaling::AutoScalingGroup",
            target_model=mocks.TAGS_IS_ARRAY_AUTOSCALING_GROUP_PROPAGATE_AT_LAUNCH_TRUE,  # noqa: E501
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name, AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::AutoScaling::AutoScalingGroup: test."  # noqa: E501
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_tags_is_array_autoscaling_group_propagate_at_launch_false() -> None:
    """Failure: PropagateAtLaunch set to false for an Auto Scaling group."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::AutoScaling::AutoScalingGroup",
            target_type="AWS::AutoScaling::AutoScalingGroup",
            target_model=mocks.TAGS_IS_ARRAY_AUTOSCALING_GROUP_PROPAGATE_AT_LAUNCH_FALSE,  # noqa: E501
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name, AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Propagation not set up for tag(s): ['Name', 'AppName']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tags_is_array_autoscaling_group_propagate_at_launch_missing() -> None:
    """Failure: PropagateAtLaunch missing for an Auto Scaling group."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::AutoScaling::AutoScalingGroup",
            target_type="AWS::AutoScaling::AutoScalingGroup",
            target_model=mocks.TAGS_IS_ARRAY_AUTOSCALING_GROUP_PROPAGATE_AT_LAUNCH_MISSING,  # noqa: E501
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name, AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Propagation not set up for tag(s): ['Name', 'AppName']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tag_propagation_boolean_true() -> None:
    """Success: tag propagation property set to True for a resource type."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::Batch::JobDefinition",
            target_type="AWS::Batch::JobDefinition",
            target_model=mocks.TAG_PROPAGATION_BOOLEAN_TRUE,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name, AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::Batch::JobDefinition: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_tag_propagation_boolean_false() -> None:
    """Failure: tag propagation property set to False for a resource type."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::Batch::JobDefinition",
            target_type="AWS::Batch::JobDefinition",
            target_model=mocks.TAG_PROPAGATION_BOOLEAN_FALSE,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name, AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Propagation not set up for property: ['PropagateTags']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tag_propagation_string_true() -> None:
    """Success: tag propagation property set to 'true' for a resource type."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::Batch::JobDefinition",
            target_type="AWS::Batch::JobDefinition",
            target_model=mocks.TAG_PROPAGATION_STRING_TRUE,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name, AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::Batch::JobDefinition: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_tag_propagation_string_false() -> None:
    """Failure: tag propagation property set to 'false' for a resource type."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::Batch::JobDefinition",
            target_type="AWS::Batch::JobDefinition",
            target_model=mocks.TAG_PROPAGATION_STRING_FALSE,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name, AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Propagation not set up for property: ['PropagateTags']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tag_propagation_missing() -> None:
    """Failure: tag propagation property missing for a resource type."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::Batch::JobDefinition",
            target_type="AWS::Batch::JobDefinition",
            target_model=mocks.TAG_PROPAGATION_MISSING,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name, AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Propagation not set up for property: ['PropagateTags']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_tag_propagation_valid_string() -> None:
    """Success: tag propagation property set to a valid string value."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::ECS::Service",
            target_type="AWS::ECS::Service",
            target_model=mocks.TAG_PROPAGATION_VALID_STRING,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name, AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::ECS::Service: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None


def test_tag_propagation_invalid_string() -> None:
    """Failure: tag propagation property set to an invalid string value."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::ECS::Service",
            target_type="AWS::ECS::Service",
            target_model=mocks.TAG_PROPAGATION_INVALID_STRING,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys="Name, AppName,",
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == "Propagation not set up for property: ['PropagateTags']."
    )
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.NonCompliant


def test_multiple_regexps__and_values_input_for_resource_target_success() -> None:  # noqa: E501
    """Success: matching regexps and values for allowed tag values."""
    return_value = handlers.pre_create_pre_update_handler(  # type: ignore
        session=None,
        request=_get_base_hook_handler_request_mock(
            target_name="AWS::S3::Bucket",
            target_type="AWS::S3::Bucket",
            target_model=mocks.TAGS_IS_ARRAY,
        ),
        callback_context=None,
        type_configuration=TypeConfigurationModel(
            TagKeys=r"Name = | Example | regexp:^[a-zA-Z]{3\,15}$ | regexp:^[a-z]+$ |",  # noqa: E501
            ValidationStrategy="resource",
        ),
    )
    assert isinstance(
        return_value,
        ProgressEvent,
    )
    assert (
        return_value.message
        == f"{handlers.TYPE_NAME} succeeded: AWS::S3::Bucket: test."
    )
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None
