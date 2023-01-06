package com.awssamples.ec2instancetypes.hook.supportedtargets;

import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.host.AwsEc2Host;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.host.AwsEc2HostTargetModel;
import com.awssamples.ec2instancetypes.hook.supportedproperties.AwsEc2HostInstanceFamilyProperty;
import com.awssamples.ec2instancetypes.hook.supportedproperties.AwsEc2HostInstanceTypeProperty;

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

/**
 * This class implements AWS::EC2::Host-related helper methods defined
 * in {@link SupportedTarget}, and consumes validation helper methods
 * defined in interface(s) relevant to supported resource properties,
 * such as {@link AwsEc2HostInstanceTypeProperty} and
 * {@link AwsEc2HostInstanceFamilyProperty}.
 */
public final class AwsEc2HostTarget
        implements SupportedTarget, AwsEc2HostInstanceTypeProperty, AwsEc2HostInstanceFamilyProperty {

    private final String typeName = AwsEc2Host.TYPE_NAME;

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
        final String targetInstanceFamily = getTargetInstanceFamily(hookContext);

        final ProgressEvent<HookTargetModel, CallbackContext> validateTargetProperties = validateInstanceTypeAndInstanceFamilyTargetProperties(
                targetInstanceType,
                targetInstanceFamily,
                logger);
        if (!validateTargetProperties.getStatus().equals(OperationStatus.IN_PROGRESS)) {
            return validateTargetProperties;
        }

        String successMessage = "";

        if (targetInstanceType != null) {
            final ProgressEvent<HookTargetModel, CallbackContext> validateInstanceTypeTargetProperty = validateInstanceTypeTargetProperty(
                    allowedEc2InstanceTypesSet,
                    targetInstanceType,
                    targetName,
                    logger);
            if (!validateInstanceTypeTargetProperty.getStatus().equals(OperationStatus.IN_PROGRESS)) {
                return validateInstanceTypeTargetProperty;
            }
            successMessage = String.format(
                    "Successfully verified instance type for target: [%s].",
                    targetName);
        } else if (targetInstanceFamily != null) {
            final ProgressEvent<HookTargetModel, CallbackContext> validateInstanceFamilyTargetProperty = validateInstanceFamilyTargetProperty(
                    allowedEc2InstanceTypesSet,
                    targetInstanceFamily,
                    targetName,
                    logger);
            if (!validateInstanceFamilyTargetProperty.getStatus().equals(OperationStatus.IN_PROGRESS)) {
                return validateInstanceFamilyTargetProperty;
            }
            successMessage = String.format(
                    "Successfully verified instance family for target: [%s].",
                    targetName);
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                .status(OperationStatus.SUCCESS)
                .message(successMessage)
                .build();
    }

    /**
     * Return resource-specific properties from this hook's context.
     *
     * @param hookContext HookContext
     * @return AwsEc2Host
     */
    @Override
    public final AwsEc2Host getResourcePropertiesFromTargetModel(final HookContext hookContext) {
        final ResourceHookTargetModel<AwsEc2Host> targetModel = hookContext
                .getTargetModel(AwsEc2HostTargetModel.class);
        return targetModel.getResourceProperties();
    }

    /**
     * Return the instance type from the target's relevant property.
     *
     * @param hookContext HookContext
     * @return String
     */
    private final String getTargetEc2InstanceType(final HookContext hookContext) {
        final AwsEc2Host resourceProperties = getResourcePropertiesFromTargetModel(hookContext);
        return resourceProperties.getInstanceType();
    }

    /**
     * Return the instance family from the target's relevant property.
     *
     * @param hookContext HookContext
     * @return String
     */
    private final String getTargetInstanceFamily(final HookContext hookContext) {
        final AwsEc2Host resourceProperties = getResourcePropertiesFromTargetModel(hookContext);
        return resourceProperties.getInstanceFamily();
    }

    /**
     * Validate that either InstanceType or InstanceFamily are specified.
     *
     * @param targetInstanceType   String
     * @param targetInstanceFamily String
     * @param logger               Logger
     * @return ProgressEvent
     */
    public final ProgressEvent<HookTargetModel, CallbackContext> validateInstanceTypeAndInstanceFamilyTargetProperties(
            final String targetInstanceType,
            final String targetInstanceFamily,
            final Logger logger) {

        if (targetInstanceType == null && targetInstanceFamily == null) {
            final String failureMessage = "Neither InstanceType nor InstanceFamily are specified.  Specify one or the other.";
            logger.log(failureMessage);

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .build();
        }

        if (targetInstanceType != null && targetInstanceFamily != null) {
            final String failureMessage = "Both InstanceType and InstanceFamily are specified.  Specify one or the other.";
            logger.log(failureMessage);

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .build();
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                .status(OperationStatus.IN_PROGRESS)
                .build();
    }

}
