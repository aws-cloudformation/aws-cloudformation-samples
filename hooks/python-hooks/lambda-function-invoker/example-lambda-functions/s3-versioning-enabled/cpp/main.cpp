// Example Lambda function called by AWSSamples::LambdaFunctionInvoker::Hook.

#include <exception>
#include <iostream>
#include <set>
#include <stdexcept>
#include <string>

#include <aws/core/utils/json/JsonSerializer.h>
#include <aws/lambda-runtime/runtime.h>

using namespace std;
using namespace Aws::Utils::Json;
using namespace aws::lambda_runtime;

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
set<string> hookInvocationPoints{
    "CREATE_PRE_PROVISION",
    "UPDATE_PRE_PROVISION",
    "DELETE_PRE_PROVISION",
};

// Add AWS resource type target that this code will evaluate. This
// example function validates if versioning is enabled for an S3
// bucket; hence, add AWS::S3::Bucket here.
set<string> targetNames{
    "AWS::S3::Bucket",
};

// MIME type to return in invocation responses.
const string invocationResponseMimeType = "application/json";

invocation_response handler(invocation_request const &request) {
  JsonValue payload(request.payload);
  JsonView payloadView = payload.View();

  try {
    // Get the entire request from the input event.
    JsonView hookRequest = payloadView.GetObject("request");
    JsonView hookContext = hookRequest.GetObject("hookContext");

    // Get the invocation point for the hook that is calling this
    // function; for example: `CREATE_PRE_PROVISION`.
    string invocationPoint = hookContext.GetString("invocationPoint");
    cout << "Invocation point: " << invocationPoint << endl;

    // Get the name of the resource type target that invoked the hook.
    // For example: `AWS::S3::Bucket`.
    string targetName = hookContext.GetString("targetName");
    cout << "Target name: " << targetName << endl;

    // If you're not using TargetFilters for the hook that invokes
    // this function, return SUCCESS immediately if you do not want to
    // perform policy-as-code validation for a given hook invocation
    // point that is commented out in hookInvocationPoints at the
    // beginning of this code, or for target names you've not added to
    // targetNames above.
    if (hookInvocationPoints.find(invocationPoint) ==
            hookInvocationPoints.end() ||
        targetNames.find(targetName) == targetNames.end()) {
      JsonValue payload;
      string message =
          "Skipping " + targetName + " evaluation for " + invocationPoint + ".";
      cout << message << endl;
      payload.WithString("status", "SUCCESS");
      payload.WithString("errorCode", "");
      payload.WithString("message", message);
      payload.WithString("callbackContext", {});
      payload.WithInteger("callbackDelaySeconds", 0);
      auto response = payload.View().WriteReadable();
      // cout << response << endl;
      return invocation_response::success(response, invocationResponseMimeType);
    }

    // Get the model of the resource type target.
    auto targetModel = hookContext.GetObject("targetModel");

    // Get the resource properties of the target resource type; this
    // should include the properties for the target resource type that
    // the user specified in their CloudFormation template.
    auto resourceProperties = targetModel.GetObject("resourceProperties");

    auto versioningConfiguration =
        resourceProperties.GetObject("VersioningConfiguration");
    auto versioningConfigurationStatus =
        versioningConfiguration.GetString("Status");

    if (!resourceProperties.IsObject() || !versioningConfiguration.IsObject() ||
        !versioningConfiguration.KeyExists("Status") ||
        versioningConfigurationStatus != "Enabled") {
      JsonValue payload;
      string message = "Versioning not set or not enabled for the S3 bucket.";
      cerr << message << endl;
      // Return FAILED to the hook, using a payload format that the
      // hook expects: a data structure that contains information on
      // status, error code, message, callback context, and callback
      // delay in seconds. This format is modeled after a
      // `ProgressEvent` object:
      // https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-progressevent.html
      // The expected data structure is serialized with
      // Aws::Utils::Json::JsonValue::View() and WriteReadable() into
      // the invocation response.
      payload.WithString("status", "FAILED");
      payload.WithString("errorCode", "NonCompliant");
      payload.WithString("message", message);
      payload.WithString("callbackContext", {});
      payload.WithInteger("callbackDelaySeconds", 0);
      auto response = payload.View().WriteReadable();
      // cout << response << endl;
      return invocation_response::success(response, invocationResponseMimeType);
    }

    JsonValue payload;
    string message = "Versioning is enabled for the S3 bucket.";
    cout << message << endl;
    payload.WithString("status", "SUCCESS");
    payload.WithString("errorCode", "");
    payload.WithString("message", message);
    payload.WithString("callbackContext", {});
    payload.WithInteger("callbackDelaySeconds", 0);
    auto response = payload.View().WriteReadable();
    // cout << response << endl;
    return invocation_response::success(response, invocationResponseMimeType);
  } catch (const runtime_error &runtimeError) {
    cerr << "Runtime error: " << runtimeError.what() << endl;
    JsonValue payload;
    payload.WithString("status", "FAILED");
    payload.WithString("errorCode", "InternalFailure");
    payload.WithString("message", runtimeError.what());
    payload.WithString("callbackContext", {});
    payload.WithInteger("callbackDelaySeconds", 0);
    auto response = payload.View().WriteReadable();
    // cout << response << endl;
    return invocation_response::success(response, invocationResponseMimeType);
  } catch (const exception &exception) {
    cerr << "Exception: " << exception.what() << endl;
    JsonValue payload;
    payload.WithString("status", "FAILED");
    payload.WithString("errorCode", "InternalFailure");
    payload.WithString("message", exception.what());
    payload.WithString("callbackContext", {});
    payload.WithInteger("callbackDelaySeconds", 0);
    auto response = payload.View().WriteReadable();
    // cout << response << endl;
    return invocation_response::success(response, invocationResponseMimeType);
  } catch (...) {
    JsonValue payload;
    string message = "Unknown error occurred.";
    cerr << message << endl;
    payload.WithString("status", "FAILED");
    payload.WithString("errorCode", "InternalFailure");
    payload.WithString("message", message);
    payload.WithString("callbackContext", {});
    payload.WithInteger("callbackDelaySeconds", 0);
    auto response = payload.View().WriteReadable();
    // cout << response << endl;
    return invocation_response::success(response, invocationResponseMimeType);
  }
}

int main() {
  cout << "Running s3-versioning-enabled." << endl;
  run_handler(handler);
  return 0;
}
