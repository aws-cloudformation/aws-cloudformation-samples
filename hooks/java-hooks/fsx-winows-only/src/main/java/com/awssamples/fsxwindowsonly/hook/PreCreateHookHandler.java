package com.awssamples.fsxwindowsonly.hook;

import com.awssamples.fsxwindowsonly.hook.model.aws.fsx.filesystem.AwsFsxFilesystem;
import com.awssamples.fsxwindowsonly.hook.model.aws.fsx.filesystem.AwsFsxFilesystemTargetModel;
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

import java.util.Collection;
import java.util.Objects;

public class PreCreateHookHandler extends BaseHookHandler<CallbackContext, TypeConfigurationModel> {

    private static final Collection<String> HOOK_TARGET_NAMES = ImmutableSet.of("AWS::FSx::FileSystem");

    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> handleRequest(final AmazonWebServicesClientProxy proxy,
            final HookHandlerRequest request, final CallbackContext callbackContext, final Logger logger,
            final TypeConfigurationModel typeConfiguration) {

        final String targetName = request.getHookContext().getTargetName();

        if (!HOOK_TARGET_NAMES.contains(targetName)) {
            throw new UnsupportedTargetException(targetName);
        }

        final ResourceHookTargetModel<AwsFsxFilesystem> targetModel = request.getHookContext()
                .getTargetModel(AwsFsxFilesystemTargetModel.class);

        return this.validateSubnet(targetModel.getResourceProperties());
    }

    private ProgressEvent<HookTargetModel, CallbackContext> validateSubnet(final AwsFsxFilesystem fileSystem) {
        if (fileSystem == null) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                    .message("The type of Amazon FSx file system can only be WINDOWS")
                    .errorCode(HandlerErrorCode.NonCompliant).build();
        }
        final String IsWindows = Objects.toString(fileSystem.get("FileSystemType"), null);

        if (StringUtils.equals(IsWindows, "WINDOWS")) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.SUCCESS)
                    .message("Successfully invoked PreCreateHookHandler for target: AWS::FSx::FileSystem").build();
        }
        return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                .message("The type of Amazon FSx file system can only be WINDOWS").errorCode(HandlerErrorCode.NonCompliant).build();

    }
}