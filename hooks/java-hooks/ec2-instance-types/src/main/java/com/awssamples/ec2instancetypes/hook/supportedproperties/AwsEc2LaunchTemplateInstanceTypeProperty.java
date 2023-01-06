package com.awssamples.ec2instancetypes.hook.supportedproperties;

import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;

import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * This interface contains AWS::EC2::LaunchTemplate-related helper methods, that
 * are relevant to the validation of the InstanceType property.
 */
public interface AwsEc2LaunchTemplateInstanceTypeProperty {

    /**
     * Validate the InstanceType property when a default value is not present.
     *
     * @param allowedEc2InstanceTypesSet Set
     * @param targetInstanceType         String
     * @param targetName                 String
     * @param logger                     Logger
     * @return ProgressEvent
     */
    default ProgressEvent<HookTargetModel, CallbackContext> validateInstanceTypeTargetProperty(
            final Set<String> allowedEc2InstanceTypesSet,
            final String targetInstanceType,
            final String targetName,
            final Logger logger) {
        if (!allowedEc2InstanceTypesSet.contains(targetInstanceType)) {
            final String failureMessage = String.format(
                    "Failed to verify instance type for target: [%s].  Allowed value(s): %s; specified value: [%s].",
                    targetName, allowedEc2InstanceTypesSet.toString(), targetInstanceType);
            logger.log(failureMessage);

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.NonCompliant)
                    .build();
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                .status(OperationStatus.IN_PROGRESS)
                .build();
    }

}
