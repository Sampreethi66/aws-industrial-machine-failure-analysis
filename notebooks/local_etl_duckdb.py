import pandas as pd
import duckdb
from pathlib import Path

# Base project directory: .../walbrydge-operations-datalake
BASE_DIR = Path(__file__).resolve().parent.parent

raw_file = BASE_DIR / "data" / "raw" / "ai4i2020.csv"
warehouse_dir = BASE_DIR / "warehouse"
bi_dir = BASE_DIR / "bi"

warehouse_dir.mkdir(exist_ok=True)
bi_dir.mkdir(exist_ok=True)

# 1) Read raw CSV
df = pd.read_csv(raw_file)

# 2) Clean up column names: remove spaces and brackets
df = df.rename(columns={
    "Air temperature [K]": "air_temperature_k",
    "Process temperature [K]": "process_temperature_k",
    "Rotational speed [rpm]": "rotational_speed_rpm",
    "Torque [Nm]": "torque_nm",
    "Tool wear [min]": "tool_wear_min",
    "Machine failure": "machine_failure",
    "Failure Type": "failure_type"
})

# 3) Connect to DuckDB (creates file if not exists)
db_path = warehouse_dir / "walbrydge.duckdb"
con = duckdb.connect(str(db_path))

# 4) Register the DataFrame as a table
con.register("raw_ai4i", df)

# 5) Create a fact table (simplified)
con.execute("""
CREATE OR REPLACE TABLE fact_equipment_health AS
SELECT
    air_temperature_k,
    process_temperature_k,
    rotational_speed_rpm,
    torque_nm,
    tool_wear_min,
    machine_failure,
    TWF,
    HDF,
    PWF,
    OSF,
    RNF
FROM raw_ai4i;
""")

# 6) Export fact table to CSV for BI
output_csv = bi_dir / "fact_equipment_health_local.csv"
con.execute(f"""
COPY (SELECT * FROM fact_equipment_health)
TO 'bi/fact_equipment_health_local.csv'
WITH (HEADER, DELIMITER ',');
""")

print("Local ETL complete.")
print(f"DuckDB file: {db_path}")
print(f"BI CSV file: {output_csv}")
