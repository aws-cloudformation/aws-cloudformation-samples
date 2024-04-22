# Sample AWS CloudFormation Hooks

Welcome to the collection of sample [AWS CloudFormation
Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html)
in this repository!

The hooks feature of CloudFormation gives you the ability to create
your own -or to reuse existing- policy compliance validation controls
for proactive evaluation of infrastructure-as-code configurations you
describe in your CloudFormation templates. You model a hook to be
invoked for one or more resource types before a CloudFormation stack
is created, updated, or deleted; in your hook, you write business
logic using Java or Python to validate that target resources you
describe in your templates have the properties you need. For example,
you'd write logic to validate that [Amazon Simple Storage Service
(Amazon S3)](https://aws.amazon.com/s3/) buckets have server-side
encryption enabled and configured according to your needs. If you then
activate and configure your hook to fail on non-compliant
configurations, when your hook is invoked and finds a resource to be
not compliant, the CloudFormation stack will roll back before the
target, non-compliant resource is created, updated, or deleted.

Sample hooks in this repository show you examples of how to perform
proactive policy compliance evaluations for a number of example use
cases.

To get started building, testing, and using hooks by using an
end-to-end, hands-on lab, see
[Hooks](https://catalog.workshops.aws/cfn101/en-US/advanced/hooks) in
the [AWS CloudFormation
Workshop](https://catalog.workshops.aws/cfn101/en-US).
