import logging
from typing import Any, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
    exceptions,
)

from .models import HookHandlerRequest, TypeConfigurationModel

REQUIRED_CONDITION_TYPE = "Bool"
REQUIRED_CONDITION_KEY = "aws:MultiFactorAuthPresent"
REQUIRED_CONDITION_VALUE = "true"

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AWSSamples::IamPoliciesRequireMfa::Hook"

LOG.setLevel(logging.INFO)

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint


def _validate_iam_statement_encryption(policy_name: str, statement: dict) -> ProgressEvent:
    status = None
    message = ""
    error_code = HandlerErrorCode.NonCompliant

    if 'Condition' in statement:
        condition = statement['Condition']

        if REQUIRED_CONDITION_TYPE in condition:
            condition_type = condition[REQUIRED_CONDITION_TYPE]

            if REQUIRED_CONDITION_KEY in condition_type:
                condition_value = condition_type[REQUIRED_CONDITION_KEY]

                if condition_value == REQUIRED_CONDITION_VALUE:
                    status = OperationStatus.SUCCESS
                    message = f"Expected condition type {REQUIRED_CONDITION_TYPE} with key {REQUIRED_CONDITION_KEY} and value {REQUIRED_CONDITION_VALUE} found for statement in policy with name: {policy_name}"
                else:
                    status = OperationStatus.FAILED
                    message = f"{REQUIRED_CONDITION_KEY} value ({condition_value}) is incorrect for a statement in policy with name: {policy_name}"
            else:
                status = OperationStatus.FAILED
                message = f"{REQUIRED_CONDITION_KEY} condtion key not present for a statement in policy with name: {policy_name}"
        else:
            status = OperationStatus.FAILED
            message = f"Expected condition type {REQUIRED_CONDITION_TYPE} not found for a statement in policy with name: {policy_name}"

    else:
        status = OperationStatus.FAILED
        message = f"No conditions present for a statement in policy with name: {policy_name}"

    return ProgressEvent(
        status=status,
        message=message,
        errorCode=error_code
    )


def _validate_iam_policy_encryption(policy: MutableMapping[str, Any]) -> ProgressEvent:
    status = None
    message = ""
    error_code = None

    if policy:
        policy_name = policy.get("PolicyName")
        policy_document = policy.get("PolicyDocument")
        LOG.info('Policy Document: %s' % policy_document)

        if policy_document:
            statements = policy_document['Statement'];

            if statements:
                statement_results = []

                for statement in statements:
                    statement_results.append(_validate_iam_statement_encryption(policy_name, statement))

                for result in statement_results:
                    if result.status == OperationStatus.FAILED:
                        return result

                return ProgressEvent(
                    status=OperationStatus.SUCCESS,
                    message=f"Expected condition type {REQUIRED_CONDITION_TYPE} with key {REQUIRED_CONDITION_KEY} and value {REQUIRED_CONDITION_VALUE} found for all statements in policy {policy_name}",
                    errorCode=None
                )

            else:
                status = OperationStatus.FAILED
                message = f"No statements in policy with name: {policy_name}"
        else:
            status = OperationStatus.FAILED
            message = f"No policy document in policy with name: {policy_name}"
    else:
        status = OperationStatus.FAILED
        message = "Resource properties for IAM Policy target model are empty"

    if status == OperationStatus.FAILED:
        error_code = HandlerErrorCode.NonCompliant

    return ProgressEvent(
        status=status,
        message=message,
        errorCode=error_code
    )


def _validate_iam_role_policies_encryption(policies: MutableMapping[str, Any]) -> ProgressEvent:
    policy_results = []

    for policy in policies:
        policy_results.append(_validate_iam_policy_encryption(policy))

    LOG.info('Policy Results: %s' % policy_results)
    for result in policy_results:
        if result.status == OperationStatus.FAILED:
            return result

    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        message=f"Expected condition type {REQUIRED_CONDITION_TYPE} with key {REQUIRED_CONDITION_KEY} and value {REQUIRED_CONDITION_VALUE} found for all inline policies in role",
        errorCode=None
    )


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_create_handler(
        _session: Optional[SessionProxy],
        request: HookHandlerRequest,
        _callback_context: MutableMapping[str, Any],
        _type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    target_name = request.hookContext.targetName
    target_model = request.hookContext.targetModel

    if "AWS::IAM::Policy" == target_name:
        response = _validate_iam_policy_encryption(target_model.get("resourceProperties", target_model))
    elif "AWS::IAM::Role" == target_name:
        policies = target_model.get("resourceProperties", target_model).get("Policies")
        if policies:
            response = _validate_iam_role_policies_encryption(policies)
        else:
            response = ProgressEvent(
                status=OperationStatus.SUCCESS,
                message=f"No inline policies in role to validate",
                errorCode=None
            )
    else:
        raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")
    return response
