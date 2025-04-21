"""
Tests for the report generator module.
"""

import csv
import json
import os

import numpy as np
import pytest
from report_generator import ReportGenerator


@pytest.fixture
def report_generator(tmp_path):
    """Create a report generator that uses a temporary directory."""
    return ReportGenerator(output_dir=str(tmp_path))


def test_generate_json_report(report_generator):
    """Test generating a JSON report."""
    data = {"test": "data"}
    filepath = report_generator.generate_json_report(data)

    assert os.path.exists(filepath)
    with open(filepath) as f:
        report_data = json.load(f)

    assert "metadata" in report_data
    assert "data" in report_data
    assert report_data["data"] == data


def test_generate_csv_report(report_generator):
    """Test generating a CSV report."""
    headers = ["ID", "Name"]
    data = [[1, "Test"], [2, "Test 2"]]
    filepath = report_generator.generate_csv_report(data, headers)

    assert os.path.exists(filepath)
    with open(filepath) as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows[0] == headers
    assert len(rows) == len(data) + 1  # +1 for headers
    for i, row in enumerate(rows[1:]):
        assert row == [str(x) for x in data[i]]


def test_generate_plot_report(report_generator):
    """Test generating a plot report."""
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    filepath = report_generator.generate_plot_report(x, y)

    assert os.path.exists(filepath)
    assert filepath.endswith(".png")
    assert os.path.getsize(filepath) > 0


def test_generate_summary_report(report_generator):
    """Test generating a summary report."""
    # First create some reports to summarize
    json_file = report_generator.generate_json_report({"test": "data"})
    csv_file = report_generator.generate_csv_report([[1, "Test"]], ["ID", "Name"])

    # Generate summary
    filepath = report_generator.generate_summary_report([json_file, csv_file])

    assert os.path.exists(filepath)
    with open(filepath) as f:
        content = f.read()

    assert "Report Generation Summary" in content
    assert os.path.basename(json_file) in content
    assert os.path.basename(csv_file) in content


def test_generate_all_reports(report_generator):
    """Test generating all reports."""
    reports = report_generator.generate_all_reports()

    assert len(reports) == 4  # JSON, CSV, Plot, and Summary

    extensions = [os.path.splitext(report)[1] for report in reports]
    assert ".json" in extensions
    assert ".csv" in extensions
    assert ".png" in extensions
    assert ".txt" in extensions

    for report in reports:
        assert os.path.exists(report)
        assert os.path.getsize(report) > 0
