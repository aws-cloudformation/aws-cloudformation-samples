# AWSSamples::SQSPolicyEncryption::Hook

This AWS CloudFormation Hook validates that when creating or updating an `AWS::SQS::Policy` resource, the SQS policy is configured to enforce encryption in transit. This hook validates that the `Effect` is set to `Deny`, and the `Bool` `aws:SecureTransport` condition is present and set to `false`. Without HTTPS (TLS), a network-based attacker can eavesdrop on network traffic or manipulate it, using an attack such as man-in-the-middle. Allow only encrypted connections over HTTPS (TLS) using the `Deny` `Effect`, and the `Bool` `aws:SecureTransport` condition set to `false` in the queue policy to force requests to use SSL.

Below is sample CloudFormation template that will trigger the hook.
```
{
    "Resources": {
        "SampleSQSPolicy": {
            "Type": "AWS::SQS::QueuePolicy",
            "Properties": {
                "Queues": [
                    "https://sqs:us-east-2.amazonaws.com/444455556666/queue2"
                ],
                "PolicyDocument": {
                    "Statement": [
                        {
                            "Action": [
                                "SQS:SendMessage",
                                "SQS:ReceiveMessage"
                            ],
                            "Effect": "Allow",
                            "Resource": "arn:aws:sqs:us-east-2:444455556666:queue2",
                            "Principal": "foo",
                            "Condition": {
                                "Bool": {
                                    "aws:SecureTransport": "false"
                                }
                            }
                        }
                    ]
                }
            }
        }
    }
}
```
Sample configuration

```bash
# Create a basic type configuration json
cat <<EOF >> type_config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode": "FAIL",
      "Properties": {}
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type HOOK \
  --type-name AWSSamples::SQSPolicyEncryption::Hook
```
