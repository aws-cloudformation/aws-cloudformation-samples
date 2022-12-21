# AWSSamples::EC2InstanceTypes::Hook

## Activation

To activate a hook in your account, use the following JSON as the `Configuration` request parameter for [`SetTypeConfiguration`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html) API request.

### Configuration

<pre>
{
    "CloudFormationConfiguration": {
        "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-hook-configuration" title="HookConfiguration">HookConfiguration</a>": {
            "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-targetstacks" title="TargetStacks">TargetStacks</a>":  <a href="#footnote-1">"ALL" | "NONE"</a>,
            "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-failuremode" title="FailureMode">FailureMode</a>": <a href="#footnote-1">"FAIL" | "WARN"</a> ,
            "<a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-properties" title="Properties">Properties</a>" : {
                "<a href="#ec2instancetypes" title="EC2InstanceTypes">EC2InstanceTypes</a>" : <i>String</i>
            }
        }
    }
}
</pre>

## Properties

#### EC2InstanceTypes

Comma-delimited list of Amazon EC2 Instance Types (https://aws.amazon.com/ec2/instance-types/) you wish to use and allow for your workload.

_Required_: No

_Type_: String


---

## Targets

* `AWS::AutoScaling::LaunchConfiguration`
* `AWS::Cloud9::EnvironmentEC2`
* `AWS::EC2::CapacityReservation`
* `AWS::EC2::CapacityReservationFleet`
* `AWS::EC2::Host`
* `AWS::EC2::Instance`
* `AWS::EC2::LaunchTemplate`

---

<p id="footnote-1"><i> Please note that the enum values for <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-targetstacks" title="TargetStacks">
TargetStacks</a> and <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-failuremode" title="FailureMode">FailureMode</a>
might go out of date, please refer to their official documentation page for up-to-date values. </i></p>

