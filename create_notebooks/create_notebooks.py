import glob
import json
import os


def create_notebook_from_json(json_file):
    """
    Creates a Jupyter notebook from a JSON file.

    Args:
        json_file (str): Path to the JSON file containing notebook content

    Returns:
        dict: A complete Jupyter notebook structure
    """
    with open(json_file, "r") as f:
        notebook_data = json.load(f)

    # Create the notebook structure
    notebook = {
        "cells": notebook_data["cells"],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.10",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }

    return notebook


def save_notebook(notebook, filename):
    """
    Saves a Jupyter notebook to a file.

    Args:
        notebook (dict): The notebook structure to save
        filename (str): The path where the notebook should be saved
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump(notebook, f, indent=1)


def main():
    """
    Main function that creates and saves all notebooks from JSON files.
    """
    # Create notebooks directory if it doesn't exist
    os.makedirs("../notebooks", exist_ok=True)

    # Find all JSON files in the json directory
    json_files = glob.glob("json/*.json")

    # Create a notebook for each JSON file
    for json_file in json_files:
        # Extract the notebook name from the JSON file path
        notebook_name = os.path.basename(json_file).replace(".json", "")

        # Create the notebook from the JSON file
        notebook = create_notebook_from_json(json_file)

        # Save the notebook
        save_notebook(notebook, f"../notebooks/{notebook_name}.ipynb")
        print(f"Created notebook: ../notebooks/{notebook_name}.ipynb")


if __name__ == "__main__":
    main()
