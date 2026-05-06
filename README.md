# CSV/XLSX to Parquet Transformer

## Introduction

This utility converts `.csv` and `.xlsx` files into `.parquet` format using Python.

It is intended for one-off manual transformations of mapping files, static reference data, or small local datasets where an Azure Data Factory pipeline is not required.

The script scans the `input` folder, identifies supported source files, and creates matching `.parquet` files in the `output` folder.

Example:
dealer_mapping.xlsx  -> dealer_mapping.parquet
model_lookup.csv     -> model_lookup.parquet

## Repository Structure

repo/
│
├─ transform_to_parquet.py
├─ requirements.txt
│
├─ input/
│  ├─ mapping.xlsx
│  └─ lookup.csv
│
└─ output/
   ├─ mapping.parquet
   └─ lookup.parquet


## Getting Started

### Prerequisites

Before running the transformer, make sure the following are available on your computer:

1. Copy the content to a repository.
2. Install Python 3.x on your computer.  
   Available in Company Portal:  
   `ApplicationId=f36664b0-f618-49b1-b8d6-f23ee4b60cff`
3. Add the Jupyter extension to VS Code.
4. Install the required Python packages.


## Installation

Open the repository folder in VS Code.

Run the following command in the terminal:

```bash
pip install -r requirements.txt
```

## Usage

Place the source files you want to convert in the `input` folder.

Supported source formats:
.csv
.xlsx


Run the transformer:

```bash
python transform_to_parquet.py
```

The converted files will be created in the `output` folder.


## Output

Each source file is converted into a `.parquet` file with the same base name.

Example:
input/mapping.xlsx  -> output/mapping.parquet
input/lookup.csv    -> output/lookup.parquet


## Example Console Output
Initiating transformer
Input folder: C:\Repos\csv-xlsx-to-parquet\input
Output folder: C:\Repos\csv-xlsx-to-parquet\output
---
Extracting xlsx files: 1
Extracting csv files: 1
---
Converting Excel: mapping.xlsx -> mapping.parquet
Converting CSV: lookup.csv -> lookup.parquet
Transformation completed.

## Notes

- Existing `.parquet` files with the same name will be overwritten.
- Excel files are read from the first sheet by default.
- CSV files are read using default pandas settings.
- The utility is intended for simple manual transformations.
- For recurring or production data loads, use an Azure Data Factory pipeline instead.


## Manual Validation

You can validate a generated Parquet file by reading it back into Python:

```python
import pandas as pd

df = pd.read_parquet("output/mapping.parquet")
print(df.head())
```