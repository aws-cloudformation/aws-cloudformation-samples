package com.awssamples.ec2instancetypes.hook;

import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.cloudformation.HookLambdaWrapper;

/**
 * This class is for building service client types. It is recommended to use
 * static HTTP client so less memory is consumed; e.g.,:
 * https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-
 * logs/blob/master/aws-logs-loggroup/src/main/java/software/amazon/logs/
 * loggroup/ClientBuilder.java#L9
 */
public class ClientBuilder {

    /**
     * Creates a static HTTP client for Amazon EC2.
     *
     * @return Ec2Client
     */
    public static Ec2Client getEc2Client() {
        return Ec2Client.builder()
                .httpClient(HookLambdaWrapper.HTTP_CLIENT)
                .build();
    }

}
