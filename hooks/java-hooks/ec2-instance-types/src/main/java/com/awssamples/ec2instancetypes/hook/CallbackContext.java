package com.awssamples.ec2instancetypes.hook;

import software.amazon.cloudformation.proxy.StdCallbackContext;

/**
 * This class can be used as part of callback operations.
 */
@lombok.Getter
@lombok.Setter
@lombok.ToString
@lombok.EqualsAndHashCode(callSuper = true)
public class CallbackContext extends StdCallbackContext {
}
