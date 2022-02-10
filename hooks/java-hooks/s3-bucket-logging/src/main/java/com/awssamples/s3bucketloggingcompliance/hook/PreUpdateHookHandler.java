package com.awssamples.s3bucketloggingcompliance.hook;

import com.awssamples.s3bucketloggingcompliance.hook.model.aws.s3.bucket.AwsS3Bucket;
import com.awssamples.s3bucketloggingcompliance.hook.model.aws.s3.bucket.AwsS3BucketTargetModel;
import com.awssamples.s3bucketloggingcompliance.hook.model.aws.s3.bucket.LoggingConfiguration;
import software.amazon.awssdk.core.SdkClient;
import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.ProxyClient;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

public class PreUpdateHookHandler extends BaseHookHandler<CallbackContext, TypeConfigurationModel> {

    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> handleRequest(
            final AmazonWebServicesClientProxy proxy,
            final HookHandlerRequest request,
            final CallbackContext callbackContext,
            final Logger logger,
            final TypeConfigurationModel typeConfiguration) {

        final HookContext hookContext = request.getHookContext();
        final String targetName = hookContext.getTargetName();

        if (!"AWS::S3::Bucket".equals(targetName)) {
            throw new UnsupportedTargetException(targetName);
        }

        logger.log(String.format("Successfully invoked PreUpdateHookHandler for target %s.", targetName));

        final String expectedLoggingBucket = typeConfiguration.getLoggingBucket();
        logger.log(String.format("Verifying S3 Bucket Logging for target %s, expecting bucket logging to be %s.",
                targetName, expectedLoggingBucket));

        final ResourceHookTargetModel<AwsS3Bucket> targetModel = hookContext.getTargetModel(AwsS3BucketTargetModel.class);

        final AwsS3Bucket bucket = targetModel.getResourceProperties();
        if (bucket != null) {
            final LoggingConfiguration loggingConfiguration = bucket.getLoggingConfiguration();
            if (loggingConfiguration != null) {
                final String targetLoggingBucket = loggingConfiguration.getDestinationBucketName();
                if (!targetLoggingBucket.equals(expectedLoggingBucket)) {
                    final String failureMessage = String.format("Failed to verify bucket logging for target %s, expecting bucket to be %s, actual bucket is %s",
                            targetName, expectedLoggingBucket, targetLoggingBucket);
                    logger.log(failureMessage);

                    return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                            .status(OperationStatus.FAILED)
                            .message(failureMessage)
                            .errorCode(HandlerErrorCode.NonCompliant)
                            .build();
                }

                return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                        .status(OperationStatus.SUCCESS)
                        .message("Successfully invoked PreUpdateHookHandler for target: AWS::S3::Bucket")
                        .build();
            }
        }

        final String failureMessage = String.format("Failed to verify bucket logging for target %s, target does not have bucket logging enabled.",
                targetName);
        logger.log(failureMessage);

        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                .status(OperationStatus.FAILED)
                .message(failureMessage)
                .errorCode(HandlerErrorCode.NonCompliant)
                .build();
    }
}
