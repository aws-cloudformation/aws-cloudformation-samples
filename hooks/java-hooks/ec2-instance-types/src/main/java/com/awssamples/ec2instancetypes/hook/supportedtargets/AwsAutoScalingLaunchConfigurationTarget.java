package com.awssamples.ec2instancetypes.hook.supportedtargets;

import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;
import com.awssamples.ec2instancetypes.hook.model.aws.autoscaling.launchconfiguration.AwsAutoscalingLaunchconfiguration;
import com.awssamples.ec2instancetypes.hook.model.aws.autoscaling.launchconfiguration.AwsAutoscalingLaunchconfigurationTargetModel;
import com.awssamples.ec2instancetypes.hook.supportedproperties.AwsAutoScalingLaunchConfigurationInstanceIdProperty;
import com.awssamples.ec2instancetypes.hook.supportedproperties.AwsAutoScalingLaunchConfigurationInstanceTypeProperty;

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

/**
 * This class implements AWS::AutoScaling::LaunchConfiguration-related
 * helper methods defined in {@link SupportedTarget}, and consumes
 * validation helper methods defined in interface(s) relevant to
 * supported resource properties, such as
 * {@link AwsAutoScalingLaunchConfigurationInstanceTypeProperty} and
 * {@link AwsAutoScalingLaunchConfigurationInstanceIdProperty}.
 */
public final class AwsAutoScalingLaunchConfigurationTarget
        implements SupportedTarget, AwsAutoScalingLaunchConfigurationInstanceTypeProperty,
        AwsAutoScalingLaunchConfigurationInstanceIdProperty {

    private final String typeName = AwsAutoscalingLaunchconfiguration.TYPE_NAME;

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
        final String targetInstanceId = getTargetInstanceId(hookContext);

        final ProgressEvent<HookTargetModel, CallbackContext> validateTargetProperties = validateInstanceTypeAndInstanceIdTargetProperties(
                targetInstanceType,
                targetInstanceId,
                logger);
        if (!validateTargetProperties.getStatus().equals(OperationStatus.IN_PROGRESS)) {
            return validateTargetProperties;
        }

        /*
         * Reflecting the intent described in this page [1], whereas
         * the InstanceType property is not required with InstanceId
         * specified. The intent for InstanceId described on this page
         * [2] is to inherit all properties except BlockDeviceMapping
         * and AssociatePublicIpAddress, and to override inherited
         * properties as needed.
         */
        // [1]
        // https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-instancetype
        // [2]
        // https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-launchconfiguration.html#cfn-autoscaling-launchconfiguration-instanceid
        if (targetInstanceId != null && targetInstanceType == null) {
            final ProgressEvent<HookTargetModel, CallbackContext> validateInstanceIdTargetProperty = validateInstanceIdTargetProperty(
                    proxy,
                    allowedEc2InstanceTypesSet,
                    targetInstanceId,
                    targetName,
                    logger);
            if (!validateInstanceIdTargetProperty.getStatus().equals(OperationStatus.IN_PROGRESS)) {
                return validateInstanceIdTargetProperty;
            }
        } else if (targetInstanceType != null) {
            final ProgressEvent<HookTargetModel, CallbackContext> validateInstanceTypeTargetProperty = validateInstanceTypeTargetProperty(
                    allowedEc2InstanceTypesSet,
                    targetInstanceType,
                    targetName,
                    logger);
            if (!validateInstanceTypeTargetProperty.getStatus().equals(OperationStatus.IN_PROGRESS)) {
                return validateInstanceTypeTargetProperty;
            }
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
     * @return AwsAutoscalingLaunchconfiguration
     */
    @Override
    public final AwsAutoscalingLaunchconfiguration getResourcePropertiesFromTargetModel(final HookContext hookContext) {
        final ResourceHookTargetModel<AwsAutoscalingLaunchconfiguration> targetModel = hookContext
                .getTargetModel(AwsAutoscalingLaunchconfigurationTargetModel.class);
        return targetModel.getResourceProperties();
    }

    /**
     * Return the instance type from the target's relevant property.
     *
     * @param hookContext HookContext
     * @return String
     */
    private final String getTargetEc2InstanceType(final HookContext hookContext) {
        final AwsAutoscalingLaunchconfiguration resourceProperties = getResourcePropertiesFromTargetModel(hookContext);
        return resourceProperties.getInstanceType();
    }

    /**
     * Return the instance ID from the target's relevant property.
     *
     * @param hookContext HookContext
     * @return String
     */
    private final String getTargetInstanceId(final HookContext hookContext) {
        final AwsAutoscalingLaunchconfiguration resourceProperties = getResourcePropertiesFromTargetModel(hookContext);
        return resourceProperties.getInstanceId();
    }

    /**
     * Return an error if both InstanceType and InstanceId are not specified.
     *
     * @param targetInstanceType String
     * @param targetInstanceId   String
     * @param logger             Logger
     * @return ProgressEvent
     */
    public final ProgressEvent<HookTargetModel, CallbackContext> validateInstanceTypeAndInstanceIdTargetProperties(
            final String targetInstanceType,
            final String targetInstanceId,
            final Logger logger) {

        if (targetInstanceType == null && targetInstanceId == null) {
            final String failureMessage = "Neither InstanceType nor InstanceId are specified.  Specify one or both.";
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
