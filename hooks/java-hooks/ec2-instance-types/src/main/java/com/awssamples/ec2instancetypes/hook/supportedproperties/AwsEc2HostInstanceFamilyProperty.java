package com.awssamples.ec2instancetypes.hook.supportedproperties;

import java.util.Set;
import java.util.stream.Collectors;

import com.awssamples.ec2instancetypes.hook.CallbackContext;

import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * This interface contains AWS::EC2::Host-related helper methods, that are
 * relevant to the validation of the InstanceFamily property.
 */
public interface AwsEc2HostInstanceFamilyProperty {

    /**
     * Validate the InstanceFamily property.
     *
     * @param allowedEc2InstanceTypesSet Set
     * @param targetInstanceFamily       String
     * @param targetName                 String
     * @param logger                     Logger
     * @return ProgressEvent
     */
    default ProgressEvent<HookTargetModel, CallbackContext> validateInstanceFamilyTargetProperty(
            final Set<String> allowedEc2InstanceTypesSet,
            final String targetInstanceFamily,
            final String targetName,
            final Logger logger) {
        final Set<String> allowedEc2InstanceFamiliesSet = allowedEc2InstanceTypesSet.stream()
                .map(t -> t.split("\\.")[0])
                .collect(Collectors.toSet());
        if (!allowedEc2InstanceFamiliesSet.contains(targetInstanceFamily)) {
            final String failureMessage = String.format(
                    "Failed to verify instance family for target: [%s].  Allowed value(s): %s; specified value: [%s].",
                    targetName, allowedEc2InstanceFamiliesSet.toString(), targetInstanceFamily);
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
