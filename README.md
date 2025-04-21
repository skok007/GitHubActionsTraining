# GitHub Actions Training Materials

Welcome to the GitHub Actions Training Materials! This repository is designed to help you learn GitHub Actions from basics to advanced concepts through hands-on exercises and interactive Jupyter notebooks.

## 🚀 Getting Started

### Prerequisites
Before you begin, make sure you have:
- A GitHub account (create one at [github.com](https://github.com) if you don't have one)
- Basic understanding of Git (check out [Git Handbook](https://guides.github.com/introduction/git-handbook/) if needed)
- Python 3.8 or higher
- Node.js 14 or higher (needed for Exercise 5)

### Quick Start
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/github-actions-training.git
   cd github-actions-training
   ```

2. Set up your Python environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Start with the first notebook:
   ```bash
   jupyter notebook notebooks/01-basic-workflow.ipynb
   ```

## 📚 Learning Path

The training materials are organized into six progressive exercises:

1. **Basic Workflow** (`01-basic-workflow.ipynb`)
   - Your first GitHub Actions workflow
   - Understanding workflow syntax
   - Running tests automatically
   - Basic CI concepts

2. **Environment Variables** (`02-environment-variables.ipynb`)
   - Working with environment variables
   - Managing configuration
   - Using GitHub contexts
   - Secure variable handling

3. **Matrix Builds** (`03-matrix-builds.ipynb`)
   - Running tests across multiple environments
   - Parallel job execution
   - Testing on different Python versions
   - Optimizing build time

4. **Artifacts** (`04-artifacts.ipynb`)
   - Storing build outputs
   - Sharing data between jobs
   - Managing test results
   - Handling large files

5. **Secrets and Security** (`05-secrets-security.ipynb`)
   - Managing sensitive data
   - Security scanning
   - AWS integration
   - Best practices for security

6. **Reusable Workflows** (`06-reusable-workflows.ipynb`)
   - Creating reusable components
   - Building composite actions
   - Sharing workflow logic
   - Advanced workflow patterns

## 📁 Repository Structure

```
.
├── notebooks/              # Jupyter notebooks for each exercise
├── exercises/             # Exercise-specific code and resources
│   ├── 01-basic-workflow/
│   ├── 02-environment-variables/
│   ├── 03-matrix-builds/
│   ├── 04-artifacts/
│   ├── 05-deployment/     # Includes AWS and security resources
│   └── 06-reusable-workflows/
├── .github/
│   └── workflows/         # Example GitHub Actions workflows
└── create_notebooks/      # Tools for maintaining notebooks
```

## 🛠️ Tools and Resources

### Notebook Creation System
The notebooks are generated from JSON files using the `create_notebooks.py` script. To update notebooks:
```bash
cd create_notebooks
python create_notebooks.py
```

### Security Tools
Exercise 5 includes several security tools:
- OWASP Dependency Check for vulnerability scanning
- Gitleaks for secret detection
- CodeQL for code analysis

### AWS Integration (Exercise 5)
Exercise 5 demonstrates secure AWS integration using:
- OIDC authentication
- Secrets Manager
- S3 deployment

## 📝 Contributing

Feel free to contribute to this training material by:
1. Opening issues for bugs or improvements
2. Suggesting new exercises or examples
3. Improving documentation
4. Adding more test cases

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [GitHub Actions Examples](https://github.com/actions/starter-workflows)
- [GitHub Actions Best Practices](https://docs.github.com/en/actions/learn-github-actions/security-hardening-for-github-actions)

## 🆘 Need Help?

If you get stuck or have questions:
1. Look for comments in the notebooks
2. Review the example workflows in `.github/workflows/`
3. Open an issue in this repository

Happy learning! 🎉 