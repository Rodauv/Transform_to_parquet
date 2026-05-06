# CSV/XLSX to Parquet Transformer

## Introduction

This utility converts `.csv` and `.xlsx` files into `.parquet` format using Python.

It is intended for one-off manual transformations of mapping files, static reference data, or small local datasets where an integration pipeline is not required.

The script scans the `input` folder, identifies supported source files, and creates matching `.parquet` files in the `output` folder.

Example:

```text
data_mapping.xlsx   ->   data_mapping.parquet
category_master.csv ->   category_master.parquet
```

---

## Repository Structure

```text
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
```

---

## Getting Started

### Prerequisites

Before running the transformer, make sure the following are available on your computer:

1. Copy the content to a repository.
2. Install Python 3.x on your computer.
3. Add the Jupyter extension to VS Code.
4. Install the required Python packages.

---

## Installation

Open the repository folder in VS Code.

Run the following command in the terminal:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```text
pandas
pyarrow
openpyxl
```

---

## Usage

Place the source files you want to convert in the `input` folder.

Supported source formats:

```text
.csv
.xlsx
```

Run the transformer:

```bash
python transform_to_parquet.py
```

The converted files will be created in the `output` folder.

---

## Output

Each source file is converted into a `.parquet` file with the same base name.

Example:

```text
input/mapping.xlsx  -> output/mapping.parquet
input/lookup.csv    -> output/lookup.parquet
```

---

## Example Console Output

```text
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
```

---

## Notes

- Existing `.parquet` files with the same name will be overwritten.
- Excel files are read from the first sheet by default.
- CSV files are read using default pandas settings.
- The utility is intended for simple manual transformations.
- For recurring or production data loads, use an Azure Data Factory pipeline instead.

---

## Manual Validation

You can validate a generated Parquet file by reading it back into Python:

```python
import pandas as pd

df = pd.read_parquet("output/mapping.parquet")
print(df.head())
```

---

## Build and Test

There is currently no automated test framework included.

To test the transformer manually:

1. Add one sample `.csv` file to the `input` folder.
2. Add one sample `.xlsx` file to the `input` folder.
3. Run the transformer.
4. Confirm that matching `.parquet` files are created in the `output` folder.
5. Read one generated `.parquet` file back into Python to confirm the content.

---

## Contribute

When updating the transformer, consider the following:

- Keep the script simple and readable.
- Avoid adding ADF-specific logic.
- Document any assumptions about delimiters, encodings, sheet names, or column handling.
- Test changes with both `.csv` and `.xlsx` input files.
- Update this README when behavior changes.
