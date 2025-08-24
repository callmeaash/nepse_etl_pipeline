# 📊 NEPSE ETL Pipeline with Airflow

This project implements an **ETL (Extract, Transform, Load) pipeline** using **Apache Airflow** for orchestration.

The pipeline extracts stock data from an API, transforms it into a structured format, and loads it into a local database as well as csv file.

---

## 🚀 Features
- **Extract**: Fetch stock OHLC data from an API.
- **Transform**: Clean, validate, and process raw data.
- **Load**: Store processed data into database and csv file.
- **Airflow DAG**: Automates and schedules the ETL workflow.
- **Logging**: Logs ETL pipeline steps for monitoring.

---

## 🛠️ Tools Used

- **[Pandas](https://pandas.pydata.org/)** – For data extraction and transformation.
- **[SQLAlchemy](https://www.sqlalchemy.org/)** – To interact with databases in a scalable and database-agnostic way.
- **[Apache Airflow](https://airflow.apache.org/)** – For orchestrating, scheduling, and monitoring ETL workflows.
- **Logging (Python `logging` module)** – For structured and configurable logging of pipeline events and errors.
- **[Pytest](https://docs.pytest.org/)** – For writing and running unit tests to ensure pipeline reliability.


---

## 🗂️ Project Structure
```bash
etl-project/
│── dags/                    # Airflow DAG definitions
│   └── etl_pipeline_dag.py           # Main ETL DAG
│
|── database_schema/
|   └── erdiagram            # ER diagram of database
│   └── sqliteSchema.sql
│   └── schema.sql           # PostgreSQL database schema  
│
│── stock_names_data/        # File storing stocks symbol
│   └── stocks.csv      
│
│── pipeline_utils/          # ETL logic
│   ├── extract.py           # Data extraction functions
│   ├── transform.py         # Data transformation functions
│   ├── load.py              # Data loading functions
│   └── __init__.py
│
│── tests/                   # Unit tests
│   └── test_extract.py
│   └── test_transform.py
│   └── test_load.py
│
|── docker-compose-yaml      # Airflow configs for docker
│── etl_pipeline.py          # Python script to execute the pipeline
│── stocks_ohlc.db           # SQLite database (created after first run)
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation

```

## ⚙️ Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/callmeaash/nepse_etl_pipeline.git
cd nepse_etl_pipeline
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate    # On Linux/Mac
.venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Airflow with Docker
Make sure you have **Docker** and **Docker Compose** installed.



#### Start Airflow
```bash
docker-compose up -d
```


### 5. Running the ETL Script Manually (Optional)
```bash
python etl_pipeline.py
```

### 6. Logs (For Manual ETL execution)
Check logs in:
```bash
etl_pipeline.log
```

---

## 🧪 Testing
Run unit tests:
```bash
pytest tests/
```

---

## 📝 Notes
- Environment variables must be defined in `.env`  
- SQLite DB (`stocks_ohlc.db`) is used for local development.  
- For production, consider PostgreSQL or MySQL.
- Extract more stocks symbol using the scrape function available in scraping_utils directory and append them in the stocks.csv in stock_names_data directory
