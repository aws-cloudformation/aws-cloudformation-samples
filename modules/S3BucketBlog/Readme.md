# S3 Bucket Blog Cloudformation module

This Cloudformation module makes it easy and quick to deploy a S3 bucket and is the template referenced in the [blog](https://aws.amazon.com/blogs/mt/introducing-aws-cloudformation-modules/).

You can use the module by consuming it from a normal Cloudformation template as follows:

```
AWSTemplateFormatVersion: 2010-09-09
Description: Template consuming S3 Bucket Blog Module

Resources:
    Bucket: 
      Type: AWSSamples::S3::Bucket::MODULE
      Properties:
        KMSKeyAlias: MyKeyAlias
        ReadOnlyArn: arn:aws:iam::123456789012:role/bucket-read-arn
        ReadWriteArn: arn:aws:iam::123456789012:role/bucket-read-write-arn
```

The module does the following things:

- Creates a KMS Key with a Policy that allows
   - The `ReadOnlyArn` to decrypt
   - The `ReadWriteArn` to encrypt and decrypt 
- KMS Key Alias associated to the created KMS Key   
- Creates a S3 Bucket with the following configured
   - Access Control set to `BucketOwnerFullControl`
   - Configured to require encryption by the KMS key created
   - Configures `PublicAccessBlockConfiguration` to keep the bucket private
- Creates a Bucket Policy and associates it to the S3 Bucket. The bucket policy will configure
   - The requirement of https only traffic
   - Requires `PutObject` calls to be encrypted
   - Gives `ReadOnlyArn` the ability to read to the S3 Bucket
   - Gives `ReadWriteArn` the ability to read and write to the S3 Bucket
