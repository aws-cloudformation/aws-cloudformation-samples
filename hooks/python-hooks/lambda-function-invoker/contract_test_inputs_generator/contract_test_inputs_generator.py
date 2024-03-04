"""AWSSamples::LambdaFunctionInvoker::Hook contract test inputs generator."""


import json
import logging
from dataclasses import (
    dataclass,
    field,
)
from os.path import join as join_os_paths
from pathlib import Path
from sys import stderr
from typing import (
    Any,
    Dict,
    List,
    Union,
)

import boto3  # type: ignore
from botocore.config import Config  # type: ignore
from botocore.paginate import PageIterator  # type: ignore

# Set up logging.
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG_STREAM_HANDLER = logging.StreamHandler(
    stream=stderr,
)
LOG_FORMATTER = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
)
LOG_STREAM_HANDLER.setFormatter(LOG_FORMATTER)
LOG.addHandler(LOG_STREAM_HANDLER)

# Set up AWS regions from which to gather resource target information.
DEPLOY_AWS_REGIONS = [
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ap-southeast-4",
    "ca-central-1",
    "ca-west-1",
    "eu-central-1",
    "eu-central-2",
    "eu-north-1",
    "eu-south-1",
    "eu-south-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "il-central-1",
    "me-central-1",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]

# Set up file paths and names for contract test input files.
INPUTS_1_PRE_CREATE_FILE = "inputs/inputs_1_pre_create.json"
INPUTS_1_PRE_UPDATE_FILE = "inputs/inputs_1_pre_update.json"
INPUTS_1_PRE_DELETE_FILE = "inputs/inputs_1_pre_delete.json"
INPUTS_1_INVALID_PRE_CREATE_FILE = "inputs/inputs_1_invalid_pre_create.json"
INPUTS_1_INVALID_PRE_UPDATE_FILE = "inputs/inputs_1_invalid_pre_update.json"
INPUTS_1_INVALID_PRE_DELETE_FILE = "inputs/inputs_1_invalid_pre_delete.json"

# Set up file encoding for contract test input files.
CONTRACT_TEST_INPUT_FILES_ENCODING = "utf-8"

# Set up a boto3 client for AWS CloudFormation, with a configuration
# to allow for custom retries.
CLOUDFORMATION_CLIENT_CONFIG = Config(
    retries={
        "max_attempts": 20,
        "mode": "standard",
    }
)


@dataclass
class ContractTestInputsGenerator:
    """Generate contract test inputs for the Lambda function invoker hook."""

    # The path of an alternate parent directory where to create the
    # input test files.  On normal operations, you want to run this
    # class code from a Python file that is at the root level of your
    # hook project: in these cases, always set `parent_directory_path`
    # to `None`, so you can update the files in the `inputs` top-level
    # directory that is at the root of your hook project.  You should
    # only set a value for `parent_directory_path` when writing unit
    # tests for this module.
    parent_directory_path: Union[str, None] = None

    discovered_resource_type_names: List[str] = field(default_factory=list)

    # Boto3 client for AWS CloudFormation.
    _cloudformation_client: Any = None

    # Pre-create, pre-update, and pre-delete will contain the same
    # structure; if this will change in the future, keeping them
    # decoupled in separate variables will help with refactoring.
    _inputs_1_pre_create: Dict[str, Any] = field(default_factory=dict)
    _inputs_1_pre_update: Dict[str, Any] = field(default_factory=dict)
    _inputs_1_pre_delete: Dict[str, Any] = field(default_factory=dict)

    _inputs_1_invalid_pre_create: Dict[str, Any] = field(default_factory=dict)
    _inputs_1_invalid_pre_update: Dict[str, Any] = field(default_factory=dict)
    _inputs_1_invalid_pre_delete: Dict[str, Any] = field(default_factory=dict)

    def discover_aws_resources(self) -> None:
        """Get a list of AWS resource type names."""
        discovered_resource_type_names: List[str] = []

        for region in DEPLOY_AWS_REGIONS:
            LOG.info(f"Fetching information from AWS region: {region}.")

            self._cloudformation_client = boto3.client(
                "cloudformation",
                config=CLOUDFORMATION_CLIENT_CONFIG,
                region_name=region,
            )

            list_types_pages = self._get_aws_resource_types_list()

            # Iterate through results above, get resource type names,
            # and store those into a list.
            discovered_resource_type_names_region_set = set(
                self._get_type_names_from_list_types_page_iterator(
                    list_types_pages=list_types_pages,
                )
            )
            discovered_resource_type_names_set = set(
                discovered_resource_type_names
            )
            discovered_resource_type_names = list(
                discovered_resource_type_names_set.union(
                    discovered_resource_type_names_region_set
                )
            )

        discovered_resource_type_names.sort()
        LOG.info(
            f"Found {len(discovered_resource_type_names)} resource type(s)."
        )

        self.discovered_resource_type_names = discovered_resource_type_names

    def _get_aws_resource_types_list(
        self,
    ) -> PageIterator:
        """Use the ListTypes CloudFormation API to list AWS resource types."""
        LOG.info("Discovering AWS resource type(s) with specified filters.")

        # Set up a paginator to use with ListTypes.
        list_types_paginator = self._cloudformation_client.get_paginator(
            "list_types",
        )

        # Set up options, get pages with discovered resource types
        # into a botocore.paginate.PageIterator.
        list_types_pages = list_types_paginator.paginate(
            DeprecatedStatus="LIVE",
            Filters={
                "Category": "AWS_TYPES",
                # For development and testing only: uncomment and
                # configure as needed the TypeNamePrefix filter.
                # "TypeNamePrefix": "AWS::S3::BucketPolicy",
            },
            Type="RESOURCE",
            Visibility="PUBLIC",
        )

        return list_types_pages

    def _get_type_names_from_list_types_page_iterator(
        self,
        list_types_pages: PageIterator,
    ) -> List[str]:
        """Return TypeName list items from a PageIterator."""
        resource_type_names: List[str] = []

        # Iterate through pages, get resource type names, and store
        # those into a list.
        for list_types_page in list_types_pages:
            discovered_type_summaries = list_types_page["TypeSummaries"]
            resource_type_names += [
                discovered_type_summary["TypeName"]
                for discovered_type_summary in discovered_type_summaries
            ]

        return resource_type_names

    def generate_contract_test_inputs(self) -> None:
        """Generate contract test inputs for discovered resource types."""
        LOG.info("Generating contract test inputs.")

        pre_create_1_inputs: Dict[str, Any] = {}
        pre_update_1_inputs: Dict[str, Any] = {}
        pre_delete_1_inputs: Dict[str, Any] = {}

        invalid_pre_create_1_inputs: Dict[str, Any] = {}
        invalid_pre_update_1_inputs: Dict[str, Any] = {}
        invalid_pre_delete_1_inputs: Dict[str, Any] = {}

        for (
            discovered_resource_type_name
        ) in self.discovered_resource_type_names:
            # Generate inputs for pre-create; will use the same for
            # pre-update and pre-delete outside this loop.
            pre_create_1_inputs[discovered_resource_type_name] = {
                "resourceProperties": {},
            }
            # Same as above for invalid inputs across pre-create,
            # pre-update, and pre-delete handlers.
            invalid_pre_create_1_inputs[discovered_resource_type_name] = {
                "resourceProperties": {
                    "InvalidPropertyKey": "invalid_property_value",
                },
            }

        pre_update_1_inputs = pre_create_1_inputs
        pre_delete_1_inputs = pre_create_1_inputs

        invalid_pre_update_1_inputs = invalid_pre_create_1_inputs
        invalid_pre_delete_1_inputs = invalid_pre_create_1_inputs

        LOG.info("Generated contract test inputs.")

        self._inputs_1_pre_create = pre_create_1_inputs
        self._inputs_1_pre_update = pre_update_1_inputs
        self._inputs_1_pre_delete = pre_delete_1_inputs

        self._inputs_1_invalid_pre_create = invalid_pre_create_1_inputs
        self._inputs_1_invalid_pre_update = invalid_pre_update_1_inputs
        self._inputs_1_invalid_pre_delete = invalid_pre_delete_1_inputs

    def write_contract_test_inputs_to_disk(self) -> None:
        """Write to disk the generated contract test inputs."""

        # Map input file names to its relevant data; this map will be
        # used to iterate through each file to commit its data to
        # disk.
        input_files_to_data = [
            {
                "input_file": INPUTS_1_PRE_CREATE_FILE,
                "datum": self._inputs_1_pre_create,
            },
            {
                "input_file": INPUTS_1_PRE_UPDATE_FILE,
                "datum": self._inputs_1_pre_update,
            },
            {
                "input_file": INPUTS_1_PRE_DELETE_FILE,
                "datum": self._inputs_1_pre_delete,
            },
            {
                "input_file": INPUTS_1_INVALID_PRE_CREATE_FILE,
                "datum": self._inputs_1_invalid_pre_create,
            },
            {
                "input_file": INPUTS_1_INVALID_PRE_UPDATE_FILE,
                "datum": self._inputs_1_invalid_pre_update,
            },
            {
                "input_file": INPUTS_1_INVALID_PRE_DELETE_FILE,
                "datum": self._inputs_1_invalid_pre_delete,
            },
        ]

        # Write data for each file to disk.
        for input_file_to_datum in input_files_to_data:
            input_file = str(input_file_to_datum["input_file"])
            datum = input_file_to_datum["datum"]

            input_file_path = (
                join_os_paths(Path.cwd(), input_file)
                if not self.parent_directory_path
                else join_os_paths(self.parent_directory_path, input_file)
            )

            LOG.info(f"Writing {input_file_path} to disk.")
            input_file_object = open(
                input_file_path,
                mode="w",
                encoding=CONTRACT_TEST_INPUT_FILES_ENCODING,
            )
            json.dump(
                datum,
                input_file_object,
                indent=4,
                sort_keys=True,
            )
            input_file_object.write("\n")
            input_file_object.close()
