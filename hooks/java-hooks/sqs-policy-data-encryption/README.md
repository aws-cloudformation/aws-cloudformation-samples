# AWSSamples::SQSPolicyEncryption::Hook

This AWS CloudFormation Hook validates that aws:SecureTransport is enabled when creating or updating an AWS SQS Policy. This hook validates that the  `aws:SecureTransport` condition is present and set to `True`. Without HTTPS (TLS), a network-based attacker can eavesdrop on network traffic or manipulate it, using an attack such as man-in-the-middle. Allow only encrypted connections over HTTPS (TLS) using the aws:SecureTransport condition in the queue policy to force requests to use SSL.

Below is sample CloudFromation template that will trigger the hook.
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
