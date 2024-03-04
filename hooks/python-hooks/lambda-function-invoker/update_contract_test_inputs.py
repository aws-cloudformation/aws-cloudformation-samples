#!/usr/bin/env python3

"""Update contract test inputs for AWSSamples::LambdaFunctionInvoker::Hook."""


from contract_test_inputs_generator.contract_test_inputs_generator import (
    ContractTestInputsGenerator,
)


def main() -> None:
    """Entry point function for the contract test inputs generator."""
    contract_test_inputs_generator = ContractTestInputsGenerator(
        parent_directory_path=None,
    )

    contract_test_inputs_generator.discover_aws_resources()
    contract_test_inputs_generator.generate_contract_test_inputs()
    contract_test_inputs_generator.write_contract_test_inputs_to_disk()


if __name__ == "__main__":
    main()
