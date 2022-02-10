package com.awssamples.noip6.hook;

import org.apache.commons.codec.binary.StringUtils;

import com.awssamples.noip6.hook.model.aws.ec2.subnet.AwsEc2Subnet;
import com.awssamples.noip6.hook.model.aws.ec2.subnet.AwsEc2SubnetTargetModel;
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

public class PreUpdateHookHandler extends BaseHookHandler<CallbackContext, TypeConfigurationModel> {

    private static final Collection<String> HOOK_TARGET_NAMES = ImmutableSet.of("AWS::EC2::Subnet");

    @Override
    public ProgressEvent<HookTargetModel, CallbackContext> handleRequest(final AmazonWebServicesClientProxy proxy,
            final HookHandlerRequest request, final CallbackContext callbackContext, final Logger logger,
            final TypeConfigurationModel typeConfiguration) {

        final String targetName = request.getHookContext().getTargetName();

        if (!HOOK_TARGET_NAMES.contains(targetName)) {
            throw new UnsupportedTargetException(targetName);
        }

        final ResourceHookTargetModel<AwsEc2Subnet> targetModel = request.getHookContext()
                .getTargetModel(AwsEc2SubnetTargetModel.class);

        return this.validateSubnet(targetModel.getResourceProperties());
    }

    private ProgressEvent<HookTargetModel, CallbackContext> validateSubnet(final AwsEc2Subnet subnet) {
        if (subnet == null) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                    .message("Resource properties for EC2 Subnet model are empty")
                    .errorCode(HandlerErrorCode.NonCompliant).build();
        }
        final String IsAssignIpv6AddressOnCreation = Objects.toString(subnet.get("AssignIpv6AddressOnCreation"), null); 
                                                                                                                        
                                                                                                                        
        if (StringUtils.equals(IsAssignIpv6AddressOnCreation, "true")) {
            return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.FAILED)
                    .message("This Subnet is trying to enable IPv6").errorCode(HandlerErrorCode.NonCompliant).build();
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder().status(OperationStatus.SUCCESS)
                .message("Successfully invoked PreCreateHookHandler for target: AWS::EC2::Subnet").build();
    }

}
