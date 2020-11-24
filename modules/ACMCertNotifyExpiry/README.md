## About
In the past few years there have been scenarios where popular sites have let their SSL certificates briefly lapse. The browser then marks the site as untrusted leading to a huge nosedive in traffic.

In the case of AWS Certificate Manager (ACM), since it allows you to import certificates that you obtained from a third-party issuer, but does not provide managed renewal this could lead to the above mentioned scenario if not monitored. 

`AWSSamples::ACMCert::NotifyExpiry::MODULE` module will help you monitor and evaluate all the ACM certificates in your account which are in `ISSUED` state and check for the expiry on them. 
When the expiration is less than the threshold, it will publish a message to an SNS topic that can have various subscriptions. This allows teams to act on renewing the certs ahead of time and not have any unwanted scenarios.

&nbsp;
&nbsp;

## Properties of the module

|    Properties     | Required (Y/N) |  Default  |
| :---------------: | :------------: | :-------: |
| `ApplicationName` |       N        | SampleApp |
|   `Environment`   |       N        |    dev    |
|    `Threshold`    |       N        |    14     |
|   `SNSTopicArn`   |       Y        |    n/a    |

&nbsp;
&nbsp;

## Important resources created as part of the module

| Logical ID               | Resource Type           | Description                                                                                                                  |
| ------------------------ | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| CheckSSLExpiryLambda     | `AWS::Lambda::Function` | AWS lambda function evaluates all the ACM certs in `ISSUED` state and uses the threshold parameter and SNSTopicArn to notify |
| ScheduledRule            | `AWS::Events::Rule`     | This is the scheduled rule to run the lambda at 12 UTC once a day                                                            |
| CheckSSLExpiryLambdaRole | `AWS::IAM::Role`        | This IAM role has permissions to list, describe the ACM certs and publish a message to an SNS topic                          |

&nbsp;
&nbsp;

## Usage

To declare this entity in your AWS CloudFormation template, use the following syntax
or refer to [example-usage.yml](https://code.amazon.com/packages/Notify-cert-expiry-cfn-module/blobs/heads/master/--/example-usage.yaml) to learn how to use the module.

&nbsp;

&nbsp;
#### JSON

```json
{
    "Type" : "AWSSamples::ACMCert::NotifyExpiry::MODULE",
    "Properties" : {
        "ApplicationName" : String,
        "Environment" : String,
        "Threshold" : Number,
        "SNSTopicArn" : String
    }
}
```

&nbsp;

#### YAML
```yaml
Type: "AWSSamples::ACMCert::NotifyExpiry::MODULE"
Properties:
  ApplicationName: String
  Environment: String
  Threshold: Number
  SNSTopicArn: String
```



