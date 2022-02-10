package com.awssamples.sqspolicyencryption.hook;

import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.HookContext;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;


import static org.mockito.Mockito.mock;

import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import com.awssamples.sqspolicyencryption.hook.model.aws.sqs.queuepolicy.AwsSqsQueuepolicy;

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
        Map<String, Object> bool = new LinkedHashMap<>();
        bool.put("aws:SecureTransport", "true");

        Map<String, Object> condition = new LinkedHashMap<>();
        condition.put("Bool", bool);

        List<String> action = Arrays.asList("SQS:SendMessage", "SQS:ReceiveMessage");

        Map<String, Object> statement = new LinkedHashMap<>();
        statement.put("Condition", condition);
        statement.put("Action", action);
        statement.put("Resource", "arn:aws:sqs:us-east-2:444455556666:queue2");
        statement.put("Effect", "Allow");
        statement.put("Principal", "foo");


        Map<String, Object> doc = new LinkedHashMap<>();
        doc.put("Statement", Arrays.asList(statement));
      AwsSqsQueuepolicy policy = AwsSqsQueuepolicy.builder().policyDocument(doc).build();


        final PreCreateHookHandler handler = new PreCreateHookHandler();

        final HookTargetModel targetModel = createHookTargetModel(policy);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::SQS::QueuePolicy").targetModel(targetModel).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, null);
        assertResponse(response, OperationStatus.SUCCESS, "Queue policy is valid.");
        
    }
   
    @Test
    public void handleRequest_AWSSQSQueuePolicyFail_SecureTransport_False() {
        Map<String, Object> bool = new LinkedHashMap<>();
        bool.put("aws:SecureTransport", "false");

        Map<String, Object> condition = new LinkedHashMap<>();
        condition.put("Bool", bool);

        List<String> action = Arrays.asList("SQS:SendMessage", "SQS:ReceiveMessage");

        Map<String, Object> statement = new LinkedHashMap<>();
        statement.put("Condition", condition);
        statement.put("Action", action);
        statement.put("Resource", "arn:aws:sqs:us-east-2:444455556666:queue2");
        statement.put("Effect", "Allow");
        statement.put("Principal", "foo");


        Map<String, Object> doc = new LinkedHashMap<>();
        doc.put("Statement", Arrays.asList(statement));
      AwsSqsQueuepolicy policy = AwsSqsQueuepolicy.builder().policyDocument(doc).build();


        final PreCreateHookHandler handler = new PreCreateHookHandler();

        final HookTargetModel targetModel = createHookTargetModel(policy);

        final HookHandlerRequest request = HookHandlerRequest.builder()
                .hookContext(HookContext.builder().targetName("AWS::SQS::QueuePolicy").targetModel(targetModel).build())
                .build();

        final ProgressEvent<HookTargetModel, CallbackContext> response = handler.handleRequest(proxy, request, null,
                logger, null);
        assertResponse(response, OperationStatus.FAILED, "Allow only encrypted connections over HTTPS (TLS) using the aws:SecureTransport condition in the queue policy to force requests to use SSL.");
    }
}
