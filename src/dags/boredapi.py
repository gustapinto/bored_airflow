from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


# When using the DAG as a context manager it will be implicity
# added to any operator inside it
with DAG('bored_api', start_date=days_ago(1)) as dag:
    hello = lambda msg : print(f'hello {msg}')

    # Defining the airflow tasks using Python operators
    t1 = PythonOperator(task_id='hello', python_callable=hello, op_args=['hello'])
    t2 = PythonOperator(task_id='world', python_callable=hello, op_args=['world'])

    t1 >> t2
