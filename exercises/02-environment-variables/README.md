# Exercise 02: Environment Variables and Secrets

In this exercise, you'll learn how to use environment variables and secrets in GitHub Actions workflows. You'll create a simple application that uses environment variables and set up a workflow that securely handles sensitive information.

## Objectives

- Understand the difference between environment variables and secrets
- Learn how to use GitHub Secrets
- Create a workflow that uses environment variables
- Implement secure handling of sensitive data
- Use environment variables across different jobs

## Steps

1. **Create a Configuration Application**
   - Create a Python application that reads configuration from environment variables
   - Add functionality to connect to a mock API using credentials
   - Create a test file to verify the functionality

2. **Set Up GitHub Secrets**
   - Add repository secrets in GitHub
   - Understand the different types of secrets (repository, environment, organization)

3. **Create GitHub Actions Workflow**
   - Create a workflow that uses environment variables
   - Implement secure handling of secrets
   - Pass environment variables between jobs

4. **Test Your Workflow**
   - Commit and push your changes
   - Verify that secrets are properly masked in logs
   - Check that the application works with the provided environment variables

## Expected Outcome

After completing this exercise, you should have:
- An application that uses environment variables
- A GitHub Actions workflow that securely handles secrets
- Understanding of different types of GitHub Secrets
- Experience with passing environment variables between jobs

## Next Steps

Once you've completed this exercise, move on to Exercise 03 to learn about matrix builds in GitHub Actions. 