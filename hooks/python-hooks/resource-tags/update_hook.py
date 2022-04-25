#!/usr/bin/env python3

"""Fetch resource types' tag-related info for the hook to consume."""

import json
import logging
import re
import sys
from typing import (
    Any,
    Dict,
    List,
)

import boto3  # type: ignore
from botocore.config import Config  # type: ignore

# Categories of resource types where to search.  For more information, see:
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation.Client.list_types in the Boto3 documentation.  # noqa: E501
RESOURCE_TYPE_CATEGORIES = [
    "AWS_TYPES",
    # "THIRD_PARTY",
    # "REGISTERED",
    # "ACTIVATED",
]

# Create a logger.
LOG = logging.getLogger(__name__)

# Set logging level
# (https://docs.python.org/3/library/logging.html#levels).
# Consider using logging.DEBUG for development and testing only.
# LOG.setLevel(logging.CRITICAL)
LOG.setLevel(logging.INFO)
# LOG.setLevel(logging.DEBUG)

# Create a console stream handler for the logger, a file handler, a
# formatter for the logger, and add handlers to the logger.
LOG_STREAM_HANDLER = logging.StreamHandler(
    stream=sys.stderr,
)
LOG_FILE_HANDLER = logging.FileHandler(
    filename="update_hook.log",
    mode="a",
)
LOG_FORMATTER = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s"
)
LOG_STREAM_HANDLER.setFormatter(LOG_FORMATTER)
LOG.addHandler(LOG_STREAM_HANDLER)
LOG.addHandler(LOG_FILE_HANDLER)

# Setting up a Boto3 client Config object:
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html
# that is used here for retries on botocore.exceptions.ClientError
# Throttling errors (e.g., when getting a rate exceeded error in
# calling the DescribeType operation).  For information on retries, see
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/retries.html .
CLIENT_CONFIG = Config(
    retries={
        "max_attempts": 15,
        "mode": "standard",
    }
)

CLIENT = boto3.client(
    "cloudformation",
    config=CLIENT_CONFIG,
)

# Data types for tag-related resource properties.
TAG_PROPERTY_TYPES = [
    "array",
    "object",
]

# Data types for tag-related resource properties.
TAG_PROPAGATION_PROPERTY_TYPES = [
    "boolean",
    "string",
]

# Data types for tag propagation property values.
TAG_PROPAGATION_VALUES_PROPERTY_TYPES = [
    "boolean",
    "enum",
]

SRC_PATH = "src/awssamples_resourcetags_hook/"

# File that will contain resource types and property information.
TARGETS_INFO_PATH = SRC_PATH + "targets_info.json"

# File that will contain user-defined ignored resource types and
# property information.
IGNORED_TARGETS_INFO_PATH = SRC_PATH + "ignored_targets_info.json"

# Path to the hook's schema file.
SCHEMA_FILE_PATH = "awssamples-resourcetags-hook.json"

# Paths to contract test input files.
INPUTS_1_PRE_CREATE_PATH = "inputs/inputs_1_pre_create.json"
INPUTS_1_PRE_UPDATE_PATH = "inputs/inputs_1_pre_update.json"
INPUTS_1_INVALID_PATH = "inputs/inputs_1_invalid.json"


def main() -> None:
    """Define the main function."""
    resource_types = []
    for resource_type_category in RESOURCE_TYPE_CATEGORIES:
        resource_types += _get_resource_types(
            category=resource_type_category,
        )

    _generate_data_file(
        resource_types=resource_types,
    )

    _patch_schema_file()

    _generate_contract_test_inputs()


def _generate_contract_test_inputs() -> None:
    """Generate contract test input files for this hook."""
    LOG.info("Generating contract test inputs.")

    _generate_inputs_1_pre_create()

    _generate_inputs_1_pre_update()

    _generate_inputs_1_invalid()


def _get_resource_types(
    category: str = "AWS_TYPES",
) -> List[Dict[str, Any]]:
    """Return a list of resource types."""
    LOG.info(f"Retrieving {category} resource types.")

    list_types_args = {
        "DeprecatedStatus": "LIVE",
        "Type": "RESOURCE",
        "Filters": {
            "Category": category,
            # "TypeNamePrefix": "",
        },
    }

    if category == "THIRD_PARTY":
        visibility = None
    elif category in [
        "AWS_TYPES",
        "ACTIVATED",
    ]:
        visibility = "PUBLIC"
    else:
        visibility = "PRIVATE"

    if visibility:
        list_types_args["Visibility"] = visibility

    paginator = CLIENT.get_paginator(
        "list_types",
    )
    LOG.debug(f"list_types() args: {list_types_args}")
    page_iterator = paginator.paginate(
        **list_types_args,
    )

    resource_types = []
    for page in page_iterator:
        type_summaries = page["TypeSummaries"]
        resource_types += [
            {
                "type_name": type_summary["TypeName"],
                # PublisherId is available if the extension is
                # published by a third party.
                "publisher_id": type_summary.get("PublisherId"),
            }
            for type_summary in type_summaries
        ]
    return resource_types


def _get_referenced_value_from_schema(
    schema_object: Dict[str, Any],
    schema_properties: Dict[str, Any],
    property_name: str,
    target_reference: str = "type",
) -> Any:
    """Return the type of a given property from a resolved JSON reference."""
    schema_prop_ref = schema_properties[property_name]["$ref"]
    schema_prop_ref_path = schema_prop_ref.split("/")
    if schema_prop_ref_path[0] == "#":
        schema_prop_ref_path.pop(0)
    schema_object_ref = schema_object
    for path_item in schema_prop_ref_path:
        schema_object_ref = schema_object_ref[path_item]
    return schema_object_ref[target_reference]


def _resource_type_tag_info_builder(
    type_name: str,
    schema_object: Dict[str, Any],
    schema_properties: Dict[str, Any],
    property_name: str,
    relevance: str = "tag",  # tag or tag_propagation
    target_reference: str = "type",
) -> Dict[str, Any]:
    """Build a dictionary with tag-related information for type_name."""
    LOG.info(f"Determining type for property: {property_name}")
    if relevance == "tag":
        relevance_filter = TAG_PROPERTY_TYPES
        tag_info = {}
    elif relevance == "tag_propagation":
        relevance_filter = TAG_PROPAGATION_PROPERTY_TYPES
        tag_propagation_values: Dict[Any, Any] = {}

    # Determine if target property information can be retrieved directly.
    if schema_properties[property_name].get(target_reference):
        property_type = schema_properties[property_name][target_reference]
    # Otherwise, resolve the schema reference.
    elif schema_properties[property_name].get("$ref"):
        property_type = _get_referenced_value_from_schema(
            schema_object=schema_object,
            schema_properties=schema_properties,
            property_name=property_name,
            target_reference=target_reference,
        )

    if property_type in relevance_filter:
        tag_info = {
            "property_name": property_name,
            "property_type": property_type,
        }
    LOG.debug(f"{type_name} tag_info: {tag_info}")

    if relevance == "tag_propagation" and property_type == "string":
        tag_propagation_values = schema_properties[property_name].get("enum")
        tag_info["tag_propagation_values"] = tag_propagation_values
    return tag_info


def _get_ignored_targets_info_data() -> List[Dict[str, Any]]:
    """Return ignored targets info from IGNORED_TARGETS_INFO_PATH."""
    ignored_targets_info_data_file = open(
        IGNORED_TARGETS_INFO_PATH,
        "r",
    )
    ignored_targets_info = json.load(
        ignored_targets_info_data_file,
    )
    ignored_targets_info_data_file.close()
    return list(ignored_targets_info)


def _is_ignored_target(
    type_name: str,
    property_name: str,
) -> bool:
    """Return whether a specific property is ignored for a given type_name."""
    ignored_targets_search = _get_ignored_targets_info_data()
    ignored_target_search = [
        ignored_target_search
        for ignored_target_search in ignored_targets_search
        if ignored_target_search["name"] == type_name
    ]
    if not ignored_target_search:
        return False
    else:
        ignored_target = ignored_target_search[0]

    ignored_target_properties = ignored_target["ignored_target_properties"]
    ignored_target_property = [
        ignored_target_property
        for ignored_target_property in ignored_target_properties
        if ignored_target_property["property_name"] == property_name
    ]

    if ignored_target_property:
        return True
    return False


def _get_resource_type_tags_info(
    resource_type: Dict[str, Any],
) -> Dict[Any, Any]:
    """Return tag- and tag-propagation-related info for a given type_name."""
    type_name = resource_type["type_name"]
    publisher_id = resource_type["publisher_id"]
    tags_info = []
    tags_propagation_info = []

    if publisher_id:
        response = CLIENT.describe_type(
            Type="RESOURCE",
            TypeName=type_name,
            PublisherId=publisher_id,
        )
    else:
        response = CLIENT.describe_type(
            Type="RESOURCE",
            TypeName=type_name,
        )

    schema_object = json.loads(
        response["Schema"],
    )
    schema_properties = schema_object["properties"]
    LOG.debug(f"{type_name} schema_properties: {schema_properties}")

    # Search for property keys that contain the `Tag` occurrence.
    tag_properties = {
        key
        for key, value in schema_properties.items()
        if re.search("Tag", key)
    }
    for tag_property in sorted(tag_properties):
        if _is_ignored_target(
            type_name=type_name,
            property_name=tag_property,
        ):
            LOG.info(f"Ignoring {type_name}: {tag_property}")
            continue
        resource_type_tag_info = _resource_type_tag_info_builder(
            type_name=type_name,
            schema_object=schema_object,
            schema_properties=schema_properties,
            property_name=tag_property,
            relevance="tag",
            target_reference="type",
        )
        if resource_type_tag_info:
            LOG.info(f"Adding {type_name}: {tag_property}")
            tags_info.append(
                resource_type_tag_info,
            )

    # Search for property keys that contain the `Propagat` occurrence.
    tag_propagation_properties = {
        key
        for key, value in schema_properties.items()
        if re.search("Propagat", key)
    }
    for tag_propagation_property in sorted(tag_propagation_properties):
        if _is_ignored_target(
            type_name=type_name,
            property_name=tag_propagation_property,
        ):
            LOG.info(f"Ignoring {type_name}: {tag_propagation_property}")
            continue
        resource_type_tag_propagation_info = _resource_type_tag_info_builder(
            type_name=type_name,
            schema_object=schema_object,
            schema_properties=schema_properties,
            property_name=tag_propagation_property,
            relevance="tag_propagation",
            target_reference="type",
        )
        if resource_type_tag_propagation_info:
            LOG.info(f"Adding {type_name}: {tag_propagation_property}")
            tags_propagation_info.append(
                resource_type_tag_propagation_info,
            )
    return {
        "tags_info": tags_info,
        "tags_propagation_info": tags_propagation_info,
    }


def _generate_data_file(
    resource_types: List[Dict[str, Any]],
) -> None:
    """Store resource type info that include tag-related properties."""
    LOG.info("Gathering resource type info, and generate the data file.")

    resource_types_target_info_data = []
    for resource_type in resource_types:
        type_name = resource_type["type_name"]
        # Prepare a dictionary with tag property information.
        resource_type_info = {}
        LOG.info(f"Gathering info for: {type_name}")
        resource_type_info = _get_resource_type_tags_info(
            resource_type,
        )
        resource_type_tags_info = resource_type_info["tags_info"]
        resource_type_tags_propagation_info = resource_type_info[
            "tags_propagation_info"
        ]
        if resource_type_tags_info:
            LOG.debug(f"{type_name} tags info: {resource_type_tags_info}")
            # Add resource type tags info to the dictionary.
            resource_type_info = {
                "name": type_name,
                "tags_info": resource_type_tags_info,
            }
            if resource_type_tags_propagation_info:
                resource_type_info[
                    "tags_propagation_info"
                ] = resource_type_tags_propagation_info
            # Append resource_type_info to the data list.
            resource_types_target_info_data.append(resource_type_info)

    # Prepare to save info data above to file.
    resource_types_target_info_data_file = open(
        TARGETS_INFO_PATH,
        "w",
    )
    json.dump(
        resource_types_target_info_data,
        resource_types_target_info_data_file,
        indent=4,
        sort_keys=False,
    )
    resource_types_target_info_data_file.write("\n")
    resource_types_target_info_data_file.close()


def _get_data_file_content() -> Any:
    """Read data from TARGETS_INFO_PATH, and return it as a list of objects."""
    targets_info_data_file = open(
        TARGETS_INFO_PATH,
        "r",
    )
    targets_info_data = json.load(
        targets_info_data_file,
    )
    targets_info_data_file.close()
    return targets_info_data


def _patch_schema_file() -> None:
    """Patches the schema file for this hook."""
    LOG.info("Reading schema file for this hook.")
    schema_file = open(
        SCHEMA_FILE_PATH,
        "r",
    )
    schema = json.load(
        schema_file,
    )
    schema_file.close()

    # Prepare data for schema updates.
    LOG.info("Preparing schema file patches.")
    targets_info = _get_data_file_content()
    resource_types = [target_info["name"] for target_info in targets_info]
    schema["handlers"]["preCreate"]["targetNames"] = resource_types
    schema["handlers"]["preUpdate"]["targetNames"] = resource_types

    # Patch the schema file.
    LOG.info("Applying schema file patches.")
    schema_file = open(
        SCHEMA_FILE_PATH,
        "w",
    )
    json.dump(
        schema,
        schema_file,
        indent=4,
        sort_keys=False,
    )
    schema_file.write("\n")
    schema_file.close()


def _get_tagspecifications_resource_type(
    resource_type: str,
) -> str:
    """Build the value for the resource type property for TagSpecifications."""
    resource_type_suffix = resource_type.split("::")[2]
    resource_type_suffix = re.sub("EC2Fleet", "Fleet", resource_type_suffix)
    return "-".join(
        [
            item.lower()
            for item in re.split(r"([A-Z][a-z]*[0-9]*)", resource_type_suffix)
            if item
        ]
    )


def _generate_contract_tests_input_stub(
    resource_type: str,
    tags_info: List[Dict[str, Any]],
    tag_key: str,
    tag_value: str,
    tags_propagation_info: List[Dict[str, Any]] = [],
) -> Dict[str, Any]:
    """Return a stub for contract test input data for a given resource type."""
    stub: Dict[str, Any] = {}
    stub["resourceProperties"] = {}

    for tag_info in tags_info:
        tag_property_name = tag_info["property_name"]
        tag_property_type = tag_info["property_type"]

        if tag_property_type == "array":
            if tag_property_name == "TagSpecifications":
                stub["resourceProperties"][tag_property_name] = [
                    {
                        "ResourceType": _get_tagspecifications_resource_type(
                            resource_type,
                        ),
                        "Tags": [
                            {
                                "Key": tag_key,
                                "Value": tag_value,
                            },
                        ],
                    },
                ]
            elif resource_type == "AWS::AutoScaling::AutoScalingGroup":
                stub["resourceProperties"][tag_property_name] = [
                    {
                        "Key": tag_key,
                        "Value": tag_value,
                        "PropagateAtLaunch": True,
                    },
                ]
            else:
                stub["resourceProperties"][tag_property_name] = [
                    {
                        "Key": tag_key,
                        "Value": tag_value,
                    },
                ]
        elif tag_property_type == "object":
            stub["resourceProperties"][tag_property_name] = {
                tag_key: tag_value,
            }

    if tags_propagation_info:
        for tag_propagation_info in tags_propagation_info:
            tag_property_name = tag_propagation_info["property_name"]
            tag_property_type = tag_propagation_info["property_type"]
            if tag_property_type == "boolean":
                tag_property_value = True
            else:
                tag_property_value = tag_propagation_info[
                    "tag_propagation_values"
                ][0]
            stub["resourceProperties"][tag_property_name] = tag_property_value
    return stub


def _write_contract_test_file(
    contract_test_file_path: str,
    contract_test_data: Dict[Any, Dict[Any, Any]],
) -> None:
    """Write data to a given contract test file."""
    contract_tests_input_file = open(
        contract_test_file_path,
        "w",
    )
    json.dump(
        contract_test_data,
        contract_tests_input_file,
        indent=4,
        sort_keys=False,
    )
    contract_tests_input_file.write("\n")
    contract_tests_input_file.close()


def _generate_inputs_1_pre_create() -> None:
    """Generate the INPUTS_1_PRE_CREATE_PATH file."""
    # Define inputs_1_pre_create data.
    inputs_1_pre_create = {}

    targets_info = _get_data_file_content()
    for target_info in targets_info:
        inputs_1_pre_create[
            target_info["name"]
        ] = _generate_contract_tests_input_stub(
            resource_type=target_info["name"],
            tags_info=target_info["tags_info"],
            tag_key="Name",
            tag_value="Test",
            tags_propagation_info=target_info.get("tags_propagation_info"),
        )

    # Write the contract tests input file for pre-create.
    _write_contract_test_file(
        contract_test_file_path=INPUTS_1_PRE_CREATE_PATH,
        contract_test_data=inputs_1_pre_create,
    )


def _generate_inputs_1_pre_update() -> None:
    """Generate the INPUTS_1_PRE_UPDATE_PATH file."""
    # Define inputs_1_pre_update data.
    inputs_1_pre_update = {}

    targets_info = _get_data_file_content()
    for target_info in targets_info:
        inputs_1_pre_update[
            target_info["name"]
        ] = _generate_contract_tests_input_stub(
            resource_type=target_info["name"],
            tags_info=target_info["tags_info"],
            tag_key="Name",
            tag_value="Test1",
            tags_propagation_info=target_info.get("tags_propagation_info"),
        )

    # Write the contract tests input file for update.
    _write_contract_test_file(
        contract_test_file_path=INPUTS_1_PRE_UPDATE_PATH,
        contract_test_data=inputs_1_pre_update,
    )


def _generate_inputs_1_invalid() -> None:
    """Generate the INPUTS_1_INVALID_PATH file."""
    inputs_1_invalid = {}

    targets_info = _get_data_file_content()
    for target_info in targets_info:
        inputs_1_invalid[
            target_info["name"]
        ] = _generate_contract_tests_input_stub(
            resource_type=target_info["name"],
            tags_info=target_info["tags_info"],
            tag_key="invalid",
            tag_value="",
            tags_propagation_info=target_info.get("tags_propagation_info"),
        )

    # Write the contract tests input file for invalid.
    _write_contract_test_file(
        contract_test_file_path=INPUTS_1_INVALID_PATH,
        contract_test_data=inputs_1_invalid,
    )


if __name__ == "__main__":
    main()
