package com.awssamples.ec2instancetypes.hook.supportedproperties;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;
import com.awssamples.ec2instancetypes.hook.ClientBuilder;
import com.awssamples.ec2instancetypes.hook.Translator;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.InstanceRequirements;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.LaunchTemplateData;

import org.apache.commons.lang3.StringUtils;

import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.GetInstanceTypesFromInstanceRequirementsRequest;
import software.amazon.awssdk.services.ec2.model.GetInstanceTypesFromInstanceRequirementsResponse;
import software.amazon.awssdk.services.ec2.model.InstanceTypeInfoFromInstanceRequirements;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * This interface contains AWS::EC2::LaunchTemplate-related helper methods, that
 * are relevant to the validation of the InstanceRequirements property.
 */
public interface AwsEc2LaunchTemplateInstanceRequirementsProperty {

    /**
     * Validate the InstanceRequirements property.
     *
     * @param targetInstanceRequirements InstanceRequirements
     * @param proxy                      AmazonWebServicesClientProxy
     * @param allowedEc2InstanceTypesSet Set
     * @param hookContext                HookContext
     * @param launchTemplateData         LaunchTemplateData
     * @param logger                     Logger
     * @return ProgressEvent
     */
    default ProgressEvent<HookTargetModel, CallbackContext> validateInstanceRequirementsTargetProperty(
            final InstanceRequirements targetInstanceRequirements,
            final AmazonWebServicesClientProxy proxy,
            final Set<String> allowedEc2InstanceTypesSet,
            final HookContext hookContext,
            final LaunchTemplateData launchTemplateData,
            final Logger logger) {
        if (targetInstanceRequirements.getVCpuCount() == null
                && targetInstanceRequirements.getMemoryMiB() == null) {
            final String failureMessage = "You must specify both VCpuCount and MemoryMiB when using InstanceRequirements.";
            logger.log(failureMessage);

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .build();
        }

        if (targetInstanceRequirements.getVCpuCount().getMin() == null) {
            final String failureMessage = "You must specify an integer minimum value for VCpuCount; specify zero for no minimum limit.";
            logger.log(failureMessage);

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .build();
        }

        if (targetInstanceRequirements.getMemoryMiB().getMin() == null) {
            final String failureMessage = "You must specify an integer minimum value for MemoryMiB; specify zero for no minimum limit.";
            logger.log(failureMessage);

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.InvalidRequest)
                    .build();
        }

        final List<InstanceTypeInfoFromInstanceRequirements> instanceTypeInfoFromInstanceRequirementsList = getInstanceTypesFromInstanceRequirements(
                proxy, hookContext, launchTemplateData);
        final Set<String> instanceTypeInfoFromInstanceRequirementsSet = new HashSet<String>();
        for (final InstanceTypeInfoFromInstanceRequirements instanceType : instanceTypeInfoFromInstanceRequirementsList) {
            instanceTypeInfoFromInstanceRequirementsSet.add(instanceType.instanceType());
        }

        final Set<String> differencesBetweenSets = new HashSet<String>(instanceTypeInfoFromInstanceRequirementsSet);
        differencesBetweenSets.removeAll(allowedEc2InstanceTypesSet);

        if (!differencesBetweenSets.isEmpty()) {
            final String failureMessage = StringUtils.abbreviate(String.format(
                    "Specified instance requirements will result in instance types not allowed by this hook's configuration.  Allowed value(s): %s; resulting value(s): %s.",
                    allowedEc2InstanceTypesSet.toString(), differencesBetweenSets.toString()), 0, 512);
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
     * Return a list of InstanceTypeInfoFromInstanceRequirements based on
     * user-specified input.
     *
     * @param proxy              AmazonWebServicesClientProxy
     * @param hookContext        HookContext
     * @param launchTemplateData LaunchTemplateData,
     * @return List
     */
    default List<InstanceTypeInfoFromInstanceRequirements> getInstanceTypesFromInstanceRequirements(
            final AmazonWebServicesClientProxy proxy,
            final HookContext hookContext,
            final LaunchTemplateData launchTemplateData) {
        String nextToken = null;
        GetInstanceTypesFromInstanceRequirementsResponse getInstanceTypesFromInstanceRequirementsResponse = null;
        final List<InstanceTypeInfoFromInstanceRequirements> instanceTypeInfoFromInstanceRequirements = new ArrayList<InstanceTypeInfoFromInstanceRequirements>();
        final Ec2Client ec2Client = ClientBuilder.getEc2Client();
        do {
            final GetInstanceTypesFromInstanceRequirementsRequest getInstanceTypesFromInstanceRequirementsRequest = buildInstanceTypesFromInstanceRequirementsRequest(
                    launchTemplateData,
                    nextToken);

            getInstanceTypesFromInstanceRequirementsResponse = proxy.injectCredentialsAndInvokeV2(
                    getInstanceTypesFromInstanceRequirementsRequest,
                    ec2Client::getInstanceTypesFromInstanceRequirements);

            instanceTypeInfoFromInstanceRequirements
                    .addAll(getInstanceTypesFromInstanceRequirementsResponse.instanceTypes());

            nextToken = getInstanceTypesFromInstanceRequirementsResponse.nextToken();
        } while (nextToken != null);

        return instanceTypeInfoFromInstanceRequirements;
    }

    /**
     * Build a GetInstanceTypesFromInstanceRequirementsRequest with the
     * translateToGetInstanceTypesFromInstanceRequirementsRequest() Translator.
     *
     * @param launchTemplateData LaunchTemplateData
     * @param nextToken          String
     * @return GetInstanceTypesFromInstanceRequirementsRequest
     */
    default GetInstanceTypesFromInstanceRequirementsRequest buildInstanceTypesFromInstanceRequirementsRequest(
            final LaunchTemplateData launchTemplateData,
            final String nextToken) {
        return Translator
                .translateToGetInstanceTypesFromInstanceRequirementsRequest(
                        launchTemplateData,
                        nextToken);
    }

}
