"""Example Lambda function called by AWSSamples::LambdaFunctionInvoker::Hook."""  # noqa: E501


import logging


# If you choose to invoke the hook for all the invocation points
# (default behavior), and to not set `TargetFilters` for your hook,
# you can define, in the example Lambda function code, for which
# invocation points to run the code in this function. It is important
# to understand that if you choose this method as opposed to target
# filters, the hook will be invoked anyway for all of the AWS resource
# types in your templates across all the invocation points, and you'll
# be billed for all the invocations. To use this feature, comment out
# the line for `HOOK_INVOCATION_POINTS` that corresponds to the
# invocation point you do not want to run. Later on in this example
# code, you'll find a conditional block that will return SUCCESS if
# the current invocation point is something you do not need to
# evaluate on during the current invocation.
HOOK_INVOCATION_POINTS = [
    "CREATE_PRE_PROVISION",
    "UPDATE_PRE_PROVISION",
    "DELETE_PRE_PROVISION",
]

# Add AWS resource type target that this code will evaluate. This
# example function validates if versioning is enabled for an S3
# bucket; hence, add AWS::S3::Bucket here.
TARGET_NAMES = [
    "AWS::S3::Bucket",
]

# Define a logger to use with Amazon CloudWatch Logs when this
# function is invoked.
LOGGER = logging.getLogger()

# Set the logging level; use INFO for normal operation.
LOGGER.setLevel("INFO")


def lambda_handler(event, context):
    """Define the entry point of the function."""
    try:
        # Get the entire request from the input event.
        request = event["request"]

        # Get the invocation point for the hook that is calling this
        # function; for example: `CREATE_PRE_PROVISION`.
        invocation_point = request["hookContext"]["invocationPoint"]
        LOGGER.info(f"Invocation point: {invocation_point}")

        # Get the name of the resource type target that invoked the
        # hook. For example: `AWS::S3::Bucket`.
        target_name = request["hookContext"]["targetName"]
        LOGGER.info(f"Target name: {target_name}")

        # If you're not using TargetFilters for the hook that invokes
        # this function, return SUCCESS immediately if you do not want
        # to perform policy-as-code validation for a given hook
        # invocation point that is commented out in
        # HOOK_INVOCATION_POINTS at the beginning of this code, or for
        # target names you've not added to TARGET_NAMES above.
        if (
            invocation_point not in HOOK_INVOCATION_POINTS
            or target_name not in TARGET_NAMES
        ):
            message = (
                f"Skipping {target_name} evaluation for {invocation_point}."
            )
            LOGGER.info(message)
            payload = {
                "status": "SUCCESS",
                "errorCode": None,
                "message": message,
                "callbackContext": None,
                "callbackDelaySeconds": 0,
            }
            LOGGER.debug(payload)
            return payload

        # Get the model of the resource type target.
        target_model = request["hookContext"]["targetModel"]

        # Get the resource properties of the target resource type.
        # This should include the properties for the target resource
        # type that the user specified in their CloudFormation
        # template.
        resource_properties = (
            target_model.get("resourceProperties")
            if target_model and target_model.get("resourceProperties")
            else None
        )
        LOGGER.debug(f"Resource properties: {resource_properties}")

        # The code below needs to validate not only if `Status` for
        # `VersioningConfiguration` is set to `Enabled`, but also if
        # all the other parent properties are present in the template.
        versioning_configuration = (
            resource_properties.get("VersioningConfiguration")
            if resource_properties
            and resource_properties.get("VersioningConfiguration")
            else None
        )
        versioning_configuration_status = (
            versioning_configuration.get("Status")
            if versioning_configuration
            and versioning_configuration.get("Status")
            else None
        )
        if (
            not resource_properties
            or not versioning_configuration
            or not versioning_configuration_status
            or not versioning_configuration_status == "Enabled"
        ):
            message = "Versioning not set or not enabled for the S3 bucket."
            LOGGER.error(message)
            # Return FAILED to the hook, using a payload format that
            # the hook expects once Lambda will serialize it in the
            # response: a dictionary that contains information on
            # status, error code, message, callback context, and
            # callback delay in seconds. This format is modeled after
            # a `ProgressEvent` object:
            # https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-progressevent.html
            payload = {
                "status": "FAILED",
                "errorCode": "NonCompliant",
                "message": message,
                "callbackContext": None,
                "callbackDelaySeconds": 0,
            }
        else:
            # Return success if the resource is compliant.
            message = "Versioning is enabled for the S3 bucket."
            LOGGER.info(message)
            payload = {
                "status": "SUCCESS",
                "errorCode": None,
                "message": message,
                "callbackContext": None,
                "callbackDelaySeconds": 0,
            }

        LOGGER.debug(payload)
        return payload
    except Exception as exception:
        # Default fallback to FAILED in the event of other errors.
        message = str(exception)
        payload = {
            "status": "FAILED",
            "errorCode": "InternalError",
            "message": message,
            "callbackContext": None,
            "callbackDelaySeconds": 0,
        }
        LOGGER.error(message)
        return payload
