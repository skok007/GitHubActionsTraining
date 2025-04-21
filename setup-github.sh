#!/bin/bash

# Exit on error
set -e

# Get repository details
REPO_OWNER="skok007"
REPO_NAME="GitHubActionsTraining"
echo "Setting up GitHub secrets for $REPO_OWNER/$REPO_NAME"

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "GitHub CLI (gh) is not installed. Please install it first."
    exit 1
fi

# Check if logged in to GitHub
if ! gh auth status &> /dev/null; then
    echo "Please login to GitHub first using: gh auth login"
    exit 1
fi

# Load AWS secrets from aws-secrets.txt
if [ -f "aws-secrets.txt" ]; then
    # Extract values using grep and cut
    AWS_REGION=$(grep "AWS_REGION=" aws-secrets.txt | cut -d'=' -f2)
    AWS_BUCKET=$(grep "AWS_BUCKET=" aws-secrets.txt | cut -d'=' -f2)
    AWS_ROLE_ARN=$(grep "AWS_ROLE_ARN=" aws-secrets.txt | cut -d'=' -f2)

    if [ -z "$AWS_REGION" ] || [ -z "$AWS_BUCKET" ] || [ -z "$AWS_ROLE_ARN" ]; then
        echo "Failed to read all required values from aws-secrets.txt"
        exit 1
    fi
else
    echo "aws-secrets.txt not found. Please create it with your AWS configuration."
    exit 1
fi

echo "Setting repository secrets..."
# Set repository secrets
gh secret set AWS_REGION --body "$AWS_REGION"
gh secret set AWS_BUCKET --body "$AWS_BUCKET"
gh secret set AWS_ROLE_ARN --body "$AWS_ROLE_ARN"

echo "Setting up GitHub environments..."
# Create staging environment
gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/$REPO_OWNER/$REPO_NAME/environments/staging"

# Create production environment
gh api \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/$REPO_OWNER/$REPO_NAME/environments/production"

echo "Setting environment secrets..."
# Set staging environment secrets
gh secret set AWS_REGION --body "$AWS_REGION" --env staging
gh secret set AWS_BUCKET --body "$AWS_BUCKET" --env staging
gh secret set AWS_ROLE_ARN --body "$AWS_ROLE_ARN" --env staging
gh secret set AWS_SECRET_ID --body "github-actions-training-test" --env staging

# Set production environment secrets
gh secret set AWS_REGION --body "$AWS_REGION" --env production
gh secret set AWS_BUCKET --body "$AWS_BUCKET" --env production
gh secret set AWS_ROLE_ARN --body "$AWS_ROLE_ARN" --env production
gh secret set AWS_SECRET_ID --body "github-actions-training-test" --env production

echo "All secrets and environments have been set up successfully."
echo "Please verify the setup in your repository settings." 