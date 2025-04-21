# Notebook Creation System

This directory contains the tools and files needed to generate Jupyter notebooks for the GitHub Actions training materials.

## Structure

- `create_notebooks.py`: Script to generate notebooks from JSON files
- `json/`: Directory containing JSON files that define the notebook content
- `README.md`: This file

## JSON File Format

Each JSON file in the `json/` directory defines the content of a notebook. The JSON file should follow this structure:

```json
{
  "title": "Exercise XX: Title of the Exercise",
  "description": "Brief description of the exercise",
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Exercise XX: Title of the Exercise\n",
        "\n",
        "Description of the exercise."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Code example\n",
        "print(\"Hello, World!\")"
      ]
    }
  ]
}
```

### Cell Types

The `cells` array can contain two types of cells:

1. **Markdown Cells**: For text content, explanations, and documentation
   ```json
   {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
       "# Heading\n",
       "\n",
       "Paragraph text with **bold** and *italic* formatting."
     ]
   }
   ```

2. **Code Cells**: For executable code examples
   ```json
   {
     "cell_type": "code",
     "execution_count": null,
     "metadata": {},
     "outputs": [],
     "source": [
       "# Python code\n",
       "import os\n",
       "print(os.getcwd())"
     ]
   }
   ```

## Creating a New Notebook

To create a new notebook:

1. Create a new JSON file in the `json/` directory with the naming convention `XX-title.json` (where XX is the exercise number)
2. Define the notebook content following the JSON structure above
3. Run the `create_notebooks.py` script to generate the notebook

## Generating Notebooks

To generate all notebooks from the JSON files, run:

```bash
cd create_notebooks
python create_notebooks.py
```

This will:
1. Find all JSON files in the `json/` directory
2. Create a notebook for each JSON file
3. Save the notebooks in the `../notebooks/` directory

## Best Practices

When creating JSON files for notebooks:

1. **Use consistent naming**: Follow the `XX-title.json` convention
2. **Include a title and description**: These help identify the notebook
3. **Structure content logically**: Group related content together
4. **Use markdown for explanations**: Keep code cells focused on examples
5. **Include code comments**: Help readers understand the code
6. **Test the generated notebooks**: Ensure they work as expected 