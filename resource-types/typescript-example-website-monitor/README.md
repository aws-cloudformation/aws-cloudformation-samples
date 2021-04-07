# Example::Monitoring::Website

Congratulations on starting development! Next steps:

1. Write the JSON schema describing your resource, [community-monitoring-website.json](./example-monitoring-website.json)
2. Implement your resource handlers in [handlers.ts](./example-monitoring-website/handlers.ts)

> Don't modify [models.ts](./example-monitoring-website/models.ts) by hand, any modifications will be overwritten when the `generate` or `package` commands are run.

Implement CloudFormation resource here. Each function must always return a ProgressEvent.

```typescript
const progress = ProgressEvent.builder<ProgressEvent<ResourceModel>>()

    // Required
    // Must be one of OperationStatus.InProgress, OperationStatus.Failed, OperationStatus.Success
    .status(OperationStatus.InProgress)
    // Required on SUCCESS (except for LIST where resourceModels is required)
    // The current resource model after the operation; instance of ResourceModel class
    .resourceModel(model)
    .resourceModels(null)
    // Required on FAILED
    // Customer-facing message, displayed in e.g. CloudFormation stack events
    .message('')
    // Required on FAILED a HandlerErrorCode
    .errorCode(HandlerErrorCode.InternalFailure)
    // Optional
    // Use to store any state between re-invocation via IN_PROGRESS
    .callbackContext({})
    // Required on IN_PROGRESS
    // The number of seconds to delay before re-invocation
    .callbackDelaySeconds(0)

    .build()
```

While importing the [cfn-rpdk](https://github.com/eduardomourar/cloudformation-cli-typescript-plugin) library, failures can be passed back to CloudFormation by either raising an exception from `exceptions`, or setting the ProgressEvent's `status` to `OperationStatus.Failed` and `errorCode` to one of `HandlerErrorCode`. There is a static helper function, `ProgressEvent.failed`, for this common case.

Keep in mind, during runtime all logs will be delivered to CloudWatch if you use the `log()` method from `LoggerProxy` class.
