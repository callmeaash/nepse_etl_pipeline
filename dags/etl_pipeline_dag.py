from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.sensors.http_sensor import HttpSensor
import os
from dotenv import load_dotenv
import json
from etl_pipeline import run_etl


load_dotenv()
api_url = os.getenv('API_KEY')

default_args = {
    'owner': 'aashish',
    'depends_on_past': True,
    'start_date': datetime(2025, 8, 23),
    'email': 'aashish@gmail.com',
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}


def is_json(response_text):
    try:
        json.loads(response_text)
        return True
    except ValueError:
        return False

symbol = "AHL"
api_url_template = os.getenv("API_KEY")
full_endpoint = f"{api_url_template}{symbol}"

with DAG(
    'nepse_pipeline',
    default_args=default_args,
    description='NEPSE ETL pipeline',
    schedule_interval='0 18 * * 0-5',
    catchup=False
) as dag:
    
    wait_for_file = FileSensor(
        task_id='check_stock_symbols_file_exists',
        filepath='/opt/airflow/stock_names_data/stocks.csv',
        poke_interval=10,
        timeout=60,
        mode='poke'
    )

    wait_for_api = HttpSensor(
        task_id='Check_api_conn',
        http_conn_id=None,
        endpoint=full_endpoint,
        method='GET',
        poke_interval=5,
        timeout=60,
        mode='poke',
        response_check=lambda response: is_json(response.text)
    )

    wait_for_etl_execution = PythonOperator(
        task_id='Execute_etl_pipeline',
        python_callable=run_etl
    )

    wait_for_file >> wait_for_api >> wait_for_etl_execution


