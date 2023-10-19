import csv
import os

__author__ = "James Thayer"
__date__ = "10/18/2023"
__assignment__ = "SER594: MS3"

DATA_PROCESSED_DIR = "data_processed"

# Load CSV
def load_csv(filename):
    records = []
    with open(filename, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append(row)

    return records

# Floor all of the ages to ints
def floor_age_values(records):
    for entry in records:
        if entry['age'] != 'NA':
            entry['age'] = int(float(entry['age']))

    return records

# Truncate mmi_score to 4 decimal places
def truncate_mmi_score(records):
    for entry in records:
        if entry['mmi_score'] != 'NA':
            entry['mmi_score'] = round(float(entry['mmi_score']), 4)
    
    return records

def save_processed_data_to_csv(filename, records):
    with open(os.path.join(DATA_PROCESSED_DIR, filename), mode='w', newline='', encoding='utf8') as csvfile:
        fieldnames = records[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
