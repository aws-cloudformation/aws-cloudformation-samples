package com.awssamples.efsencrypt.hook;

import org.apache.commons.codec.binary.StringUtils;

import com.awssamples.efsencrypt.hook.model.aws.efs.filesystem.AwsEfsFilesystem;
import com.awssamples.efsencrypt.hook.model.aws.efs.filesystem.AwsEfsFilesystemTargetModel;
import com.google.common.collect.ImmutableSet;
import software.amazon.cloudformation.exceptions.UnsupportedTargetException;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTargetModel;

import java.util.Collection;
import java.util.Objects;

public class PreCreateHookHandler extends BaseHookHandler<CallbackContext, TypeConfigurationModel> {

    private static final Collection<String> HOOK_TARGET_NAMES = ImmutableSet.of(
            "AWS::EFS::FileSystem");

    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> handleRequest(
            final AmazonWebServicesClientProxy proxy,
            final HookHandlerRequest request,
            final CallbackContext callbackContext,
            final Logger logger,
            final TypeConfigurationModel typeConfiguration) {

        final String targetName = request.getHookContext().getTargetName();

        if (!HOOK_TARGET_NAMES.contains(targetName)) {
            throw new UnsupportedTargetException(targetName);
        }

        final ResourceHookTargetModel<AwsEfsFilesystem> targetModel = request.getHookContext()
                .getTargetModel(AwsEfsFilesystemTargetModel.class);

        return this.validateSubnet(targetModel.getResourceProperties());
    }

    private ProgressEvent<HookTargetModel, CallbackContext> validateSubnet(final AwsEfsFilesystem fileSystem) {
        if (fileSystem == null) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message("Encryption must be enabled")
                    .errorCode(HandlerErrorCode.NonCompliant).build();
        }
        final String IsEncrypted = Objects.toString(fileSystem.get("Encrypted"), null);

        if (IsEncrypted == null) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message("Encryption must be enabled").errorCode(HandlerErrorCode.NonCompliant).build();
        }

        if (StringUtils.equals(IsEncrypted, "false")) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message("Encryption must be enabled").errorCode(HandlerErrorCode.NonCompliant).build();
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                .status(OperationStatus.SUCCESS)
                .message("Successfully invoked PreCreateHookHandler for target: AWS::EFS::FileSystem").build();
    }
}
