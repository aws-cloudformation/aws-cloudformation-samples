# CfnModuleApiGatewayCustomDomain
CloudFormation module to create a custom domain for API Gateway REST API.

This module creates the Custom Domain for the API Gateway, the base path mapping for the domain, and Route53 alias records.

## Getting Started
This custom module creates the following resources:
  
- ApiGateway Domain (`AWS::ApiGateway::DomainName`)
- ApiGateway base path mapping	(`AWS::ApiGateway::BasePathMapping`)
- Private hosted zone IPv4 and IPv6 Route53 alias records (`AWS::Route53::RecordSet`), if `PrivateHostedZoneId` value is defined
- Public hosted zone IPv4 and IPv6 Route53 alias records (`AWS::Route53::RecordSet`), if `PublicHostedZoneId` value is defined

## Input Parameters
| Name                | Type   | Required?   | Default | Comments                                                                          |
| ------------------- | ------ | ----------- | ------- | --------------------------------------------------------------------------------- |
| ApiBasePath         | String | No          | `''`    |                                                                                   |
| ApiId               | String | Yes         |         |                                                                                   |
| ApiStage            | String | Yes         |         |                                                                                   |
| ApiType             | String | Yes         | `EDGE`  | Allowed Values: `EDGE` or `REGIONAL`                                              |
| CertificateArn      | String | Yes         |         |                                                                                   |
| CustomDomainName    | String | Yes         |         |                                                                                   |
| PrivateHostedZoneId | String | Conditional | `''`    | Either or both of `PrivateHostedZoneId` and `PublicHostedZoneId` must be defined. |
| PublicHostedZoneId  | String | Conditional | `''`    | Either or both of `PrivateHostedZoneId` and `PublicHostedZoneId` must be defined. |

## Usage
Example usage
```json
{
    "Resources": {
        "MyModule": {
            "Type": "AWSSamples::ApiGateway::CustomDomain::MODULE",
            "Properties": {
                "CertificateArn": "CertificateArn",
                "CustomDomainName": "CustomDomainName",
                "ApiType": "ApiType",
                "ApiId": "ApiId",
                "ApiStage": "ApiStage",
                "ApiBasePath": "ApiBasePath",
                "PrivateHostedZoneId": "PrivateHostedZoneId",
                "PublicHostedZoneId": "PublicHostedZoneId"
            }
        }
    }
}
```

Sample template using the module: [apigw-hello-world.yml](apigw-hello-world.yml)