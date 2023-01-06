package com.awssamples.ec2instancetypes.hook.supportedtargets;

import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;
import com.awssamples.ec2instancetypes.hook.model.aws.cloud9.environmentec2.AwsCloud9Environmentec2;
import com.awssamples.ec2instancetypes.hook.model.aws.cloud9.environmentec2.AwsCloud9Environmentec2TargetModel;
import com.awssamples.ec2instancetypes.hook.supportedproperties.AwsCloud9EnvironmentEc2InstanceTypeProperty;

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

/**
 * This class implements AWS::Cloud9::EnvironmentEC2-related helper methods
 * defined in
 * {@link SupportedTarget}, and consumes validation helper methods defined in
 * interface(s) relevant to supported resource properties, such as
 * {@link AwsCloud9EnvironmentEc2InstanceTypeProperty}.
 */
public final class AwsCloud9EnvironmentEc2Target
        implements SupportedTarget, AwsCloud9EnvironmentEc2InstanceTypeProperty {

    private final String typeName = AwsCloud9Environmentec2.TYPE_NAME;

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
        if (targetInstanceType == null) {
            final String failureMessage = String.format(
                    "Failed to verify instance type for target: [%s].  Missing property value: InstanceType.",
                    targetName);
            logger.log(failureMessage);
            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .build();
        }

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
     * @return AwsEc2Instance
     */
    @Override
    public final AwsCloud9Environmentec2 getResourcePropertiesFromTargetModel(final HookContext hookContext) {
        final ResourceHookTargetModel<AwsCloud9Environmentec2> targetModel = hookContext
                .getTargetModel(AwsCloud9Environmentec2TargetModel.class);
        return targetModel.getResourceProperties();
    }

    /**
     * Return the instance type from the target's relevant property.
     *
     * @param hookContext HookContext
     * @return String
     */
    private final String getTargetEc2InstanceType(final HookContext hookContext) {
        final AwsCloud9Environmentec2 resourceProperties = getResourcePropertiesFromTargetModel(hookContext);
        return resourceProperties.getInstanceType();
    }

}
