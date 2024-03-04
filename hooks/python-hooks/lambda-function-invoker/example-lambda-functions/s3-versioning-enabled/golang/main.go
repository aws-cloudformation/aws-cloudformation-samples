// Example Lambda function called by AWSSamples::LambdaFunctionInvoker::Hook.

package main

import (
	"context"
	"fmt"
	"github.com/aws/aws-lambda-go/lambda"
	"log"
)

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
var hookInvocationPoints = []string{
	"CREATE_PRE_PROVISION",
	"UPDATE_PRE_PROVISION",
	"DELETE_PRE_PROVISION",
}

// Add AWS resource type target that this code will evaluate. This
// example function validates if versioning is enabled for an S3
// bucket; hence, add AWS::S3::Bucket here.
var targetNames = []string{
	"AWS::S3::Bucket",
}

type InputEvent struct {
	Request map[string]interface{} `json:"request"`
}

func HandleRequest(ctx context.Context, event *InputEvent) (*map[string]interface{}, error) {

	// Get the entire request from the input event.
	request := event.Request

	hookContext := request["hookContext"].(map[string]interface{})

	// Get the invocation point for the hook that is calling this
	// function; for example: `CREATE_PRE_PROVISION`.
	invocationPoint := hookContext["invocationPoint"].(string)
	log.Printf("Invocation point: %s", invocationPoint)

	targetName := hookContext["targetName"].(string)
	log.Printf("Target name: %s", targetName)

	// If you're not using TargetFilters for the hook that invokes
	// this function, return SUCCESS immediately if you do not
	// want to perform policy-as-code validation for a given hook
	// invocation point that is commented out in
	// hookInvocationPoints at the beginning of this code, or for
	// target names you've not added to targetNames above.
	if !stringsSliceHas(hookInvocationPoints, invocationPoint) || !stringsSliceHas(targetNames, targetName) {
		message := fmt.Sprintf("Skipping %s evaluation for %s.", targetName, invocationPoint)
		log.Printf(message)
		response := map[string]interface{}{
			"status":               "SUCCESS",
			"errorCode":            nil,
			"message":              message,
			"callbackContext":      nil,
			"callbackDelaySeconds": 0,
		}
		return &response, nil
	}

	// Get the model of the resource type target.
	targetModel := hookContext["targetModel"].(map[string]interface{})

	resourceProperties := make(map[string]interface{})

	// Get the resource properties of the target resource type;
	// this should include the properties for the target resource
	// type that the user specified in their CloudFormation
	// template.
	if resourcePropertiesValue, hasResourceProperties := targetModel["resourceProperties"]; hasResourceProperties {
		resourceProperties = resourcePropertiesValue.(map[string]interface{})
	}
	// log.Printf("%s", resourceProperties)

	// The code below needs to validate not only if `Status` for
	// `VersioningConfiguration` is set to `Enabled`, but also if
	// all the other parent properties are present in the
	// template.
	versioningConfiguration := make(map[string]interface{})
	if versioningConfigurationValue, hasVersioningConfiguration := resourceProperties["VersioningConfiguration"]; hasVersioningConfiguration {
		versioningConfiguration = versioningConfigurationValue.(map[string]interface{})
	}
	// log.Printf("%s", versioningConfiguration)

	versioningConfigurationStatus := ""
	if versioningConfigurationStatusValue, hasVersioningConfigurationStatus := versioningConfiguration["Status"]; hasVersioningConfigurationStatus {
		versioningConfigurationStatus = versioningConfigurationStatusValue.(string)
	}
	// log.Printf("%s", versioningConfigurationStatus)

	if versioningConfigurationStatus != "Enabled" {
		message := "Versioning not set or not enabled for the S3 bucket."
		log.Printf(message)
		// Return FAILED to the hook, using a payload format
		// that the hook expects: a data structure that
		// contains information on status, error code,
		// message, callback context, and callback delay in
		// seconds. This format is modeled after a
		// `ProgressEvent` object:
		// https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-progressevent.html
		response := map[string]interface{}{
			"status":               "FAILED",
			"errorCode":            "NonCompliant",
			"message":              message,
			"callbackContext":      nil,
			"callbackDelaySeconds": 0,
		}
		return &response, nil
	}

	// Return success if the resource is compliant.
	message := "Versioning is enabled for the S3 bucket."
	log.Printf(message)
	response := map[string]interface{}{
		"status":               "SUCCESS",
		"errorCode":            nil,
		"message":              message,
		"callbackContext":      nil,
		"callbackDelaySeconds": 0,
	}
	return &response, nil
}

func stringsSliceHas(stringsSlice []string, inputString string) bool {
	for _, stringInSlice := range stringsSlice {
		if stringInSlice == inputString {
			return true
		}
	}
	return false
}

func main() {
	lambda.Start(HandleRequest)
}
