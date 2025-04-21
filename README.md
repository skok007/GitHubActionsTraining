# GitHub Actions Training Materials

This repository contains training materials for learning GitHub Actions, including Jupyter notebooks with interactive examples.

## Prerequisites

- GitHub account
- Basic understanding of Git
- Python 3.8 or higher
- Node.js 14 or higher
- AWS account with appropriate permissions (for Exercise 5)
- Required AWS services:
  - S3 bucket for deployment
  - IAM role with appropriate permissions
  - Secrets Manager for secret rotation
  - Access to AWS credentials
- Java 17 or higher (for OWASP Dependency Check)

## Notebook Creation System

The notebooks are generated from JSON files using the `create_notebooks.py` script. This approach makes it easy to maintain and update the training materials.

### Structure

- `notebooks/`: Directory containing the generated Jupyter notebooks
- `create_notebooks/`: Directory containing the notebook creation tools
  - `json/`: JSON files that define the notebook content
  - `create_notebooks.py`: Script to generate notebooks from JSON files
  - `README.md`: Documentation for the notebook creation system

### How to Use

To generate all notebooks:

```bash
cd create_notebooks
python create_notebooks.py
```

This will create or update the notebooks in the `notebooks` directory based on the JSON files in `create_notebooks/json/`.

For more details on the JSON file format and how to create new notebooks, see [create_notebooks/README.md](create_notebooks/README.md).

## Exercises

The training materials include hands-on exercises for learning GitHub Actions:

1. **Basic Workflow** (`01-basic-workflow.ipynb`)
   - Introduction to GitHub Actions
   - Basic workflow syntax
   - Running tests and linting

2. **Environment Variables** (`02-environment-variables.ipynb`)
   - Working with environment variables
   - Using GitHub contexts
   - Managing configuration

3. **Matrix Builds** (`03-matrix-builds.ipynb`)
   - Running parallel jobs
   - Testing across multiple versions
   - Optimizing build matrices

4. **Artifacts** (`04-artifacts.ipynb`)
   - Storing and retrieving artifacts
   - Sharing data between jobs
   - Managing build outputs

5. **Secrets and Security** (`05-secrets-security.ipynb`)
   - Managing sensitive data
   - Implementing security best practices
   - Using GitHub's security features
   - AWS integration for secure deployments
   - OWASP Dependency Check for vulnerability scanning
   - Gitleaks for secret detection
   - CodeQL for code analysis
   - Secret rotation with AWS Secrets Manager

6. **Reusable Workflows and Composite Actions** (`06-reusable-workflows.ipynb`)
   - Creating reusable workflows
   - Building composite actions
   - Sharing workflow logic
   - Maintaining consistent CI/CD processes
   - Advanced workflow composition

Each exercise includes a Jupyter notebook with explanations and examples, along with practical exercises to complete.

## Project Structure

```
.
├── .github/
│   └── workflows/          # GitHub Actions workflow files
├── notebooks/              # Generated Jupyter notebooks
├── create_notebooks/       # Notebook creation tools
│   ├── json/               # JSON files defining notebook content
│   ├── create_notebooks.py # Script to generate notebooks
│   └── README.md           # Documentation for notebook creation
├── src/                    # Source code
├── tests/                  # Test files
├── requirements.txt        # Python dependencies
├── suppression.xml         # OWASP Dependency Check suppressions
├── aws-secrets.txt         # AWS configuration template
├── aws-permissions.md      # AWS permissions documentation
└── README.md              # This file
```

## Workflows

### 1. Basic Workflow (.github/workflows/01-basic.yml)
Demonstrates basic GitHub Actions concepts:
- Workflow triggers
- Job configuration
- Step execution
- Environment variables

### 2. Matrix Strategy (.github/workflows/02-matrix.yml)
Shows how to use matrix strategy for:
- Multiple Python versions
- Multiple operating systems
- Parallel job execution

### 3. Caching (.github/workflows/03-caching.yml)
Illustrates caching mechanisms:
- pip cache
- Custom cache keys
- Cache restoration
- Cache invalidation

### 4. Artifacts (.github/workflows/04-artifacts.yml)
Demonstrates artifact handling:
- Uploading artifacts
- Downloading artifacts
- Processing artifacts
- Artifact cleanup

### 5. Secrets and Security (.github/workflows/05-secrets-security.yml)
Shows security best practices:
- Secret management
- Security scanning with OWASP Dependency Check
- Secret detection with Gitleaks
- Code analysis with CodeQL
- AWS integration with OIDC
- Environment protection
- Secret rotation with AWS Secrets Manager

### 6. Reusable Workflows (.github/workflows/06-reusable-workflows.yml)
Demonstrates workflow reuse:
- Reusable workflow creation
- Composite action development
- Workflow composition
- Parameter passing
- Secret handling

## Security Tools

The project includes several security tools to enhance your security posture:

### OWASP Dependency Check
- Identifies project dependencies
- Checks for known vulnerabilities
- Generates HTML reports
- Configurable CVSS threshold
- False positive suppression

### Gitleaks
- Detects hardcoded secrets
- Scans for API keys, passwords, and tokens
- Prevents accidental secret commits
- Open-source version

### CodeQL
- Semantic code analysis
- Identifies security vulnerabilities
- Language-specific analysis
- GitHub's security engine

## AWS Integration

The project demonstrates secure AWS integration:

### OIDC Authentication
- Short-lived credentials
- No stored secrets
- Role-based access
- Secure authentication

### Secrets Manager
- Centralized secret storage
- Automated secret rotation
- Access control
- Audit logging

### S3 Deployment
- Secure file storage
- Environment-specific deployments
- Access control
- Versioning

## Testing

The project includes comprehensive test cases demonstrating various testing scenarios:

1. Basic Assertions
   - Simple truth assertions
   - Value comparisons

2. String Operations
   - String manipulation
   - String transformations
   - String splitting

3. File Operations
   - File creation
   - File reading
   - Temporary file handling

4. JSON Operations
   - Serialization
   - Deserialization
   - Data validation

5. Parametrized Tests
   - Multiple test cases
   - Input/output validation
   - Edge cases

6. Environment Variables
   - Variable access
   - Default values
   - Variable modification

## Artifacts

The artifacts workflow demonstrates several key concepts:

1. Build Artifacts
   - Test results
   - Coverage reports
   - Build outputs

2. Artifact Processing
   - Combining multiple artifacts
   - Generating reports
   - Data aggregation

3. Artifact Management
   - Automatic cleanup
   - Retention policies
   - Storage optimization

## Getting Started

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up AWS resources (for Exercise 5):
   - Create an S3 bucket
   - Set up an IAM role with appropriate permissions
   - Configure AWS credentials
4. Start with Exercise 1 and work through each notebook sequentially

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 