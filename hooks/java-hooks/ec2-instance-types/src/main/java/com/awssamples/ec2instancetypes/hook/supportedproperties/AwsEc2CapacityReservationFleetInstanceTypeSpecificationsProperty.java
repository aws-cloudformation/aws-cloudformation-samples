package com.awssamples.ec2instancetypes.hook.supportedproperties;

import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.capacityreservationfleet.InstanceTypeSpecification;

import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * This interface contains AWS::EC2::CapacityReservationFleet-related helper
 * methods, that are relevant to the validation of the InstanceType property.
 */
public interface AwsEc2CapacityReservationFleetInstanceTypeSpecificationsProperty {

    /**
     * Validate the InstanceType property when a default value is not present.
     *
     * @param allowedEc2InstanceTypesSet      Set
     * @param targetInstanceTypeSpecification Set
     * @param targetName                      String
     * @param logger                          Logger
     * @return ProgressEvent
     */
    default ProgressEvent<HookTargetModel, CallbackContext> validateInstanceTypeSpecificationsTargetProperty(
            final Set<String> allowedEc2InstanceTypesSet,
            final Set<InstanceTypeSpecification> targetInstanceTypeSpecification,
            final String targetName,
            final Logger logger) {
        String targetInstanceType = null;
        for (final InstanceTypeSpecification instanceTypeSpecification : targetInstanceTypeSpecification) {
            targetInstanceType = instanceTypeSpecification.getInstanceType();
            if (targetInstanceType == null) {
                final String failureMessage = String.format(
                        "Failed to verify instance type(s) for target: [%s].  Missing InstanceType for an item in the InstanceTypeSpecifications list of properties.",
                        targetName);
                logger.log(failureMessage);

                return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                        .status(OperationStatus.FAILED)
                        .message(failureMessage)
                        .errorCode(HandlerErrorCode.InvalidRequest)
                        .build();
            }

            if (!allowedEc2InstanceTypesSet.contains(targetInstanceType)) {
                final String failureMessage = String.format(
                        "Failed to verify instance type(s) for target: [%s] while inspecting InstanceType for an item in the InstanceTypeSpecifications list of properties.  Allowed value(s): %s; specified value: [%s].",
                        targetName, allowedEc2InstanceTypesSet.toString(), targetInstanceType);
                logger.log(failureMessage);

                return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                        .status(OperationStatus.FAILED)
                        .message(failureMessage)
                        .errorCode(HandlerErrorCode.NonCompliant)
                        .build();
            }
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                .status(OperationStatus.IN_PROGRESS)
                .build();
    }

}
