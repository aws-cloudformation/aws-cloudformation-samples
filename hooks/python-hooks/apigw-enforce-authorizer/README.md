# AWSSamples::APIGWEnforceAuthorizer::Hook

This sample AWS CloudFormation Hook enforces [Amazon API Gateway](https://aws.amazon.com/api-gateway/) resources to have authorizers attached when created and updated.

* When creating or updating an `AWS::ApiGateway::RestApi` or `AWS::ApiGatewayV2::Api` resource, the hook will check the JSON definition specified in `Body` to see whether all sections in `paths` have `security` defined.
* When creating or updating an `AWS::ApiGateway::Method` or `AWS::ApiGatewayV2::Route`, the hook will check whether `AuthorizerId` is defined in the resource.

## Limitations
This hook serves as a simple example on how authorizers can be enforced on API Gateway resources. There are a few limitations associated with it in favor of simplicity. It is encouraged to fork this example and customize it depending on the need.
1. OpenAPI definitions specified in an [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket object will be skipped and not validated.
2. Hook will be enforced on all stacks and all routes. There is no way to skip certain stack or route.

## Method/Route Resource
### Valid
```yaml
  MyApiRoute:
    Type: AWS::ApiGatewayV2::Route
    Properties:
      ApiId: !Ref MyApi
      RouteKey: 'POST /route-post'
      AuthorizerId: MyLambdaAuthUpdated
```
### Invalid
```yaml
  MyApiRoute:
    Type: AWS::ApiGatewayV2::Route
    Properties:
      ApiId: !Ref MyApi
      RouteKey: 'POST /route-post'
```

## OpenAPI
### Valid
```json
{
	"Body": {
		"components": {
			"securitySchemes": {
				"MyLambdaAuthUpdated": {
					...
				}
			}
		},
		"openapi": "3.0",
		"paths": {
			"/post": {
				"post": {
					"x-amazon-apigateway-integration": {
						"payloadFormatVersion": "1.0",
						"httpMethod": "POST",
						"type": "aws_proxy",
						"uri": "..."
					},
                    "security": [
                        {
                            "MyLambdaAuthUpdated": []
                        }
                    ]
				}
			}
		},
		"info": {
			...
		}
	}
}
```
### Invalid
```json
{
	"Body": {
		"components": {
			"securitySchemes": {
				"MyLambdaAuthUpdated": {
					...
				}
			}
		},
		"openapi": "3.0",
		"paths": {
			"/post": {
				"post": {
					"x-amazon-apigateway-integration": {
						"payloadFormatVersion": "1.0",
						"httpMethod": "POST",
						"type": "aws_proxy",
						"uri": "..."
					}
				}
			}
		},
		"info": {
			...
		}
	}
}
```
## Usage

This hook has no required properties.
Sample configuration:

```bash
# Create a basic type configuration json
cat <<EOF >> type_config.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode": "FAIL",
      "Properties": {}
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://type_config.json \
  --type HOOK \
  --type-name AWSSamples::APIGWEnforceAuthorizer::Hook
```
