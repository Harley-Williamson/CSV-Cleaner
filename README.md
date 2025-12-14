
#CSV Cleaner

## Overview
This Python script cleans and standardizes customer data exporte from small business CRM systems.

It is designed to:
- Normalize data (lowercase, trim whitespace)
- Preserve CRM data structure
- Output a clean CSV ready for re-import or reporting
- Log processing activity for record keeping

This tool is ideal for small businesses that regularly export customer data for reporting, marketing, or system migrations.

---

## Features
- Cleans all CSV fields automatically
- Handles large files efficiently
- Command-line driven
- Creates a processing log
- No external dependencies

---

## Requirements
- Python 3.12.3+
- Standard Python libraries on only (csv, argparse, datetime)

---

## Usage
From the parent directory:

bash
python3 main.py input_file.csv output_file.csv


Example:

python3 main.py customers.csv cleaned_customers.csv

---

## Output
- A cleaned CSV file with standardized formatting
- A log entry recorded in logging.txt

## Example Use Cases
- Cleaning customer exports from CRM
- Preparing data for email campaigns
- Normalizing data before system migration
- Improving reporting accuracy

## Notes
- The script does not modify the original file.
- All cleaning is done on a new output file.
