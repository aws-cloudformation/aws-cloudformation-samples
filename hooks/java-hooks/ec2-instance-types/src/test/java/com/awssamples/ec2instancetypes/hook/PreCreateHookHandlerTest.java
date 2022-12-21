package com.awssamples.ec2instancetypes.hook;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.spy;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.mockito.junit.jupiter.MockitoSettings;
import org.mockito.quality.Strictness;

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;

/**
 * This class is used for calling common test actions in AbstractTestBase.
 */
@ExtendWith(MockitoExtension.class)
public class PreCreateHookHandlerTest extends AbstractTestBase {

    private PreCreateHookHandler handler;

    @Mock
    private AmazonWebServicesClientProxy proxy;

    @Mock
    private Logger logger;

    @BeforeEach
    public void setup() {
        proxy = mock(AmazonWebServicesClientProxy.class);
        logger = mock(Logger.class);
        handler = spy(new PreCreateHookHandler());
    }

    @Test
    @ExtendWith(MockitoExtension.class)
    @MockitoSettings(strictness = Strictness.LENIENT)
    public void handleRequest_unsupportedTarget() {
        handleRequest_unsupportedTarget(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_missingEc2InstanceTypesInHookConfiguration() {
        handleRequest_missingEc2InstanceTypesInHookConfiguration(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_exceptionCaughtInPreCreatePreUpdateOperations() {
        handleRequest_exceptionCaughtInPreCreatePreUpdateOperations(
                PRE_CREATE_OPERATION,
                proxy,
                logger,
                handler);
    }

    @Test
    public void handleRequest_exceptionCaughtInPreCreatePreUpdateOperationsNullThrowableMessage() {
        handleRequest_exceptionCaughtInPreCreatePreUpdateOperationsNullThrowableMessage(
                PRE_CREATE_OPERATION,
                proxy,
                logger,
                handler);
    }

    @Test
    public void handleRequest_Ec2InstanceTypesInHookConfigurationInvalidFormat() {
        handleRequest_Ec2InstanceTypesInHookConfigurationInvalidFormat(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2Instance_MissingTargetInRequestDefaultInstanceTypeValueMatchFailure() {
        handleRequest_AWSEC2Instance_MissingTargetInRequestDefaultInstanceTypeValueMatchFailure(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2Instance_MissingTargetInRequestDefaultInstanceTypeValueMatchSuccess() {
        handleRequest_AWSEC2Instance_MissingTargetInRequestDefaultInstanceTypeValueMatchSuccess(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2Instance_Failure() {
        handleRequest_AWSEC2Instance_Failure(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2Instance_Success() {
        handleRequest_AWSEC2Instance_Success(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSLaunchTemplate_LaunchTemplateData_Property_Missing() {
        handleRequest_AWSLaunchTemplate_LaunchTemplateData_Property_Missing(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2LaunchTemplate_NeitherInstanceTypeNorInstanceRequirementsSpecified() {
        handleRequest_AWSEC2LaunchTemplate_NeitherInstanceTypeNorInstanceRequirementsSpecified(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2LaunchTemplate_BothInstanceTypeAndInstanceRequirementsSpecified() {
        handleRequest_AWSEC2LaunchTemplate_BothInstanceTypeAndInstanceRequirementsSpecified(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_Property_Missing_Required_Properties() {
        handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_Property_Missing_Required_Properties(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2LaunchTemplate_InstanceType_Property_Failure() {
        handleRequest_AWSEC2LaunchTemplate_InstanceType_Property_Failure(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    @MockitoSettings(strictness = Strictness.LENIENT)
    public void handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_Property_Failure() {
        handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_Property_Failure(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    @MockitoSettings(strictness = Strictness.LENIENT)
    public void handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_VCpuCount_Missing_Min_Property() {
        handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_VCpuCount_Missing_Min_Property(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    @MockitoSettings(strictness = Strictness.LENIENT)
    public void handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_MemoryMiB_Missing_Min_Property() {
        handleRequest_AWSEC2LaunchTemplate_InstanceRequirements_MemoryMiB_Missing_Min_Property(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2LaunchTemplate_InstanceType_Property_Success() {
        handleRequest_AWSEC2LaunchTemplate_InstanceType_Property_Success(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2CapacityReservation_InstanceType_Property_Missing() {
        handleRequest_AWSEC2CapacityReservation_InstanceType_Property_Missing(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2CapacityReservation_Failure() {
        handleRequest_AWSEC2CapacityReservation_Failure(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2CapacityReservation_Success() {
        handleRequest_AWSEC2CapacityReservation_Success(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2CapacityReservationFleet_InstanceTypeSpecifications_Property_Missing() {
        handleRequest_AWSEC2CapacityReservationFleet_InstanceTypeSpecifications_Property_Missing(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2CapacityReservationFleet_InstanceTypeSpecifications_Property_Empty() {
        handleRequest_AWSEC2CapacityReservationFleet_InstanceTypeSpecifications_Property_Empty(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2CapacityReservationFleet_InstanceType_Property_Missing() {
        handleRequest_AWSEC2CapacityReservationFleet_InstanceType_Property_Missing(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2CapacityReservationFleet_InstanceType_Property_For_List_item_Failure() {
        handleRequest_AWSEC2CapacityReservationFleet_InstanceType_Property_For_List_item_Failure(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2CapacityReservationFleet_InstanceType_Property_For_List_item_Success() {
        handleRequest_AWSEC2CapacityReservationFleet_InstanceType_Property_For_List_item_Success(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2Host_NeitherInstanceTypeNorInstanceFamilySpecified() {
        handleRequest_AWSEC2Host_NeitherInstanceTypeNorInstanceFamilySpecified(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2Host_BothInstanceTypeAndInstanceFamilySpecified() {
        handleRequest_AWSEC2Host_BothInstanceTypeAndInstanceFamilySpecified(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2Host_InstanceType_Property_Failure() {
        handleRequest_AWSEC2Host_InstanceType_Property_Failure(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2Host_InstanceFamily_Property_Failure() {
        handleRequest_AWSEC2Host_InstanceFamily_Property_Failure(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2Host_InstanceType_Property_Success() {
        handleRequest_AWSEC2Host_InstanceType_Property_Success(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSEC2Host_InstanceFamily_Property_Success() {
        handleRequest_AWSEC2Host_InstanceFamily_Property_Success(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSCloud9EnvironmentEC2_InstanceType_Property_Missing() {
        handleRequest_AWSCloud9EnvironmentEC2_InstanceType_Property_Missing(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSCloud9EnvironmentEC2_InstanceType_Property_Failure() {
        handleRequest_AWSCloud9EnvironmentEC2_InstanceType_Property_Failure(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSCloud9EnvironmentEC2_InstanceType_Property_Success() {
        handleRequest_AWSCloud9EnvironmentEC2_InstanceType_Property_Success(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSAutoScalingLaunchConfiguration_InstanceTypeAndInstanceFamilyNotSpecified() {
        handleRequest_AWSAutoScalingLaunchConfiguration_InstanceTypeAndInstanceFamilyNotSpecified(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSAutoScalingLaunchConfiguration_InstanceType_Property_Failure() {
        handleRequest_AWSAutoScalingLaunchConfiguration_InstanceType_Property_Failure(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSAutoScalingLaunchConfiguration_InstanceId_Property_Failure() {
        handleRequest_AWSAutoScalingLaunchConfiguration_InstanceId_Property_Failure(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSAutoScalingLaunchConfiguration_InstanceType_Property_Success() {
        handleRequest_AWSAutoScalingLaunchConfiguration_InstanceType_Property_Success(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

    @Test
    public void handleRequest_AWSAutoScalingLaunchConfiguration_InstanceId_Property_Success() {
        handleRequest_AWSAutoScalingLaunchConfiguration_InstanceId_Property_Success(
                PRE_CREATE_OPERATION,
                proxy,
                logger);
    }

}
