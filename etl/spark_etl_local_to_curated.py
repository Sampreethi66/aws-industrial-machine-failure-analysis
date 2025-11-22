from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pathlib import Path
import pandas as pd  # <— NEW: use pandas to write parquet

BASE_DIR = Path(__file__).resolve().parent.parent
raw_file = BASE_DIR / "data" / "raw" / "ai4i2020.csv"
curated_dir = BASE_DIR / "data" / "curated"

curated_dir.mkdir(exist_ok=True)

# 1) Start Spark
spark = SparkSession.builder \
    .appName("WalbrydgeLocalSparkETL") \
    .getOrCreate()

# 2) Read raw CSV with Spark
df = spark.read.csv(str(raw_file), header=True, inferSchema=True)

# 3) Rename columns
df = df.withColumnRenamed("Air temperature [K]", "air_temperature_k") \
       .withColumnRenamed("Process temperature [K]", "process_temperature_k") \
       .withColumnRenamed("Rotational speed [rpm]", "rotational_speed_rpm") \
       .withColumnRenamed("Torque [Nm]", "torque_nm") \
       .withColumnRenamed("Tool wear [min]", "tool_wear_min") \
       .withColumnRenamed("Machine failure", "machine_failure")

# 4) Cast numeric columns
numeric_cols = [
    "air_temperature_k",
    "process_temperature_k",
    "rotational_speed_rpm",
    "torque_nm",
    "tool_wear_min"
]

for c in numeric_cols:
    df = df.withColumn(c, col(c).cast("double"))

# 5) Convert Spark DataFrame -> pandas DataFrame
pdf = df.toPandas()

# 6) Write Parquet LOCALLY (pandas)
output_path = Path("data/curated/ai4i2020_parquet")
output_path.mkdir(parents=True, exist_ok=True)

parquet_file = output_path / "ai4i2020.parquet"
pdf.to_parquet(parquet_file, index=False)

print("Local Parquet generated:", parquet_file)
