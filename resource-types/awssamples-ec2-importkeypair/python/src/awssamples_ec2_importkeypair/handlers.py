import logging
import traceback
from typing import (
    Any,
    MutableMapping,
    Optional,
)

import botocore
from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
)

from . models import (
    ResourceHandlerRequest,
    ResourceModel,
    Tag,
)


# Use this logger to forward log messages to CloudWatch Logs
LOG = logging.getLogger(__name__)

# Set logging level
# (https://docs.python.org/3/library/logging.html#levels)
# Consider using logging.DEBUG for development and testing only
LOG.setLevel(logging.CRITICAL)
# LOG.setLevel(logging.DEBUG)

# This is the name of the resource type
TYPE_NAME = 'AWSSamples::EC2::ImportKeyPair'

resource = Resource(
    TYPE_NAME,
    ResourceModel,
)

test_entrypoint = resource.test_entrypoint

# When you want to have a resource to be in a specific state before
# you, e.g., determine the resource is ready in your resource type
# implementation logic, you want to implement a stabilization logic.
# For example, you would want to look, in the Read handler, for the
# presence of a resource-specific property value and drive the
# callback process accordingly to determine if the resource is ready.
# The example resource type in this sample would not need
# stabilization, and hence it would not need to use a callback
# mechanism to leverage the Read handler to determine if the resource
# is ready.  However, this sample is meant to illustrate how a
# callback mechanism would work, and that is why it is being leveraged
# here.  In the example CALLBACK_DELAY_SECONDS variable below, you
# specify how long to wait, in seconds, to call again a given handler
# as part of a resource stabilization logic
CALLBACK_DELAY_SECONDS = 5

# Define a context for the callback logic.  The value for the 'status'
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
    LOG.debug('*CREATE handler*')

    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    LOG.debug(f'Progress status: {progress.status}')

    # Check whether or not this is a new invocation of this handler
    if _is_callback(
            callback_context,
    ):
        return _callback_helper(
            session,
            request,
            callback_context,
            model,
        )
    # If no callback context is present, then this is a new invocation
    else:
        LOG.debug('No callback context present')

    try:
        client = _get_session_client(
            session,
            'ec2',
        )
        # Prepare kwargs to pass to import_key_pair()
        import_key_pair_kwargs = _import_key_pair_helper(
            model=model,
            request=request,
        )
        # Import the key pair
        response = client.import_key_pair(
            **import_key_pair_kwargs,
        )

        # Every returned model must include the primary identifier,
        # that in this case is the KeyPairId.  Retrieving the primary
        # identifier and setting it in the model
        model.KeyPairId = response['KeyPairId']

        # PublicKeyMaterial is not available in ImportKeyPair and
        # DescribeKeyPairs response elements: hence, not including it
        # in the model on responses.  In this example resource type,
        # PublicKeyMaterial is then described as part of
        # writeOnlyProperties in the schema: as such, it will not be
        # returned in Read and List handlers.  Setting its value to
        # None in handler responses as shown next, and elsewhere in
        # handlers-related code for this example resource type
        model.PublicKeyMaterial = None
    except botocore.exceptions.ClientError as ce:
        return _progress_event_failed(
            handler_error_code=_get_handler_error_code(
                ce.response['Error']['Code'],
            ),
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
    LOG.debug('*UPDATE handler*')

    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    LOG.debug(f'Progress status: {progress.status}')

    # Reusing the callback context logic leveraged in the Read handler
    if _is_callback(
            callback_context,
    ):
        return _callback_helper(
            session,
            request,
            callback_context,
            model,
        )
    else:
        LOG.debug('No callback context present')

    # KeyPairName and KeyPairPublicKey are set as createOnlyProperties
    # in the model; specifying values for such will then result in a
    # new resource being created.  The Update handler for this
    # specific resource is only used for update of Tags
    try:
        client = _get_session_client(
            session,
            'ec2',
        )
        # Update tags for the resource
        _update_tags_helper(
            client=client,
            model=model,
            request=request,
        )

        model.PublicKeyMaterial = None
    except botocore.exceptions.ClientError as ce:
        return _progress_event_failed(
            handler_error_code=_get_handler_error_code(
                ce.response['Error']['Code'],
            ),
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
    LOG.debug('*DELETE handler*')

    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    LOG.debug(f'Progress status: {progress.status}')

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
        LOG.debug('No callback context present')

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
            handler_error_code=_get_handler_error_code(
                ce.response['Error']['Code'],
            ),
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
    LOG.debug('*READ handler*')

    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    LOG.debug(f'Progress status: {progress.status}')

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
        key_pair = response['KeyPairs'][0]
        model.KeyPairId = key_pair['KeyPairId']
        model.KeyName = key_pair['KeyName']
        if 'Tags' in key_pair and key_pair['Tags']:
            model.Tags = _get_model_tags_from_tags(
                key_pair['Tags'],
            )
        else:
            model.Tags = None
        model.KeyFingerprint = key_pair['KeyFingerprint']
        model.KeyType = key_pair['KeyType']
        model.PublicKeyMaterial = None
    except botocore.exceptions.ClientError as ce:
        return _progress_event_failed(
            handler_error_code=_get_handler_error_code(
                ce.response['Error']['Code'],
            ),
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
    )


@resource.handler(Action.LIST)
def list_handler(
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Define the LIST handler"""
    LOG.debug('*LIST handler*')

    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    LOG.debug(f'Progress status: {progress.status}')

    try:
        client = _get_session_client(
            session,
            'ec2',
        )
        response = client.describe_key_pairs(
        )
        key_pairs = response['KeyPairs']
        resource_model_list = []
        resource_model_list = _get_resource_model_list(
            key_pairs,
        )
    except botocore.exceptions.ClientError as ce:
        return _progress_event_failed(
            handler_error_code=_get_handler_error_code(
                ce.response['Error']['Code'],
            ),
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
        is_list_handler=True,
    )


def _get_handler_error_code(
        api_error_code: str,
) -> HandlerErrorCode:
    """Get a handler error code for a given service API error code"""
    LOG.debug('_get_handler_error_code()')

    # Handler error codes in the User Guide for Extension Development:
    # https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-contract-errors.html
    #
    # Error codes for the Amazon EC2 API:
    # https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html
    if api_error_code == 'InvalidKeyPair.NotFound':
        return HandlerErrorCode.NotFound
    elif api_error_code == 'InvalidKeyPair.Duplicate':
        return HandlerErrorCode.AlreadyExists
    elif api_error_code in [
            'InvalidKey.Format',
            'InvalidKeyPair.Format',
            'InvalidParameter',
            'InvalidParameterCombination',
            'InvalidParameterValue',
            'InvalidTagKey.Malformed',
            'MissingAction',
            'MissingParameter',
            'UnknownParameter',
            'ValidationError',
    ]:
        return HandlerErrorCode.InvalidRequest
    elif api_error_code in [
            'KeyPairLimitExceeded',
            'TagLimitExceeded',
    ]:
        return HandlerErrorCode.ServiceLimitExceeded
    elif api_error_code in [
            'ConcurrentTagAccess',
            'RequestLimitExceeded',
    ]:
        return HandlerErrorCode.Throttling
    else:
        return HandlerErrorCode.GeneralServiceException


def _progress_event_callback(
        model: ResourceModel,
) -> ProgressEvent:
    """Return a ProgressEvent indicating a callback should occur next"""
    LOG.debug('_progress_event_callback()')

    return ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
        callbackContext=CALLBACK_STATUS_IN_PROGRESS,
        callbackDelaySeconds=CALLBACK_DELAY_SECONDS,
    )


def _progress_event_success(
        model: ResourceModel = None,
        models: list = None,
        is_delete_handler: bool = False,
        is_list_handler: bool = False,
) -> ProgressEvent:
    """Return a ProgressEvent indicating a success"""
    LOG.debug('_progress_event_success()')

    if not model \
       and not models \
       and not is_delete_handler \
       and not is_list_handler:
        raise ValueError(
            'Model, or models, or is_delete_handler, or is_list_handler unset',
        )
    # Otherwise, specify 'is_delete_handler' or 'is_list_handler', not both
    elif is_delete_handler and is_list_handler:
        raise ValueError(
            'Specify either is_delete_handler or is_list_handler, not both',
        )
    # In the case of the Delete handler, just return the status
    elif is_delete_handler:
        return ProgressEvent(
            status=OperationStatus.SUCCESS,
        )
    # In the case of the List handler, return the status and 'resourceModels'
    elif is_list_handler:
        return ProgressEvent(
            status=OperationStatus.SUCCESS,
            resourceModels=models,
        )
    else:
        return ProgressEvent(
            status=OperationStatus.SUCCESS,
            resourceModel=model,
        )


def _progress_event_failed(
        handler_error_code: HandlerErrorCode,
        error_message: str,
        traceback_content: str = None,
) -> ProgressEvent:
    """Log an error, and return a ProgressEvent indicating a failure"""
    LOG.debug('_progress_event_failed()')

    # Choose a logging level depending on the handler error code
    log_entry = f"""Error message: {error_message},
    traceback content: {traceback_content}"""

    if handler_error_code == HandlerErrorCode.InternalFailure:
        LOG.critical(log_entry)
    elif handler_error_code == HandlerErrorCode.NotFound:
        LOG.debug(log_entry)
    return ProgressEvent.failed(
        handler_error_code,
        f'Error: {error_message}',
    )


def _is_callback(
        callback_context: MutableMapping[str, Any],
) -> bool:
    """Logic to determine whether or not a handler invocation is new"""
    LOG.debug('_is_callback()')

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
    LOG.debug('_callback_helper()')

    # Call the Read handler to determine status
    rh = read_handler(
        session,
        request,
        callback_context,
    )
    LOG.debug(f'Callback: Read handler status: {rh.status}')
    # Return success if the Read handler returns success
    if rh.status == OperationStatus.SUCCESS:
        return _progress_event_success(
            model=model,
        )
    elif rh.errorCode:
        LOG.debug(f'Callback: Read handler error code: {rh.errorCode}')
        if rh.errorCode == HandlerErrorCode.NotFound and is_delete_handler:
            LOG.debug('NotFound error in Delete handler: returning success')
            # Return a success status if the resource is not found
            # (thus, assuming it has been deleted).  The Delete
            # handler's response object must not contain a model:
            # hence, the logic driven by is_delete_handler set to True
            # below will not specify a model for ProgressEvent
            return _progress_event_success(
                is_delete_handler=True,
            )
        elif rh.errorCode == HandlerErrorCode.NotFound:
            return _progress_event_failed(
                handler_error_code=rh.errorCode,
                error_message=rh.message,
                traceback_content=None,
            )
    # Otherwise, call this handler again by using a callback logic
    else:
        return _progress_event_callback(
            model=model,
        )


def _get_session_client(
        session: Optional[SessionProxy],
        service_name: str,
) -> type:
    """Create and return a session client for a given service"""
    LOG.debug('_get_session_client()')

    if isinstance(
            session,
            SessionProxy,
    ):
        client = session.client(
            service_name,
        )
        return client
    return None


def _get_tags_from_desired_resource_tags(
        desired_resource_tags: dict,
) -> list:
    """Create and return a list of tags from
request.desiredResourceTags"""
    LOG.debug('_get_tags_from_desired_resource_tags()')

    tags = [
        {
            'Key': desired_resource_tag,
            'Value': desired_resource_tags[desired_resource_tag],
        }
        for desired_resource_tag in desired_resource_tags
    ]
    return tags


def _get_tags_from_previous_resource_tags(
        previous_resource_tags: dict,
) -> list:
    """Create and return a list of tags from
request.previousResourceTags"""
    LOG.debug('_get_tags_from_previous_resource_tags()')

    tags = [
        {
            'Key': previous_resource_tag,
            'Value': previous_resource_tags[previous_resource_tag],
        }
        for previous_resource_tag in previous_resource_tags
    ]
    return tags


def _get_tags_from_model_tags(
        model_tags: list,
) -> list:
    """Create and return a list of tags from model.Tags"""
    LOG.debug('_get_tags_from_model_tags()')

    tags = [
        {
            'Key': model_tag.Key,
            'Value': model_tag.Value,
        }
        for model_tag in model_tags
    ]
    return tags


def _get_model_tags_from_tags(
        tags: list,
) -> list:
    """Create and return a list of model.Tags from tags"""
    LOG.debug('_get_model_tags_from_tags()')

    model_tags = [
        Tag(
            Key=tag.get('Key'),
            Value=tag.get('Value'),
        )
        for tag in tags
    ]
    return model_tags


def _build_tag_list(
        model: ResourceModel,
        request: ResourceHandlerRequest,
) -> list:
    """Build and return a list of resource tags"""
    LOG.debug('_build_tag_list()')

    tags = []

    # Determine if stack-level tags are present
    if request.desiredResourceTags:
        desired_resource_tags = _get_tags_from_desired_resource_tags(
            request.desiredResourceTags,
        )
        tags += desired_resource_tags

    # Retrieve tags if specified in the model
    if model.Tags:
        model_tags = _get_tags_from_model_tags(
            model.Tags,
        )
        tags += model_tags

    return tags


def _get_tag_lists_diff(
        list_a: list,
        list_b: list,
) -> list:
    """Return a list of tag differences between list_a and list_b"""
    LOG.debug('_get_tag_lists_diff()')

    return [list_item for list_item in list_a if list_item not in list_b]


def _update_tags_helper(
        client: type,
        model: ResourceModel,
        request: ResourceHandlerRequest,
) -> None:
    """Update tags on stack update"""
    LOG.debug('_update_tags_helper()')

    previous_resource_tags = []

    # Retrieve existing tags, if any, from the request
    if request.previousResourceTags:
        previous_resource_tags = _get_tags_from_previous_resource_tags(
            request.previousResourceTags,
        )

    # Retrieve current tags specified in the model and/or at the stack
    # level
    tags = _build_tag_list(
        model,
        request,
    )

    # Retrieve a list containing differences, if any, between previous
    # resource tags and current tags
    tag_lists_diff = _get_tag_lists_diff(
        previous_resource_tags,
        tags,
    )

    # Add/overwrite new tags if present
    if tags:
        # Create new tags
        client.create_tags(
            Resources=[
                model.KeyPairId,
            ],
            Tags=tags,
        )

    # Delete existing tags that are not specified in the update
    # request
    if tag_lists_diff:
        client.delete_tags(
            Resources=[
                model.KeyPairId,
            ],
            Tags=tag_lists_diff,
        )


def _import_key_pair_helper(
        model: ResourceModel,
        request: ResourceHandlerRequest,
) -> dict:
    """Create and return a dictionary of arguments for import_key_pair()"""
    LOG.debug('_import_key_pair_helper()')

    import_key_pair_kwargs = {
        'KeyName': model.KeyName,
        'PublicKeyMaterial': bytes(
            model.PublicKeyMaterial,
            encoding='utf-8',
        ),
    }

    tags = _build_tag_list(
        model,
        request,
    )

    # Add TagSpecifications to kwargs if tags are present
    if tags:
        import_key_pair_kwargs['TagSpecifications'] = [
            {
                'ResourceType': 'key-pair',
                'Tags': tags,
            },
        ]
    return import_key_pair_kwargs


def _get_resource_model_list(
        key_pairs: dict,
) -> list:
    """Create and return a list of resource model items"""
    LOG.debug('_get_resource_model_list()')

    resource_model_list = []
    for key_pair in key_pairs:

        if 'Tags' in key_pair and key_pair['Tags']:
            model_tags = _get_model_tags_from_tags(
                key_pair['Tags'],
            )
        else:
            model_tags = None

        resource_model_list_item = ResourceModel(
            KeyPairId=key_pair['KeyPairId'],
            KeyFingerprint=key_pair['KeyFingerprint'],
            KeyName=key_pair['KeyName'],
            KeyType=key_pair['KeyType'],
            Tags=model_tags,
            PublicKeyMaterial=None,
        )
        resource_model_list.append(
            resource_model_list_item,
        )
    return resource_model_list
