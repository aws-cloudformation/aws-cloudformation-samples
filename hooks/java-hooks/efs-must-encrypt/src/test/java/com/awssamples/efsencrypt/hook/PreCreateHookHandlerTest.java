package com.awssamples.efsencrypt.hook;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;

import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

import java.util.LinkedHashMap;
import java.util.Map;

import static org.mockito.Mockito.mock;

@ExtendWith(MockitoExtension.class)
public class PreCreateHookHandlerTest extends AbstractTestBase {

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
        final PreCreateHookHandler handler = new PreCreateHookHandler();

        final Map<String, Object> fileSystem = buildFileSystem(true);
        final HookTargetModel targetModel = createHookTargetModel(fileSystem);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EFS::FileSystem").targetModel(targetModel).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, null);
        assertResponse(response, OperationStatus.SUCCESS,
                "Successfully invoked PreCreateHookHandler for target: AWS::EFS::FileSystem");
    }


    @Test
    public void handleRequest_AWS_EFS_FileSystem_Encrypted_False() {
        final PreCreateHookHandler handler = new PreCreateHookHandler();

        final Map<String, Object> fileSystem = buildFileSystem(false);
        final HookTargetModel targetModel = createHookTargetModel(fileSystem);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EFS::FileSystem").targetModel(targetModel).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, null);
        assertResponse(response, OperationStatus.FAILED, "Encryption must be enabled");
    }


    @SuppressWarnings("SameParameterValue")
    private Map<String, Object> buildFileSystem(final Boolean encryptionState) {
        final Map<String, Object> subnet = new LinkedHashMap<>();
        subnet.put("Encrypted", encryptionState); // "Encryption" is name of the property for an
                                                            // AWS::EFS::FileSystem resource
        return subnet;
    }
}