package com.awssamples.ec2instancetypes.hook;

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookHandlerRequest;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * This class is used for calling common operations in BaseHookHandlerStd.
 */
public class PreCreateHookHandler extends BaseHookHandlerStd {

    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> handleRequest(
            final AmazonWebServicesClientProxy proxy,
            final HookHandlerRequest request,
            final CallbackContext callbackContext,
            final Logger logger,
            final TypeConfigurationModel typeConfiguration) {
        return preCreatePreUpdateOperations(
                proxy,
                request,
                callbackContext,
                logger,
                typeConfiguration);
    }

}
