package com.awssamples.ec2instancetypes.hook;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatExceptionOfType;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import com.awssamples.ec2instancetypes.hook.model.aws.ec2.capacityreservationfleet.InstanceTypeSpecification;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.AcceleratorCount;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.AcceleratorTotalMemoryMiB;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.BaselineEbsBandwidthMbps;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.InstanceRequirements;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.MemoryGiBPerVCpu;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.MemoryMiB;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.NetworkInterfaceCount;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.TotalLocalStorageGB;
import com.awssamples.ec2instancetypes.hook.model.aws.ec2.launchtemplate.VCpuCount;

import org.junit.jupiter.api.Test;

import software.amazon.awssdk.services.ec2.model.AcceleratorManufacturer;
import software.amazon.awssdk.services.ec2.model.AcceleratorName;
import software.amazon.awssdk.services.ec2.model.AcceleratorType;
import software.amazon.awssdk.services.ec2.model.AttributeValue;
import software.amazon.awssdk.services.ec2.model.BareMetal;
import software.amazon.awssdk.services.ec2.model.BurstablePerformance;
import software.amazon.awssdk.services.ec2.model.CpuManufacturer;
import software.amazon.awssdk.services.ec2.model.DescribeInstanceAttributeResponse;
import software.amazon.awssdk.services.ec2.model.GetInstanceTypesFromInstanceRequirementsResponse;
import software.amazon.awssdk.services.ec2.model.InstanceGeneration;
import software.amazon.awssdk.services.ec2.model.InstanceRequirementsRequest;
import software.amazon.awssdk.services.ec2.model.InstanceTypeInfoFromInstanceRequirements;
import software.amazon.awssdk.services.ec2.model.LocalStorage;
import software.amazon.awssdk.services.ec2.model.LocalStorageType;
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
 * This class is used for common pre-create and pre-update tests for this hook.
 */
public class AbstractTestBase {

    protected final String PRE_CREATE_OPERATION = "PreCreate";
    protected final String PRE_UPDATE_OPERATION = "PreUpdate";

    /**
     * Run common unit test requests for pre-create and pre-update operations for
     * this hook.
     *
     * @param handlerOperation  String
     * @param proxy             AmazonWebServicesClientProxy
     * @param typeConfiguration TypeConfigurationModel
     * @param request           HookHandlerRequest
     * @param logger            Logger
     * @return ProgressEvent
     */
    private ProgressEvent<HookTargetModel, CallbackContext> makeRequestAndGetResponse(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final TypeConfigurationModel typeConfiguration,
            final HookHandlerRequest request,
            final Logger logger) {
        ProgressEvent<HookTargetModel, CallbackContext> response = null;
        if (handlerOperation.equals(PRE_CREATE_OPERATION)) {
            final PreCreateHookHandler handler = new PreCreateHookHandler();
            response = handler.handleRequest(
                    proxy,
                    request,
                    null,
                    logger,
                    typeConfiguration);
        } else if (handlerOperation.equals(PRE_UPDATE_OPERATION)) {
            final PreUpdateHookHandler handler = new PreUpdateHookHandler();
            response = handler.handleRequest(
                    proxy,
                    request,
                    null,
                    logger,
                    typeConfiguration);
        }
        return response;
    }

    /**
     * Validate the resource type is supported.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_unsupportedTarget(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("NON_EXISTENT")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        assertThatExceptionOfType(UnsupportedTargetException.class)
                .isThrownBy(() -> {
                    makeRequestAndGetResponse(
                            handlerOperation,
                            proxy,
                            typeConfiguration,
                            request,
                            logger);
                });
    }

    /**
     * Validate the user input for this hook's configuration.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_missingEc2InstanceTypesInHookConfiguration(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn(null);

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.small");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Instance")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo("No EC2 instance types specified in the hook configuration.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidTypeConfiguration);
    }

    /**
     * Validate a failure event is sent when an exception is caught in the
     * preCreatePreUpdateOperations() method of the BaseHookHandlerStd class.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     * @param handler          BaseHookHandlerStd
     */
    protected void handleRequest_exceptionCaughtInPreCreatePreUpdateOperations(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.micro");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Instance")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();
        when(handler.handleRequest(proxy, request, new CallbackContext(), logger, typeConfiguration))
                .thenThrow(new NullPointerException("Unit test-injected error, testing only."));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(
                proxy,
                request,
                new CallbackContext(),
                logger,
                typeConfiguration);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo("A handler internal failure error has occurred.  Unit test-injected error, testing only.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.HandlerInternalFailure);
    }

    /**
     * Validate a failure event is sent when an exception is caught in the
     * preCreatePreUpdateOperations() method of the BaseHookHandlerStd class. This
     * test is for verifying the output message when the throwable has a null
     * message.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     * @param handler          BaseHookHandlerStd
     */
    protected void handleRequest_exceptionCaughtInPreCreatePreUpdateOperationsNullThrowableMessage(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger,
            final BaseHookHandlerStd handler) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.micro");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Instance")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        when(handler.handleRequest(proxy, request, new CallbackContext(), logger, typeConfiguration))
                .thenThrow(new NullPointerException(null));

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(
                proxy,
                request,
                new CallbackContext(),
                logger,
                typeConfiguration);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo("A handler internal failure error has occurred.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.HandlerInternalFailure);
    }

    /**
     * Validate the input format for this hook's configuration.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_Ec2InstanceTypesInHookConfigurationInvalidFormat(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("invalid format");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.small");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Instance")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "This hook's input configuration should contain one or more values representing EC2 instance type name patterns, delimited by commas.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidTypeConfiguration);
    }

    /**
     * When you do not specify an instance type for AWS::EC2::Instance, this
     * defaults to m1.small: validate this value against the user input
     * configuration.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2Instance_MissingTargetInRequestDefaultInstanceTypeValueMatchFailure(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Instance")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type for target: [AWS::EC2::Instance].  Allowed value(s): [t2.micro]; specified value: [m1.small].  If you have not specified an EC2 instance type, its value defaults to m1.small.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    /**
     * When you do not specify an instance type for AWS::EC2::Instance, this
     * defaults to m1.small: validate this value against the user input
     * configuration.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2Instance_MissingTargetInRequestDefaultInstanceTypeValueMatchSuccess(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro, m1.small");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Instance")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Successfully verified instance type for target: [AWS::EC2::Instance].  If you have not specified an EC2 instance type, its value defaults to m1.small.");
        assertThat(response.getErrorCode()).isNull();
    }

    /**
     * Compliance failure test for AWS::EC2::Instance.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2Instance_Failure(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.small");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Instance")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type for target: [AWS::EC2::Instance].  Allowed value(s): [t2.nano, t2.micro]; specified value: [t2.small].  If you have not specified an EC2 instance type, its value defaults to m1.small.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    /**
     * Compliance success test for AWS::EC2::Instance.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2Instance_Success(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t1.micro,t2.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.micro");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Instance")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Successfully verified instance type for target: [AWS::EC2::Instance].  If you have not specified an EC2 instance type, its value defaults to m1.small.");
        assertThat(response.getErrorCode()).isNull();
    }

    /**
     * Invalid request failure test for AWS::EC2::LaunchTemplate: missing
     * LaunchTemplateData property.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSLaunchTemplate_LaunchTemplateData_Property_Missing(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::LaunchTemplate")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type for target: [AWS::EC2::LaunchTemplate].  Missing property: LaunchTemplateData.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * You need to specify either InstanceType or InstanceRequirements for
     * AWS::EC2::LaunchTemplate.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2LaunchTemplate_NeitherInstanceTypeNorInstanceRequirementsSpecified(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        targetModel.put("ResourceProperties", resourceProperties);

        final Map<String, Object> launchTemplateData = new HashMap<String, Object>();
        launchTemplateData.put("LaunchTemplateData", resourceProperties);
        targetModel.put("ResourceProperties", launchTemplateData);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::LaunchTemplate")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Neither InstanceType nor InstanceRequirements are specified.  Specify one or the other.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * You need to specify either InstanceType or InstanceRequirements for
     * AWS::EC2::LaunchTemplate, and not both.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2LaunchTemplate_BothInstanceTypeAndInstanceRequirementsSpecified(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "test");
        targetModel.put("ResourceProperties", resourceProperties);

        resourceProperties.put("InstanceRequirements", InstanceRequirements.builder().build());
        final Map<String, Object> launchTemplateData = new HashMap<String, Object>();
        launchTemplateData.put("LaunchTemplateData", resourceProperties);
        targetModel.put("ResourceProperties", launchTemplateData);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::LaunchTemplate")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Both InstanceType and InstanceRequirements are specified.  Specify one or the other.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * Compliance failure test for AWS::EC2::LaunchTemplate (InstanceType property).
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2LaunchTemplate_InstanceType_Property_Failure(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> launchTemplateData = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.small");
        launchTemplateData.put("LaunchTemplateData", resourceProperties);
        targetModel.put("ResourceProperties", launchTemplateData);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::LaunchTemplate")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type for target: [AWS::EC2::LaunchTemplate].  Allowed value(s): [t2.nano, t2.micro]; specified value: [t2.small].");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    /**
     * Compliance failure test for AWS::EC2::LaunchTemplate (InstanceRequirements
     * property).
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_Property_Failure(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        final InstanceRequirements instanceRequirements = InstanceRequirements.builder()
                .vCpuCount(VCpuCount.builder().min(1).max(1).build())
                .memoryMiB(MemoryMiB.builder().min(1).max(1).build())
                .acceleratorCount(AcceleratorCount.builder().min(1).max(1).build())
                .acceleratorManufacturers(new ArrayList<String>() {
                    {
                        add(AcceleratorManufacturer.AMAZON_WEB_SERVICES.name());
                    }
                })
                .acceleratorNames(new ArrayList<String>() {
                    {
                        add(AcceleratorName.A100.name());
                    }
                })
                .acceleratorTotalMemoryMiB(AcceleratorTotalMemoryMiB.builder().min(1).max(1).build())
                .acceleratorTypes(new ArrayList<String>() {
                    {
                        add(AcceleratorType.GPU.name());
                    }
                })
                .bareMetal(BareMetal.EXCLUDED.name())
                .baselineEbsBandwidthMbps(BaselineEbsBandwidthMbps.builder().min(1).max(1).build())
                .burstablePerformance(BurstablePerformance.EXCLUDED.name())
                .cpuManufacturers(new ArrayList<String>() {
                    {
                        add(CpuManufacturer.AMAZON_WEB_SERVICES.name());
                    }
                })
                .excludedInstanceTypes(new ArrayList<String>() {
                    {
                        add("m5.8xlarge");
                    }
                })
                .instanceGenerations(new ArrayList<String>() {
                    {
                        add(InstanceGeneration.CURRENT.name());
                    }
                })
                .localStorage(LocalStorage.EXCLUDED.name())
                .localStorageTypes(new ArrayList<String>() {
                    {
                        add(LocalStorageType.SSD.name());
                    }
                })
                .memoryGiBPerVCpu(MemoryGiBPerVCpu.builder().min(1.0).max(1.0).build())
                .networkInterfaceCount(NetworkInterfaceCount.builder().min(1).max(1).build())
                .onDemandMaxPricePercentageOverLowestPrice(20)
                .requireHibernateSupport(true)
                .spotMaxPricePercentageOverLowestPrice(100)
                .totalLocalStorageGB(TotalLocalStorageGB.builder().min(1.0).max(1.0).build())

                .build();

        resourceProperties.put("InstanceRequirements", instanceRequirements);

        final Map<String, Object> launchTemplateData = new HashMap<String, Object>();
        launchTemplateData.put("LaunchTemplateData", resourceProperties);
        targetModel.put("ResourceProperties", launchTemplateData);

        final List<InstanceTypeInfoFromInstanceRequirements> instanceTypeInfoFromInstanceRequirementsList = new ArrayList<InstanceTypeInfoFromInstanceRequirements>();
        instanceTypeInfoFromInstanceRequirementsList.add(
                InstanceTypeInfoFromInstanceRequirements.builder()
                        .instanceType("t2.nano")
                        .build());
        instanceTypeInfoFromInstanceRequirementsList.add(
                InstanceTypeInfoFromInstanceRequirements.builder()
                        .instanceType("t2.micro")
                        .build());
        instanceTypeInfoFromInstanceRequirementsList.add(
                InstanceTypeInfoFromInstanceRequirements.builder()
                        .instanceType("t2.medium")
                        .build());
        instanceTypeInfoFromInstanceRequirementsList.add(
                InstanceTypeInfoFromInstanceRequirements.builder()
                        .instanceType("t2.large")
                        .build());

        when(proxy.injectCredentialsAndInvokeV2(any(), any()))
                .thenReturn(
                        GetInstanceTypesFromInstanceRequirementsResponse.builder()
                                .instanceTypes(instanceTypeInfoFromInstanceRequirementsList).build());

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::LaunchTemplate")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Specified instance requirements will result in instance types not allowed by this hook's configuration.  Allowed value(s): [t2.nano, t2.micro]; resulting value(s): [t2.large, t2.medium].");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    /**
     * Missing required InstanceRequirements properties (VCpuCount and MemoryMiB)
     * when using AWS::EC2::LaunchTemplate.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_Property_Missing_Required_Properties(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        final InstanceRequirements instanceRequirements = InstanceRequirements.builder()
                .build();

        resourceProperties.put("InstanceRequirements", instanceRequirements);

        final Map<String, Object> launchTemplateData = new HashMap<String, Object>();
        launchTemplateData.put("LaunchTemplateData", resourceProperties);
        targetModel.put("ResourceProperties", launchTemplateData);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::LaunchTemplate")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "You must specify both VCpuCount and MemoryMiB when using InstanceRequirements.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * Missing Min for VCpuCount in InstanceRequirements when using
     * AWS::EC2::LaunchTemplate.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_VCpuCount_Missing_Min_Property(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        final InstanceRequirements instanceRequirements = InstanceRequirements.builder()
                .vCpuCount(VCpuCount.builder().build())
                .memoryMiB(MemoryMiB.builder().min(1).max(1).build())

                .build();

        resourceProperties.put("InstanceRequirements", instanceRequirements);

        final Map<String, Object> launchTemplateData = new HashMap<String, Object>();
        launchTemplateData.put("LaunchTemplateData", resourceProperties);
        targetModel.put("ResourceProperties", launchTemplateData);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::LaunchTemplate")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "You must specify an integer minimum value for VCpuCount; specify zero for no minimum limit.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * Missing Min for MemoryMiB in InstanceRequirements when using
     * AWS::EC2::LaunchTemplate.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_MemoryMiB_Missing_Min_Property(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();

        final InstanceRequirements instanceRequirements = InstanceRequirements.builder()
                .vCpuCount(VCpuCount.builder().min(1).max(1).build())
                .memoryMiB(MemoryMiB.builder().build())

                .build();

        resourceProperties.put("InstanceRequirements", instanceRequirements);

        final Map<String, Object> launchTemplateData = new HashMap<String, Object>();
        launchTemplateData.put("LaunchTemplateData", resourceProperties);
        targetModel.put("ResourceProperties", launchTemplateData);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::LaunchTemplate")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "You must specify an integer minimum value for MemoryMiB; specify zero for no minimum limit.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * Compliance success test for AWS::EC2::LaunchTemplate (InstanceType property
     * or InstanceRequirements property).
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2LaunchTemplate_InstanceType_Property_Success(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t1.micro,t2.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> launchTemplateData = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.micro");
        launchTemplateData.put("LaunchTemplateData", resourceProperties);
        targetModel.put("ResourceProperties", launchTemplateData);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::LaunchTemplate")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo("Successfully verified instance type(s) for target: [AWS::EC2::LaunchTemplate].");
        assertThat(response.getErrorCode()).isNull();
    }

    /**
     * Translator test for GetInstanceRequirementsRequest. Test that omitted request
     * parameters for GetInstanceRequirementsRequest result in null or empty values
     * when translated in the request. This is a direct test with the Translator
     * class, and it is not called from mock calls from PreCreateHookHandlerTest and
     * PreUpdateHookHandlerTest.
     */
    @Test
    protected void translateToGetInstanceRequirementsRequest_BuiltRequestOmittedRequestParameters() {
        final InstanceRequirements instanceRequirements = InstanceRequirements.builder()
                .vCpuCount(VCpuCount.builder().min(0).build())
                .memoryMiB(MemoryMiB.builder().min(0).build())

                .build();

        final InstanceRequirementsRequest getInstanceRequirementsRequest = Translator
                .translateToGetInstanceRequirementsRequest(instanceRequirements);

        assertThat(getInstanceRequirementsRequest.vCpuCount().min().equals(0));
        assertThat(getInstanceRequirementsRequest.vCpuCount().max()).isNull();

        assertThat(getInstanceRequirementsRequest.memoryMiB().min().equals(0));
        assertThat(getInstanceRequirementsRequest.memoryMiB().max()).isNull();

        assertThat(getInstanceRequirementsRequest.acceleratorCount()).isNull();
        assertThat(getInstanceRequirementsRequest.acceleratorManufacturers()).isEmpty();
        assertThat(getInstanceRequirementsRequest.acceleratorNames()).isEmpty();
        assertThat(getInstanceRequirementsRequest.acceleratorTotalMemoryMiB()).isNull();
        assertThat(getInstanceRequirementsRequest.acceleratorTypes()).isEmpty();
        assertThat(getInstanceRequirementsRequest.bareMetal()).isNull();
        assertThat(getInstanceRequirementsRequest.baselineEbsBandwidthMbps()).isNull();
        assertThat(getInstanceRequirementsRequest.burstablePerformance()).isNull();
        assertThat(getInstanceRequirementsRequest.cpuManufacturers()).isEmpty();
        assertThat(getInstanceRequirementsRequest.excludedInstanceTypes()).isEmpty();
        assertThat(getInstanceRequirementsRequest.instanceGenerations()).isEmpty();
        assertThat(getInstanceRequirementsRequest.localStorage()).isNull();
        assertThat(getInstanceRequirementsRequest.localStorageTypes()).isEmpty();
        assertThat(getInstanceRequirementsRequest.memoryGiBPerVCpu()).isNull();
        assertThat(getInstanceRequirementsRequest.networkInterfaceCount()).isNull();
        assertThat(getInstanceRequirementsRequest.onDemandMaxPricePercentageOverLowestPrice()).isNull();
        assertThat(getInstanceRequirementsRequest.requireHibernateSupport()).isNull();
        assertThat(getInstanceRequirementsRequest.spotMaxPricePercentageOverLowestPrice()).isNull();
        assertThat(getInstanceRequirementsRequest.totalLocalStorageGB()).isNull();
    }

    /**
     * Translator test for GetInstanceRequirementsRequest. Test that specified
     * request parameters for GetInstanceRequirementsRequest result in expected
     * translated values. This is a direct test with the Translator class, and it is
     * not called from mock calls from PreCreateHookHandlerTest and
     * PreUpdateHookHandlerTest.
     */
    @Test
    protected void translateToGetInstanceRequirementsRequest_BuiltRequestSpecifiedRequestParameters() {
        final InstanceRequirements instanceRequirements = InstanceRequirements.builder()
                .vCpuCount(VCpuCount.builder().min(1).max(1).build())
                .memoryMiB(MemoryMiB.builder().min(1).max(1).build())
                .acceleratorCount(AcceleratorCount.builder().min(1).max(1).build())
                .acceleratorManufacturers(new ArrayList<String>() {
                    {
                        add(AcceleratorManufacturer.AMAZON_WEB_SERVICES.name());
                    }
                })
                .acceleratorNames(new ArrayList<String>() {
                    {
                        add(AcceleratorName.A100.name());
                    }
                })
                .acceleratorTotalMemoryMiB(AcceleratorTotalMemoryMiB.builder().min(1).max(1).build())
                .acceleratorTypes(new ArrayList<String>() {
                    {
                        add(AcceleratorType.GPU.name());
                    }
                })
                .bareMetal(BareMetal.EXCLUDED.name())
                .baselineEbsBandwidthMbps(BaselineEbsBandwidthMbps.builder().min(1).max(1).build())
                .burstablePerformance(BurstablePerformance.EXCLUDED.name())
                .cpuManufacturers(new ArrayList<String>() {
                    {
                        add(CpuManufacturer.AMAZON_WEB_SERVICES.name());
                    }
                })
                .excludedInstanceTypes(new ArrayList<String>() {
                    {
                        add("m5.8xlarge");
                    }
                })
                .instanceGenerations(new ArrayList<String>() {
                    {
                        add(InstanceGeneration.CURRENT.name());
                    }
                })
                .localStorage(LocalStorage.EXCLUDED.name())
                .localStorageTypes(new ArrayList<String>() {
                    {
                        add(LocalStorageType.SSD.name());
                    }
                })
                .memoryGiBPerVCpu(MemoryGiBPerVCpu.builder().min(1.0).max(1.0).build())
                .networkInterfaceCount(NetworkInterfaceCount.builder().min(1).max(1).build())
                .onDemandMaxPricePercentageOverLowestPrice(20)
                .requireHibernateSupport(true)
                .spotMaxPricePercentageOverLowestPrice(100)
                .totalLocalStorageGB(TotalLocalStorageGB.builder().min(1.0).max(1.0).build())

                .build();

        final InstanceRequirementsRequest getInstanceRequirementsRequest = Translator
                .translateToGetInstanceRequirementsRequest(instanceRequirements);

        assertThat(getInstanceRequirementsRequest.vCpuCount().min().equals(1));
        assertThat(getInstanceRequirementsRequest.vCpuCount().max().equals(1));

        assertThat(getInstanceRequirementsRequest.memoryMiB().min().equals(1));
        assertThat(getInstanceRequirementsRequest.memoryMiB().max().equals(1));

        assertThat(getInstanceRequirementsRequest.acceleratorCount().min().equals(1));
        assertThat(getInstanceRequirementsRequest.acceleratorCount().max().equals(1));

        assertThat(getInstanceRequirementsRequest.acceleratorManufacturers()
                .contains(AcceleratorManufacturer.AMAZON_WEB_SERVICES.name()));

        assertThat(getInstanceRequirementsRequest.acceleratorNames().contains(AcceleratorName.A100.name()));

        assertThat(getInstanceRequirementsRequest.acceleratorTotalMemoryMiB().min().equals(1));
        assertThat(getInstanceRequirementsRequest.acceleratorTotalMemoryMiB().max().equals(1));

        assertThat(getInstanceRequirementsRequest.acceleratorTypes().contains(AcceleratorType.GPU.name()));

        assertThat(getInstanceRequirementsRequest.bareMetal().equals(BareMetal.EXCLUDED.name()));

        assertThat(getInstanceRequirementsRequest.baselineEbsBandwidthMbps().min().equals(1));
        assertThat(getInstanceRequirementsRequest.baselineEbsBandwidthMbps().max().equals(1));

        assertThat(getInstanceRequirementsRequest.burstablePerformance().equals(BurstablePerformance.EXCLUDED));

        assertThat(
                getInstanceRequirementsRequest.cpuManufacturers().contains(CpuManufacturer.AMAZON_WEB_SERVICES.name()));

        assertThat(getInstanceRequirementsRequest.excludedInstanceTypes().contains("m5.8xlarge"));

        assertThat(getInstanceRequirementsRequest.instanceGenerations().contains(InstanceGeneration.CURRENT.name()));

        assertThat(getInstanceRequirementsRequest.localStorage().equals(LocalStorage.EXCLUDED));

        assertThat(getInstanceRequirementsRequest.localStorageTypes().contains(LocalStorageType.SSD.name()));

        assertThat(getInstanceRequirementsRequest.memoryGiBPerVCpu().min().equals(1.0));
        assertThat(getInstanceRequirementsRequest.memoryGiBPerVCpu().max().equals(1.0));

        assertThat(getInstanceRequirementsRequest.networkInterfaceCount().min().equals(1));
        assertThat(getInstanceRequirementsRequest.networkInterfaceCount().max().equals(1));

        assertThat(getInstanceRequirementsRequest.onDemandMaxPricePercentageOverLowestPrice().equals(20));

        assertThat(getInstanceRequirementsRequest.requireHibernateSupport()).isTrue();

        assertThat(getInstanceRequirementsRequest.spotMaxPricePercentageOverLowestPrice().equals(100));

        assertThat(getInstanceRequirementsRequest.totalLocalStorageGB().min().equals(1.0));
        assertThat(getInstanceRequirementsRequest.totalLocalStorageGB().max().equals(1.0));
    }

    /**
     * Translator test for GetInstanceRequirementsRequest. Test that specified
     * request parameters for GetInstanceRequirementsRequest result in expected
     * translated values, and that Min values are null in the request if not
     * specified before the translation. This is a direct test with the Translator
     * class, and it is not called from mock calls from PreCreateHookHandlerTest and
     * PreUpdateHookHandlerTest.
     */
    @Test
    protected void translateToGetInstanceRequirementsRequest_BuiltRequestSpecifiedRequestParametersNullMinValues() {
        final InstanceRequirements instanceRequirements = InstanceRequirements.builder()
                .vCpuCount(VCpuCount.builder().max(1).build())
                .memoryMiB(MemoryMiB.builder().max(1).build())
                .acceleratorCount(AcceleratorCount.builder().max(1).build())
                .acceleratorManufacturers(new ArrayList<String>() {
                    {
                        add(AcceleratorManufacturer.AMAZON_WEB_SERVICES.name());
                    }
                })
                .acceleratorNames(new ArrayList<String>() {
                    {
                        add(AcceleratorName.A100.name());
                    }
                })
                .acceleratorTotalMemoryMiB(AcceleratorTotalMemoryMiB.builder().max(1).build())
                .acceleratorTypes(new ArrayList<String>() {
                    {
                        add(AcceleratorType.GPU.name());
                    }
                })
                .bareMetal(BareMetal.EXCLUDED.name())
                .baselineEbsBandwidthMbps(BaselineEbsBandwidthMbps.builder().max(1).build())
                .burstablePerformance(BurstablePerformance.EXCLUDED.name())
                .cpuManufacturers(new ArrayList<String>() {
                    {
                        add(CpuManufacturer.AMAZON_WEB_SERVICES.name());
                    }
                })
                .excludedInstanceTypes(new ArrayList<String>() {
                    {
                        add("m5.8xlarge");
                    }
                })
                .instanceGenerations(new ArrayList<String>() {
                    {
                        add(InstanceGeneration.CURRENT.name());
                    }
                })
                .localStorage(LocalStorage.EXCLUDED.name())
                .localStorageTypes(new ArrayList<String>() {
                    {
                        add(LocalStorageType.SSD.name());
                    }
                })
                .memoryGiBPerVCpu(MemoryGiBPerVCpu.builder().max(1.0).build())
                .networkInterfaceCount(NetworkInterfaceCount.builder().max(1).build())
                .onDemandMaxPricePercentageOverLowestPrice(20)
                .requireHibernateSupport(true)
                .spotMaxPricePercentageOverLowestPrice(100)
                .totalLocalStorageGB(TotalLocalStorageGB.builder().max(1.0).build())

                .build();

        final InstanceRequirementsRequest getInstanceRequirementsRequest = Translator
                .translateToGetInstanceRequirementsRequest(instanceRequirements);

        assertThat(getInstanceRequirementsRequest.vCpuCount().min()).isNull();
        assertThat(getInstanceRequirementsRequest.vCpuCount().max().equals(1));

        assertThat(getInstanceRequirementsRequest.memoryMiB().min()).isNull();
        assertThat(getInstanceRequirementsRequest.memoryMiB().max().equals(1));

        assertThat(getInstanceRequirementsRequest.acceleratorCount().min()).isNull();
        assertThat(getInstanceRequirementsRequest.acceleratorCount().max().equals(1));

        assertThat(getInstanceRequirementsRequest.acceleratorManufacturers()
                .contains(AcceleratorManufacturer.AMAZON_WEB_SERVICES.name()));

        assertThat(getInstanceRequirementsRequest.acceleratorNames().contains(AcceleratorName.A100.name()));

        assertThat(getInstanceRequirementsRequest.acceleratorTotalMemoryMiB().min()).isNull();
        assertThat(getInstanceRequirementsRequest.acceleratorTotalMemoryMiB().max().equals(1));

        assertThat(getInstanceRequirementsRequest.acceleratorTypes().contains(AcceleratorType.GPU.name()));

        assertThat(getInstanceRequirementsRequest.bareMetal().equals(BareMetal.EXCLUDED.name()));

        assertThat(getInstanceRequirementsRequest.baselineEbsBandwidthMbps().min()).isNull();
        assertThat(getInstanceRequirementsRequest.baselineEbsBandwidthMbps().max().equals(1));

        assertThat(getInstanceRequirementsRequest.burstablePerformance().equals(BurstablePerformance.EXCLUDED));

        assertThat(
                getInstanceRequirementsRequest.cpuManufacturers().contains(CpuManufacturer.AMAZON_WEB_SERVICES.name()));

        assertThat(getInstanceRequirementsRequest.excludedInstanceTypes().contains("m5.8xlarge"));

        assertThat(getInstanceRequirementsRequest.instanceGenerations().contains(InstanceGeneration.CURRENT.name()));

        assertThat(getInstanceRequirementsRequest.localStorage().equals(LocalStorage.EXCLUDED));

        assertThat(getInstanceRequirementsRequest.localStorageTypes().contains(LocalStorageType.SSD.name()));

        assertThat(getInstanceRequirementsRequest.memoryGiBPerVCpu().min()).isNull();
        assertThat(getInstanceRequirementsRequest.memoryGiBPerVCpu().max().equals(1.0));

        assertThat(getInstanceRequirementsRequest.networkInterfaceCount().min()).isNull();
        assertThat(getInstanceRequirementsRequest.networkInterfaceCount().max().equals(1));

        assertThat(getInstanceRequirementsRequest.onDemandMaxPricePercentageOverLowestPrice().equals(20));

        assertThat(getInstanceRequirementsRequest.requireHibernateSupport()).isTrue();

        assertThat(getInstanceRequirementsRequest.spotMaxPricePercentageOverLowestPrice().equals(100));

        assertThat(getInstanceRequirementsRequest.totalLocalStorageGB().min()).isNull();
        assertThat(getInstanceRequirementsRequest.totalLocalStorageGB().max().equals(1.0));
    }

    /**
     * Translator test for GetInstanceRequirementsRequest. Test that specified
     * request parameters for GetInstanceRequirementsRequest result in expected
     * translated values, and that Max values are null in the request if not
     * specified before the translation. This is a direct test with the Translator
     * class, and it is not called from mock calls from PreCreateHookHandlerTest and
     * PreUpdateHookHandlerTest.
     */
    @Test
    protected void translateToGetInstanceRequirementsRequest_BuiltRequestSpecifiedRequestParametersNullMaxValues() {
        final InstanceRequirements instanceRequirements = InstanceRequirements.builder()
                .vCpuCount(VCpuCount.builder().min(1).build())
                .memoryMiB(MemoryMiB.builder().min(1).build())
                .acceleratorCount(AcceleratorCount.builder().min(1).build())
                .acceleratorManufacturers(new ArrayList<String>() {
                    {
                        add(AcceleratorManufacturer.AMAZON_WEB_SERVICES.name());
                    }
                })
                .acceleratorNames(new ArrayList<String>() {
                    {
                        add(AcceleratorName.A100.name());
                    }
                })
                .acceleratorTotalMemoryMiB(AcceleratorTotalMemoryMiB.builder().min(1).build())
                .acceleratorTypes(new ArrayList<String>() {
                    {
                        add(AcceleratorType.GPU.name());
                    }
                })
                .bareMetal(BareMetal.EXCLUDED.name())
                .baselineEbsBandwidthMbps(BaselineEbsBandwidthMbps.builder().min(1).build())
                .burstablePerformance(BurstablePerformance.EXCLUDED.name())
                .cpuManufacturers(new ArrayList<String>() {
                    {
                        add(CpuManufacturer.AMAZON_WEB_SERVICES.name());
                    }
                })
                .excludedInstanceTypes(new ArrayList<String>() {
                    {
                        add("m5.8xlarge");
                    }
                })
                .instanceGenerations(new ArrayList<String>() {
                    {
                        add(InstanceGeneration.CURRENT.name());
                    }
                })
                .localStorage(LocalStorage.EXCLUDED.name())
                .localStorageTypes(new ArrayList<String>() {
                    {
                        add(LocalStorageType.SSD.name());
                    }
                })
                .memoryGiBPerVCpu(MemoryGiBPerVCpu.builder().min(1.0).build())
                .networkInterfaceCount(NetworkInterfaceCount.builder().min(1).build())
                .onDemandMaxPricePercentageOverLowestPrice(20)
                .requireHibernateSupport(true)
                .spotMaxPricePercentageOverLowestPrice(100)
                .totalLocalStorageGB(TotalLocalStorageGB.builder().min(1.0).build())

                .build();

        final InstanceRequirementsRequest getInstanceRequirementsRequest = Translator
                .translateToGetInstanceRequirementsRequest(instanceRequirements);

        assertThat(getInstanceRequirementsRequest.vCpuCount().min().equals(1));
        assertThat(getInstanceRequirementsRequest.vCpuCount().max()).isNull();

        assertThat(getInstanceRequirementsRequest.memoryMiB().min().equals(1));
        assertThat(getInstanceRequirementsRequest.memoryMiB().max()).isNull();

        assertThat(getInstanceRequirementsRequest.acceleratorCount().min().equals(1));
        assertThat(getInstanceRequirementsRequest.acceleratorCount().max()).isNull();

        assertThat(getInstanceRequirementsRequest.acceleratorManufacturers()
                .contains(AcceleratorManufacturer.AMAZON_WEB_SERVICES.name()));

        assertThat(getInstanceRequirementsRequest.acceleratorNames().contains(AcceleratorName.A100.name()));

        assertThat(getInstanceRequirementsRequest.acceleratorTotalMemoryMiB().min().equals(1));
        assertThat(getInstanceRequirementsRequest.acceleratorTotalMemoryMiB().max()).isNull();

        assertThat(getInstanceRequirementsRequest.acceleratorTypes().contains(AcceleratorType.GPU.name()));

        assertThat(getInstanceRequirementsRequest.bareMetal().equals(BareMetal.EXCLUDED.name()));

        assertThat(getInstanceRequirementsRequest.baselineEbsBandwidthMbps().min().equals(1));
        assertThat(getInstanceRequirementsRequest.baselineEbsBandwidthMbps().max()).isNull();

        assertThat(getInstanceRequirementsRequest.burstablePerformance().equals(BurstablePerformance.EXCLUDED));

        assertThat(
                getInstanceRequirementsRequest.cpuManufacturers().contains(CpuManufacturer.AMAZON_WEB_SERVICES.name()));

        assertThat(getInstanceRequirementsRequest.excludedInstanceTypes().contains("m5.8xlarge"));

        assertThat(getInstanceRequirementsRequest.instanceGenerations().contains(InstanceGeneration.CURRENT.name()));

        assertThat(getInstanceRequirementsRequest.localStorage().equals(LocalStorage.EXCLUDED));

        assertThat(getInstanceRequirementsRequest.localStorageTypes().contains(LocalStorageType.SSD.name()));

        assertThat(getInstanceRequirementsRequest.memoryGiBPerVCpu().min().equals(1.0));
        assertThat(getInstanceRequirementsRequest.memoryGiBPerVCpu().max()).isNull();

        assertThat(getInstanceRequirementsRequest.networkInterfaceCount().min().equals(1));
        assertThat(getInstanceRequirementsRequest.networkInterfaceCount().max()).isNull();

        assertThat(getInstanceRequirementsRequest.onDemandMaxPricePercentageOverLowestPrice().equals(20));

        assertThat(getInstanceRequirementsRequest.requireHibernateSupport()).isTrue();

        assertThat(getInstanceRequirementsRequest.spotMaxPricePercentageOverLowestPrice().equals(100));

        assertThat(getInstanceRequirementsRequest.totalLocalStorageGB().min().equals(1.0));
        assertThat(getInstanceRequirementsRequest.totalLocalStorageGB().max()).isNull();
    }

    /**
     * Invalid request failure test for AWS::EC2::CapacityReservation: missing
     * InstanceType property.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2CapacityReservation_InstanceType_Property_Missing(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::CapacityReservation")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type for target: [AWS::EC2::CapacityReservation].  Missing value for the InstanceType property.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * Compliance failure test for AWS::EC2::CapacityReservation.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2CapacityReservation_Failure(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.small");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::CapacityReservation")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type for target: [AWS::EC2::CapacityReservation].  Allowed value(s): [t2.nano, t2.micro]; specified value: [t2.small].");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    /**
     * Compliance success test for AWS::EC2::CapacityReservation.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2CapacityReservation_Success(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t1.micro,t2.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.micro");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::CapacityReservation")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Successfully verified instance type for target: [AWS::EC2::CapacityReservation].");
        assertThat(response.getErrorCode()).isNull();
    }

    /**
     * Invalid request failure test for AWS::EC2::CapacityReservationFleet: missing
     * InstanceTypeSpecifications property.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2CapacityReservationFleet_InstanceTypeSpecifications_Property_Missing(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::CapacityReservationFleet")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type(s) for target: [AWS::EC2::CapacityReservationFleet].  Missing property: InstanceTypeSpecifications.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * Invalid request failure test for AWS::EC2::CapacityReservationFleet:
     * InstanceTypeSpecifications property containing no list items.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2CapacityReservationFleet_InstanceTypeSpecifications_Property_Empty(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        final Set<InstanceTypeSpecification> instanceTypeSpecifications = new HashSet<InstanceTypeSpecification>();
        resourceProperties.put("InstanceTypeSpecifications", instanceTypeSpecifications);
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::CapacityReservationFleet")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type(s) for target: [AWS::EC2::CapacityReservationFleet].  The InstanceTypeSpecifications property contains no items.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * Invalid request failure test for AWS::EC2::CapacityReservationFleet:
     * the InstanceType property underneath InstanceTypeSpecifications is missing.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2CapacityReservationFleet_InstanceType_Property_Missing(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        final Set<InstanceTypeSpecification> instanceTypeSpecifications = new HashSet<InstanceTypeSpecification>();
        final InstanceTypeSpecification instanceTypeSpecification = InstanceTypeSpecification.builder()
                .availabilityZone("us-east-2a")
                .build();
        instanceTypeSpecifications.add(instanceTypeSpecification);
        resourceProperties.put("InstanceTypeSpecifications", instanceTypeSpecifications);
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::CapacityReservationFleet")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type(s) for target: [AWS::EC2::CapacityReservationFleet].  Missing InstanceType for an item in the InstanceTypeSpecifications list of properties.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * Compliance failure test for AWS::EC2::CapacityReservationFleet.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2CapacityReservationFleet_InstanceType_Property_For_List_item_Failure(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        final Set<InstanceTypeSpecification> instanceTypeSpecifications = new HashSet<InstanceTypeSpecification>();
        final InstanceTypeSpecification instanceTypeSpecification = InstanceTypeSpecification.builder()
                .availabilityZone("us-east-2a")
                .instancePlatform("Linux/UNIX")
                .instanceType("t2.small")
                .build();
        instanceTypeSpecifications.add(instanceTypeSpecification);
        resourceProperties.put("InstanceTypeSpecifications", instanceTypeSpecifications);
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::CapacityReservationFleet")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type(s) for target: [AWS::EC2::CapacityReservationFleet] while inspecting InstanceType for an item in the InstanceTypeSpecifications list of properties.  Allowed value(s): [t2.nano, t2.micro]; specified value: [t2.small].");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    /**
     * Compliance success test for AWS::EC2::CapacityReservationFleet.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2CapacityReservationFleet_InstanceType_Property_For_List_item_Success(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        final Set<InstanceTypeSpecification> instanceTypeSpecifications = new HashSet<InstanceTypeSpecification>();
        final InstanceTypeSpecification instanceTypeSpecification = InstanceTypeSpecification.builder()
                .availabilityZone("us-east-2a")
                .instancePlatform("Linux/UNIX")
                .instanceType("t2.micro")
                .build();
        instanceTypeSpecifications.add(instanceTypeSpecification);
        resourceProperties.put("InstanceTypeSpecifications", instanceTypeSpecifications);
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::CapacityReservationFleet")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Successfully verified instance type(s) for target: [AWS::EC2::CapacityReservationFleet].");
        assertThat(response.getErrorCode()).isNull();
    }

    /**
     * You need to specify either InstanceType or InstanceFamily for
     * AWS::EC2::Host.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2Host_NeitherInstanceTypeNorInstanceFamilySpecified(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro,t3.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Host")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Neither InstanceType nor InstanceFamily are specified.  Specify one or the other.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * You need to specify either InstanceType or InstanceFamily for
     * AWS::EC2::Host, and not both.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2Host_BothInstanceTypeAndInstanceFamilySpecified(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro,t3.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "test");
        resourceProperties.put("InstanceFamily", "test");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Host")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Both InstanceType and InstanceFamily are specified.  Specify one or the other.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * Compliance failure test for AWS::EC2::Host (InstanceType property).
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2Host_InstanceType_Property_Failure(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro,t3.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t3.small");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Host")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type for target: [AWS::EC2::Host].  Allowed value(s): [t3.micro, t2.micro]; specified value: [t3.small].");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    /**
     * Compliance failure test for AWS::EC2::Host (InstanceFamily property).
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2Host_InstanceFamily_Property_Failure(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro,t3.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceFamily", "m5");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Host")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance family for target: [AWS::EC2::Host].  Allowed value(s): [t2, t3]; specified value: [m5].");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    /**
     * Compliance success test for AWS::EC2::Host (InstanceType property).
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2Host_InstanceType_Property_Success(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro,t3.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t3.micro");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Host")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Successfully verified instance type for target: [AWS::EC2::Host].");
        assertThat(response.getErrorCode()).isNull();
    }

    /**
     * Compliance success test for AWS::EC2::Host (InstanceFamily property).
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSEC2Host_InstanceFamily_Property_Success(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro,t3.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceFamily", "t3");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Host")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Successfully verified instance family for target: [AWS::EC2::Host].");
        assertThat(response.getErrorCode()).isNull();
    }

    /**
     * Validate the InstanceType is not empty for the AWS::Cloud9::EnvironmentEC2
     * resource type.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSCloud9EnvironmentEC2_InstanceType_Property_Missing(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::Cloud9::EnvironmentEC2")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type for target: [AWS::Cloud9::EnvironmentEC2].  Missing property value: InstanceType.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * Compliance failure test for AWS::Cloud9::EnvironmentEC2.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSCloud9EnvironmentEC2_InstanceType_Property_Failure(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "m1.small");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::Cloud9::EnvironmentEC2")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type for target: [AWS::Cloud9::EnvironmentEC2].  Allowed value(s): [t2.micro]; specified value: [m1.small].");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    /**
     * Compliance success test for AWS::Cloud9::EnvironmentEC2.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSCloud9EnvironmentEC2_InstanceType_Property_Success(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.micro");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::Cloud9::EnvironmentEC2")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Successfully verified instance type for target: [AWS::Cloud9::EnvironmentEC2].");
        assertThat(response.getErrorCode()).isNull();
    }

    /**
     * Both InstanceType and InstanceId are missing for
     * AWS::AutoScaling::LaunchConfiguration.
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSAutoScalingLaunchConfiguration_InstanceTypeAndInstanceFamilyNotSpecified(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro,t3.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::AutoScaling::LaunchConfiguration")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Neither InstanceType nor InstanceId are specified.  Specify one or both.");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.InvalidRequest);
    }

    /**
     * Compliance failure test for AWS::AutoScaling::LaunchConfiguration
     * (InstanceType property).
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSAutoScalingLaunchConfiguration_InstanceType_Property_Failure(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro,t3.micro,");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t3.small");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::AutoScaling::LaunchConfiguration")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type for target: [AWS::AutoScaling::LaunchConfiguration].  Allowed value(s): [t3.micro, t2.micro]; specified value: [t3.small].");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    /**
     * Compliance failure test for AWS::AutoScaling::LaunchConfiguration (InstanceId
     * property).
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSAutoScalingLaunchConfiguration_InstanceId_Property_Failure(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceId", "i-1234abcd");
        targetModel.put("ResourceProperties", resourceProperties);

        when(proxy.injectCredentialsAndInvokeV2(any(), any()))
                .thenReturn(
                        DescribeInstanceAttributeResponse.builder()
                                .instanceType(AttributeValue.builder().value("t2.large").build())
                                .build());

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::AutoScaling::LaunchConfiguration")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Failed to verify instance type for target: [AWS::AutoScaling::LaunchConfiguration].  Allowed value(s): [t2.nano, t2.micro]; specified value: [t2.large].");
        assertThat(response.getErrorCode()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    /**
     * Compliance success test for AWS::AutoScaling::LaunchConfiguration
     * (InstanceType property).
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSAutoScalingLaunchConfiguration_InstanceType_Property_Success(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.micro");

        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceType", "t2.micro");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::AutoScaling::LaunchConfiguration")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Successfully verified instance type for target: [AWS::AutoScaling::LaunchConfiguration].");
        assertThat(response.getErrorCode()).isNull();
    }

    /**
     * Compliance success test for AWS::AutoScaling::LaunchConfiguration (InstanceId
     * property).
     *
     * @param handlerOperation String
     * @param proxy            AmazonWebServicesClientProxy
     * @param logger           Logger
     */
    protected void handleRequest_AWSAutoScalingLaunchConfiguration_InstanceId_Property_Success(
            final String handlerOperation,
            final AmazonWebServicesClientProxy proxy,
            final Logger logger) {
        final TypeConfigurationModel typeConfiguration = mock(TypeConfigurationModel.class);
        when(typeConfiguration.getEC2InstanceTypes()).thenReturn("t2.nano,t2.micro,");
        final Map<String, Object> targetModel = new HashMap<String, Object>();
        final Map<String, Object> resourceProperties = new HashMap<String, Object>();
        resourceProperties.put("InstanceId", "i-1234abcd");
        targetModel.put("ResourceProperties", resourceProperties);

        when(proxy.injectCredentialsAndInvokeV2(any(), any()))
                .thenReturn(
                        DescribeInstanceAttributeResponse.builder()
                                .instanceType(AttributeValue.builder().value("t2.micro").build())
                                .build());

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::AutoScaling::LaunchConfiguration")
                        .targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = makeRequestAndGetResponse(
                handlerOperation,
                proxy,
                typeConfiguration,
                request,
                logger);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getMessage())
                .isEqualTo(
                        "Successfully verified instance type for target: [AWS::AutoScaling::LaunchConfiguration].");
        assertThat(response.getErrorCode()).isNull();
    }

}
