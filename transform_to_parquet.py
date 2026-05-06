import pandas as pd
from pyarrow.parquet import ParquetFile
from pathlib import Path

input_cwd = Path("input")
output_cwd = Path("output")

output_cwd.mkdir(parents=True, exist_ok=True)

print("Initiating transformer")
print(f"Input folder: {input_cwd.resolve()}")
print(f"Output folder: {output_cwd.resolve()}")
print("---")

input_xls = list(input_cwd.glob("*.xlsx"))
input_csv = list(input_cwd.glob("*.csv"))

print(f"Extracting xlsx files: {len(input_xls)}")
print(f"Extracting csv files: {len(input_csv)}")
print("---")

for file in input_xls:
    output_file = output_cwd / file.with_suffix(".parquet").name

    print(f"Converting Excel: {file.name} -> {output_file.name}")

    df = pd.read_excel(file)
    df.to_parquet(output_file, engine="pyarrow", index=False)

    print(ParquetFile(output_file).metadata)
    print("---")

for file in input_csv:
    output_file = output_cwd / file.with_suffix(".parquet").name

    print(f"Converting CSV: {file.name} -> {output_file.name}")

    df = pd.read_csv(file)
    df.to_parquet(output_file, engine="pyarrow", index=False)

    print(ParquetFile(output_file).metadata)
    print("---")

print("Transformation completed.")