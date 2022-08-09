package com.awssamples.ec2instancetypes.hook;

import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * This class contains helper methods to validate this hook's input
 * configuration.
 */
class HookInputConfigValidationHelpers {

    /**
     * Validates that the hook configuration is not null.
     *
     * @param allowedEc2InstanceTypesConfig String
     * @return ProgressEvent<HookTargetModel, CallbackContext>
     */
    protected static ProgressEvent<HookTargetModel, CallbackContext> validateHookInputIsNotNull(
            final String allowedEc2InstanceTypesConfig) {
        if (allowedEc2InstanceTypesConfig == null) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message("No EC2 instance types specified in the hook configuration.")
                    .errorCode(HandlerErrorCode.InvalidTypeConfiguration)
                    .build();
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                .status(OperationStatus.IN_PROGRESS)
                .build();
    }

    /**
     * Removes spaces, contiguous and trailing commas from this hook's
     * user-specified input configuration.
     *
     * @param allowedEc2InstanceTypes String
     * @return String
     */
    protected static String cleanupHookInput(final String allowedEc2InstanceTypes) {
        return allowedEc2InstanceTypes
                .replaceAll("\\s", "")
                .replaceAll("[,]+", ",")
                .replaceAll(",$", "");
    }

    /**
     * Validate this hook's user-specified input format against a regex pattern.
     *
     * @param allowedEc2InstanceTypes String
     * @return ProgressEvent<HookTargetModel, CallbackContext>
     */
    protected static ProgressEvent<HookTargetModel, CallbackContext> validateHookInputFormat(
            final String allowedEc2InstanceTypes) {
        if (!allowedEc2InstanceTypes.matches("^([a-z0-9-]+\\.[a-z0-9]+)(,[a-z0-9-]+\\.[a-z0-9]+)*$")) {
            final String failureMessage = "This hook's input configuration should contain one or more values representing EC2 instance type name patterns, delimited by commas.";
            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.InvalidTypeConfiguration)
                    .build();
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                .status(OperationStatus.IN_PROGRESS)
                .build();
    }

}
