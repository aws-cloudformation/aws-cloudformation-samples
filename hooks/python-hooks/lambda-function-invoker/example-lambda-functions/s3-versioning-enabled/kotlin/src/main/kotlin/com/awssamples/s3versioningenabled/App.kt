/** Example Lambda function called by AWSSamples::LambdaFunctionInvoker::Hook. */
package com.awssamples.s3versioningenabled

import com.amazonaws.services.lambda.runtime.Context
import com.amazonaws.services.lambda.runtime.RequestStreamHandler
import com.amazonaws.services.lambda.runtime.logging.LogLevel
import org.json.JSONObject
import java.io.BufferedReader
import java.io.InputStream
import java.io.InputStreamReader
import java.io.OutputStream
import java.io.OutputStreamWriter
import java.util.stream.Collectors

/**
 * Example Lambda function called by AWSSamples::LambdaFunctionInvoker::Hook.
 *
 * @see <a href=https://docs.aws.amazon.com/lambda/latest/dg/java-handler.html>Lambda Handler</a>
 * for more information
 */
class App : RequestStreamHandler {
    /**
     * If you choose to invoke the hook for all the invocation points (default behavior), and to not
     * set `TargetFilters` for your hook, you can define, in the example Lambda function code, for
     * which invocation points to run the code in this function. It is important to understand that
     * if you choose this method as opposed to target filters, the hook will be invoked anyway for
     * all of the AWS resource types in your templates across all the invocation points, and you'll
     * be billed for all the invocations. To use this feature, comment out the line for
     * `hookInvocationPoints` that corresponds to the invocation point you do not want to run.
     * Later on in this example code, you'll find a conditional block that will return SUCCESS if
     * the current invocation point is something you do not need to evaluate on during the current
     * invocation.
     */
    val hookInvocationPoints =
        setOf(
            "CREATE_PRE_PROVISION",
            "UPDATE_PRE_PROVISION",
            "DELETE_PRE_PROVISION",
        )

    /**
     * Add AWS resource type target that this code will evaluate. This example function validates if
     * versioning is enabled for an S3 bucket; hence, add AWS::S3::Bucket here.
     */
    val targetNames =
        setOf(
            "AWS::S3::Bucket",
        )

    /**
     * The name of the charset to use when reading the input request for this Lambda function's
     * code.
     */
    val inputStreamCharset = "UTF-8"

    /**
     * The name of the charset to use when outputting responses from this Lambda function's code.
     */
    val outputStreamCharset = "UTF-8"

    /**
     * Defines this Lambda function's entry point; accepts an [inputStream] InputStream object, an
     * [outputStream], and the function's [context].
     *
     * @param inputStream - the InputStream input
     * @param outputStream - the OutputStream output
     * @param context - the function's Context
     */
    override fun handleRequest(
        inputStream: InputStream,
        outputStream: OutputStream,
        context: Context,
    ) {
        val logger = context.getLogger()

        val inputStreamReader = InputStreamReader(inputStream, inputStreamCharset)
        val bufferedReader = BufferedReader(inputStreamReader)
        val inputJson = bufferedReader.lines().collect(Collectors.joining()).trim()

        val event = JSONObject(inputJson)

        // Get the entire request from the input event.
        val request = event.getJSONObject("request")
        val hookContext = request.getJSONObject("hookContext")

        // Get the invocation point for the hook that is calling this
        // function; for example: `CREATE_PRE_PROVISION`.
        val invocationPoint = hookContext.getString("invocationPoint")
        logger.log("Invocation point: " + invocationPoint, LogLevel.INFO)

        // Get the name of the resource type target that invoked the
        // hook. For example: `AWS::S3::Bucket`.
        val targetName = hookContext.getString("targetName")
        logger.log("Target name: " + targetName, LogLevel.INFO)

        // If you're not using TargetFilters for the hook that invokes
        // this function, return SUCCESS immediately if you do not
        // want to perform policy-as-code validation for a given hook
        // invocation point that is commented out in
        // hookInvocationPoints at the beginning of this code, or for
        // target names you've not added to targetNames above.
        if (!hookInvocationPoints.contains(invocationPoint) || !targetNames.contains(targetName)) {
            val message = "Skipping " + targetName + " evaluation for " + invocationPoint + "."
            logger.log(message, LogLevel.INFO)
            val response = JSONObject()
            response.put("status", "SUCCESS")
            response.put("errorCode", JSONObject.NULL)
            response.put("message", message)
            response.put("callbackContext", emptyMap<String, Object>())
            response.put("callbackDelaySeconds", 0)
            // logger.log(response.toString(), LogLevel.DEBUG)
            val outputStreamWriter = OutputStreamWriter(outputStream, outputStreamCharset)
            outputStreamWriter.write(response.toString())
            outputStreamWriter.close()
            return
        }

        // Get the model of the resource type target.
        val targetModel = hookContext.getJSONObject("targetModel")

        // Get the resource properties of the target resource type;
        // this should include the properties for the target resource
        // type that the user specified in their CloudFormation
        // template.
        val resourceProperties =
            if (targetModel.has("resourceProperties")) {
                targetModel.getJSONObject("resourceProperties")
            } else {
                JSONObject()
            }
        // logger.log(resourceProperties.toString(), LogLevel.DEBUG)

        // The code below needs to validate not only if `Status` for
        // `VersioningConfiguration` is set to `Enabled`, but also if
        // all the other parent properties are present in the
        // template.
        val versioningConfiguration =
            if (resourceProperties.has("VersioningConfiguration")) {
                resourceProperties.getJSONObject("VersioningConfiguration")
            } else {
                JSONObject()
            }
        val versioningConfigurationStatus =
            if (versioningConfiguration.has("Status")) {
                versioningConfiguration.getString("Status")
            } else {
                ""
            }

        if (!versioningConfigurationStatus.equals("Enabled")) {
            val message = "Versioning not set or not enabled for the S3 bucket."
            logger.log(message, LogLevel.ERROR)
            // Return FAILED to the hook, using a payload format that
            // the hook expects: a data structure that contains
            // information on status, error code, message, callback
            // context, and callback delay in seconds. This format is
            // modeled after a `ProgressEvent` object:
            // https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-progressevent.html
            val response = JSONObject()
            response.put("status", "FAILED")
            response.put("errorCode", "NonCompliant")
            response.put("message", message)
            response.put("callbackContext", emptyMap<String, Object>())
            response.put("callbackDelaySeconds", 0)
            logger.log(message, LogLevel.ERROR)
            // logger.log(response.toString(), LogLevel.DEBUG)
            val outputStreamWriter = OutputStreamWriter(outputStream, outputStreamCharset)
            outputStreamWriter.write(response.toString())
            outputStreamWriter.close()
            return
        } else {
            // Return success if the resource is compliant.
            val message = "Versioning is enabled for the S3 bucket."
            logger.log(message, LogLevel.INFO)
            val response = JSONObject()
            response.put("status", "SUCCESS")
            response.put("errorCode", JSONObject.NULL)
            response.put("message", message)
            response.put("callbackContext", emptyMap<String, Object>())
            response.put("callbackDelaySeconds", 0)
            // logger.log(response.toString(), LogLevel.DEBUG)
            val outputStreamWriter = OutputStreamWriter(outputStream, outputStreamCharset)
            outputStreamWriter.write(response.toString())
            outputStreamWriter.close()
            return
        }
    }
}
