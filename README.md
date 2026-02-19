# NEPSE ETL Pipeline (Apache Airflow)

An ETL pipeline built to collect, validate, transform, and store **NEPSE stock market data** using **Apache Airflow**, **PostgreSQL**, and **Docker**.

This project focuses on **data reliability, validation, and orchestration**.

---

## Architecture Overview

- **Apache Airflow (LocalExecutor)**  
  Orchestrates and schedules ETL workflows.

- **PostgreSQL**  
  Stores Airflow metadata and processed stock market data.

- **Docker Compose**  
  Manages containerized services for Airflow and PostgreSQL.

---

## ETL Workflow

1. **File Sensor**  
   Waits for the stock symbol file (`stocks.csv`) to become available.

2. **HTTP Sensor**  
   Verifies API availability and validates JSON responses before execution.

3. **Extract**  
   Fetches OHLC stock data from an external API.

4. **Transform**  
   - Performs data cleaning and validation  
   - Computes technical indicators  
   - Ensures schema consistency  

5. **Load**  
   - Stores cleaned OHLC data in PostgreSQL  
   - Saves transformed datasets as CSV files for offline analysis  


---

## Project Structure

```text
.
├── dags/
│   └── nepse_pipeline.py
├── stock_names_data/
│   └── stocks.csv
├── cleanData/
├── pipeline_utils/
├── etl_pipeline.py
├── requirements.txt
├── .env
└── docker-compose.yml
```

---

## 🚀 Setup & Execution

### 1️⃣ Start Services

```bash
docker compose up -d
```

### Access Airflow UI

```text
URL      : http://localhost:8080
Username : admin
Password : admin
```

### Run the Pipeline

```text
1. Open the Airflow UI
2. Enable the `nepse_pipeline` DAG
3. Trigger the DAG manually or wait for the scheduled run
```

---

## Technologies Used

```text
- Python 3.12
- Apache Airflow 2.9.3
- PostgreSQL 17
- Docker & Docker Compose
- Pandas
- SQLAlchemy
```

---

## Purpose

```text
Demonstrates practical ETL design, Airflow orchestration,
data validation, and containerized data engineering setup.
```
