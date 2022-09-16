# AWSSamples::EC2::ImportKeyPair

- [Overview](#Overview)

- [Usage](#Usage)

- [Resource type deployment with StackSets](#Resource-type-deployment-with-StackSets)

- [Tests](#Tests)

  - [Unit tests](#Unit-tests)

  - [Contract tests](#Contract-tests)

- [Example schema and handlers](#Example-schema-and-handlers)

  - [Type hints](#Type-hints)


## Overview
This is an example resource type for [AWS CloudFormation](https://aws.amazon.com/cloudformation/) that describes a key pair you wish to import.  For more information on creating resource types, see [Creating resource types](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html) in the CloudFormation Command Line Interface documentation.


## Usage
For more information on syntax usage for this example resource type, see the [docs/README.md](docs/README.md) page.

If you choose to activate and test this example resource type in your AWS account:

- install and configure the [CloudFormation Command Line Interface (CLI)](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)
- clone this repository on your workstation
- on your workstation, change directory to the directory where this `README.md` file is located
- register the example resource type with CloudFormation as a private extension in the AWS account and region where you want to use the resource.  As part of this process, you leverage CloudFormation to describe and create, in your account, an [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) role, that is assumed by CloudFormation when _Create, Read, Update, Delete, List_ (CRUDL) operations occur to manage the resource on your behalf.  The IAM role policy will include actions specified in the [handlers](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers) section of the JSON schema file for the resource.  In this example, the _handlers_ section of the `awssamples-ec2-importkeypair.json` schema file describes actions such as `ec2:CreateTags`, `ec2:DeleteKeyPair`, `ec2:DeleteTags`, `ec2:DescribeKeyPairs`, `ec2:ImportKeyPair`, where applicable in relevant `create`, `read`, `update`, `delete`, and `list` handlers
  - choose to use the [submit](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html) command of the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html) to register the example resource type, e.g.: `cfn generate && cfn submit --set-default --region REGION_YOU_WISH_TO_USE`
  - verify the example resource type is registered in the account and region you chose: navigate to the AWS CloudFormation console, and from _Registry_ choose _Activated extensions_; you should find the `AWSSamples::EC2::ImportKeyPair` resource type in the _Resource types_ list
  - for more information, see [register private extensions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html)
- test the example resource by using the `examples/example-template-import-keypair.yaml` template:
  - create an example key pair on your workstation.  For example, with the `ssh-keygen` command: `ssh-keygen -t rsa -C "YOUR_COMMENT_" -f ~/.ssh/YOUR_KEY`
  - the `ssh-keygen` command you ran should produce a file called e.g., `YOUR_KEY`, that is your private key, and another file called e.g., `YOUR_KEY.pub`.  Please note the `.pub` extension in the second file, that is the public key you will import.  Open, with a text editor of your choice, the file with the `.pub` extension (public key material): you will need to copy and paste its content when specifying the public key material in the next step
  - create a CloudFormation stack off of the template mentioned earlier: specify a name for the key pair to import, and the public key material you wish to use, that is the content of the file with the `.pub` extension mentioned earlier
  - CloudFormation will leverage the example resource type described in the template to import the public key in your account and region


## Resource type deployment with StackSets
You can choose to use [StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to make this resource type available in other regions for your account.  For this, you can choose to use the `examples/resource-type-deployment-stack.yaml` sample CloudFormation template that describes deployment-related resources for this resource type with code, and then use StackSets to deploy the resource type across AWS regions you need.  To get started, follow steps shown next:

- Create a stack with the `examples/resource-type-deployment-bucket.yaml` sample template, that describes an [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket where you will store the resource type archive file you'll generate, and the `examples/resource-type-deployment-stack.yaml` template file that you will use with StackSets.  Choose a stack creation method, such as via the AWS CloudFormation console, or the AWS Command Line interface: for more information, see [Working with stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html).

- When done, navigate to the **Outputs** tab for your stack in the AWS CloudFormation console, and note the value for the `BucketName` output key: this is the name of the bucket you created in the previous step, and you will use this bucket next.

- Next, create the ZIP archive for this resource type content with the following commands:

```shell
cfn generate && cfn submit --dry-run
```

- The last command above should have created the `awssamples-ec2-importkeypair.zip` archive in the same directory as this `README.md` file.  Upload the ZIP archive to the bucket whose name you noted earlier.  Use a method of your choice, such as the S3 console or the AWS CLI; for more information, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html).

- Next, upload the `resource-type-deployment-stack.yaml` template file - that you can find in the `examples/` directory - to your bucket as well.

- In this next step, prepare your account for it to work with StackSets, by referring to [Prerequisites for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html).  For example, if you choose to use [Self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html#prereqs-self-managed-permissions), refer to [Set up basic permissions for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html#stacksets-prereqs-accountsetup) to create `AWSCloudFormationStackSetAdministrationRole` and `AWSCloudFormationStackSetExecutionRole` roles with provided templates.

- Next, [create](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html) your StackSet.  As an example, the following process describes next steps if you choose to use the AWS CloudFormation [console](https://console.aws.amazon.com/cloudformation/) and [self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html).

- From the navigation pane in the console, choose **StackSets**, and then **Create StackSet**.

- In the **Prerequisite - Prepare template** section, specify the Amazon S3 URL of the `resource-type-deployment-stack.yaml` template you uploaded to your bucket earlier.  Alternatively, choose to upload the `resource-type-deployment-stack.yaml` template file.

- Specify a name for your StackSet, for example: `AWSSamples-EC2-ImportKeyPair-deployment`.

- For the `SchemaHandlerPackage` parameter, specify the URL of the ZIP file you uploaded to your bucket earlier.  Choose **Next** when done specifying parameter values.

- In **Execution configuration**, choose `Active` for **Managed execution**.  Choose **Next**.

- Specify your account number in the **Account numbers** section for **Accounts**.

- In the **Regions** section, specify regions where you wish to deploy this resource type.

- In **Deployment options**, choose `Parallel` for **Region Concurrency**.  Choose **Next**.

- In the **Review** page, review your selections.  Choose **I acknowledge that AWS CloudFormation might create IAM resources** at the bottom of the page, and choose **Next**.

- Your StackSet creation process should start shortly; you can review the status in the **Operations** pane in **StackSet details**.

At the end of the process, your resource type should have been deployed into target regions you chose earlier.


## Tests
Example unit tests and information on how to run unit and contract tests are shown next.


### Unit tests
Example unit tests are available in `src/awssamples_ec2_importkeypair/tests`, and are meant to be used with [pytest](https://docs.pytest.org/) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/).  To run example unit tests:

- choose to install `pytest-cov` with `pip`; for example: `pip install pytest-cov`
- choose to install `cloudformation-cli-python-lib` with `pip`; for example: `pip install cloudformation-cli-python-lib`
- you should now be able to run unit tests for this example resource type; make sure to be in the same directory where this README.md file is located, and choose to run unit tests with: `pytest --cov src --cov-report term-missing`.  The `.coveragerc` configuration file (located in the same directory as this README.md file) will be used to read configuration preferences, that include omitting a number of files as part of unit test runs and reports.


### Contract tests
Contract tests help you validate the resource type you're developing works as you expect.  For more information, see [Testing resource types using contract tests](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html) in the AWS documentation.  You use the [test](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-test.html) command of the CloudFormation CLI to run contract tests in your account: in this example, you will specify example values to create, update, delete EC2 key pair resources (named with an `example-keypair-for-contract-tests` prefix) in your account and region.  For contract tests runs, you can choose to specify an execution role that contract tests can assume; alternatively, contract tests will use your environment credentials or credentials specified in the Boto3 credentials chain.

When you run contract tests, you pass in input values; for more information, see [Specifying input data for use in contract tests](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html#resource-type-test-input-data).  Contract tests for this example resource type use `create`, `update` and `invalid` input data from files in the `inputs` directory.  If you inspect create- and update-related input files content in the aforementioned directory, you will see a line such as `"PublicKeyMaterial": "{{KeyPairPublicKeyForContractTests}}",`: this line is used by contract tests to take, as an input, the public key material that you will use to run contract tests, and input data in this case is taken from a CloudFormation stack you will need to create before running contract tests.  To run contract tests for this resource type:

- create a CloudFormation stack using the `examples/example-template-contract-tests-input.yaml` template; for the `KeyPairPublicKey` input parameter, provide the public key material you wish to use for your contract tests.  This stack will create an [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) resource in your account and region, to store the public key material for your reference.  In the `Outputs` section of this stack, you will find an `KeyPairPublicKey` output exported as `KeyPairPublicKeyForContractTests`, which is the value contract tests in this example will read
- run the Local Lambda Service: `sam local start-lambda`; for more information, see [Testing resource types locally using SAM](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html#resource-type-develop-test)
- run contract tests as follows: `cfn generate && cfn submit --dry-run && cfn test`
- when you are done running contract tests/submitting the module, you can choose to delete the stack you created as part of this contract tests section


## Example schema and handlers
For more information on this example resource type, see the following files:

1. JSON schema describing the example resource: `awssamples-ec2-importkeypair.json`
2. resource handlers for `CREATE`, `READ`, `UPDATE`, `DELETE`, `LIST` actions: `src/awssamples_ec2_importkeypair/handlers.py`

> Don't modify `models.py` by hand, any modifications will be overwritten when the `generate` or `package` commands are run.

When implementing the resource, each function must always return a `ProgressEvent`; example:

```python
ProgressEvent(
    # Required
    # Must be one of OperationStatus.IN_PROGRESS, OperationStatus.FAILED, OperationStatus.SUCCESS
    status=OperationStatus.IN_PROGRESS,
    # Required on SUCCESS (except for LIST where resourceModels is required)
    # The current resource model after the operation; instance of ResourceModel class
    resourceModel=model,
    resourceModels=None,
    # Required on FAILED
    # Customer-facing message, displayed in e.g. CloudFormation stack events
    message="",
    # Required on FAILED: a HandlerErrorCode
    errorCode=HandlerErrorCode.InternalFailure,
    # Optional
    # Use to store any state between re-invocation via IN_PROGRESS
    callbackContext={},
    # Required on IN_PROGRESS
    # The number of seconds to delay before re-invocation
    callbackDelaySeconds=0,
)
```

Failures can be passed back to CloudFormation by either raising an exception from `cloudformation_cli_python_lib.exceptions`, or setting the ProgressEvent's `status` to `OperationStatus.FAILED` and `errorCode` to one of `cloudformation_cli_python_lib.HandlerErrorCode`. There is a static helper function, `ProgressEvent.failed`, for this common case.


### Type hints
We hope they'll be useful for getting started quicker with an IDE that support type hints. Type hints are optional - if your code doesn't use them, it will still work.
