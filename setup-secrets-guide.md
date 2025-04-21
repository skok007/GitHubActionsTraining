# Setting up Secrets for Exercise 5

## AWS Credentials
1. Create an AWS IAM user with programmatic access
2. Attach the following policies:
   - AmazonS3FullAccess
   - IAMFullAccess (for creating roles and policies)
3. Save the Access Key ID and Secret Access Key

## Security Scanning Tools

### Snyk
1. Sign up for a free Snyk account at https://snyk.io
2. Go to Account Settings > API tokens
3. Create a new API token
4. Save the token

### Gitleaks
1. Gitleaks doesn't require a license for basic usage
2. For enterprise features, sign up at https://gitleaks.io
3. Save the license key if you have one

## GitHub Secrets Setup

Add the following secrets to your GitHub repository (Settings > Secrets and variables > Actions):

### Repository Secrets
1. `AWS_ACCESS_KEY_ID`: Your AWS Access Key ID
2. `AWS_SECRET_ACCESS_KEY`: Your AWS Secret Access Key
3. `AWS_REGION`: Your AWS region (e.g., us-east-1)
4. `SNYK_TOKEN`: Your Snyk API token
5. `GITLEAKS_LICENSE`: Your Gitleaks license key (if applicable)

### Environment Secrets
Create two environments: `staging` and `production`

For each environment, add:
1. `AWS_BUCKET`: The S3 bucket name (will be provided by setup script)
2. `AWS_ROLE_ARN`: The IAM role ARN (will be provided by setup script)

## Environment Protection Rules

For each environment (staging and production):

1. Go to Settings > Environments
2. Click "New environment"
3. Add protection rules:
   - Required reviewers: Add at least one reviewer
   - Wait timer: Set to 1 minute
   - Deployment branches: Restrict to main branch

## Testing the Setup

After adding all secrets:

1. Go to Actions tab
2. Select "Secrets and Security Example" workflow
3. Click "Run workflow"
4. Select environment (staging or production)
5. Watch the workflow execution

## Troubleshooting

If you encounter issues:

1. Check AWS credentials are correct
2. Verify all secrets are properly set
3. Ensure environment protection rules are configured
4. Check workflow file permissions
5. Verify OIDC provider is properly set up in AWS 