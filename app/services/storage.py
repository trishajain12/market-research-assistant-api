import json
import os
import uuid


# reports will be stored in this path
DATA_FILE = "data/reports.json"

# reads the JSON file and returns the saved reports
def load_reports():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)

# takes a python list and writes it into a JSON file
def save_reports(reports):
    with open(DATA_FILE, "w") as file:
        json.dump(reports, file, indent=2)

# loads exisiting reports, generates a unique ID, adds ID to report, appends the report, saves everything
def create_report(report_data):
    reports = load_reports()

    report_id = str(uuid.uuid4())                     # create a unique ID
    report_data["report_id"] = report_id

    reports.append(report_data)
    save_reports(reports)

    return report_data


# returns all saved
def get_all_reports():
    return load_reports()

# search if report is found
def get_report_by_id(report_id):
    reports = load_reports()

    for report in reports:
        if report["report_id"] == report_id:
            return report

    return None

def delete_report_by_id(report_id):
    reports = load_reports()

    updated_reports = [report for report in reports if report["report_id"] != report_id]

    if len(updated_reports) == len(reports):
        return False

    save_reports(updated_reports)
    return True


def delete_all_reports():
    save_reports([])