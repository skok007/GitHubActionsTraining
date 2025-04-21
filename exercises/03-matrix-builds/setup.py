from setuptools import find_packages, setup

setup(
    name="matrix-demo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
    ],
    python_requires=">=3.7",
    author="GitHub Actions Training",
    author_email="example@example.com",
    description="A demo package for GitHub Actions matrix builds",
    keywords="github-actions, matrix-builds, python",
    url="https://github.com/yourusername/github-actions-training",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
