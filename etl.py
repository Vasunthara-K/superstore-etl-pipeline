import pandas as pd
import mysql.connector
import numpy as np

print("Reading CSV file...")
df = pd.read_csv("sales.csv")

# Remove corrupted rows
df = df[pd.to_numeric(df["Row ID"], errors="coerce").notnull()]
df["Row ID"] = df["Row ID"].astype(int)

# ---------- TRANSFORM DATES ----------
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# ---------- REPLACE NaN WITH None ----------
df = df.replace({np.nan: None})

print("Data cleaned!")
print(df.head())

print("Connecting to MySQL...")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vasurenu96!@",   # change this
    database="sales_db"    # change this
)

cursor = conn.cursor()

print("Connected to MySQL!")

print("Inserting data into superstore_raw...")

sql = """
INSERT INTO superstore_raw (
    `Row ID`, `Order ID`, `Order Date`, `Ship Date`,
    `Ship Mode`, `Customer ID`, `Customer Name`,
    `Segment`, `Country`, `City`, `State`,
    `Postal Code`, `Region`, `Product ID`,
    `Category`, `Sub-Category`, `Product Name`,
    `Sales`, `Quantity`, `Discount`, `Profit`
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():

    clean_values = (
        int(row["Row ID"]) if pd.notna(row["Row ID"]) else None,
        row["Order ID"],
        row["Order Date"],
        row["Ship Date"],
        row["Ship Mode"],
        row["Customer ID"],
        row["Customer Name"],
        row["Segment"],
        row["Country"],
        row["City"],
        row["State"],
        row["Postal Code"],
        row["Region"],
        row["Product ID"],
        row["Category"],
        row["Sub-Category"],
        row["Product Name"],
        float(row["Sales"]) if pd.notna(row["Sales"]) else None,
        int(row["Quantity"]) if pd.notna(row["Quantity"]) else None,
        float(row["Discount"]) if pd.notna(row["Discount"]) else None,
        float(row["Profit"]) if pd.notna(row["Profit"]) else None
    )

    cursor.execute(sql, clean_values)

conn.commit()

print("Data inserted successfully into superstore_raw!")

cursor.close()
conn.close()

print("ETL Process Completed 🚀")