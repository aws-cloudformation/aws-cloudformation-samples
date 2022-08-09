package com.awssamples.ec2instancetypes.hook.supportedproperties;

import java.util.Set;

import com.awssamples.ec2instancetypes.hook.CallbackContext;

import software.amazon.cloudformation.proxy.HandlerErrorCode;
import software.amazon.cloudformation.proxy.Logger;
import software.amazon.cloudformation.proxy.OperationStatus;
import software.amazon.cloudformation.proxy.ProgressEvent;
import software.amazon.cloudformation.proxy.hook.targetmodel.HookTargetModel;

/**
 * This interface contains AWS::EC2::Instance-related helper methods, that are
 * relevant to the validation of the InstanceType property.
 */
public interface AwsEc2InstanceInstanceTypeProperty {

    /**
     * Validate the InstanceType property when a default value is present.
     *
     * @param allowedEc2InstanceTypesSet Set<String>
     * @param targetInstanceType         String
     * @param targetName                 String
     * @param logger                     Logger
     * @return ProgressEvent<HookTargetModel, CallbackContext>
     */
    default ProgressEvent<HookTargetModel, CallbackContext> validateInstanceTypeTargetPropertyWithDefaultValue(
            final Set<String> allowedEc2InstanceTypesSet,
            final String targetInstanceType,
            final String targetName,
            final Logger logger) {
        /*
         * For AWS::EC2::Instance, the InstanceType parameter is not required. When not
         * specified, its value defaults to m1.small: hence, reflecting this behavior
         * here.
         */
        String targetInstanceTypeToVerify = targetInstanceType;
        if (targetInstanceType == null)
            targetInstanceTypeToVerify = "m1.small";

        if (!allowedEc2InstanceTypesSet.contains(targetInstanceTypeToVerify)) {
            final String failureMessage = String.format(
                    "Failed to verify instance type for target: [%s].  Allowed value(s): %s; specified value: [%s].  If you have not specified an EC2 instance type, its value defaults to m1.small.",
                    targetName, allowedEc2InstanceTypesSet.toString(), targetInstanceTypeToVerify);
            logger.log(failureMessage);

            return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                    .status(OperationStatus.FAILED)
                    .message(failureMessage)
                    .errorCode(HandlerErrorCode.NonCompliant)
                    .build();
        }

        return ProgressEvent.<HookTargetModel, CallbackContext>builder()
                .status(OperationStatus.IN_PROGRESS)
                .build();
    }

}
