# AWSSamples::S3BlockPublicAccess::Hook

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
                "<a href="#excludedbucketsuffixes" title="excludedBucketSuffixes">excludedBucketSuffixes</a>" : <i>String</i>
            }
        }
    }
}
</pre>

## Properties

#### excludedBucketSuffixes

A comma separated list of bucket names that should be excluded from the BPA requirement. Each name provided will be matched using starts-with logic.

_Required_: No

_Type_: String


---

## Targets

* `AWS::S3::Bucket`

---

<p id="footnote-1"><i> Please note that the enum values for <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-targetstacks" title="TargetStacks">
TargetStacks</a> and <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/hooks-structure.html#hooks-failuremode" title="FailureMode">FailureMode</a>
might go out of date, please refer to their official documentation page for up-to-date values. </i></p>

