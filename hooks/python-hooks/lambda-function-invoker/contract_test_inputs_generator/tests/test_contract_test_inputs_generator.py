"""Unit tests for contract_test_inputs_generator."""


import json
import os
import tempfile
from collections import OrderedDict
from os.path import join as join_os_paths
from pathlib import Path
from unittest.mock import (
    MagicMock,
    patch,
)

from ..contract_test_inputs_generator import (
    CONTRACT_TEST_INPUT_FILES_ENCODING,
    INPUTS_1_INVALID_PRE_CREATE_FILE,
    INPUTS_1_INVALID_PRE_DELETE_FILE,
    INPUTS_1_INVALID_PRE_UPDATE_FILE,
    INPUTS_1_PRE_CREATE_FILE,
    INPUTS_1_PRE_DELETE_FILE,
    INPUTS_1_PRE_UPDATE_FILE,
    ContractTestInputsGenerator,
)
from .mocks import (
    INVALID_1_PRE_CREATE_FILE_CONTENT,
    INVALID_1_PRE_CREATE_INPUTS,
    INVALID_1_PRE_DELETE_FILE_CONTENT,
    INVALID_1_PRE_DELETE_INPUTS,
    INVALID_1_PRE_UPDATE_FILE_CONTENT,
    INVALID_1_PRE_UPDATE_INPUTS,
    LIST_TYPES_PAGINATOR_RESPONSE_MOCK_RESOURCE_TYPE,
    VALID_1_PRE_CREATE_FILE_CONTENT,
    VALID_1_PRE_CREATE_INPUTS,
    VALID_1_PRE_DELETE_FILE_CONTENT,
    VALID_1_PRE_DELETE_INPUTS,
    VALID_1_PRE_UPDATE_FILE_CONTENT,
    VALID_1_PRE_UPDATE_INPUTS,
)


def test_given_found_resource_type_when_get_aws_resource_types_list_called_then_discovered_resource_type_name_should_match() -> (  # noqa: E501
    None
):
    mock_cloudformation_client = MagicMock()

    mock_contract_test_inputs_generator = ContractTestInputsGenerator(
        _cloudformation_client=mock_cloudformation_client,
        parent_directory_path=None,
    )
    with patch.object(
        mock_contract_test_inputs_generator,
        "_get_aws_resource_types_list",
        return_value=LIST_TYPES_PAGINATOR_RESPONSE_MOCK_RESOURCE_TYPE,
    ):
        mock_contract_test_inputs_generator.discover_aws_resources()

        assert (
            len(
                mock_contract_test_inputs_generator.discovered_resource_type_names  # noqa: E501
            )
            == 1
        )
        assert (
            mock_contract_test_inputs_generator.discovered_resource_type_names
            == ["AWS::MockResourceName::ForUnitTests"]
        )


def test_given_found_resource_types_when_get_type_names_from_list_types_page_iterator_called_then_discovered_resource_type_names_should_match() -> (  # noqa: E501
    None
):
    mock_cloudformation_client = MagicMock()

    mock_contract_test_inputs_generator = ContractTestInputsGenerator(
        _cloudformation_client=mock_cloudformation_client,
        parent_directory_path=None,
    )
    with patch.object(
        mock_contract_test_inputs_generator,
        "_get_type_names_from_list_types_page_iterator",
        return_value=[
            "AWS::S3::Bucket",
            "AWS::S3::BucketPolicy",
        ],
    ):
        mock_contract_test_inputs_generator.discover_aws_resources()

        assert (
            len(
                mock_contract_test_inputs_generator.discovered_resource_type_names  # noqa: E501
            )
            == 2
        )
        assert (
            mock_contract_test_inputs_generator.discovered_resource_type_names
            == [
                "AWS::S3::Bucket",
                "AWS::S3::BucketPolicy",
            ]
        )


def test_given_get_type_names_from_list_types_page_iterator_called_when_contract_test_inputs_generated_then_inputs_should_match_expected() -> (  # noqa: E501
    None
):
    mock_cloudformation_client = MagicMock()

    mock_contract_test_inputs_generator = ContractTestInputsGenerator(
        _cloudformation_client=mock_cloudformation_client,
        parent_directory_path=None,
    )
    with patch.object(
        mock_contract_test_inputs_generator,
        "_get_type_names_from_list_types_page_iterator",
        return_value=[
            "AWS::S3::Bucket",
            "AWS::S3::BucketPolicy",
        ],
    ):
        mock_contract_test_inputs_generator.discover_aws_resources()
        mock_contract_test_inputs_generator.generate_contract_test_inputs()
        assert (
            mock_contract_test_inputs_generator._inputs_1_pre_create.get(
                "AWS::S3::Bucket"
            )
            == VALID_1_PRE_CREATE_INPUTS
        )
        assert (
            mock_contract_test_inputs_generator._inputs_1_pre_update.get(
                "AWS::S3::Bucket"
            )
            == VALID_1_PRE_UPDATE_INPUTS
        )
        assert (
            mock_contract_test_inputs_generator._inputs_1_pre_delete.get(
                "AWS::S3::Bucket"
            )
            == VALID_1_PRE_DELETE_INPUTS
        )
        assert (
            mock_contract_test_inputs_generator._inputs_1_invalid_pre_create.get(  # noqa: E501
                "AWS::S3::Bucket"
            )
            == INVALID_1_PRE_CREATE_INPUTS
        )
        assert (
            mock_contract_test_inputs_generator._inputs_1_invalid_pre_update.get(  # noqa: E501
                "AWS::S3::Bucket"
            )
            == INVALID_1_PRE_UPDATE_INPUTS
        )
        assert (
            mock_contract_test_inputs_generator._inputs_1_invalid_pre_delete.get(  # noqa: E501
                "AWS::S3::Bucket"
            )
            == INVALID_1_PRE_DELETE_INPUTS
        )


def test_given_generated_contract_test_inputs_when_written_to_disk_then_inputs_should_match_expected() -> (  # noqa: E501
    None
):
    with tempfile.TemporaryDirectory() as temp_contract_test_inputs_dir:
        temp_input_files_path = join_os_paths(
            temp_contract_test_inputs_dir, "inputs"
        )
        os.mkdir(temp_input_files_path)

        mock_cloudformation_client = MagicMock()

        mock_contract_test_inputs_generator = ContractTestInputsGenerator(
            _cloudformation_client=mock_cloudformation_client,
            parent_directory_path=temp_contract_test_inputs_dir,
        )
        with patch.object(
            mock_contract_test_inputs_generator,
            "_get_type_names_from_list_types_page_iterator",
            return_value=[
                "AWS::S3::Bucket",
                "AWS::S3::BucketPolicy",
            ],
        ):
            mock_contract_test_inputs_generator.discover_aws_resources()
            mock_contract_test_inputs_generator.generate_contract_test_inputs()
            mock_contract_test_inputs_generator.write_contract_test_inputs_to_disk()  # noqa: E501

            input_files_to_expected_data = [
                {
                    "input_file": INPUTS_1_PRE_CREATE_FILE,
                    "expected_datum": VALID_1_PRE_CREATE_FILE_CONTENT,
                },
                {
                    "input_file": INPUTS_1_PRE_UPDATE_FILE,
                    "expected_datum": VALID_1_PRE_UPDATE_FILE_CONTENT,
                },
                {
                    "input_file": INPUTS_1_PRE_DELETE_FILE,
                    "expected_datum": VALID_1_PRE_DELETE_FILE_CONTENT,
                },
                {
                    "input_file": INPUTS_1_INVALID_PRE_CREATE_FILE,
                    "expected_datum": INVALID_1_PRE_CREATE_FILE_CONTENT,
                },
                {
                    "input_file": INPUTS_1_INVALID_PRE_UPDATE_FILE,
                    "expected_datum": INVALID_1_PRE_UPDATE_FILE_CONTENT,
                },
                {
                    "input_file": INPUTS_1_INVALID_PRE_DELETE_FILE,
                    "expected_datum": INVALID_1_PRE_DELETE_FILE_CONTENT,
                },
            ]

            for input_file_to_expected_datum in input_files_to_expected_data:
                input_file = str(input_file_to_expected_datum["input_file"])
                expected_datum = input_file_to_expected_datum["expected_datum"]

                generated_file = join_os_paths(
                    temp_contract_test_inputs_dir,
                    input_file,
                )
                assert Path(generated_file).is_file()
                with open(
                    generated_file,
                    mode="r",
                    encoding=CONTRACT_TEST_INPUT_FILES_ENCODING,
                ) as generated_file_read_from_disk:
                    assert (
                        json.loads(
                            generated_file_read_from_disk.read(),
                            object_pairs_hook=OrderedDict,
                        )
                    ) == json.loads(
                        json.dumps(
                            expected_datum,
                            sort_keys=True,
                        ),
                        object_pairs_hook=OrderedDict,
                    )
