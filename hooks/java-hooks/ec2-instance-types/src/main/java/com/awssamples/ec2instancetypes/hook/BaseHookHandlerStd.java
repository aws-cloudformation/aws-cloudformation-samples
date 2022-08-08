package com.awssamples.ec2instancetypes.hook;

import static com.awssamples.ec2instancetypes.hook.HookInputConfigValidationHelpers.cleanupHookInput;
import static com.awssamples.ec2instancetypes.hook.HookInputConfigValidationHelpers.validateHookInputFormat;
import static com.awssamples.ec2instancetypes.hook.HookInputConfigValidationHelpers.validateHookInputIsNotNull;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

import com.awssamples.ec2instancetypes.hook.supportedtargets.AwsEc2InstanceTarget;
import com.awssamples.ec2instancetypes.hook.supportedtargets.AwsEc2LaunchTemplateTarget;

import org.apache.commons.lang3.exception.ExceptionUtils;

import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * This class is used for common pre-create and pre-update operations with this
 * hook.
 */
public abstract class BaseHookHandlerStd extends BaseHookHandler<CallbackContext, TypeConfigurationModel> {

    /**
     * Define supported types for this hook.
     */
    private static final Set<String> SUPPORTED_TARGETS = new HashSet<String>(
            Arrays.asList(
                    new String[] {
                            new AwsEc2InstanceTarget().getTypeName(),
                            new AwsEc2LaunchTemplateTarget().getTypeName(),
                    }));

    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> handleRequest(
            final AmazonWebServicesClientProxy proxy,
            final HookHandlerRequest request,
            final CallbackContext callbackContext,
            final Logger logger,
            final TypeConfigurationModel typeConfiguration) {
        return handleRequest(
                proxy,
                request,
                callbackContext != null ? callbackContext : new CallbackContext(),
                logger,
                typeConfiguration);
    }

    /**
     * Run operations common to pre-create and pre-update phases for this hook.
     *
     * @param proxy             AmazonWebServicesClientProxy
     * @param request           HookHandlerRequest
     * @param callbackContext   CallbackContext
     * @param logger            Logger
     * @param typeConfiguration TypeConfigurationModel
     * @return ProgressEvent<HookTargetModel, CallbackContext>
     */
    protected ProgressEvent<HookTargetModel, CallbackContext> preCreatePreUpdateOperations(
            final AmazonWebServicesClientProxy proxy,
            final HookHandlerRequest request,
            final CallbackContext callbackContext,
            final Logger logger,
            final TypeConfigurationModel typeConfiguration) {
        final HookContext hookContext = request.getHookContext();
        final String targetName = hookContext.getTargetName();

        if (!SUPPORTED_TARGETS.contains(targetName)) {
            throw new UnsupportedTargetException(targetName);
        }
        try {
            final ProgressEvent<HookTargetModel, CallbackContext> validateHookInputIsNotNull = validateHookInputIsNotNull(
                    typeConfiguration.getEC2InstanceTypes());
            if (!validateHookInputIsNotNull.getStatus().equals(OperationStatus.IN_PROGRESS)) {
                return validateHookInputIsNotNull;
            }

            final String allowedEc2InstanceTypesString = cleanupHookInput(typeConfiguration.getEC2InstanceTypes());

            final ProgressEvent<HookTargetModel, CallbackContext> validateHookInputFormat = validateHookInputFormat(
                    allowedEc2InstanceTypesString);
            if (!validateHookInputFormat.getStatus().equals(OperationStatus.IN_PROGRESS)) {
                return validateHookInputFormat;
            }

            /*
             * Build a Set containing EC2 instance type values specified by the user in this
             * hook's configuration. Use this Set to validate configurations specified in
             * the input CloudFormation template's data.
             */
            final Set<String> allowedEc2InstanceTypesSet = new HashSet<String>(
                    Arrays.asList(allowedEc2InstanceTypesString.split(",")));

            ProgressEvent<HookTargetModel, CallbackContext> validationResult = null;

            if (targetName.equals(new AwsEc2InstanceTarget().getTypeName())) {
                // Handle the case of the AWS::EC2::Instance resource type target.
                validationResult = new AwsEc2InstanceTarget().validateTarget(
                        proxy,
                        allowedEc2InstanceTypesSet,
                        hookContext,
                        logger,
                        targetName);
            } else if (targetName.equals(new AwsEc2LaunchTemplateTarget().getTypeName())) {
                // Handle the case of the AWS::EC2::LaunchTemplate resource type target.
                validationResult = new AwsEc2LaunchTemplateTarget().validateTarget(
                        proxy,
                        allowedEc2InstanceTypesSet,
                        hookContext,
                        logger,
                        targetName);
            }
            return validationResult;
        } catch (final Throwable throwable) {
            logger.log(ExceptionUtils.getStackTrace(throwable));
            String messageFromThrowable = "A handler internal failure error has occurred.";
            if (throwable.getMessage() != null) {
                messageFromThrowable += String.format("  %s", throwable.getMessage());
            }
            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(messageFromThrowable)
                    .errorCode(HandlerErrorCode.HandlerInternalFailure)
                    .build();
        }
    }

}
