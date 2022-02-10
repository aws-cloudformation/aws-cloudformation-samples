package com.awssamples.sqspolicyencryption.hook;

import com.amazonaws.auth.policy.internal.JsonPolicyReader;
import com.awssamples.sqspolicyencryption.hook.model.aws.sqs.queuepolicy.AwsSqsQueuepolicy;
import com.awssamples.sqspolicyencryption.hook.model.aws.sqs.queuepolicy.AwsSqsQueuepolicyTargetModel;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.google.common.collect.ImmutableSet;

import org.apache.commons.codec.binary.StringUtils;

import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;
import software.amazon.cloudformation.resource.Serializer;

import com.amazonaws.auth.policy.Condition;
import com.amazonaws.auth.policy.Policy;
import com.amazonaws.auth.policy.Statement;

import java.util.Collection;

public class PreUpdateHookHandler extends BaseHookHandler<CallbackContext, TypeConfigurationModel> {

    private static final Collection<String> HOOK_TARGET_NAMES = ImmutableSet.of("AWS::SQS::QueuePolicy");

    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> handleRequest(final AmazonWebServicesClientProxy proxy,
            final HookHandlerRequest request, final CallbackContext callbackContext, final Logger logger,
            final TypeConfigurationModel typeConfiguration) {

        final String targetName = request.getHookContext().getTargetName();

        if (!HOOK_TARGET_NAMES.contains(targetName)) {
            throw new UnsupportedTargetException(targetName);
        }

        final ResourceHookTargetModel<AwsSqsQueuepolicy> targetModel = request.getHookContext()
                .getTargetModel(AwsSqsQueuepolicyTargetModel.class);

        AwsSqsQueuepolicy policy = targetModel.getResourceProperties();
        JsonPolicyReader policyReader = new JsonPolicyReader();
        Serializer ser = new Serializer();

        String jsonString = "";
        try {
            jsonString = ser.serialize(policy.getPolicyDocument());
        } catch (JsonProcessingException e) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                    .message(e.getMessage()).errorCode(HandlerErrorCode.NonCompliant).build();
        }

        return validatePolicy(policyReader.createPolicyFromJsonString(jsonString), logger);
    }

    private ProgressEvent<HookTargetModel, CallbackContext> validatePolicy(final Policy policy, Logger logger) {

        if (policy == null || policy.getStatements().isEmpty()) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED).message(
                    "Allow only encrypted connections over HTTPS (TLS) using the aws:SecureTransport condition in the queue policy to force requests to use SSL.")
                    .errorCode(HandlerErrorCode.NonCompliant).build();
        }

        for (Statement statement : policy.getStatements()) {
            // only review allow statements
            if (StringUtils.equals(statement.getEffect().name(), "Allow")) {
                // Return falure if policy contains less than one condition
                if (statement.getConditions().size() < 1) {
                    return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                            .message(
                                    "Allow only encrypted connections over HTTPS (TLS) using the aws:SecureTransport condition in the queue policy to force requests to use SSL.")
                            .errorCode(HandlerErrorCode.NonCompliant).build();
                }
                // Must have aws:SecureTransport condition
                for (Condition condition : statement.getConditions()) {
                    logger.log("Condition type: " + condition.getType());
                    logger.log("Condition key: " + condition.getConditionKey());
                    logger.log("Condition values: " + condition.getValues());

                    if (StringUtils.equals(condition.getType(), "Bool")
                            || StringUtils.equals(condition.getConditionKey(), "aws:SecureTransport")) {
                        if (condition.getValues().contains("true")) {
                            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                                    .status(OperationStatus.SUCCESS).message("Queue policy is valid.").build();
                        }
                    }
                }
            }
        }
        return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED).message(
                "Allow only encrypted connections over HTTPS (TLS) using the aws:SecureTransport condition in the queue policy to force requests to use SSL.")
                .errorCode(HandlerErrorCode.NonCompliant).build();
    }
}