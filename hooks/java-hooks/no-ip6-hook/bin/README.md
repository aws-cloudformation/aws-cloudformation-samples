# AWSSamples::NoIP6::Hook

Congratulations on starting development! Next steps:

1. Write the JSON schema describing your hook, `awssamples-noip6-hook.json`
1. Implement your hook handlers.

The RPDK will automatically generate the correct hook input model from the schema whenever the project is built via Maven. You can also do this manually with the following command: `cfn generate`.

> Please don't modify files under `target/generated-sources/rpdk`, as they will be automatically overwritten.

The code uses [Lombok](https://projectlombok.org/), and [you may have to install IDE integrations](https://projectlombok.org/) to enable auto-complete for Lombok-annotated classes.
