# Exercise 03: Matrix Builds

In this exercise, you'll learn how to use matrix builds in GitHub Actions to run your tests across multiple Python versions and operating systems. This is useful for ensuring your code works correctly in different environments.

## Objectives

- Understand the concept of matrix builds
- Create a workflow that runs tests on multiple Python versions
- Test your code on different operating systems
- Use matrix strategies to optimize your workflow
- Handle matrix-specific environment variables

## Steps

1. **Create a Python Package**
   - Create a simple Python package with tests
   - Add compatibility checks for different Python versions
   - Create a setup.py file for packaging

2. **Set Up Matrix Build Workflow**
   - Create a workflow file that uses matrix strategy
   - Define Python versions and operating systems to test
   - Configure environment variables for each matrix combination
   - Add steps to run tests in each environment

3. **Optimize Your Matrix Build**
   - Use matrix exclusions to skip unnecessary combinations
   - Implement matrix strategy to reduce the number of jobs
   - Add conditional steps based on matrix parameters

4. **Test Your Workflow**
   - Commit and push your changes
   - Check the Actions tab to see the matrix build in action
   - Verify that tests run correctly in all environments

## Expected Outcome

After completing this exercise, you should have:
- A Python package that can be tested across different environments
- A GitHub Actions workflow that uses matrix builds
- Understanding of how to optimize matrix builds
- Experience with conditional steps based on matrix parameters

## Next Steps

Once you've completed this exercise, move on to Exercise 04 to learn about artifacts in GitHub Actions. 