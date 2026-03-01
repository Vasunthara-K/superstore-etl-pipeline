# Superstore Sales ETL Pipeline
## 📌 Project Overview
This project demonstrates an **End-to-End Data Engineering ETL Pipeline** built using **Python, Pandas, and MySQL**.

The pipeline ingests raw sales data from a CSV file, performs data cleaning and transformation, and loads analytics-ready data into a curated database table.

---

## 🏗️ Architecture

```
Sales CSV File
      ↓
Python ETL (Extraction & Cleaning)
      ↓
MySQL Raw Table (superstore_raw)
      ↓
SQL Transformation
      ↓
Clean Analytics Table (sales_clean)
```

---

## ⚙️ Technologies Used

* Python
* Pandas
* MySQL
* MySQL Workbench
* VS Code
* SQL

---

## 📂 Project Structure

```
sales_etl_project/
│
├── etl.py
|__ sql
├── sales.csv
└── documentation
```

---

## 🔄 ETL Process

### Extract

* Read Superstore CSV using Pandas

### Transform

* Removed invalid records
* Handled NULL values
* Converted date formats
* Created derived columns (Year, Month)

### Load

* Loaded raw data into `superstore_raw`
* Transformed data into `sales_clean`

---

## ✅ Data Validation

```
SELECT COUNT(*) FROM superstore_raw;
SELECT COUNT(*) FROM sales_clean;
```

---

## ▶️ How to Run

1. Install dependencies:

```
pip install pandas mysql-connector-python
```

2. Update database credentials in `etl.py`

3. Run ETL:

```
python etl.py
```

4. Execute transformation SQL in MySQL Workbench.

---

## 📊 Outcome

* Built Raw and Curated data layers
* Implemented real-world ETL workflow
* Handled data quality issues and schema constraints

---

## 🚀 Future Improvements

* Incremental loading
* Job scheduling automation
* Logging & monitoring
* Airflow orchestration
* Dashboard integration

---

## 👩‍💻 Author

**Vasunthara K**
