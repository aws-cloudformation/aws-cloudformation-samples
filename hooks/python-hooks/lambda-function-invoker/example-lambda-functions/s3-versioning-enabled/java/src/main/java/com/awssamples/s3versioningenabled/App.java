/**
 * Example Lambda function called by AWSSamples::LambdaFunctionInvoker::Hook.
 */

package com.awssamples.s3versioningenabled;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.Set;
import java.util.stream.Collectors;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestStreamHandler;
import com.amazonaws.services.lambda.runtime.logging.LogLevel;

import org.json.JSONObject;

/**
 * Example Lambda function called by AWSSamples::LambdaFunctionInvoker::Hook.
 *
 * @see <a
 *      href=https://docs.aws.amazon.com/lambda/latest/dg/java-handler.html>Lambda
 *      Java Handler</a> for more information
 */
public class App implements RequestStreamHandler {

    /**
     * If you choose to invoke the hook for all the invocation points
     * (default behavior), and to not set `TargetFilters` for your
     * hook, you can define, in the example Lambda function code, for
     * which invocation points to run the code in this function. It is
     * important to understand that if you choose this method as
     * opposed to target filters, the hook will be invoked anyway for
     * all of the AWS resource types in your templates across all the
     * invocation points, and you'll be billed for all the
     * invocations. To use this feature, comment out the line for
     * `HOOK_INVOCATION_POINTS` that corresponds to the invocation
     * point you do not want to run. Later on in this example code,
     * you'll find a conditional block that will return SUCCESS if the
     * current invocation point is something you do not need to
     * evaluate on during the current invocation.
     */
    public static final Set<String> HOOK_INVOCATION_POINTS = Set.of(
            "CREATE_PRE_PROVISION",
            "UPDATE_PRE_PROVISION",
            "DELETE_PRE_PROVISION");

    /**
     * Add AWS resource type target that this code will evaluate. This
     * example function validates if versioning is enabled for an S3
     * bucket; hence, add AWS::S3::Bucket here.
     */
    public static final Set<String> TARGET_NAMES = Set.of(
            "AWS::S3::Bucket");

    /**
     * The name of the charset to use when reading the input request
     * for this Lambda function's code.
     */
    private static final String INPUT_STREAM_CHARSET = "UTF-8";

    /**
     * The name of the charset to use when outputting responses from
     * this Lambda function's code.
     */
    private static final String OUTPUT_STREAM_CHARSET = "UTF-8";

    /**
     * Defines this Lambda function's entry point.
     *
     * @param inputStream  - the {@link InputStream} input
     * @param outputStream - the {@link OutputStream} output
     * @param context      - the function's {@link Context}
     */
    @Override
    public void handleRequest(final InputStream inputStream, final OutputStream outputStream, final Context context)
            throws IOException {
        final LambdaLogger logger = context.getLogger();

        try {
            final InputStreamReader inputStreamReader = new InputStreamReader(inputStream, INPUT_STREAM_CHARSET);
            final BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
            final String inputJson = bufferedReader.lines().collect(Collectors.joining()).trim();

            final JSONObject event = new JSONObject(inputJson);

            // Get the entire request from the input event.
            final JSONObject request = event.getJSONObject("request");
            final JSONObject hookContext = request.getJSONObject("hookContext");

            // Get the invocation point for the hook that is calling
            // this function; for example: `CREATE_PRE_PROVISION`.
            final String invocationPoint = hookContext.getString("invocationPoint");
            logger.log("Invocation point: " + invocationPoint, LogLevel.INFO);

            // Get the name of the resource type target that invoked
            // the hook. For example: `AWS::S3::Bucket`.
            final String targetName = hookContext.getString("targetName");
            logger.log("Target name: " + targetName, LogLevel.INFO);

            // If you're not using TargetFilters for the hook that
            // invokes this function, return SUCCESS immediately if
            // you do not want to perform policy-as-code validation
            // for a given hook invocation point that is commented out
            // in HOOK_INVOCATION_POINTS at the beginning of this
            // code, or for target names you've not added to
            // TARGET_NAMES above.
            if (!HOOK_INVOCATION_POINTS.contains(invocationPoint) || !TARGET_NAMES.contains(targetName)) {
                final String message = "Skipping " + targetName + " evaluation for " + invocationPoint + ".";
                logger.log(message, LogLevel.INFO);
                final JSONObject response = new JSONObject();
                response.put("status", "SUCCESS");
                response.put("errorCode", JSONObject.NULL);
                response.put("message", message);
                response.put("callbackContext", Collections.EMPTY_MAP);
                response.put("callbackDelaySeconds", 0);
                // logger.log(response.toString(), LogLevel.DEBUG);
                final OutputStreamWriter outputStreamWriter = new OutputStreamWriter(outputStream,
                        OUTPUT_STREAM_CHARSET);
                outputStreamWriter.write(response.toString());
                outputStreamWriter.close();
                return;
            }

            // Get the model of the resource type target.
            final JSONObject targetModel = hookContext.getJSONObject("targetModel");

            // Get the resource properties of the target resource
            // type; this should include the properties for the target
            // resource type that the user specified in their
            // CloudFormation template.
            final JSONObject resourceProperties = targetModel.has("resourceProperties")
                    ? targetModel.getJSONObject("resourceProperties")
                    : new JSONObject();
            // logger.log(resourceProperties.toString(), LogLevel.DEBUG);

            // The code below needs to validate not only if `Status`
            // for `VersioningConfiguration` is set to `Enabled`, but
            // also if all the other parent properties are present in
            // the template.
            final JSONObject versioningConfiguration = resourceProperties.has("VersioningConfiguration")
                    ? resourceProperties.getJSONObject("VersioningConfiguration")
                    : new JSONObject();
            final String versioningConfigurationStatus = versioningConfiguration.has("Status")
                    ? versioningConfiguration.getString("Status")
                    : "";

            if (!versioningConfigurationStatus.equals("Enabled")) {
                final String message = "Versioning not set or not enabled for the S3 bucket.";
                logger.log(message, LogLevel.ERROR);
                // Return FAILED to the hook, using a payload format
                // that the hook expects: a data structure that
                // contains information on status, error code,
                // message, callback context, and callback delay in
                // seconds. This format is modeled after a
                // `ProgressEvent` object:
                // https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-progressevent.html
                final JSONObject response = new JSONObject();
                response.put("status", "FAILED");
                response.put("errorCode", "NonCompliant");
                response.put("message", message);
                response.put("callbackContext", Collections.EMPTY_MAP);
                response.put("callbackDelaySeconds", 0);
                logger.log(message, LogLevel.ERROR);
                // logger.log(response.toString(), LogLevel.DEBUG);
                final OutputStreamWriter outputStreamWriter = new OutputStreamWriter(outputStream,
                        OUTPUT_STREAM_CHARSET);
                outputStreamWriter.write(response.toString());
                outputStreamWriter.close();
                return;
            } else {
                // Return success if the resource is compliant.
                final String message = "Versioning is enabled for the S3 bucket.";
                logger.log(message, LogLevel.INFO);
                final JSONObject response = new JSONObject();
                response.put("status", "SUCCESS");
                response.put("errorCode", JSONObject.NULL);
                response.put("message", message);
                response.put("callbackContext", Collections.EMPTY_MAP);
                response.put("callbackDelaySeconds", 0);
                // logger.log(response.toString(), LogLevel.DEBUG);
                final OutputStreamWriter outputStreamWriter = new OutputStreamWriter(outputStream,
                        OUTPUT_STREAM_CHARSET);
                outputStreamWriter.write(response.toString());
                outputStreamWriter.close();
                return;
            }
        } catch (final Exception exception) {
            final String message = exception.getMessage();
            // Default fallback to FAILED in the event of other errors.
            final JSONObject response = new JSONObject();
            response.put("status", "FAILED");
            response.put("errorCode", "InternalFailure");
            response.put("message", message);
            response.put("callbackContext", Collections.EMPTY_MAP);
            response.put("callbackDelaySeconds", 0);
            logger.log(message, LogLevel.ERROR);
            final OutputStreamWriter outputStreamWriter = new OutputStreamWriter(outputStream,
                    OUTPUT_STREAM_CHARSET);
            outputStreamWriter.write(response.toString());
            outputStreamWriter.close();
            return;
        }
    }
}
