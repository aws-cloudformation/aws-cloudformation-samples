package com.awssamples.ec2instancetypes.hook.supportedproperties;

import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;
import com.awssamples.ec2instancetypes.hook.ClientBuilder;
import com.awssamples.ec2instancetypes.hook.Translator;

import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.DescribeInstanceAttributeRequest;
import software.amazon.awssdk.services.ec2.model.DescribeInstanceAttributeResponse;
import software.amazon.awssdk.services.ec2.model.InstanceAttributeName;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * This interface contains
 * AWS::AutoScaling::LaunchConfiguration-related helper methods, that
 * are relevant to the validation of the InstanceId property.
 */
public interface AwsAutoScalingLaunchConfigurationInstanceIdProperty {

    /**
     * Validate the InstanceId property.
     *
     * @param proxy                      AmazonWebServicesClientProxy
     * @param allowedEc2InstanceTypesSet Set
     * @param targetInstanceId           String
     * @param targetName                 String
     * @param logger                     Logger
     * @return ProgressEvent
     */
    default ProgressEvent<HookTargetModel, CallbackContext> validateInstanceIdTargetProperty(
            final AmazonWebServicesClientProxy proxy,
            final Set<String> allowedEc2InstanceTypesSet,
            final String targetInstanceId,
            final String targetName,
            final Logger logger) {
        final Ec2Client ec2Client = ClientBuilder.getEc2Client();
        final DescribeInstanceAttributeRequest describeInstanceAttributeRequest = buildDescribeInstanceAttributeRequest(
                targetInstanceId,
                InstanceAttributeName.INSTANCE_TYPE);
        final DescribeInstanceAttributeResponse describeInstanceAttributeResponse = proxy.injectCredentialsAndInvokeV2(
                describeInstanceAttributeRequest,
                ec2Client::describeInstanceAttribute);

        if (!allowedEc2InstanceTypesSet.contains(describeInstanceAttributeResponse.instanceType().value())) {
            final String failureMessage = String.format(
                    "Failed to verify instance type for target: [%s].  Allowed value(s): %s; specified value: [%s].",
                    targetName, allowedEc2InstanceTypesSet.toString(),
                    describeInstanceAttributeResponse.instanceType().value());
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

    /**
     * Build a DescribeInstanceAttributeRequest with the
     * translateToDescribeInstanceAttributeRequest() Translator.
     *
     * @param targetInstanceId      String
     * @param instanceAttributeName InstanceAttributeName
     * @return DescribeInstanceAttributeRequest
     */
    default DescribeInstanceAttributeRequest buildDescribeInstanceAttributeRequest(
            final String targetInstanceId,
            final InstanceAttributeName instanceAttributeName) {
        return Translator
                .translateToDescribeInstanceAttributeRequest(
                        targetInstanceId,
                        instanceAttributeName);
    }

}
