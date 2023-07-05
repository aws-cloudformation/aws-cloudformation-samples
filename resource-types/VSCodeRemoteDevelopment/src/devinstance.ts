#!/usr/bin/env node
import * as cdk from '@aws-cdk/core';
import { DevinstanceStack } from './devinstance-stack';



export function getTemplate(): any {
    const app = new cdk.App();
    new DevinstanceStack(app, 'DevinstanceStack');
    const assembly = app.synth()
    return assembly.getStackByName('DevinstanceStack').template
}