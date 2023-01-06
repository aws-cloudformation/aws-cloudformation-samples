package com.awssamples.ec2instancetypes.hook.supportedtargets;

import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;

import software.amazon.cloudformation.proxy.AmazonWebServicesClientProxy;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.HookContext;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;
import software.amazon.cloudformation.proxy.hook.targetmodel.ResourceHookTarget;

/**
 * Interface meant to be used for utility methods implementing a supported
 * resource type. Once implemented, each supported type must be added to
 * SUPPORTED_TARGETS in BaseHookHandlerStd.
 */
public interface SupportedTarget {

    /**
     * Return the resource type name.
     *
     * @return String
     */
    public String getTypeName();

    /**
     * Validate the specified target's configuration.
     *
     * @param proxy                      AmazonWebServicesClientProxy
     * @param allowedEc2InstanceTypesSet Set
     * @param hookContext                HookContext
     * @param logger                     Logger
     * @param targetName                 String
     * @return ProgressEvent
     */
    public ProgressEvent<HookTargetModel, CallbackContext> validateTarget(
            AmazonWebServicesClientProxy proxy,
            Set<String> allowedEc2InstanceTypesSet,
            HookContext hookContext,
            Logger logger,
            String targetName);

    /**
     * Return resource-specific properties from this hook's context.
     *
     * @param hookContext HookContext
     * @return ResourceHookTarget - Each implementing class should
     *         specialize and return an object whose type inherits
     *         from ResourceHookTarget; for example: AwsEc2Instance,
     *         AwsEc2Launchtemplate
     */
    public ResourceHookTarget getResourcePropertiesFromTargetModel(HookContext hookContext);

}
