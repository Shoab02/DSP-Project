import os
import datetime
import pendulum
from pendulum import today
import logging
import requests
from airflow.decorators import dag, task


@dag(
    schedule_interval="*/5 * * * *",
    start_date=today().add(hours=-1),
    catchup=False,
    dag_id='prediction_job',
    dagrun_timeout=datetime.timedelta(minutes=60),
)
def make_predictions():
    @task(
        task_id='make_prediction'
    )
    def send_files():
        cur_dr = os.path.dirname(os.path.realpath(__file__))
        data_dir = os.path.join(cur_dr, 'data')
        if not os.path.isdir(data_dir):
            raise FileExistsError
        files = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]

        for f in files:
            send_file_to_api(f)

    send_files()


dag = make_predictions()


####
def send_file_to_api(f):
    logger = logging.getLogger("console")
    response = requests.post(
        'https://epita-2022-dsp-api.herokuapp.com/',
        files={'csv_file': open(f, 'rb')}
    )
    logger.info(f"{response.status_code}")
    logger.info(f"{response.json()}")
