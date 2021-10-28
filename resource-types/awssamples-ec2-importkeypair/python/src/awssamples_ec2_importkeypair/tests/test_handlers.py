import re

from unittest.mock import (
    MagicMock,
    patch,
)

from functools import (
    wraps,
)

from typing import (
    Any,
    Callable,
)

from cloudformation_cli_python_lib import (
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
)

from .. import handlers

import botocore


def handler_assertions(
        handler_name: str,
        test_case: str,
) -> Callable:
    """Configurable decorator for testing assertions for a given handler"""

    def decorator_function(
            decorated_function: Callable,
    ) -> Callable:
        """Returns a wrapper for the decorated function"""

        @wraps(decorated_function)
        def decorated_function_wrapper(
                *args: list,
                **kwargs: dict,
        ) -> Any:
            """Runs the input function and performs test assertions"""
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
                # Injecting a mock ValidationError as an example
                return_value = \
                    _get_session_client_inject_error_and_call_handler(
                        handler_name=handler_name,
                        error_name='ValidationError',
                    )
                _operation_status_failed_botocore_client_error_assertions(
                    return_value=return_value,
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
            {
                'Error':
                {
                    'Code': error_name,
                    'Message': MagicMock()
                },
            },
            MagicMock(),
        )
    else:
        side_effect = KeyError(
            MagicMock(),
        )

    # Determine the base module path name from the resource type name
    base_module_path_name = re.sub('::', '_', handlers.TYPE_NAME.lower())
    with patch(
            f'{base_module_path_name}.handlers._get_session_client',
            side_effect=side_effect,
    ):
        return _mock_call_handler(
            handler_name=handler_name,
        )


def _mock_call_handler(
        handler_name: str,
) -> ProgressEvent:
    """Helper method to call a given handler for testing"""
    session = _mock_get_session_client()
    request = MagicMock(
        name='request',
    )
    callback_context = MagicMock(
        name='callback_context',
    )
    if handler_name == 'create':
        return handlers.create_handler(
            session,
            request,
            callback_context,
        )
    elif handler_name == 'update':
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
) -> None:
    """Assertions for botocore.exceptions.ClientError test cases"""
    assert isinstance(return_value, ProgressEvent)
    assert return_value.status == OperationStatus.FAILED
    assert return_value.errorCode == HandlerErrorCode.InvalidRequest
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


def _mock_get_session_client(
) -> SessionProxy:
    """Create and return a mock session client"""
    session = MagicMock(
        name='session',
    )
    session.client = MagicMock(
        name='client',
        return_value=MagicMock(
            name='client',
        ),
    )
    return SessionProxy(
        session,
    )


@handler_assertions(
    handler_name='create',
    test_case='operation_status_in_progress',
)
def test_create_handler_returns_operation_status_in_progress(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)
    handlers._import_key_pair_helper = MagicMock()


@handler_assertions(
    handler_name='update',
    test_case='operation_status_in_progress',
)
def test_update_handler_returns_operation_status_in_progress(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)
    handlers._update_tags_helper = MagicMock()


@handler_assertions(
    handler_name='delete',
    test_case='operation_status_in_progress',
)
def test_delete_handler_returns_operation_status_in_progress(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='read',
    test_case='operation_status_success',
)
def test_read_handler_returns_operation_status_success(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='list',
    test_case='operation_status_success',
)
def test_list_handler_returns_operation_status_success(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='create',
    test_case='operation_status_failed_botocore_client_error',
)
def test_create_handler_returns_operation_status_failed_botocore_client_error(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='create',
    test_case='operation_status_failed_generic_error',
)
def test_create_handler_returns_operation_status_failed_generic_error(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='update',
    test_case='operation_status_failed_botocore_client_error',
)
def test_update_handler_returns_operation_status_failed_botocore_client_error(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='update',
    test_case='operation_status_failed_generic_error',
)
def test_update_handler_returns_operation_status_failed_generic_error(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='delete',
    test_case='operation_status_failed_botocore_client_error',
)
def test_delete_handler_returns_operation_status_failed_botocore_client_error(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='delete',
    test_case='operation_status_failed_generic_error',
)
def test_delete_handler_returns_operation_status_failed_generic_error(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='read',
    test_case='operation_status_failed_botocore_client_error',
)
def test_read_handler_returns_operation_status_failed_botocore_client_error(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='read',
    test_case='operation_status_failed_generic_error',
)
def test_read_handler_returns_operation_status_failed_generic_error(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='list',
    test_case='operation_status_failed_botocore_client_error',
)
def test_list_handler_returns_operation_status_failed_botocore_client_error(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)


@handler_assertions(
    handler_name='list',
    test_case='operation_status_failed_generic_error',
)
def test_list_handler_returns_operation_status_failed_generic_error(
) -> None:
    session = _mock_get_session_client()
    client = session
    assert isinstance(client, SessionProxy)
