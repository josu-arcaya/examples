import logging
import time

import pendulum

from airflow.models.dag import DAG
from airflow.decorators import task

def expensive_api_call():
    """Simulates an API call that takes time and returns a value."""
    print("Making an expensive API call...")
    logging.warning("This is a warning from the API call function.")
    time.sleep(10)
    return "This is the response from the expensive API!"


with DAG(
    dag_id="sample_dag",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:

    @task()
    def get_expensive_response():
        """
        This task calls the expensive function.
        Its return value will be passed to downstream tasks.
        """
        response = expensive_api_call()
        return response

    @task()
    def print_the_response(api_response: str):
        """
        This task receives the result from the upstream task
        and prints it.
        """
        print("The received response is:")
        print(api_response)

    # Use the function call syntax to set the dependency.
    # Airflow automatically passes the return value from the first task
    # as an argument to the second task.
    api_data = get_expensive_response()
    print_the_response(api_response=api_data)

