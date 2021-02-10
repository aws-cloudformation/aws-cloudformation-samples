# Managed VS Code Remote Dev Environments

The `AWSSamples::Devtools::Devinstance` resource manages an EC2 instance and additional services that make a great dev environment for the [Visual Studio Code Remote - Containers](https://code.visualstudio.com/docs/remote/containers) extension. VS Code and other IDEs like Cloud9 are popularizing remote dev environments, which in general offer the following benefits:

- Ability to acquire computing resources (CPU, RAM, GPU...) as needed and tear them down when idle
- Don't be restricted by the hardware limits of the local machine
- Try different CPU architectures and hardware variants with minimal effort (e.g. ARM)
- Enjoy a consistent developer experience from any device
- Easily recreate the dev environment with automation if something went terribly wrong

The `Devinstance` resource supports this in the following ways:

- **The developer can choose from a wide variety of instance types**, depending on the requirements (currently, only instances with hibernate support are allowed, although technically anything should work)

- **Dev environment as code:** With [VS Code Remote Containers]((https://code.visualstudio.com/docs/remote/containers)), the developer connects to the instance via VS Code, which builds and starts a container defined by a `Dockerfile` in the developer's local project directory. The instance is preconfigured with Docker to allow VS Code to use it as a remote environment.

- **The instance is cattle, but your data is persistent:** The developer can update the `Devinstance` resource to change the instance type, while not losing any data. This is possible because a persistent EBS volume is used to store the developer's workspace that is mounted into the Docker container. This volume is automatically moved between instances and is protected from deletion (will remain even after the resource is deleted).

- **The size of the EBS volume can be increased at any time** by updating the resource (currently triggers the recreation of the instance, which might feel like overkill but is a nice way to stop all processes before changing volume properties). The filesystem size is extendend automatically.

- **The instance has a stable hostname, even throughout recreation**, so the configuration in VS Code (the SSH URI) always stays the same. 

## Installing the resource type

This resource type is built with the [community Typescript plugin for CloudFormation](https://github.com/eduardomourar/cloudformation-cli-typescript-plugin):

```
pip install git+https://github.com/eduardomourar/cloudformation-cli-typescript-plugin.git@v0.5.0#egg=cloudformation-cli-typescript-plugin
```

Note that as of this writing, the Typescript plugin does only support cfn cli version 0.1.x. You will get an error during `cfn submit` when you try to use a higher version.

After checking out this repository,

```
git clone https://github.com/hypescaler/aws-vscode-remote-containers.git
```

 a complete build and submission can be started with:

```
# equals "npm install && npm run build && cfn submit --set-default"
npm run all

```

### Installing - the Docker way

The included Dockerfile has everything to build and submit the resource type. Provided that you are running on MacOS or Linux and have your AWS CLI config in `~/.aws`:

```
git clone https://github.com/hypescaler/aws-vscode-remote-containers.git
cd aws-vscode-remote-containers
docker build . -t dev-container
SRC=$(pwd) && docker run --rm -it -e SRC=$SRC -v /var/run/docker.sock:/var/run/docker.sock -v $SRC:$SRC -v ~/.aws:/root/.aws dev-container /bin/bash -c "cd \$SRC && eval \$(/home/linuxbrew/.linuxbrew/bin/brew shellenv) && npm run all"
```

If you want to use a specific AWS profile, you can add `-e AWS_PROFILE=your_profile_name` to the docker command.

## Installing and preparing VS Code

1) You need to have `ssh` installed.
2) [Install VS Code](https://code.visualstudio.com/docs/setup/setup-overview).
3) [Install the Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.

## Usage

You need to have a [key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) set up. Put the name of the key pair into the `Keypair` property in `cloudformation/template.json`. The key must be known by your ssh client. 

```
aws cloudformation create-stack --stack-name myteststack01 --template-body file://cloudformation/template.json
```

Get the output of the stack to find the SSH URI of your instance:

```
aws cloudformation describe-stacks --stack-name myteststack01

 ...
 "Outputs": [
                {
                    "OutputKey": "ssh",
                    "OutputValue": "ssh://ec2-user@ec2-3-122-69-112.eu-central-1.compute.amazonaws.com"
                }
            ],
 ...
```

Connect to the instance once via your ssh client so that you can accept the fingerprint:

```
ssh ec2-user@ec2-3-122-69-112.eu-central-1.compute.amazonaws.com
```

In this code repository, open `.vscode/settings.json` and set your SSH URI (e.g. `ssh://ec2-user@ec2-3-122-69-112.eu-central-1.compute.amazonaws.com`) for `docker.host`. 

Open this repository in VS Code, or, if you already did that, restart VS Code so that the config changes are applied.

You should now be able to open your remote environment. Click the green icon in the bottom left of the IDE and choose *Remote-Containers: Reopen in Container*. VS Code will connect with the instance, build and run a container as specified by the `Dockerfile` and `devcontainer.json` in the `.devcontainer` directory. You can customize this Dockerfile to your liking.

Once done, you will be greeted with an empty workspace - that's expected, there is no way to sync your local files with a remote environment. You'd now check out the source code for whatever project you are working on. 

To open a shell, hit F1 and start typing "terminal", then select *Terminal: Create New Integrated Terminal*.

Your workspace and home directory are backed by the mounted EBS volume, so as long as you put your data there, it will persist even if the container stops or is rebuilt. 

## Hibernate your instance

You can hibernate your instance to save costs via the AWS Console or other well-known means.

## Reconfiguring your `Devinstance` resource

You can

- change the instance type, e.g. from `m4.xlarge` to `m4.2xlarge` (others should work, too) 
- increase the EBS volume size
- change your key pair name

in `template.json` and then update your stack:

```
aws cloudformation update-stack --stack-name myteststack01 --template-body file://cloudformation/template.json
```

Any update will result in the recreation of the instance. After that, you will need to clean your `known_hosts` file from the old fingerprint and connect once via your SSH client to accept the new one.

After the update is finished, you will find that the container starts quicker than the first time (because the Docker images are preserved on the EBS volume, too) and all your files in the workspace are still there.

## Under the hood: Using CDK to simplify resource management

The resource handler uses CDK programmatically by defining a CDK App and then calling `app.synth()` to produce dynamic CloudFormation templates to manage the resources comprising a dev environment. Typically, resource handlers use the AWS SDK to create resources in an imperative way; an alternative is using a declarative approach via CDK and CloudFormation. The benefits of this approach are:

- reuse existing CDK code or CloudFormation templates
- benefit from simpler resource configuration via CDK (a single `Devinstance` resource is already made up of 15 AWS resources)
- delegate the long-running task of standing up all resources in the correct order to CloudFormation
- easily map CloudFormation states and errors to your Resource Type
- debug your deployment by testing / sharing the CloudFormation template instead of your whole handler code and benefit from a large community of CloudFormation experts

As CDK is invoked at runtime in the resource handler code, the CDK App code can react to arbitrary input values before synthesizing the CloudFormation template, thus enabling any reconfiguration of the template, e.g. depending on the current state of a resource. 

For example, in order to force a clean recreation of the EC2 instance when the instance type is changed (which is required because hibernate-enabled instances cannot change their type in-place), the CDK App code, when called, always adds a new UUID to the logical identifier of the instance, which results in CloudFormation seeing a new instance, while the old one is no longer present in the template. Such a behavior is hard to implement with plain CloudFormation templates, but the dynamic "pre-configuration" via CDK code enables almost any rearrangement of the template.

It should be possible to derive a more generalized handler framework that could take any CDK App and expose it as a Resource Type.

## Passing `cfn test`

The run the tests, you need to pass a set of AWS credentials with full permissions. The tester is injecting credentials that aren't authorized to make IAM calls, which is required for the CloudFormation template to be deployed.

1. Make a copy of `env.template.json` as `env.json` and add an access key ID and secret access key (with full permissions) to it. 
2. Start the funtion locally via `sam local start-lambda -n env.json` 
3. Run the tests with `cfn test`

**Note: Make sure to delete the superfluous EBS volumes afterwards, as they are not deleted with the resource.**

##  Using the CDK stack directly

You can apply the stack directly for testing purposes (or because you do not want to consume it as a Resource Type).

```
npm install
npm run build

# After that, you can use cdk cli commands like:

# Create the CloudFormation template
cdk --app dist/devinstance-app.js synth DevinstanceStack

# Show diff to currently deployed stack
cdk --app dist/devinstance-app.js diff DevinstanceStack

# Deploy the stack
cdk --app dist/devinstance-app.js deploy DevinstanceStack
```