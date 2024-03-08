// Example Lambda function called by AWSSamples::LambdaFunctionInvoker::Hook.


// If you choose to invoke the hook for all the invocation points
// (default behavior), and to not set `TargetFilters` for your hook,
// you can define, in the example Lambda function code, for which
// invocation points to run the code in this function. It is important
// to understand that if you choose this method as opposed to target
// filters, the hook will be invoked anyway for all of the AWS
// resource types in your templates across all the invocation points,
// and you'll be billed for all the invocations. To use this feature,
// comment out the line for `hookInvocationPoints` that corresponds to
// the invocation point you do not want to run. Later on in this
// example code, you'll find a conditional block that will return
// SUCCESS if the current invocation point is something you do not
// need to evaluate on during the current invocation.
const hookInvocationPoints = [
  "CREATE_PRE_PROVISION",
  "UPDATE_PRE_PROVISION",
  "DELETE_PRE_PROVISION",
];

// Add AWS resource type target that this code will evaluate. This
// example function validates if versioning is enabled for an S3
// bucket; hence, add AWS::S3::Bucket here.
const targetNames = [
  "AWS::S3::Bucket",
];


export const handler = async (event) => {
  try {
    // Get the entire request from the input event.
    var request = event["request"];

    // Get the invocation point for the hook that is calling this
    // function; for example: `CREATE_PRE_PROVISION`.
    var invocationPoint = request["hookContext"]["invocationPoint"];
    console.info(`Invocation point: ${invocationPoint}`);

    // Get the name of the resource type target that invoked the hook.
    // For example: `AWS::S3::Bucket`.
    var targetName = request['hookContext']['targetName'];
    console.info(`Target name: ${targetName}`);

    // If you're not using TargetFilters for the hook that invokes
    // this function, return SUCCESS immediately if you do not want to
    // perform policy-as-code validation for a given hook invocation
    // point that is commented out in hookInvocationPoints at the
    // beginning of this code, or for target names you've not added to
    // targetNames above.
    if (!hookInvocationPoints.includes(invocationPoint) || !targetNames.includes(targetName)) {
      var message = `Skipping ${targetName} evaluation for ${invocationPoint}.`;
      console.info(message);
      var payload = {
        'status': 'SUCCESS',
        'errorCode': null,
        'message': message,
        'callbackContext': null,
        'callbackDelaySeconds': 0,
      };
      // console.trace(payload);
      return payload;
    }

    // Get the model of the resource type target.
    var targetModel = request['hookContext']['targetModel'];

    // Get the resource properties of the target resource type; this
    // should include the properties for the target resource type that
    // the user specified in their CloudFormation template.
    var resourceProperties = 'resourceProperties' in targetModel ? targetModel['resourceProperties'] : {};
    // console.dir(resourceProperties, { depth: null });

    // The code below needs to validate not only if `Status` for
    // `VersioningConfiguration` is set to `Enabled`, but also if all
    // the other parent properties are present in the template.
    var versioningConfiguration = 'VersioningConfiguration' in resourceProperties ? resourceProperties['VersioningConfiguration'] : {};
    var versioningConfigurationStatus = 'Status' in versioningConfiguration ? versioningConfiguration['Status'] : "";

    if (versioningConfigurationStatus != 'Enabled') {
      message = 'Versioning not set or not enabled for the S3 bucket.';
      console.error(message);
      // Return FAILED to the hook, using a payload format that the
      // hook expects once Lambda will serialize it in the response: a
      // dictionary that contains information on status, error code,
      // message, callback context, and callback delay in
      // seconds. This format is modeled after a `ProgressEvent`
      // object:
      // https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-progressevent.html
      payload = {
        'status': 'FAILED',
        'errorCode': 'NonCompliant',
        'message': message,
        'callbackContext': null,
        'callbackDelaySeconds': 0,
      };
    }
    else {
      // Return success if the resource is compliant.
      message = 'Versioning is enabled for the S3 bucket.';
      console.info(message);
      payload = {
        'status': 'SUCCESS',
        'errorCode': null,
        'message': message,
        'callbackContext': null,
        'callbackDelaySeconds': 0,
      };
    }

    // console.trace(payload);
    return payload;
  }
  catch (error) {
    message = error.message;
    // Default fallback to FAILED in the event of other errors.
    payload = {
      'status': 'FAILED',
      'errorCode': 'InternalFailure',
      'message': message,
      'callbackContext': null,
      'callbackDelaySeconds': 0,
    };
    console.error(message);
    return payload;
  }
};
