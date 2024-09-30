from datetime import datetime

import requests
from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator

"""
from datetime import datetime

import requests


def check_updated(request: requests.models.Response) -> bool:
    print(type(request))

    return True


if __name__ == "__main__":
    r = requests.get("https://kworb.net/spotify/country/global_daily.html")
    last_modified = r.headers["Last-Modified"]
    last_modified = " ".join(last_modified.split()[1:])
    check_updated(r)

    date = datetime.strptime(last_modified, "%d %b %Y %H:%M:%S %Z")

    print(date)
"""


def print_thing() -> None:
    print("Hello world")


def check_updated(request: requests.models.Response) -> bool:
    print(type(request))

    return True


# with DAG(dag_id="dag_test") as dag:
@dag(dag_id="fetch_spotify")
def hitkworb():
    # x = PythonOperator(task_id="print", python_callable=print_thing)
    # x

    @task()
    def check_status():
        r = requests.get("https://kworb.net/spotify/country/global_daily.html")
        last_modified = r.headers["Last-Modified"]
        last_modified = " ".join(last_modified.split()[1:])
        check_updated(r)

        date = datetime.strptime(last_modified, "%d %b %Y %H:%M:%S %Z")

        print(date)

    check_status()


hitkworb()
