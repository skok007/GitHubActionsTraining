# Required AWS Permissions for Notebook 5

## S3 Permissions
Required for deployment:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "s3:ListAllMyBuckets"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject",
                "s3:PutObjectAcl"
            ],
            "Resource": "arn:aws:s3:::github-actions-training-bucket/*"
        }
    ]
}
```

## Secrets Manager Permissions
Required for secret rotation:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:ListSecrets",
                "secretsmanager:GetSecretValue",
                "secretsmanager:UpdateSecret"
            ],
            "Resource": "*"
        }
    ]
}
```

## IAM Permissions
Required for role assumption:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole",
                "iam:GetRole"
            ],
            "Resource": "arn:aws:iam::287485889672:user/kok-steven-github-actions-training"
        }
    ]
}
```

## Current Status
1. S3 Access:
   - ✅ Basic bucket operations working
   - ✅ Bucket created successfully
   - ✅ List buckets permission confirmed

2. Secrets Manager Access:
   - ❌ ListSecrets permission missing
   - ❌ UpdateSecret permission needed
   - ❌ GetSecretValue permission needed

3. IAM/STS Access:
   - Needs verification for:
   - [ ] sts:AssumeRole
   - [ ] iam:GetRole

## Next Steps
1. Request the following permissions to be added to the IAM user:
   - secretsmanager:ListSecrets
   - secretsmanager:GetSecretValue
   - secretsmanager:UpdateSecret
   - sts:AssumeRole
   - iam:GetRole

2. After permissions are granted:
   - Verify Secrets Manager access
   - Test role assumption
   - Create and configure required secrets 