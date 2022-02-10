package com.awssamples.noip6.hook;

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
        final PreCreateHookHandler handler = new PreCreateHookHandler();

        final Map<String, Object> subnet = buildSubnet(false);
        final HookTargetModel targetModel = createHookTargetModel(subnet);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Subnet").targetModel(targetModel).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, null);
        assertResponse(response, OperationStatus.SUCCESS,
                "Successfully invoked PreCreateHookHandler for target: AWS::EC2::Subnet");
    }

    @Test
    public void handleRequest_awsEC2SubnetFail_AssignIpv6AddressOnCreation_True() {
        final PreCreateHookHandler handler = new PreCreateHookHandler();

        final Map<String, Object> subnet = buildSubnet(true);
        final HookTargetModel targetModel = createHookTargetModel(subnet);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::EC2::Subnet").targetModel(targetModel).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, null);
        assertResponse(response, OperationStatus.FAILED, "This Subnet is trying to enable IPv6");
    }

    @SuppressWarnings("SameParameterValue")
    private Map<String, Object> buildSubnet(final Boolean assignIpv6AddressOnCreationState) {
        final Map<String, Object> subnet = new LinkedHashMap<>();
        subnet.put("AssignIpv6AddressOnCreation", assignIpv6AddressOnCreationState); // "AssignIpv6AddressOnCreationState"
                                                                                     // is name of the property for an
        // AWS::EC2::Subnet resource
        return subnet;
    }
}