import logging
import traceback

from typing import (
    Any,
    MutableMapping,
    Optional,
)

from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
)

from .models import (
    ResourceHandlerRequest,
    ResourceModel,
)

import botocore


# Use this logger to forward log messages to CloudWatch Logs
LOG = logging.getLogger(__name__)

# Set logging level
# (https://docs.python.org/3/library/logging.html#levels)
# Consider using logging.DEBUG for development and testing only
LOG.setLevel(logging.CRITICAL)
# LOG.setLevel(logging.DEBUG)

# This is name of the resource type
TYPE_NAME = "AWSSamples::EC2::ImportKeyPair"

resource = Resource(
    TYPE_NAME,
    ResourceModel,
)

test_entrypoint = resource.test_entrypoint

# How long to wait, in seconds, to call again a given handler as part
# of a resource stabilization logic
CALLBACK_DELAY_SECONDS = 5

# Define a context for the callback logic.  The value for the "status"
# key in the dictionary below is consumed in is_callback() and in
# _callback_helper(), that are invoked from a given handler
CALLBACK_STATUS_IN_PROGRESS = {
    'status': OperationStatus.IN_PROGRESS,
}


@resource.handler(Action.CREATE)
def create_handler(
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Define the CREATE handler"""
    LOG.debug("*CREATE handler*")

    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    LOG.debug(f"Progress status: {progress.status}")

    # Check whether or not this is a new invocation of this handler
    if _is_callback(
            callback_context,
    ):
        return _callback_helper(
            session,
            request,
            callback_context,
            model,
            is_delete_handler=False,
        )
    # If no callback context is present, then this is a new invocation
    else:
        LOG.debug("No callback context present")

    try:
        client = _get_session_client(
            session,
            'ec2',
        )
        # Prepare kwargs to pass to import_key_pair()
        import_key_pair_kwargs = _import_key_pair_helper(
            model=model,
        )
        # Import the key pair
        response = client.import_key_pair(
            **import_key_pair_kwargs,
        )

        # Every returned model must include the primary identifier,
        # that in this case is the KeyPairId.  Retrieving the primary
        # identifier and setting it in the model
        model.KeyPairId = response['KeyPairId']
    except botocore.exceptions.ClientError as ce:
        return _progress_event_failed(
            handler_error_code=HandlerErrorCode.NotFound,
            error_message=str(ce),
            traceback_content=traceback.format_exc(),
        )
    except Exception as e:
        return _progress_event_failed(
            handler_error_code=HandlerErrorCode.InternalFailure,
            error_message=str(e),
            traceback_content=traceback.format_exc(),
        )
    return _progress_event_callback(
        model=model,
    )


@resource.handler(Action.UPDATE)
def update_handler(
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Define the UPDATE handler"""
    LOG.debug("*UPDATE handler*")

    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    LOG.debug(f"Progress status: {progress.status}")

    # Reusing the callback context logic leveraged in the Read handler
    if _is_callback(
            callback_context,
    ):
        return _callback_helper(
            session,
            request,
            callback_context,
            model,
            is_delete_handler=False,
        )
    else:
        LOG.debug("No callback context present")

    # KeyPairName and KeyPairPublicKey are set as createOnlyProperties
    # in the model; specifying values for such will then result in a
    # new resource being created.  This Update handler is only used to
    # update Tags as specified in the template
    try:
        client = _get_session_client(
            session,
            'ec2',
        )
        # delete and create, if any, tags for the resource
        _delete_create_tags_helper(
            client=client,
            model=model,
        )
    except botocore.exceptions.ClientError as ce:
        return _progress_event_failed(
            handler_error_code=HandlerErrorCode.NotFound,
            error_message=str(ce),
            traceback_content=traceback.format_exc(),
        )
    except Exception as e:
        return _progress_event_failed(
            handler_error_code=HandlerErrorCode.InternalFailure,
            error_message=str(e),
            traceback_content=traceback.format_exc(),
        )
    return _progress_event_callback(
        model=model,
    )


@resource.handler(Action.DELETE)
def delete_handler(
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Define the DELETE handler"""
    LOG.debug("*DELETE handler*")

    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    LOG.debug(f"Progress status: {progress.status}")

    # Callback context logic
    if _is_callback(
            callback_context,
    ):
        return _callback_helper(
            session,
            request,
            callback_context,
            model,
            is_delete_handler=True,
        )
    else:
        LOG.debug("No callback context present")

    try:
        client = _get_session_client(
            session,
            'ec2',
        )
        # Call the Read handler to look for the resource, and return a
        # NotFound handler error code if the resource is not found
        rh = read_handler(
            session,
            request,
            callback_context,
        )
        if rh.errorCode:
            if rh.errorCode == HandlerErrorCode.NotFound:
                return _progress_event_failed(
                    handler_error_code=HandlerErrorCode.NotFound,
                    error_message=str(rh.message),
                    traceback_content=None,
                )
        client.delete_key_pair(
            KeyName=model.KeyName,
        )
    except botocore.exceptions.ClientError as ce:
        return _progress_event_failed(
            handler_error_code=HandlerErrorCode.NotFound,
            error_message=str(ce),
            traceback_content=traceback.format_exc(),
        )
    except Exception as e:
        return _progress_event_failed(
            handler_error_code=HandlerErrorCode.InternalFailure,
            error_message=str(e),
            traceback_content=traceback.format_exc(),
        )
    return _progress_event_callback(
        model=model,
    )


@resource.handler(Action.READ)
def read_handler(
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Define the READ handler"""
    LOG.debug("*READ handler*")

    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    LOG.debug(f"Progress status: {progress.status}")

    try:
        client = _get_session_client(
            session,
            'ec2',
        )
        response = client.describe_key_pairs(
            KeyPairIds=[
                model.KeyPairId,
            ],
        )
        model.KeyFingerprint = response['KeyPairs'][0]['KeyFingerprint']
    except botocore.exceptions.ClientError as ce:
        return _progress_event_failed(
            handler_error_code=HandlerErrorCode.NotFound,
            error_message=str(ce),
            traceback_content=traceback.format_exc(),
        )
    except Exception as e:
        return _progress_event_failed(
            handler_error_code=HandlerErrorCode.InternalFailure,
            error_message=str(e),
            traceback_content=traceback.format_exc(),
        )
    return _progress_event_success(
        model=model,
        is_delete_handler=False,
    )


@resource.handler(Action.LIST)
def list_handler(
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Define the LIST handler"""
    LOG.debug("*LIST handler*")

    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    LOG.debug(f"Progress status: {progress.status}")

    try:
        client = _get_session_client(
            session,
            'ec2',
        )
        response = client.describe_key_pairs(
        )
        key_pairs = response['KeyPairs']
        resource_model_list = []
        for key_pair in key_pairs:
            resource_model_list_item = ResourceModel(
                KeyPairId=key_pair['KeyPairId'],
                KeyFingerprint=key_pair['KeyFingerprint'],
                KeyName=key_pair['KeyName'],
                Tags=key_pair['Tags'],
                PublicKeyMaterial=None,
            )
            resource_model_list.append(
                resource_model_list_item,
            )
    except botocore.exceptions.ClientError as ce:
        return _progress_event_failed(
            handler_error_code=HandlerErrorCode.NotFound,
            error_message=str(ce),
            traceback_content=traceback.format_exc(),
        )
    except Exception as e:
        return _progress_event_failed(
            handler_error_code=HandlerErrorCode.InternalFailure,
            error_message=str(e),
            traceback_content=traceback.format_exc(),
        )
    return _progress_event_success(
        models=resource_model_list,
        is_delete_handler=False,
    )


def _progress_event_callback(
        model: ResourceModel,
) -> ProgressEvent:
    """Return a ProgressEvent indicating a callback should occur next"""
    LOG.debug("_progress_event_callback()")

    return ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
        callbackContext=CALLBACK_STATUS_IN_PROGRESS,
        callbackDelaySeconds=CALLBACK_DELAY_SECONDS,
    )


def _progress_event_success(
        model: ResourceModel = None,
        models: list = None,
        is_delete_handler=False,
) -> ProgressEvent:
    """Return a ProgressEvent indicating a success"""
    LOG.debug("_progress_event_success()")

    if not model and not models and not is_delete_handler:
        raise ValueError(
            "Specify a model or models, or set is_delete_handler to True",
        )
    # In the case of the Delete handler, just return the status
    if is_delete_handler:
        if model or models:
            raise ValueError(
                "Specified model data with is_delete_handler set to True",
            )
        return ProgressEvent(
            status=OperationStatus.SUCCESS,
        )
    # Otherwise, specify either 'model' or 'models'
    if not bool(model) ^ bool(models):
        raise ValueError(
            "Specify a model or models when is_delete_handler is set to False",
        )
    elif(model):
        return ProgressEvent(
            status=OperationStatus.SUCCESS,
            resourceModel=model,
        )
    elif(models):
        return ProgressEvent(
            status=OperationStatus.SUCCESS,
            resourceModels=models,
        )


def _progress_event_failed(
        handler_error_code: HandlerErrorCode,
        error_message: str,
        traceback_content: str = None,
) -> ProgressEvent:
    """Log an error, and return a ProgressEvent indicating a failure"""
    LOG.debug("_progress_event_failed()")

    # Choose a logging level depending on the handler error code
    log_entry = f"""Error message: {error_message},
    traceback content: {traceback_content}"""

    if handler_error_code == HandlerErrorCode.InternalFailure:
        LOG.critical(log_entry)
    elif handler_error_code == HandlerErrorCode.NotFound:
        LOG.debug(log_entry)
    return ProgressEvent.failed(
        handler_error_code,
        f"Error: {error_message}",
    )


def _is_callback(
        callback_context: MutableMapping[str, Any],
) -> bool:
    """Logic to determine whether or not a handler invocation is new"""
    LOG.debug("_is_callback()")

    # If there is a callback context status set, then assume this is a
    # handler invocation (e.g., Create handler) for a previous request
    # that is still in progress
    return callback_context.get('status') == \
        CALLBACK_STATUS_IN_PROGRESS['status']


def _callback_helper(
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
        model: ResourceModel,
        is_delete_handler: bool = False,
) -> ProgressEvent:
    """Define a callback logic used for resource stabilization"""
    LOG.debug("_callback_helper()")

    # Call the Read handler to determine status
    rh = read_handler(
        session,
        request,
        callback_context,
    )
    LOG.debug(f"Callback: Read handler status: {rh.status}")
    # Return success if the Read handler returns success
    if rh.status == OperationStatus.SUCCESS:
        return _progress_event_success(
            model=model,
            is_delete_handler=False,
        )
    elif rh.errorCode:
        LOG.debug(f"Callback: Read handler error code: {rh.errorCode}")
        if rh.errorCode == HandlerErrorCode.NotFound and is_delete_handler:
            # Return a success status if the resource is not found
            # (thus, assuming it has been deleted).  The Delete
            # handler's response object must not contain a model:
            # hence, the logic driven by is_delete_handler set to True
            # below will not specify a model for ProgressEvent
            return _progress_event_success(
                is_delete_handler=True,
            )
    # Otherwise, call this handler again by using a callback logic
    else:
        return _progress_event_callback(
            model=model,
        )


def _get_session_client(
        session: Optional[SessionProxy],
        service: str,
) -> type:
    """Create and return a session client for a given service"""
    LOG.debug("_get_session_client()")

    if isinstance(
            session,
            SessionProxy,
    ):
        client = session.client(
            'ec2',
        )
        return client
    return None


def _get_tags_from_model_tags(
        model_tags: list,
) -> list:
    """Create and return a list of key/value tags from model.Tags"""
    LOG.debug("_get_tags_from_model_tags()")

    tags = [
        {
            "Key": model_tag.Key,
            "Value": model_tag.Value,
        }
        for model_tag in model_tags
    ]
    return tags


def _delete_create_tags_helper(
        client: type,
        model: ResourceModel,
) -> None:
    """Delete and create tags, if present"""
    LOG.debug("_delete_create_tags_helper()")

    # Delete existing tags
    client.delete_tags(
        Resources=[
            model.KeyPairId,
        ],
    )
    # Add new tags if specified in the template
    if model.Tags:
        tags = _get_tags_from_model_tags(
            model.Tags,
        )
        # Create new tags
        client.create_tags(
            Resources=[
                model.KeyPairId,
            ],
            Tags=tags,
        )


def _import_key_pair_helper(
        model: ResourceModel,
) -> dict:
    """Create and return a dictionary of arguments for import_key_pair()"""
    LOG.debug("_import_key_pair_helper()")

    import_key_pair_kwargs = {
        'KeyName': model.KeyName,
        'PublicKeyMaterial': bytes(
            model.PublicKeyMaterial,
            encoding='utf-8',
        ),
    }
    if model.Tags:
        tags = _get_tags_from_model_tags(
            model.Tags,
        )
        # Add TagSpecifications to kwargs if Tags are specified in
        # the template, and specify key/value data for Tags
        import_key_pair_kwargs['TagSpecifications'] = [
            {
                'ResourceType': 'key-pair',
                'Tags': tags,
            },
        ]
    return import_key_pair_kwargs
