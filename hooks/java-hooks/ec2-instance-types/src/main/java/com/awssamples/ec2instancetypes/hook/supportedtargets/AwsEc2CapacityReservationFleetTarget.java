package com.awssamples.ec2instancetypes.hook.supportedtargets;

import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.capacityreservationfleet.AwsEc2Capacityreservationfleet;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.capacityreservationfleet.AwsEc2CapacityreservationfleetTargetModel;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.capacityreservationfleet.InstanceTypeSpecification;
import com.awssamples.ec2instancetypes.hook.supportedproperties.AwsEc2CapacityReservationFleetInstanceTypeSpecificationsProperty;

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

/**
 * This class implements AWS::EC2::CapacityReservationFleet-related helper
 * methods defined in {@link SupportedTarget}, and consumes validation helper
 * methods defined in interface(s) relevant to supported resource properties,
 * such as
 * {@link AwsEc2CapacityReservationFleetInstanceTypeSpecificationsProperty}.
 */
public final class AwsEc2CapacityReservationFleetTarget
        implements SupportedTarget, AwsEc2CapacityReservationFleetInstanceTypeSpecificationsProperty {

    private final String typeName = AwsEc2Capacityreservationfleet.TYPE_NAME;

    /**
     * Return the resource type name.
     *
     * @return String
     */
    @Override
    public final String getTypeName() {
        return typeName;
    }

    /**
     * Validate the specified target's configuration.
     *
     * @param proxy                      AmazonWebServicesClientProxy
     * @param allowedEc2InstanceTypesSet Set
     * @param hookContext                HookContext
     * @param logger                     Logger
     * @param targetName                 String
     * @return ProgressEvent
     */
    @Override
    public final ProgressEvent<HookTargetModel, CallbackContext> validateTarget(
            final AmazonWebServicesClientProxy proxy,
            final Set<String> allowedEc2InstanceTypesSet,
            final HookContext hookContext,
            final Logger logger,
            final String targetName) {
        try {
            getTargetInstanceTypeSpecifications(hookContext);
        } catch (final NullPointerException nullPointerException) {
            final String failureMessage = String.format(
                    "Failed to verify instance type(s) for target: [%s].  Missing property: InstanceTypeSpecifications.",
                    targetName);
            logger.log(failureMessage);

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .build();
        }

        final Set<InstanceTypeSpecification> targetInstanceTypeSpecifications = getTargetInstanceTypeSpecifications(
                hookContext);
        if (targetInstanceTypeSpecifications.isEmpty()) {
            final String failureMessage = String.format(
                    "Failed to verify instance type(s) for target: [%s].  The InstanceTypeSpecifications property contains no items.",
                    targetName);
            logger.log(failureMessage);

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .build();
        }

        final ProgressEvent<HookTargetModel, CallbackContext> validateInstanceTypeSpecificationsTargetProperty = validateInstanceTypeSpecificationsTargetProperty(
                allowedEc2InstanceTypesSet,
                targetInstanceTypeSpecifications,
                targetName,
                logger);
        if (!validateInstanceTypeSpecificationsTargetProperty.getStatus().equals(OperationStatus.IN_PROGRESS)) {
            return validateInstanceTypeSpecificationsTargetProperty;
        }

        final String successMessage = String.format(
                "Successfully verified instance type(s) for target: [%s].",
                targetName);

        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                .status(OperationStatus.SUCCESS)
                .message(successMessage)
                .build();
    }

    /**
     * Return resource-specific properties from this hook's context.
     *
     * @param hookContext HookContext
     * @return AwsEc2Capacityreservationfleet
     */
    @Override
    public final AwsEc2Capacityreservationfleet getResourcePropertiesFromTargetModel(final HookContext hookContext) {
        final ResourceHookTargetModel<AwsEc2Capacityreservationfleet> targetModel = hookContext
                .getTargetModel(AwsEc2CapacityreservationfleetTargetModel.class);
        return targetModel.getResourceProperties();
    }

    /**
     * Return instance type specifications from the target's relevant property.
     *
     * @param hookContext HookContext
     * @return Set
     */
    private final Set<InstanceTypeSpecification> getTargetInstanceTypeSpecifications(final HookContext hookContext) {
        final AwsEc2Capacityreservationfleet resourceProperties = getResourcePropertiesFromTargetModel(hookContext);
        return resourceProperties.getInstanceTypeSpecifications();
    }

}
