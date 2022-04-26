"""Validate user-defined tags for supported resource types."""

import json
import logging
import os
import re
import traceback
from typing import (
    Any,
    Dict,
    List,
    MutableMapping,
    Optional,
    Sequence,
)

from cloudformation_cli_python_lib import (  # type: ignore
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
)

from .models import (
    HookHandlerRequest,
    TypeConfigurationModel,
)

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)

# Set logging level
# (https://docs.python.org/3/library/logging.html#levels).
# Consider using logging.DEBUG for development and testing only.
LOG.setLevel(logging.CRITICAL)
# LOG.setLevel(logging.INFO)
# LOG.setLevel(logging.DEBUG)

TYPE_NAME = "AWSSamples::ResourceTags::Hook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

# Path to the targets info data file, in JSON format, for this hook.
TARGET_INFO_FILE_NAME = "targets_info.json"

# Locate TARGET_INFO_FILE_NAME in the same directory of this handlers.py file.
TARGETS_INFO_PATH = os.path.join(
    os.path.dirname(
        os.path.abspath(
            __file__,
        ),
    ),
    TARGET_INFO_FILE_NAME,
)

# Delimiter between tag keys entries.
TAGKEYS_DELIM = ","

# Tag key and allowed values delimiter.
TAGKEY_ARGS_DELIM = "="

# Delimited between allowed values for a given key.
TAGKEY_ALLOWED_VALUES_DELIM = "|"

# Token to specify a regular expression in the hook's input.
REGEXP_TOKEN = "regexp:"  # nosec B105


@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)  # type: ignore
@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)  # type: ignore
def pre_create_pre_update_handler(
    session: Optional[SessionProxy],
    request: HookHandlerRequest,
    callback_context: MutableMapping[str, Any],
    type_configuration: TypeConfigurationModel,
) -> ProgressEvent:
    """Use this handler for CREATE and UPDATE pre-provision operations."""
    target_model = request.hookContext.targetModel
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
    )
    try:
        target_name = str(request.hookContext.targetName)
        target_logical_id = str(request.hookContext.targetLogicalId)
        LOG.debug(f"***{TYPE_NAME}, {target_name}, {target_logical_id}***")

        hook_input_validation = _validate_hook_input(
            progress=progress,
            type_configuration=type_configuration,
        )
        if hook_input_validation.status == OperationStatus.FAILED:
            return hook_input_validation
        type_config_tag_keys = _get_type_config_tag_keys(
            type_config_tag_keys=type_configuration.TagKeys,  # type: ignore
        )
        type_config_tag_allowed_values = _get_type_config_tags_allowed_values(
            type_config_tag_keys=type_configuration.TagKeys,  # type: ignore
        )

        resource_properties = target_model.get(  # type: ignore
            "resourceProperties"
        )

        # Read target information from the JSON data file.
        target_info = _get_target_info_data(
            target_name=target_name,
        )
        if not target_info:
            message = "Resource or hook not supporting tags."
            return _non_compliant(
                progress=progress,
                target_name=target_name,
                target_logical_id=target_logical_id,
                message=message,
                error_code=HandlerErrorCode.InvalidRequest,
            )

        if (
            type_configuration.ValidationStrategy == "resource"
            or type_configuration.ValidationStrategy == ""
            or not type_configuration.ValidationStrategy
            or not hasattr(type_configuration, "ValidationStrategy")
        ):
            return _resource_tags_validation(
                progress=progress,
                target_name=target_name,
                target_logical_id=target_logical_id,
                resource_properties=resource_properties,  # type: ignore
                target_info=target_info,
                type_config_tag_keys=type_config_tag_keys,
                type_config_tag_allowed_values=type_config_tag_allowed_values,
            )
        elif type_configuration.ValidationStrategy == "stack":
            stack_id = request.hookContext.stackId
            stack_name = stack_id.split("/")[1]  # type: ignore
            return _stack_tags_validation(
                progress=progress,
                stack_name=stack_name,
                stack_tags=_get_stack_tags(
                    session=session,
                    stack_id=stack_id,  # type: ignore
                ),
                type_config_tag_keys=type_config_tag_keys,
                type_config_tag_allowed_values=type_config_tag_allowed_values,
            )
        else:
            return ProgressEvent.failed(
                HandlerErrorCode.InvalidTypeConfiguration,
                "Unknown tag validation strategy.",
            )
    except Exception as e:
        LOG.debug(f"Exception in hook handler: {str(e)}.")
        LOG.debug(traceback.format_exc())
        return ProgressEvent.failed(
            HandlerErrorCode.InternalFailure,
            str(e),
        )


def _get_session_client(
    session: Optional[SessionProxy],
    service_name: str,
) -> Any:
    """Create and return a session client for service_name."""
    if isinstance(
        session,
        SessionProxy,
    ):
        client = session.client(
            service_name,
        )
        return client
    return None


def _get_stack_info(
    client: Any,
    stack_id: str,
) -> Any:
    """Call the DescribeStacks operation for stack_id."""
    response = client.describe_stacks(
        StackName=stack_id,
    )
    return response


def _get_stack_tags(
    session: Optional[SessionProxy],
    stack_id: str,
) -> Any:
    """Get tags from the specified stack."""
    client = _get_session_client(
        session,
        "cloudformation",
    )
    if not client:
        raise Exception("Unable to create a client for AWS CloudFormation.")
    response = _get_stack_info(
        client=client,
        stack_id=stack_id,
    )
    stack_tags = response["Stacks"][0]["Tags"]
    LOG.info(f"stack tags: {stack_tags}")
    return stack_tags


def _resource_tags_validation(
    progress: ProgressEvent,
    target_name: str,
    target_logical_id: str,
    resource_properties: Dict[str, Any],
    target_info: Dict[Any, Any],
    type_config_tag_keys: List[str],
    type_config_tag_allowed_values: List[Dict[str, Sequence[str]]],
) -> ProgressEvent:
    """Run the resource tags validation logic."""
    # Read tags-related information from target_info.
    for target_tag_info in target_info["tags_info"]:
        target_tag_property_name = target_tag_info["property_name"]
        target_tag_property_type = target_tag_info["property_type"]

        if resource_properties:
            resource_tags = resource_properties.get(target_tag_property_name)
        else:
            resource_tags = []
        validate_resource_properties = _validate_resource_properties(
            progress=progress,
            target_name=target_name,
            target_logical_id=target_logical_id,
            target_tag_property_name=target_tag_property_name,
            resource_properties=resource_properties,
            resource_tags=resource_tags,
        )
        if validate_resource_properties.status == OperationStatus.FAILED:
            return validate_resource_properties

        tags_validation = _validate_resource_tags(
            progress=progress,
            target_name=target_name,
            target_logical_id=target_logical_id,
            target_tag_property_name=target_tag_property_name,
            target_tag_property_type=target_tag_property_type,
            type_config_tag_keys=type_config_tag_keys,
            type_config_tag_allowed_values=type_config_tag_allowed_values,
            resource_tags=resource_tags,
        )
        if tags_validation.status == OperationStatus.FAILED:
            return tags_validation

    # Validate tag propagation-related configuration settings.
    validate_tag_propagation = _validate_tag_propagation(
        progress=progress,
        target_name=target_name,
        target_logical_id=target_logical_id,
        resource_properties=resource_properties,
        resource_tags=resource_tags,
    )
    if validate_tag_propagation.status == OperationStatus.FAILED:
        return validate_tag_propagation
    return tags_validation


def _validate_allowed_values_regexps(
    progress: ProgressEvent,
    type_configuration: TypeConfigurationModel,
) -> ProgressEvent:
    """Validate regular expression input data in the hook's config."""
    for list_entry in _get_type_config_tags_allowed_values(
        type_config_tag_keys=type_configuration.TagKeys,  # type: ignore
    ):
        for regexp in _get_allowed_values_filtered_list(
            allowed_values=list_entry["allowed_values"],
            regexps=True,
        ):
            try:
                re.compile(
                    pattern=regexp,
                )
            except re.error as ree:
                return ProgressEvent.failed(
                    HandlerErrorCode.InvalidTypeConfiguration,
                    f"Regular expression: {regexp}: {str(ree)}",
                )
    return progress


def _validate_hook_input(
    progress: ProgressEvent,
    type_configuration: TypeConfigurationModel,
) -> ProgressEvent:
    """Validate hook input structure and data."""
    if not hasattr(type_configuration, "TagKeys"):
        return ProgressEvent.failed(
            HandlerErrorCode.InvalidTypeConfiguration,
            "No TagKeys hook configuration property.",
        )

    if not type_configuration.TagKeys:
        return ProgressEvent.failed(
            HandlerErrorCode.InvalidTypeConfiguration,
            "Hook configuration for TagKeys missing.",
        )

    for delimiter in _get_delimiter_list():
        if re.match(
            rf"^.*(?=\{delimiter}\{delimiter})",
            _remove_whitespaces_around_delimiters(
                input_string=type_configuration.TagKeys,
            ),
        ):
            return ProgressEvent.failed(
                HandlerErrorCode.InvalidTypeConfiguration,
                f"Can't parse: adjacent '{delimiter}' delimiters found.",
            )

    if re.match(
        rf"(^.*\{TAGKEYS_DELIM}\{TAGKEY_ARGS_DELIM})|(^.*\{TAGKEY_ARGS_DELIM}\{TAGKEYS_DELIM})",  # noqa: E501
        _remove_whitespaces_around_delimiters(
            input_string=type_configuration.TagKeys,
        ),
    ):
        return ProgressEvent.failed(
            HandlerErrorCode.InvalidTypeConfiguration,
            f"Can't parse: '{TAGKEYS_DELIM}' around '{TAGKEY_ARGS_DELIM}'.",
        )

    if not _get_type_config_tag_keys(
        type_config_tag_keys=type_configuration.TagKeys,
    ):
        return ProgressEvent.failed(
            HandlerErrorCode.InvalidTypeConfiguration,
            "Invalid hook configuration: no keys for TagKeys.",
        )

    validate_allowed_values_regexps = _validate_allowed_values_regexps(
        progress=progress,
        type_configuration=type_configuration,
    )
    if validate_allowed_values_regexps.status == OperationStatus.FAILED:
        return validate_allowed_values_regexps

    return progress


def _get_targets_info_data() -> List[Dict[str, Any]]:
    """Return targets info from TARGETS_INFO_PATH."""
    targets_info_data_file = open(
        TARGETS_INFO_PATH,
        "r",
    )
    targets_info = json.load(
        targets_info_data_file,
    )
    targets_info_data_file.close()
    return list(targets_info)


def _get_supported_targets() -> List[str]:
    """Return a list of supported targets from _get_targets_info_data()."""
    targets_info = _get_targets_info_data()

    supported_targets = [target_info["name"] for target_info in targets_info]
    return supported_targets


def _get_target_info_data(
    target_name: str,
) -> Dict[str, Any]:
    """Return target_name resource type info from _get_targets_info_data()."""
    targets_info = _get_targets_info_data()

    if target_name in _get_supported_targets():
        target_info_data = [
            target_info
            for target_info in targets_info
            if target_info["name"] == target_name
        ][0]
        return target_info_data
    return {}


def _tags_object_to_list(
    tags_object: Dict[str, str],
) -> List[Dict[str, str]]:
    """Use this function to convert an object of tags into a key/value list."""
    tags_list = [{"Key": t[0], "Value": t[1]} for t in tags_object.items()]
    LOG.debug(
        f"Converted: {tags_object} into: {tags_list}.",
    )
    return tags_list


def _compliant(
    progress: ProgressEvent,
    target_name: str,
    target_logical_id: str,
) -> ProgressEvent:
    """Return a ProgressEvent with OperationStatus.SUCCESS."""
    progress.status = OperationStatus.SUCCESS
    message = f"{TYPE_NAME} succeeded: {target_name}: {target_logical_id}."
    progress.message = message
    LOG.debug(message)
    return progress


def _non_compliant(
    progress: ProgressEvent,
    target_name: str,
    target_logical_id: str,
    message: str,
    error_code: HandlerErrorCode,
) -> ProgressEvent:
    """Return a ProgressEvent with OperationStatus.FAILED."""
    progress.status = OperationStatus.FAILED
    progress.message = message
    progress.errorCode = error_code
    LOG.debug(f"{TYPE_NAME} failed: {target_name}: {target_logical_id}.")
    LOG.debug(message)
    return progress


def _validate_resource_properties(
    progress: ProgressEvent,
    target_name: str,
    target_logical_id: str,
    target_tag_property_name: str,
    resource_properties: Dict[str, Any],
    resource_tags: Any,
) -> ProgressEvent:
    """Validate properties for a supported resource."""
    LOG.debug(f"target_tag_property_name: {target_tag_property_name}")
    validation_error_found = None
    if not resource_properties:
        validation_error_found = True
        message = "No resource properties specified."
    elif resource_tags is None:
        validation_error_found = True
        message = f"Resource property missing: {target_tag_property_name}."
    elif target_tag_property_name == "TagSpecifications":
        if not resource_tags:
            validation_error_found = True
            message = "TagSpecifications does not contain items."
        elif not resource_tags[0].get("Tags"):
            validation_error_found = True
            message = "TagSpecifications: missing Tags property."

    if validation_error_found:
        return _non_compliant(
            progress=progress,
            target_name=target_name,
            target_logical_id=target_logical_id,
            message=message,
            error_code=HandlerErrorCode.NonCompliant,
        )
    else:
        return progress


def _get_delimiter_list() -> List[str]:
    """Return a list of delimiters defined for this hook."""
    return [
        TAGKEYS_DELIM,
        TAGKEY_ARGS_DELIM,
        TAGKEY_ALLOWED_VALUES_DELIM,
    ]


def _remove_whitespaces_around_delimiters(
    input_string: str,
    delimiters: List[str] = _get_delimiter_list(),
) -> str:
    """Remove whitespaces around specified delimiters in input_string."""
    output_string = input_string
    for delimiter in delimiters:
        output_string = re.sub(
            rf"[\s]*\{delimiter}[\s]*",
            delimiter,
            output_string,
        ).strip()
    return output_string


def _get_type_config_tag_keys(
    type_config_tag_keys: str,
) -> List[str]:
    """Get a list of required tag keys from the hook's configuration."""
    tag_keys_string = _remove_whitespaces_around_delimiters(
        input_string=type_config_tag_keys,
    )
    tag_keys_items = list(
        filter(None, re.split(rf"(?<!\\)\{TAGKEYS_DELIM}", tag_keys_string)),
    )
    tag_keys_list = [
        _remove_char_escape(
            re.split(rf"(?<!\\)\{TAGKEY_ARGS_DELIM}", tag_keys_item)[0],
        )
        for tag_keys_item in tag_keys_items
    ]
    return tag_keys_list


def _get_type_config_tags_allowed_values(
    type_config_tag_keys: str,
) -> List[Dict[str, Sequence[str]]]:
    """Get a list of allowed tags' values from the hook's configuration."""
    tag_keys_string = _remove_whitespaces_around_delimiters(
        input_string=type_config_tag_keys,
    )
    tag_keys_items = list(
        filter(None, re.split(rf"(?<!\\)\{TAGKEYS_DELIM}", tag_keys_string)),
    )
    tags_allowed_values = [
        {
            "allowed_values": list(
                map(
                    _remove_char_escape,
                    list(
                        filter(
                            None,
                            re.split(
                                rf"(?<!\\)\{TAGKEY_ALLOWED_VALUES_DELIM}",
                                re.split(
                                    rf"(?<!\\)\{TAGKEY_ARGS_DELIM}",
                                    tag_keys_item,
                                )[1],
                            ),
                        ),
                    ),
                ),
            ),
            "name": _remove_char_escape(
                re.split(rf"(?<!\\)\{TAGKEY_ARGS_DELIM}", tag_keys_item)[0],
            ),
        }
        for tag_keys_item in tag_keys_items
        if len(re.split(rf"(?<!\\)\{TAGKEY_ARGS_DELIM}", tag_keys_item)) == 2
    ]
    return tags_allowed_values


def _validate_resource_tag_keys(
    progress: ProgressEvent,
    target_name: str,
    target_logical_id: str,
    type_config_tag_keys: List[str],
    resource_tags: List[Dict[str, str]],
) -> ProgressEvent:
    """Validate required tag keys are present for a given resource."""
    # Extract tag keys from resource_tags.
    resource_tag_keys = [resource_tag["Key"] for resource_tag in resource_tags]

    # Return a difference between required tag keys
    # (type_config_tag_keys), and the ones specified for the resource.
    tag_keys_diff = [
        key for key in type_config_tag_keys if key not in resource_tag_keys
    ]
    tag_keys_diff.sort()

    # Non-compliant if required tag keys are missing.
    if tag_keys_diff:
        message = f"Required tag key(s) missing: {tag_keys_diff}."
        return _non_compliant(
            progress=progress,
            target_name=target_name,
            target_logical_id=target_logical_id,
            message=message,
            error_code=HandlerErrorCode.NonCompliant,
        )
    LOG.debug("Required tag keys validation passed.")
    return progress


def _remove_char_escape(
    input_string: str,
    delimiters: List[str] = _get_delimiter_list(),
) -> str:
    """Remove the backslash character before a delimiter in input_string."""
    output_string = input_string
    for delimiter in delimiters:
        output_string = output_string.replace(rf"\{delimiter}", delimiter)
    return output_string


def _get_allowed_values_filtered_list(
    allowed_values: Sequence[str],
    regexps: bool = False,
) -> List[str]:
    """Return either allowed values or regexps from allowed_values."""
    if regexps:
        return [
            regexp.split(REGEXP_TOKEN)[1]
            for regexp in allowed_values
            if regexp.startswith(REGEXP_TOKEN)
        ]
    return [
        allowed_value
        for allowed_value in allowed_values
        if not allowed_value.startswith(REGEXP_TOKEN)
    ]


def _validate_tag_allowed_values(
    progress: ProgressEvent,
    target_name: str,
    target_logical_id: str,
    tags: List[Dict[str, str]],
    type_config_tag_allowed_values: List[Dict[str, Sequence[str]]],
) -> ProgressEvent:
    """Validate specified tag values against user-specified allowed values."""
    validation_errors = []
    for tag in tags:
        for list_entry in type_config_tag_allowed_values:
            value_match_found = None
            regexp_match_found = None
            if tag["Key"] == list_entry["name"]:
                # Find if there is a match in allowed values.
                if tag["Value"] in _get_allowed_values_filtered_list(
                    allowed_values=list_entry["allowed_values"],
                    regexps=False,
                ):
                    value_match_found = True
                    break
                # Find if there is a match in regular expressions.
                for regexp in _get_allowed_values_filtered_list(
                    allowed_values=list_entry["allowed_values"],
                    regexps=True,
                ):
                    if re.match(regexp, tag["Value"]):
                        regexp_match_found = True
                        break

                if not value_match_found and not regexp_match_found:
                    LOG.debug(
                        f"Invalid tag value: {tag['Key']}: {tag['Value']}."
                    )
                    validation_errors.append(
                        f"{tag['Value']} for {tag['Key']}"
                    )

    if validation_errors:
        message = f"Tag(s) with invalid value: {validation_errors}."
        return _non_compliant(
            progress=progress,
            target_name=target_name,
            target_logical_id=target_logical_id,
            message=message,
            error_code=HandlerErrorCode.NonCompliant,
        )
    LOG.debug("Tags have expected values.")
    return progress


def _root_level_tag_propagation_property_defined() -> List[str]:
    """Return resource types with a tag propagation root-level property."""
    return [
        target_info_data["name"]
        for target_info_data in _get_targets_info_data()
        if target_info_data.get("tags_propagation_info")
    ]


def _get_tags_propagation_info(
    target_name: str,
) -> Any:
    """Return tags propagation information for a given target_name."""
    return [
        target_info_data.get("tags_propagation_info")
        for target_info_data in _get_targets_info_data()
        if target_info_data["name"] == target_name
    ][0]


def _validate_tag_propagation_values(
    property_type: str,
    property_value: str,
    expected_values: List[Any],
) -> bool:
    """Validate tag propagation property values."""
    if expected_values is None:
        expected_values = [
            True,
            "true",
        ]
    if property_value not in expected_values:
        return False
    return True


def _validate_tag_propagation(
    progress: ProgressEvent,
    target_name: str,
    target_logical_id: str,
    resource_properties: Dict[str, Any],
    resource_tags: Any,
) -> ProgressEvent:
    """Validate tag propagation is enabled for relevant resources."""
    if (
        target_name != "AWS::AutoScaling::AutoScalingGroup"
        and target_name not in _root_level_tag_propagation_property_defined()
    ):
        return progress

    validation_errors = []
    if target_name == "AWS::AutoScaling::AutoScalingGroup":
        for resource_tag in resource_tags:
            if not resource_tag.get(
                "PropagateAtLaunch"
            ) or not _validate_tag_propagation_values(
                property_type="boolean",
                property_value=resource_tag["PropagateAtLaunch"],
                expected_values=[
                    True,
                    "true",
                ],
            ):
                validation_errors.append(resource_tag["Key"])
                message = (
                    f"Propagation not set up for tag(s): {validation_errors}."
                )

    if target_name in _root_level_tag_propagation_property_defined():
        for tag_propagation_info in _get_tags_propagation_info(
            target_name=target_name,
        ):
            if not resource_properties.get(
                tag_propagation_info["property_name"]
            ) or not _validate_tag_propagation_values(
                property_type=tag_propagation_info["property_name"],
                property_value=resource_properties[
                    tag_propagation_info["property_name"]
                ],
                expected_values=tag_propagation_info.get(
                    "tag_propagation_values"
                ),
            ):
                validation_errors.append(tag_propagation_info["property_name"])
                message = f"Propagation not set up for property: {validation_errors}."  # noqa: E501

    if validation_errors:
        return _non_compliant(
            progress=progress,
            target_name=target_name,
            target_logical_id=target_logical_id,
            message=message,
            error_code=HandlerErrorCode.NonCompliant,
        )
    LOG.debug("Tag propagation settings have expected values.")
    return progress


def _validate_resource_tag_values(
    progress: ProgressEvent,
    target_name: str,
    target_logical_id: str,
    resource_tags: List[Dict[str, str]],
    type_config_tag_allowed_values: List[Dict[str, Sequence[str]]],
) -> ProgressEvent:
    """Validate tag values are not empty."""
    # Determines if tags have empty values.
    tag_values_empty = [
        resource_tag["Key"]
        for resource_tag in resource_tags
        if not resource_tag["Value"]
    ]
    tag_values_empty.sort()

    # Non-compliant if empty values for tag keys are found.
    if tag_values_empty:
        message = f"Empty value(s) for tag(s): {tag_values_empty}."
        return _non_compliant(
            progress=progress,
            target_name=target_name,
            target_logical_id=target_logical_id,
            message=message,
            error_code=HandlerErrorCode.NonCompliant,
        )
    LOG.debug("Tag keys have non-empty values: validation passed.")

    # Validate tag values against user-specified allowed values.
    validate_tag_allowed_values = _validate_tag_allowed_values(
        progress=progress,
        target_name=target_name,
        target_logical_id=target_logical_id,
        tags=resource_tags,
        type_config_tag_allowed_values=type_config_tag_allowed_values,
    )
    if validate_tag_allowed_values.status == OperationStatus.FAILED:
        return validate_tag_allowed_values
    return progress


def _validate_resource_tags(
    progress: ProgressEvent,
    target_name: str,
    target_logical_id: str,
    target_tag_property_name: str,
    target_tag_property_type: str,
    type_config_tag_keys: List[str],
    type_config_tag_allowed_values: List[Dict[str, Sequence[str]]],
    resource_tags: Any,
) -> ProgressEvent:
    """Perform resource tags validation against comma-delimited tag_keys."""
    LOG.debug(f"resource_tags: {resource_tags}")

    # If the tag property type is an object, convert it to a list model.
    LOG.debug(f"target_tag_property_type: {target_tag_property_type}")
    if target_tag_property_type == "object":
        resource_tags = _tags_object_to_list(
            tags_object=resource_tags,
        )

    # If the target resource type property is TagSpecifications,
    # validate tag keys and values for each TagSpecification item.
    if target_tag_property_name == "TagSpecifications":
        for tagspecification_tags in resource_tags:
            validate_tagspecification_tag_keys_values = _validate_resource_tag_keys_values(  # noqa: E501
                progress=progress,
                target_name=target_name,
                target_logical_id=target_logical_id,
                type_config_tag_keys=type_config_tag_keys,
                type_config_tag_allowed_values=type_config_tag_allowed_values,
                resource_tags=tagspecification_tags["Tags"],
            )
            if (
                validate_tagspecification_tag_keys_values.status
                == OperationStatus.FAILED
            ):
                return validate_tagspecification_tag_keys_values
        return validate_tagspecification_tag_keys_values

    validate_tag_keys_values = _validate_resource_tag_keys_values(
        progress=progress,
        target_name=target_name,
        target_logical_id=target_logical_id,
        type_config_tag_keys=type_config_tag_keys,
        type_config_tag_allowed_values=type_config_tag_allowed_values,
        resource_tags=resource_tags,
    )
    return validate_tag_keys_values


def _validate_resource_tag_keys_values(
    progress: ProgressEvent,
    target_name: str,
    target_logical_id: str,
    type_config_tag_keys: List[str],
    type_config_tag_allowed_values: List[Dict[str, Sequence[str]]],
    resource_tags: Any,
) -> ProgressEvent:
    """Validate tag keys and values for the given resource."""
    # Validate tag keys.
    tag_keys_validation = _validate_resource_tag_keys(
        progress=progress,
        target_name=target_name,
        target_logical_id=target_logical_id,
        type_config_tag_keys=type_config_tag_keys,
        resource_tags=resource_tags,
    )
    if tag_keys_validation.status == OperationStatus.FAILED:
        return tag_keys_validation

    # Validate tag values.
    tag_values_validation = _validate_resource_tag_values(
        progress=progress,
        target_name=target_name,
        target_logical_id=target_logical_id,
        resource_tags=resource_tags,
        type_config_tag_allowed_values=type_config_tag_allowed_values,
    )
    if tag_values_validation.status == OperationStatus.FAILED:
        return tag_values_validation
    return _compliant(
        progress=progress,
        target_name=target_name,
        target_logical_id=target_logical_id,
    )


def _validate_stack_tag_keys(
    progress: ProgressEvent,
    stack_name: str,
    type_config_tag_keys: List[str],
    stack_tags: List[Dict[str, str]],
) -> ProgressEvent:
    """Validate required tag keys are present in the stack."""
    # Extract tag keys from resource_tags.
    stack_tag_keys = [stack_tag["Key"] for stack_tag in stack_tags]

    # Return a difference between required tag keys
    # (type_config_tag_keys), and the ones specified for the stack.
    tag_keys_diff = [
        key for key in type_config_tag_keys if key not in stack_tag_keys
    ]
    tag_keys_diff.sort()

    # Non-compliant if required tag keys are missing.
    if tag_keys_diff:
        message = f"Required tag key(s) missing: {tag_keys_diff} on stack."
        return _non_compliant(
            progress=progress,
            target_name="stack",
            target_logical_id=stack_name,
            message=message,
            error_code=HandlerErrorCode.NonCompliant,
        )
    LOG.debug("Required tag keys validation passed.")
    return progress


def _stack_tags_validation(
    progress: ProgressEvent,
    stack_name: str,
    stack_tags: List[Dict[str, str]],
    type_config_tag_keys: List[str],
    type_config_tag_allowed_values: List[Dict[str, Sequence[str]]],
) -> ProgressEvent:
    """Validate tag keys and values for the given stack."""
    # Validate tag keys.
    tag_keys_validation = _validate_stack_tag_keys(
        progress=progress,
        stack_name=stack_name,
        type_config_tag_keys=type_config_tag_keys,
        stack_tags=stack_tags,
    )
    if tag_keys_validation.status == OperationStatus.FAILED:
        return tag_keys_validation

    # Stack tag values cannot be empty, skipping relevant validation.
    # Validate tag values against user-specified allowed values.
    validate_tag_allowed_values = _validate_tag_allowed_values(
        progress=progress,
        target_name="stack",
        target_logical_id=stack_name,
        tags=stack_tags,
        type_config_tag_allowed_values=type_config_tag_allowed_values,
    )
    if validate_tag_allowed_values.status == OperationStatus.FAILED:
        return validate_tag_allowed_values
    return _compliant(
        progress=progress,
        target_name="stack",
        target_logical_id=stack_name,
    )
