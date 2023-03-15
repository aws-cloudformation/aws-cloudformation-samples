# AWSSamples::IAMPrincipalBoundary::Hook

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
                "<a href="#iamprincipalboundaryarn" title="iamPrincipalBoundaryArn">iamPrincipalBoundaryArn</a>" : <i>String</i>,
                "<a href="#excludedprincipalsuffixes" title="excludedPrincipalSuffixes">excludedPrincipalSuffixes</a>" : <i>String</i>
            }
        }
    }
}
</pre>

## Properties

#### iamPrincipalBoundaryArn

The ARN that must be attached as an IAM Principal

_Required_: No

_Type_: String

#### excludedPrincipalSuffixes

A comma separated list of principal names that should be excluded from the boundary. Each name provided will be matched using starts-with logic.

_Required_: No

_Type_: String


---

## Targets

* `AWS::IAM::Role`
* `AWS::IAM::User`

---

<p id="footnote-1"><i> Please note that the enum values for <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-targetstacks" title="TargetStacks">
TargetStacks</a> and <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-failuremode" title="FailureMode">FailureMode</a>
might go out of date, please refer to their official documentation page for up-to-date values. </i></p>

