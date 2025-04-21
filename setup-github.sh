#!/bin/bash

# Exit on error
set -e

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "GitHub CLI is not installed. Please install it first."
    exit 1
fi

# Check if user is logged in
if ! gh auth status &> /dev/null; then
    echo "Please login to GitHub CLI first: gh auth login"
    exit 1
fi

# Get repository name
REPO_NAME=$(gh repo view --json name -q .name)
REPO_OWNER=$(gh repo view --json owner -q .owner.login)

echo "Setting up GitHub environments and secrets for $REPO_OWNER/$REPO_NAME"
echo

# Create environments
echo "Creating environments..."
gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/$REPO_OWNER/$REPO_NAME/environments/staging" \
  -f name=staging

gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/$REPO_OWNER/$REPO_NAME/environments/production" \
  -f name=production

# Add environment protection rules
echo "Adding environment protection rules..."
gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/$REPO_OWNER/$REPO_NAME/environments/staging" \
  -f wait_timer=60 \
  -f required_reviewers='[{"id":1}]' \
  -f deployment_branch_policy='{"protected_branches":true,"custom_branches":[]}'

gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/$REPO_OWNER/$REPO_NAME/environments/production" \
  -f wait_timer=60 \
  -f required_reviewers='[{"id":1}]' \
  -f deployment_branch_policy='{"protected_branches":true,"custom_branches":[]}'

# Add repository secrets
echo "Adding repository secrets..."
gh secret set AWS_ACCESS_KEY_ID -b"$AWS_ACCESS_KEY_ID"
gh secret set AWS_SECRET_ACCESS_KEY -b"$AWS_SECRET_ACCESS_KEY"
gh secret set AWS_REGION -b"$AWS_REGION"

# Add environment secrets
echo "Adding environment secrets..."
gh secret set AWS_BUCKET -b"$AWS_BUCKET" -e staging
gh secret set AWS_BUCKET -b"$AWS_BUCKET" -e production
gh secret set AWS_ROLE_ARN -b"$AWS_ROLE_ARN" -e staging
gh secret set AWS_ROLE_ARN -b"$AWS_ROLE_ARN" -e production

echo
echo "Setup complete! Please verify the following:"
echo "1. Environments 'staging' and 'production' are created"
echo "2. Environment protection rules are set"
echo "3. Secrets are properly configured"
echo
echo "You can now run the workflow manually to test the deployment." 