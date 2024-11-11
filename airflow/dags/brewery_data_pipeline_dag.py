from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from src.0_fetch_breweries import fetch_breweries
from src.1_store_raw_data import store_raw_data
from src.2_transform_data import transform_data
from src.3_aggregate_data import aggregate_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'brewery_data_pipeline',
    default_args=default_args,
    description='Data pipeline for Open Brewery DB',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
)

def fetch_and_store():
    data = fetch_breweries()
    store_raw_data(data)

fetch_task = PythonOperator(
    task_id='0_fetch_and_store',
    python_callable=0_fetch_and_store,
    dag=dag,
)

store_raw_task = PythonOperator(
    task_id='1_store_raw_data',
    python_callable=1_store_raw_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=2_transform_data,
    dag=dag,
)

aggregate_task = PythonOperator(
    task_id='3_aggregate_data',
    python_callable=3_aggregate_data,
    dag=dag,
)

fetch_task >> store_raw_task >> transform_task >> aggregate_task
