"""
Report Generator Module

This module generates different types of reports for demonstrating GitHub Actions artifacts.
"""

import csv
import datetime
import json
import os
import numpy as np


class ReportGenerator:
    """A class that generates different types of reports."""

    def __init__(self, output_dir="reports"):
        """Initialize the report generator."""
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_json_report(self, data, filename="report.json"):
        """Generate a JSON report."""
        filepath = os.path.join(self.output_dir, filename)

        # Add metadata to the report
        report_data = {
            "metadata": {
                "generated_at": datetime.datetime.now().isoformat(),
                "report_type": "json",
            },
            "data": data,
        }

        with open(filepath, "w") as f:
            json.dump(report_data, f, indent=2)

        return filepath

    def generate_csv_report(self, data, headers, filename="report.csv"):
        """Generate a CSV report."""
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(data)

        return filepath

    def generate_plot_report(
        self, x_data, y_data, title="Plot Report", filename="plot.txt"
    ):
        """Generate a text-based plot report."""
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, "w") as f:
            f.write(f"{title}\n")
            f.write("=" * len(title) + "\n\n")
            
            # Create a simple ASCII plot
            height = 20
            width = 60
            y_range = max(abs(min(y_data)), abs(max(y_data)))
            y_scale = height / (2 * y_range)
            
            for i in range(height, -1, -1):
                line = []
                for x, y in zip(x_data, y_data):
                    if abs(y * y_scale - i) < 0.5:
                        line.append("*")
                    else:
                        line.append(" ")
                f.write("".join(line) + "\n")
            
            f.write("\nX-axis: 0 to 10\n")
            f.write("Y-axis: -1 to 1\n")

        return filepath

    def generate_summary_report(self, reports, filename="summary.txt"):
        """Generate a summary of all reports."""
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, "w") as f:
            f.write("Report Generation Summary\n")
            f.write("=======================\n\n")
            f.write(f"Generated at: {datetime.datetime.now().isoformat()}\n\n")

            for report in reports:
                f.write(f"Report: {os.path.basename(report)}\n")
                f.write(f"Size: {os.path.getsize(report)} bytes\n")
                f.write(
                    f"Created: {datetime.datetime.fromtimestamp(os.path.getctime(report)).isoformat()}\n"
                )
                f.write("-" * 50 + "\n")

        return filepath

    def generate_all_reports(self):
        """Generate all types of reports with sample data."""
        reports = []

        # Generate JSON report
        json_data = {
            "metrics": {"users": 1000, "active_users": 750, "conversion_rate": 0.25}
        }
        reports.append(self.generate_json_report(json_data))

        # Generate CSV report
        headers = ["ID", "Name", "Value"]
        data = [[1, "Item 1", 100], [2, "Item 2", 200], [3, "Item 3", 300]]
        reports.append(self.generate_csv_report(data, headers))

        # Generate plot report
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        reports.append(self.generate_plot_report(x, y, "Sample Plot"))

        # Generate summary report
        summary_report = self.generate_summary_report(reports)
        reports.append(summary_report)

        return reports


if __name__ == "__main__":
    # Generate all reports when run directly
    generator = ReportGenerator()
    reports = generator.generate_all_reports()
    print("Generated reports:")
    for report in reports:
        print(f"- {report}")
