from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from src.tasks.boredapi.extractor import extract_boredapi
from src.tasks.boredapi.parser import parse_boredapi
from src.tasks.boredapi.loader import load_boredapi


# When using the DAG as a context manager it will be implicity
# added to any operator inside it
with DAG('bored_api', start_date=days_ago(1), scheduler_interval=timedelta(minutes=5)) as dag:
    extract = PythonOperator(task_id='extract', python_callable=extract_boredapi)
    transform = PythonOperator(task_id='parse', python_callable=parse_boredapi)
    load = PythonOperator(task_id='load', python_callable=load_boredapi)

    extract >> transform
    transform >> load
