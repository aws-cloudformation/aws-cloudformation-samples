package com.awssamples.ec2instancetypes.hook.supportedtargets;

import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.capacityreservation.AwsEc2Capacityreservation;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.capacityreservation.AwsEc2CapacityreservationTargetModel;
import com.awssamples.ec2instancetypes.hook.supportedproperties.AwsEc2CapacityReservationInstanceTypeProperty;

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

/**
 * This class implements AWS::EC2::CapacityReservation-related helper methods
 * defined in {@link SupportedTarget}, and consumes validation helper methods
 * defined in interface(s) relevant to supported resource properties, such as
 * {@link AwsEc2CapacityReservationInstanceTypeProperty}.
 */
public final class AwsEc2CapacityReservationTarget
        implements SupportedTarget, AwsEc2CapacityReservationInstanceTypeProperty {

    private final String typeName = AwsEc2Capacityreservation.TYPE_NAME;

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
        final String targetInstanceType = getTargetEc2InstanceType(hookContext);

        final ProgressEvent<HookTargetModel, CallbackContext> validateInstanceTypeTargetProperty = validateInstanceTypeTargetProperty(
                allowedEc2InstanceTypesSet,
                targetInstanceType,
                targetName,
                logger);
        if (!validateInstanceTypeTargetProperty.getStatus().equals(OperationStatus.IN_PROGRESS)) {
            return validateInstanceTypeTargetProperty;
        }

        final String successMessage = String.format(
                "Successfully verified instance type for target: [%s].",
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
     * @return AwsEc2Capacityreservation
     */
    @Override
    public final AwsEc2Capacityreservation getResourcePropertiesFromTargetModel(final HookContext hookContext) {
        final ResourceHookTargetModel<AwsEc2Capacityreservation> targetModel = hookContext
                .getTargetModel(AwsEc2CapacityreservationTargetModel.class);
        return targetModel.getResourceProperties();
    }

    /**
     * Return the instance type from the target's relevant property.
     *
     * @param hookContext HookContext
     * @return String
     */
    private final String getTargetEc2InstanceType(final HookContext hookContext) {
        final AwsEc2Capacityreservation resourceProperties = getResourcePropertiesFromTargetModel(hookContext);
        return resourceProperties.getInstanceType();
    }

}
