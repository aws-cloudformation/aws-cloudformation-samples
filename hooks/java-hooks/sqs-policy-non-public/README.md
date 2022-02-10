# AWSSamples::SQSNonPublic::Hook

This AWS CloudFormation Hook validates that queues aren't publicly accessible. Unless you explicitly require anyone on the internet to be able to read or write to your Amazon SQS queue, you should make sure that your queue isn't publicly accessible (accessible by everyone in the world or by any authenticated AWS user).

- Avoid creating policies with Principal set to "".

- Avoid using a wildcard (*). Instead, name a specific user or users.

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
                            "Principal": "*",
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
  --type-name AWSSamples::SQSNonPublic::Hook
```
