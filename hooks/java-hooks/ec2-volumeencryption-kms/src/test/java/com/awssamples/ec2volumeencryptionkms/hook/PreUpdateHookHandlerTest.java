package com.awssamples.ec2volumeencryptionkms.hook;

import java.util.Map;
import java.util.HashMap;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class PreUpdateHookHandlerTest extends AbstractTestBase {

    @Mock
    private AmazonWebServicesClientProxy proxy;

    @Mock
    private Logger logger;

    @BeforeEach
    public void setup() {
        proxy = mock(AmazonWebServicesClientProxy.class);
        logger = mock(Logger.class);
    }

    @Test
    public void handleRequest_SimpleSuccess() {
        final PreUpdateHookHandler handler = new PreUpdateHookHandler();

        final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().kmsKeyId("kms:key:id").build();


        final Map<String, Object> targetModel = new HashMap<>();
        final Map<String, Object> resourceProperties = new HashMap<>();
        resourceProperties.put("Encrypted", true);
        resourceProperties.put("KmsKeyId", "kms:key:id");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Volume").targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.SUCCESS);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getErrorCode()).isNull();
    }

    @Test
    public void handleRequest_NoPropertiesFailure() {
        final PreUpdateHookHandler handler = new PreUpdateHookHandler();

        final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().kmsKeyId("kms:key:id").build();

        final Map<String, Object> targetModel = new HashMap<>();

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Volume").targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    @Test
    public void handleRequest_NoEncryptionFailure() {
        final PreUpdateHookHandler handler = new PreUpdateHookHandler();

        final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().kmsKeyId("kms:key:id").build();

        final Map<String, Object> targetModel = new HashMap<>();
        final Map<String, Object> resourceProperties = new HashMap<>();
        resourceProperties.put("KmsKeyId", "kms:key:id");
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Volume").targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }

    @Test
    public void handleRequest_NoKmsKeyIdFailure() {
        final PreUpdateHookHandler handler = new PreUpdateHookHandler();

        final TypeConfigurationModel typeConfiguration = TypeConfigurationModel.builder().kmsKeyId("kms:key:id").build();

        final Map<String, Object> targetModel = new HashMap<>();
        final Map<String, Object> resourceProperties = new HashMap<>();
        resourceProperties.put("Encrypted", true);
        targetModel.put("ResourceProperties", resourceProperties);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Volume").targetModel(HookTargetModel.of(targetModel)).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null, logger, typeConfiguration);

        assertThat(response).isNotNull();
        assertThat(response.getStatus()).isEqualTo(OperationStatus.FAILED);
        assertThat(response.getCallbackContext()).isNull();
        assertThat(response.getCallbackDelaySeconds()).isEqualTo(0);
        assertThat(response.getMessage()).isNotNull();
        assertThat(response.getErrorCode()).isEqualTo(HandlerErrorCode.NonCompliant);
    }
}
