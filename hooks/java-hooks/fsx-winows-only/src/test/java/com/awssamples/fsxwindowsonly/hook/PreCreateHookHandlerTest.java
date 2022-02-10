package com.awssamples.fsxwindowsonly.hook;

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

        final Map<String, Object> fileSystem = buildFileSystem("WINDOWS");
        final HookTargetModel targetModel = createHookTargetModel(fileSystem);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::FSx::FileSystem").targetModel(targetModel).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, null);
        assertResponse(response, OperationStatus.SUCCESS,
                "Successfully invoked PreCreateHookHandler for target: AWS::FSx::FileSystem");
    }


    @Test
    public void handleRequest_FSxFileSystemFail_LUSTRE() {
        final PreCreateHookHandler handler = new PreCreateHookHandler();

        final Map<String, Object> fileSystem = buildFileSystem("LUSTRE");
        final HookTargetModel targetModel = createHookTargetModel(fileSystem);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::FSx::FileSystem").targetModel(targetModel).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, null);
        assertResponse(response, OperationStatus.FAILED, "The type of Amazon FSx file system can only be WINDOWS");
    }

    @SuppressWarnings("SameParameterValue")
    private Map<String, Object> buildFileSystem(final String fileType) {
        final Map<String, Object> subnet = new LinkedHashMap<>();
        subnet.put("FileSystemType", fileType); 
                                                            
        return subnet;
    }
}