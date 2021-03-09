#!/usr/bin/env node
import * as cdk from '@aws-cdk/core';
import { DevinstanceStack } from './devinstance-stack';

const app = new cdk.App();
new DevinstanceStack(app, 'DevinstanceStack');
new DevinstanceStack(app, 'CanaryStack', {}, true);