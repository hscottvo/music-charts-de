from airflow import DAG
from airflow.operators.python import PythonOperator


def print_thing() -> None:
    print("Hello world")


with DAG(dag_id="dag_test") as dag:
    x = PythonOperator(task_id="print", python_callable=print_thing)
    x
