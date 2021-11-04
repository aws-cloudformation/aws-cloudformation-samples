import re
from functools import (
    wraps,
)
from unittest.mock import (
    MagicMock,
    patch,
)
from typing import (
    Any,
    Callable,
)

import botocore
from cloudformation_cli_python_lib import (
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
)

from .. models import (
    ResourceHandlerRequest,
    ResourceModel,
    Tag,
)
from .. import handlers


# Determine the base module path name from the resource type name;
# using this value for patching during tests
BASE_MODULE_PATH_NAME = re.sub('::', '_', handlers.TYPE_NAME.lower())


# Test helpers
def handler_assertions(
        handler_name: str,
        test_case: str,
        error_name: str = None,
) -> Callable:
    """Configurable decorator for testing assertions for a given handler"""

    def decorator_function(
            decorated_function: Callable,
    ) -> Callable:
        """Return a wrapper for the decorated function"""

        @wraps(decorated_function)
        def decorated_function_wrapper(
                *args: list,
                **kwargs: dict,
        ) -> Any:
            """Run the input function and perform test assertions"""
            decorated_function(
                *args,
                **kwargs,
            )
            if test_case in [
                    'operation_status_in_progress',
                    'operation_status_success',
            ]:
                return_value = _mock_call_handler(
                    handler_name=handler_name,
                )
                if handler_name in [
                        'create',
                        'update',
                        'delete',
                ]:
                    _operation_status_in_progress_assertions(
                        return_value=return_value,
                    )
                else:
                    _operation_status_success_assertions(
                        return_value=return_value,
                        handler_name=handler_name,
                    )
            elif test_case == \
                    'operation_status_failed_botocore_client_error':
                # Injecting a mock botocore client error as an example
                return_value = \
                    _get_session_client_inject_error_and_call_handler(
                        handler_name=handler_name,
                        error_name=error_name,
                    )
                _operation_status_failed_botocore_client_error_assertions(
                    return_value=return_value,
                    error_name=error_name,
                )
            elif test_case == 'operation_status_failed_generic_error':
                return_value = \
                    _get_session_client_inject_error_and_call_handler(
                        handler_name=handler_name,
                    )
                _operation_status_failed_generic_error_assertions(
                    return_value=return_value,
                )
        return decorated_function_wrapper
    return decorator_function


def _get_session_client_inject_error_and_call_handler(
        handler_name: str,
        error_name: str = None,
) -> ProgressEvent:
    """Inject a given botocore client error and call a given handler"""
    if error_name:
        side_effect = botocore.exceptions.ClientError(
            error_response={
                'Error': {
                    'Code': error_name,
                    'Message': MagicMock(),
                },
            },
            operation_name=MagicMock(),
        )
    else:
        side_effect = KeyError(
            MagicMock(),
        )

    with patch(
            f'{BASE_MODULE_PATH_NAME}.handlers._get_session_client',
            side_effect=side_effect,
    ):
        return _mock_call_handler(
            handler_name=handler_name,
        )


def _mock_call_handler(
        handler_name: str,
) -> ProgressEvent:
    """Helper method to call a given handler for testing"""
    session = _mock_get_session_proxy()
    request = MagicMock(
        name='request',
    )
    callback_context = MagicMock(
        name='callback_context',
    )
    if handler_name == 'create':
        with patch(
                f'{BASE_MODULE_PATH_NAME}.handlers._import_key_pair_helper',
                return_value=MagicMock(),
        ):
            return handlers.create_handler(
                session,
                request,
                callback_context,
            )
    elif handler_name == 'update':
        with patch(
                f'{BASE_MODULE_PATH_NAME}.handlers._update_tags_helper',
                return_value=MagicMock(),
        ):
            return handlers.update_handler(
                session,
                request,
                callback_context,
            )
    elif handler_name == 'delete':
        return handlers.delete_handler(
            session,
            request,
            callback_context,
        )
    elif handler_name == 'read':
        return handlers.read_handler(
            session,
            request,
            callback_context,
        )
    elif handler_name == 'list':
        return handlers.list_handler(
            session,
            request,
            callback_context,
        )
    else:
        raise ValueError(
            'Specify a valid handler name: create, update, delete, read, list',
        )


def _operation_status_in_progress_assertions(
        return_value: ProgressEvent,
) -> None:
    """Assertions for create, update, and delete operations in progress"""
    assert isinstance(return_value, ProgressEvent)
    assert return_value.status == OperationStatus.IN_PROGRESS
    assert return_value.errorCode is None
    assert return_value.callbackContext == {
        'status': OperationStatus.IN_PROGRESS,
    }
    assert return_value.callbackDelaySeconds >= 0
    assert return_value.resourceModel is not None
    assert return_value.resourceModels is None


def _operation_status_success_assertions(
        return_value: ProgressEvent,
        handler_name: str,
) -> None:
    """Assertions for read, and delete operation status success"""
    assert isinstance(return_value, ProgressEvent)
    assert return_value.status == OperationStatus.SUCCESS
    assert return_value.errorCode is None
    assert return_value.callbackContext is None

    if handler_name == 'read':
        assert return_value.resourceModel is not None
        assert return_value.resourceModels is None
    elif handler_name == 'list':
        assert return_value.resourceModel is None
        assert return_value.resourceModels is not None


def _operation_status_failed_botocore_client_error_assertions(
        return_value: ProgressEvent,
        error_name: str,
) -> None:
    """Assertions for botocore.exceptions.ClientError test cases"""
    expected_errors_map = {
        'InvalidKeyPair.NotFound': HandlerErrorCode.NotFound,
        'InvalidKeyPair.Duplicate': HandlerErrorCode.AlreadyExists,
        'InvalidKey.Format': HandlerErrorCode.InvalidRequest,
        'InvalidKeyPair.Format': HandlerErrorCode.InvalidRequest,
        'InvalidParameter': HandlerErrorCode.InvalidRequest,
        'InvalidParameterCombination': HandlerErrorCode.InvalidRequest,
        'InvalidParameterValue': HandlerErrorCode.InvalidRequest,
        'InvalidTagKey.Malformed': HandlerErrorCode.InvalidRequest,
        'MissingAction': HandlerErrorCode.InvalidRequest,
        'MissingParameter': HandlerErrorCode.InvalidRequest,
        'UnknownParameter': HandlerErrorCode.InvalidRequest,
        'ValidationError': HandlerErrorCode.InvalidRequest,
        'KeyPairLimitExceeded': HandlerErrorCode.ServiceLimitExceeded,
        'TagLimitExceeded': HandlerErrorCode.ServiceLimitExceeded,
        'ConcurrentTagAccess': HandlerErrorCode.Throttling,
        'RequestLimitExceeded': HandlerErrorCode.Throttling,
    }
    assert isinstance(return_value, ProgressEvent)
    assert return_value.status == OperationStatus.FAILED
    if error_name == 'example_error':
        assert return_value.errorCode == \
            HandlerErrorCode.GeneralServiceException
    else:
        assert return_value.errorCode == expected_errors_map[error_name]
    assert return_value.message is not None
    assert return_value.callbackContext is None
    assert return_value.callbackDelaySeconds == 0
    assert return_value.resourceModel is None
    assert return_value.resourceModels is None


def _operation_status_failed_generic_error_assertions(
        return_value: ProgressEvent,
) -> None:
    """Assertions for Exception cases"""
    assert isinstance(return_value, ProgressEvent)
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.InternalFailure
    assert return_value.message is not None
    assert return_value.callbackContext is None
    assert return_value.callbackDelaySeconds == 0
    assert return_value.resourceModel is None
    assert return_value.resourceModels is None


def _mock_get_session_proxy(
) -> SessionProxy:
    """Create and return a mock SessionProxy with a mock session client"""
    # Create a mock session
    session = MagicMock(
        name='session',
    )
    # Create a mock session client
    session.client = MagicMock(
        name='client',
        return_value=MagicMock(
            name='client',
        ),
    )
    # Return a SessionProxy with the mock session and client
    return SessionProxy(
        session,
    )


def _get_mock_model_tags_list(
) -> list:
    """Create and return a list of mock model tags"""
    return [
        Tag(
            Key='mock-key-1',
            Value='mock-value-1',
        ),
        Tag(
            Key='mock-key-2',
            Value='mock-value-2',
        ),
    ]


def _get_mock_tags_dict(
        sample_name: str = 'sample1',
) -> dict:
    """Create and return a dictionary of mock tags"""
    if sample_name == 'sample1':
        return {
            'mock-key-a': 'mock-value-a',
            'mock-key-b': 'mock-value-b',
        }
    elif sample_name == 'sample2':
        return {
            'mock-key-c': 'mock-value-c',
            'mock-key-d': 'mock-value-d',
        }
    else:
        return {
            'mock-key': 'mock-value',
        }


def _get_mock_model(
) -> ResourceModel:
    """Create and return a mock resource model for the example resource type"""
    return ResourceModel(
        KeyPairId='mock-key-pair-id',
        KeyFingerprint='mock-key-fingerprint',
        KeyName='mock-key-name',
        KeyType='mock-key-type',
        Tags=_get_mock_model_tags_list(),
        PublicKeyMaterial='mock-public-key-material',
    )


def _get_mock_request(
) -> ResourceHandlerRequest:
    """Create and return a mock resource handler request"""
    return ResourceHandlerRequest(
        clientRequestToken=MagicMock(),
        desiredResourceState=MagicMock(),
        previousResourceState=MagicMock(),
        desiredResourceTags=_get_mock_tags_dict(sample_name='sample1',),
        previousResourceTags=_get_mock_tags_dict(sample_name='sample2',),
        systemTags=MagicMock(),
        previousSystemTags=MagicMock(),
        awsAccountId=MagicMock(),
        logicalResourceIdentifier='mock-logical-resource-identifier',
        typeConfiguration=MagicMock(),
        nextToken=MagicMock(),
        region=MagicMock(),
        awsPartition=MagicMock(),
        stackId=MagicMock(),
    )


def _get_mock_key_pair_dict(
) -> dict:
    """Create and return a dict of mock key pairs"""
    return {
        'KeyPairs': [
            {
                'KeyPairId': 'mock-key-pair-1',
                'KeyFingerprint': 'mock-key-fingerprint-1',
                'KeyName': 'mock-key-pair-name-1',
                'KeyType': 'mock-key-pair-type-1',
                'Tags': [
                    {
                        'Key': 'mock-key-1',
                        'Value': 'mock-value-1'
                    },
                ],
            },
            {
                'KeyPairId': 'mock-key-pair-2',
                'KeyFingerprint': 'mock-key-fingerprint-2',
                'KeyName': 'mock-key-pair-name-2',
                'KeyType': 'mock-key-pair-type-2',
                'Tags': [
                    {
                        'Key': 'mock-key-2',
                        'Value': 'mock-value-2'
                    },
                ],
            },
        ],
    }


# Tests
@handler_assertions(
    handler_name='create',
    test_case='operation_status_in_progress',
)
def test_create_handler_returns_operation_status_in_progress(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='update',
    test_case='operation_status_in_progress',
)
def test_update_handler_returns_operation_status_in_progress(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='delete',
    test_case='operation_status_in_progress',
)
def test_delete_handler_returns_operation_status_in_progress(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='read',
    test_case='operation_status_success',
)
def test_read_handler_returns_operation_status_success(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='list',
    test_case='operation_status_success',
)
def test_list_handler_returns_operation_status_success(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='create',
    test_case='operation_status_failed_botocore_client_error',
    error_name='ValidationError',
)
def test_create_handler_returns_operation_status_failed_botocore_client_error(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='create',
    test_case='operation_status_failed_generic_error',
)
def test_create_handler_returns_operation_status_failed_generic_error(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='update',
    test_case='operation_status_failed_botocore_client_error',
    error_name='ValidationError',
)
def test_update_handler_returns_operation_status_failed_botocore_client_error(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='update',
    test_case='operation_status_failed_generic_error',
)
def test_update_handler_returns_operation_status_failed_generic_error(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='delete',
    test_case='operation_status_failed_botocore_client_error',
    error_name='ValidationError',
)
def test_delete_handler_returns_operation_status_failed_botocore_client_error(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='delete',
    test_case='operation_status_failed_generic_error',
)
def test_delete_handler_returns_operation_status_failed_generic_error(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='read',
    test_case='operation_status_failed_botocore_client_error',
    error_name='ValidationError',
)
def test_read_handler_returns_operation_status_failed_botocore_client_error(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='read',
    test_case='operation_status_failed_generic_error',
)
def test_read_handler_returns_operation_status_failed_generic_error(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='list',
    test_case='operation_status_failed_botocore_client_error',
    error_name='ValidationError',
)
def test_list_handler_returns_operation_status_failed_botocore_client_error(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='list',
    test_case='operation_status_failed_generic_error',
)
def test_list_handler_returns_operation_status_failed_generic_error(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='read',
    test_case='operation_status_failed_botocore_client_error',
    error_name='InvalidKeyPair.NotFound',
)
def test_list_handler_returns_operation_status_failed_not_found(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='create',
    test_case='operation_status_failed_botocore_client_error',
    error_name='InvalidKeyPair.Duplicate',
)
def test_list_handler_returns_operation_status_failed_duplicate(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='create',
    test_case='operation_status_failed_botocore_client_error',
    error_name='KeyPairLimitExceeded',
)
def test_list_handler_returns_operation_status_failed_key_pair_limit_exceeded(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='create',
    test_case='operation_status_failed_botocore_client_error',
    error_name='RequestLimitExceeded',
)
def test_list_handler_returns_operation_status_failed_request_limit_exceeded(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


@handler_assertions(
    handler_name='create',
    test_case='operation_status_failed_botocore_client_error',
    error_name='example_error',
)
def test_list_handler_returns_operation_status_failed_general_service(
) -> None:
    session = _mock_get_session_proxy()
    assert isinstance(
        session,
        SessionProxy,
    )


def test__progress_event_success_no_parameters_provided(
) -> None:
    try:
        handlers._progress_event_success()
    except Exception as e:
        assert e.__class__.__name__ == 'ValueError'


def test__progress_event_success_delete_and_list_handler_parameters_specified(
) -> None:
    try:
        handlers._progress_event_success(
            is_delete_handler=True,
            is_list_handler=True,
        )
    except Exception as e:
        assert e.__class__.__name__ == 'ValueError'


def test__is_callback(
) -> None:
    callback_context = {
        'status': OperationStatus.IN_PROGRESS,
    }
    return_value = handlers._is_callback(
        callback_context,
    )
    assert return_value is True


def test__callback_helper_read_handler_success(
) -> None:
    with patch(
            f'{BASE_MODULE_PATH_NAME}.handlers.read_handler',
            return_value=ProgressEvent(
                status=OperationStatus.SUCCESS,
            ),
    ):
        return_value = handlers._callback_helper(
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )
        assert return_value.status == OperationStatus.SUCCESS


def test__callback_helper_read_handler_not_found_error_and_is_delete_handler(
) -> None:
    with patch(
            f'{BASE_MODULE_PATH_NAME}.handlers.read_handler',
            return_value=ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.NotFound,
            ),
    ):
        return_value = handlers._callback_helper(
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
            is_delete_handler=True,
        )
        assert return_value.status == OperationStatus.SUCCESS


def test__callback_helper_read_handler_not_found_error(
) -> None:
    with patch(
            f'{BASE_MODULE_PATH_NAME}.handlers.read_handler',
            return_value=ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.NotFound,
            ),
    ):
        return_value = handlers._callback_helper(
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )
        assert return_value.status == OperationStatus.FAILED


def test__callback_helper_progress_event_callback(
) -> None:
    with patch(
            f'{BASE_MODULE_PATH_NAME}.handlers.read_handler',
            return_value=ProgressEvent(
                status=OperationStatus.IN_PROGRESS,
            ),
    ):
        return_value = handlers._callback_helper(
            MagicMock(),
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )
        assert return_value.status == OperationStatus.IN_PROGRESS


def test__get_session_client_session_is_instance_of_session_proxy(
) -> None:
    return_value = handlers._get_session_client(
        _mock_get_session_proxy(),
        MagicMock(),
    )
    assert return_value is not None
    assert isinstance(
        return_value,
        MagicMock,
    )


def test__get_session_client_session_not_instance_of_session_proxy(
) -> None:
    assert handlers._get_session_client(
        MagicMock(),
        MagicMock(),
    ) is None


def test__get_tags_from_previous_resource_tags(
) -> None:
    tags_dict = _get_mock_tags_dict()
    return_value = handlers._get_tags_from_previous_resource_tags(
        tags_dict,
    )
    expected_value = [
        {'Key': 'mock-key-a', 'Value': 'mock-value-a'},
        {'Key': 'mock-key-b', 'Value': 'mock-value-b'},
    ]
    assert return_value == expected_value


def test__get_tag_lists_diff(
) -> None:
    list_a = [1, 2, 3, ]
    list_b = [3, 4, 5, ]
    return_value = handlers._get_tag_lists_diff(
        list_a,
        list_b,
    )
    assert return_value == [1, 2, ]


def test__update_tags_helper(
) -> None:
    session = _mock_get_session_proxy()
    client = session.client
    client.create_tags = MagicMock(
        name='create_tags',
        return_value={},
    )
    client.delete_tags = MagicMock(
        name='delete_tags',
        return_value={},
    )
    return_value = handlers._update_tags_helper(
        client=client,
        model=_get_mock_model(),
        request=_get_mock_request(),
    )
    assert return_value is None


def test__import_key_pair_helper(
) -> None:
    model = _get_mock_model()
    request = _get_mock_request()
    return_value = handlers._import_key_pair_helper(
        model=model,
        request=request,
    )
    expected_value = {
        'KeyName': 'mock-key-name',
        'PublicKeyMaterial': b'mock-public-key-material',
        'TagSpecifications': [
            {
                'ResourceType': 'key-pair',
                'Tags': [
                    {'Key': 'mock-key-a', 'Value': 'mock-value-a'},
                    {'Key': 'mock-key-b', 'Value': 'mock-value-b'},
                    {'Key': 'mock-key-1', 'Value': 'mock-value-1'},
                    {'Key': 'mock-key-2', 'Value': 'mock-value-2'},
                ]
            }
        ]
    }
    assert return_value == expected_value


def test__get_resource_model_list(
) -> None:
    key_pairs = _get_mock_key_pair_dict()
    return_value = handlers._get_resource_model_list(
        key_pairs['KeyPairs'],
    )
    expected_value = [
        ResourceModel(
            KeyPairId='mock-key-pair-1',
            KeyFingerprint='mock-key-fingerprint-1',
            KeyName='mock-key-pair-name-1',
            KeyType='mock-key-pair-type-1',
            PublicKeyMaterial=None,
            Tags=[
                Tag(
                    Key='mock-key-1',
                    Value='mock-value-1',
                )
            ]
        ),
        ResourceModel(
            KeyPairId='mock-key-pair-2',
            KeyFingerprint='mock-key-fingerprint-2',
            KeyName='mock-key-pair-name-2',
            KeyType='mock-key-pair-type-2',
            PublicKeyMaterial=None,
            Tags=[
                Tag(
                    Key='mock-key-2',
                    Value='mock-value-2',
                )
            ]
        ),
    ]
    assert return_value == expected_value


def test_create_handler__is_callback(
) -> None:
    session = _mock_get_session_proxy()
    request = MagicMock(
        name='request',
    )
    return_value = handlers.create_handler(
        session,
        request,
        callback_context={'status': OperationStatus.IN_PROGRESS},
    )
    assert return_value.status == OperationStatus.SUCCESS


def test_update_handler__is_callback(
) -> None:
    session = _mock_get_session_proxy()
    request = MagicMock(
        name='request',
    )
    return_value = handlers.update_handler(
        session,
        request,
        callback_context={'status': OperationStatus.IN_PROGRESS},
    )
    assert return_value.status == OperationStatus.SUCCESS


def test_delete_handler__is_callback(
) -> None:
    session = _mock_get_session_proxy()
    request = MagicMock(
        name='request',
    )
    return_value = handlers.delete_handler(
        session,
        request,
        callback_context={'status': OperationStatus.IN_PROGRESS},
    )
    assert return_value.status == OperationStatus.SUCCESS


def test_delete_handler__progress_event_failed(
) -> None:
    with patch(
            f'{BASE_MODULE_PATH_NAME}.handlers.read_handler',
            return_value=ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.NotFound,
            ),
    ):
        return_value = handlers.delete_handler(
            MagicMock(),
            MagicMock(),
            MagicMock(),
        )
        assert return_value.status == OperationStatus.FAILED
