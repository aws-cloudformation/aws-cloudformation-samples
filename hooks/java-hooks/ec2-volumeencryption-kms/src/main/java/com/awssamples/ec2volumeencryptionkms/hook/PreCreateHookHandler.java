package com.awssamples.ec2volumeencryptionkms.hook;

import com.awssamples.ec2volumeencryptionkms.hook.model.aws.ec2.volume.AwsEc2Volume;
import com.awssamples.ec2volumeencryptionkms.hook.model.aws.ec2.volume.AwsEc2VolumeTargetModel;
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

public class PreCreateHookHandler extends BaseHookHandler<CallbackContext, TypeConfigurationModel> {

    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> handleRequest(
            final AmazonWebServicesClientProxy proxy,
            final HookHandlerRequest request,
            final CallbackContext callbackContext,
            final Logger logger,
            final TypeConfigurationModel typeConfiguration) {

        final HookContext hookContext = request.getHookContext();
        final String targetName = hookContext.getTargetName();

        if (!"AWS::EC2::Volume".equals(targetName)) {
            throw new UnsupportedTargetException(targetName);
        }

        logger.log(String.format("Successfully invoked PreCreateHookHandler for target %s.", targetName));

        final String expectedKmsKeyId = typeConfiguration.getKmsKeyId();
        final Boolean expectedEncrypted = true;
        logger.log(String.format("Verifying ec2 volume encryption for target %s, expecting target to be encrypted with KMS key ID %s.",
                targetName, expectedKmsKeyId));

        final ResourceHookTargetModel<AwsEc2Volume> targetModel = hookContext.getTargetModel(AwsEc2VolumeTargetModel.class);

        final AwsEc2Volume volume = targetModel.getResourceProperties();
        if (volume != null) {
            final String targetKmsKeyId = volume.getKmsKeyId();
            final Boolean targetEncrypted = volume.getEncrypted();
            if (targetEncrypted != expectedEncrypted) {

                final String failureMessage = String.format("Failed to verify volume encryption for target %s, expecting volume encryption to be %s, actual encryption algorithm is %s",
                        targetName, expectedEncrypted, targetEncrypted);
                logger.log(failureMessage);

                return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                        .status(OperationStatus.FAILED)
                        .message(failureMessage)
                        .errorCode(HandlerErrorCode.NonCompliant)
                        .build();
            }
            if (!expectedKmsKeyId.equals(targetKmsKeyId)) {
                final String failureMessage = String.format("Failed to verify volume KmsKeyId for target %s, expecting volume KmsKeyId to be %s, actual KmsKeyId is %s",
                        targetName, expectedKmsKeyId, targetKmsKeyId);
                logger.log(failureMessage);

                return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                        .status(OperationStatus.FAILED)
                        .message(failureMessage)
                        .errorCode(HandlerErrorCode.NonCompliant)
                        .build();
            }

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.SUCCESS)
                    .message("Successfully invoked PreCreateHookHandler for target: AWS::EC2::Volume")
                    .build();

        }

        final String failureMessage = String.format("Failed to verify volume for target %s, expecting volume KmsKeyId to be %s and Encrypted to be %s",
                targetName, expectedKmsKeyId, expectedEncrypted);
        logger.log(failureMessage);

        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                .status(OperationStatus.FAILED)
                .message(failureMessage)
                .errorCode(HandlerErrorCode.NonCompliant)
                .build();
    }
}