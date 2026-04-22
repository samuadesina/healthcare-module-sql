import pandas as pd
import os

# Load the CSV that run.py produced
df = pd.read_csv("data/raw-data.csv")

def test_file_exists():
    """Check the CSV file was actually created"""
    assert os.path.exists("data/raw-data.csv"), "raw-data.csv not found"

def test_has_rows():
    """Check we got data back, not an empty file"""
    assert len(df) > 0, "CSV is empty"

def test_has_expected_columns():
    """Check the right columns are there"""
    expected_columns = [
        "patient_name",
        "appointment_date",
        "status",
        "doctor_name",
        "billed_amount",
        "department"
    ]
    for col in expected_columns:
        assert col in df.columns, f"Missing column: {col}"

def test_no_null_patient_names():
    """Check every row has a patient name"""
    assert df["patient_name"].isnull().sum() == 0, "Some patient names are missing"

def test_status_values_are_valid():
    """Check status column only has known values"""
    valid_statuses = ["Completed", "Cancelled", "No-show", "Scheduled"]
    invalid = df[~df["status"].isin(valid_statuses)]
    assert len(invalid) == 0, f"Unexpected status values found: {invalid['status'].unique()}"