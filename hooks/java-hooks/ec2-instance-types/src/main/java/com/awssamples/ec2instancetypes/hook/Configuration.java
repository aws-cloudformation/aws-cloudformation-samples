package com.awssamples.ec2instancetypes.hook;

/**
 * This class is for setting up this hook's configuration based on its model.
 */
class Configuration extends BaseHookConfiguration {

    public Configuration() {
        super("awssamples-ec2instancetypes-hook.json");
    }

}
