#!/bin/bash

# Assume the role and save credentials
aws sts assume-role --role-arn arn:aws:iam::287485889672:role/kok-steven-github-actions-training-role --role-session-name test-session > assume-role-output.json

# Extract credentials from the output
CREDS=$(cat assume-role-output.json | jq -r '.Credentials')
export AWS_ACCESS_KEY_ID=$(echo $CREDS | jq -r '.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo $CREDS | jq -r '.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo $CREDS | jq -r '.SessionToken')

# Verify we're using the assumed role
echo "Verifying identity..."
aws sts get-caller-identity

# Try to create the secret
echo "Creating secret..."
aws secretsmanager create-secret --name github-actions-training-test --secret-string '{"test": "value"}' --region eu-west-2 