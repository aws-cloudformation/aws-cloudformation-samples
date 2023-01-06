package com.awssamples.ec2instancetypes.hook.supportedtargets;

import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.AwsEc2Launchtemplate;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.AwsEc2LaunchtemplateTargetModel;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.InstanceRequirements;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.LaunchTemplateData;
import com.awssamples.ec2instancetypes.hook.supportedproperties.AwsEc2LaunchTemplateInstanceRequirementsProperty;
import com.awssamples.ec2instancetypes.hook.supportedproperties.AwsEc2LaunchTemplateInstanceTypeProperty;

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

/**
 * This class implements AWS::EC2::LaunchTemplate-related helper methods defined
 * in {@link SupportedTarget}, and consumes validation helper methods defined in
 * interface(s) relevant to supported resource properties, such as
 * {@link AwsEc2LaunchTemplateInstanceTypeProperty}, and
 * {@link AwsEc2LaunchTemplateInstanceRequirementsProperty}.
 */
public final class AwsEc2LaunchTemplateTarget
        implements SupportedTarget, AwsEc2LaunchTemplateInstanceTypeProperty,
        AwsEc2LaunchTemplateInstanceRequirementsProperty {

    private final String typeName = AwsEc2Launchtemplate.TYPE_NAME;

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
            getTargetLaunchTemplateData(hookContext);
        } catch (final NullPointerException nullPointerException) {
            final String failureMessage = String.format(
                    "Failed to verify instance type for target: [%s].  Missing property: LaunchTemplateData.",
                    targetName);
            logger.log(failureMessage);

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .build();
        }

        final String targetInstanceType = getTargetEc2InstanceType(hookContext);
        final InstanceRequirements targetInstanceRequirements = getTargetInstanceRequirements(hookContext);

        final ProgressEvent<HookTargetModel, CallbackContext> validateTargetProperties = validateInstanceTypeAndInstanceRequirementsTargetProperties(
                targetInstanceType,
                targetInstanceRequirements,
                logger);
        if (!validateTargetProperties.getStatus().equals(OperationStatus.IN_PROGRESS)) {
            return validateTargetProperties;
        }

        if (targetInstanceType != null) {
            final ProgressEvent<HookTargetModel, CallbackContext> validateInstanceTypeTargetProperty = validateInstanceTypeTargetProperty(
                    allowedEc2InstanceTypesSet,
                    targetInstanceType,
                    targetName,
                    logger);
            if (!validateInstanceTypeTargetProperty.getStatus().equals(OperationStatus.IN_PROGRESS)) {
                return validateInstanceTypeTargetProperty;
            }
        } else if (targetInstanceRequirements != null) {
            final LaunchTemplateData launchTemplateData = getTargetLaunchTemplateData(hookContext);

            final ProgressEvent<HookTargetModel, CallbackContext> validateInstanceRequirementsTargetProperty = validateInstanceRequirementsTargetProperty(
                    targetInstanceRequirements,
                    proxy,
                    allowedEc2InstanceTypesSet,
                    hookContext,
                    launchTemplateData,
                    logger);
            if (!validateInstanceRequirementsTargetProperty.getStatus().equals(OperationStatus.IN_PROGRESS)) {
                return validateInstanceRequirementsTargetProperty;
            }
        }

        final String successMessage = String.format("Successfully verified instance type(s) for target: [%s].",
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
     * @return AwsEc2Launchtemplate
     */
    @Override
    public final AwsEc2Launchtemplate getResourcePropertiesFromTargetModel(final HookContext hookContext) {
        final ResourceHookTargetModel<AwsEc2Launchtemplate> targetModel = hookContext
                .getTargetModel(AwsEc2LaunchtemplateTargetModel.class);
        return targetModel.getResourceProperties();
    }

    /**
     * Return the instance type from the target's relevant property.
     *
     * @param hookContext HookContext
     * @return String
     */
    public final String getTargetEc2InstanceType(final HookContext hookContext) {
        return getTargetLaunchTemplateData(hookContext).getInstanceType();
    }

    /**
     * Return the LaunchTemplateData property from this resource type.
     *
     * @param hookContext HookContext
     * @return LaunchTemplateData
     */
    public final LaunchTemplateData getTargetLaunchTemplateData(final HookContext hookContext) {
        final AwsEc2Launchtemplate resourceProperties = getResourcePropertiesFromTargetModel(hookContext);
        return resourceProperties.getLaunchTemplateData();
    }

    /**
     * Return the InstanceRequirements property from this resource type.
     *
     * @param hookContext HookContext
     * @return InstanceRequirements
     */
    public final InstanceRequirements getTargetInstanceRequirements(final HookContext hookContext) {
        final AwsEc2Launchtemplate resourceProperties = getResourcePropertiesFromTargetModel(hookContext);
        return resourceProperties.getLaunchTemplateData().getInstanceRequirements();
    }

    /**
     * Validate that either InstanceType or InstanceRequirements are specified.
     *
     * @param targetInstanceType         String
     * @param targetInstanceRequirements InstanceRequirements
     * @param logger                     Logger
     * @return ProgressEvent
     */
    public final ProgressEvent<HookTargetModel, CallbackContext> validateInstanceTypeAndInstanceRequirementsTargetProperties(
            final String targetInstanceType,
            final InstanceRequirements targetInstanceRequirements,
            final Logger logger) {

        if (targetInstanceType == null && targetInstanceRequirements == null) {
            final String failureMessage = "Neither InstanceType nor InstanceRequirements are specified.  Specify one or the other.";
            logger.log(failureMessage);

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .build();
        }

        if (targetInstanceType != null && targetInstanceRequirements != null) {
            final String failureMessage = "Both InstanceType and InstanceRequirements are specified.  Specify one or the other.";
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
