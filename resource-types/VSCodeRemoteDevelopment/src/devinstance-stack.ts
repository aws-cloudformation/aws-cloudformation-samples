import * as cdk from '@aws-cdk/core'
import * as ec2 from '@aws-cdk/aws-ec2'
import * as ecs from '@aws-cdk/aws-ecs'
import * as iam from '@aws-cdk/aws-iam'
import * as efs from '@aws-cdk/aws-efs'
import * as fs from 'fs'
import { v4 as uuidv4 } from 'uuid'

export class DevinstanceStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps, canary: boolean = false) {
    super(scope, id, props);

    const keypairParameter = new cdk.CfnParameter(this, "keypair", {
      type: "String",
      default: 'dev',
      description: "The name of the SSH keypair to connect to your dev environment."
    })

    const instanceTypeParameter = new cdk.CfnParameter(this, "instanceType", {
      type: "String",
      default: 'm4.xlarge',
      description: "The instance type for your dev environment."
    })

    const diskSizeParameter = new cdk.CfnParameter(this, "diskSize", {
      type: "Number",
      default: 100,
      description: "The size of the persistent volume for your dev environment in Gibibytes."
    })

    const vpc = new ec2.Vpc(this, 'DevVpc', {
      maxAzs: 1,
      subnetConfiguration: [{
        cidrMask: 26,
        name: 'publicSubnet',
        subnetType: ec2.SubnetType.PUBLIC,
      }],
      natGateways: 0
    })

    const volume = new ec2.Volume(this, 'Volume', {
      availabilityZone: vpc.availabilityZones[0],
      size: cdk.Size.gibibytes(diskSizeParameter.valueAsNumber),
    });

    const cfnVolume = volume.node.findChild('Resource') as cdk.CfnResource
    cfnVolume.applyRemovalPolicy(cdk.RemovalPolicy.RETAIN);

    const publicSubnet = vpc.selectSubnets({
      subnetType: ec2.SubnetType.PUBLIC
    })

    const ec2Sg = new ec2.SecurityGroup(this, "ec2Sg", {
      vpc: vpc
    })

    ec2Sg.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(22))

    const instance = new ec2.Instance(this, "Devinstance-" + uuidv4(), {
      vpc: vpc,
      vpcSubnets: publicSubnet,
      instanceType: new ec2.InstanceType(instanceTypeParameter.valueAsString),
      machineImage: ec2.MachineImage.latestAmazonLinux({
        generation: ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
      }),
      keyName: keypairParameter.valueAsString,
      securityGroup: ec2Sg,
      blockDevices: [
        {
          deviceName: '/dev/xvda',
          volume: ec2.BlockDeviceVolume.ebs(100, { encrypted: true }),
        }
      ]
    })

    const volumesPolicy = new iam.PolicyStatement({
      resources: ['*'],
      actions: [
        "ec2:DescribeAvailabilityZones",
        "ec2:DescribeInstances",
        "ec2:DescribeVolumes",
        "ec2:DescribeVolumeAttribute",
        "ec2:DescribeVolumeStatus",
        "ec2:DescribeSnapshots",
        "ec2:DescribeSnapshotAttribute",
        "ec2:DescribeTags"
      ]
    })

    instance.addToRolePolicy(volumesPolicy)

    const targetDevice = '/dev/xvdz'
    const mointPoint = '/mnt/ebs/fs1'

    const attachGrant = volume.grantAttachVolumeByResourceTag(instance.grantPrincipal, [instance]);
    const detachGrant = volume.grantDetachVolumeByResourceTag(instance.grantPrincipal, [instance]);

    const eIp = new ec2.CfnEIP(this, "DevIp");
    const ec2Assoc = new ec2.CfnEIPAssociation(this, "Ec2Association", {
      eip: eIp.ref,
      instanceId: instance.instanceId
    });

    const cfnInstance = instance.node.defaultChild as ec2.CfnInstance
    cfnInstance.hibernationOptions = { configured: true }

    instance.userData.addCommands(
      "yum check-update -y",
      "yum upgrade -y",
    )

    instance.userData.addCommands(`
aws configure set region ${this.region}
INST_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id) 
VOL_ID=${volume.volumeId}
# aws ec2 detach-volume --force --volume-id $VOL_ID
VOLUME_STATUS=''
until [ "$VOLUME_STATUS" == \\\"available\\\" ]; do
    echo "Waiting for volume $VOL_ID to be available for attaching..."
    VOLUME_STATUS=$(aws ec2 describe-volumes --volume-ids $VOL_ID --query 'Volumes[0].State')
    echo "Volume status is $VOLUME_STATUS"
    sleep 5
done
echo "Attaching volume..."
aws ec2 attach-volume --volume-id $VOL_ID --instance-id $INST_ID --device ${targetDevice}
while ! test -e ${targetDevice}; do sleep 1; done
`
    )

    instance.userData.addCommands(
      `mkfs.xfs ${targetDevice}`,
      `mkdir -p ${mointPoint}`,
      `mount ${targetDevice} ${mointPoint}`,
      `xfs_growfs -d ${mointPoint}`,
      `echo "${targetDevice} ${mointPoint}   xfs  defaults,nofail  0  2" >> /etc/fstab`,
      `mkdir -p ${mointPoint}/home ${mointPoint}/workspace ${mointPoint}/docker`)

    instance.userData.addCommands(
      `ln -s ${mointPoint}/docker /var/lib/docker`,
      "amazon-linux-extras install docker",
      "service docker start",
      "usermod -a -G docker ec2-user",
      "chkconfig docker on")

    new cdk.CfnOutput(this, 'ssh', {
      value: `ssh://ec2-user@${instance.instancePublicDnsName}`,
    });
  }

}

