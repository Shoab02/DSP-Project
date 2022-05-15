import os
import datetime
import pendulum
import logging
import requests
from airflow.decorators import dag, task


@dag(
    schedule_interval="*/5 * * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dag_id='prediction_job',
    dagrun_timeout=datetime.timedelta(minutes=60),
)
def pipeline():
    @task(
        task_id='make_prediction'
    )
    def send_file():
        logger = logging.getLogger("console")
        cur_dr = os.path.dirname(os.path.realpath(__file__))
        data_dir = os.path.join(cur_dr, 'data')
        if not os.path.isdir(data_dir):
            raise FileExistsError
        files = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]

        for f in files:
            response = requests.post(
                'https://postman-echo.com/post',
                files={'file': open(f, 'rb')}
            )
            logger.info(f"{response.status_code}")
            logger.info(f"{response.json()}")

    send_file()


dag = pipeline()
