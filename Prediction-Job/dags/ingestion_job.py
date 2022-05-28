import os
import datetime
import logging
import pandas as pd
from airflow import DAG
from pendulum import today
from airflow.decorators import dag
from great_expectations.core.batch import RuntimeBatchRequest
from great_expectations_provider.operators.great_expectations import (
    GreatExpectationsOperator
)

####
# Get the runtime batch request


def get_runtime_batch_request(data_asset_name):
    cur_dr = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(cur_dr, 'data', 'new_data', data_asset_name)
    df = pd.read_csv(data_dir)

    return RuntimeBatchRequest(**{
        "datasource_name": "new_data_source",
        "data_connector_name": "default_runtime_data_connector_name",
        "data_asset_name": data_asset_name,
        "runtime_parameters": {
            "batch_data": df
        },
        "batch_identifiers": {"default_identifier_name": "default_identifier"}
    })


with DAG(
    schedule_interval="*/10 * * * *",
    start_date=today().add(hours=-1),
    catchup=False,
    dag_id='ingestion_job',
    dagrun_timeout=datetime.timedelta(minutes=60),
) as dag:
    logger = logging.getLogger("console")

    runtime_batch_request = get_runtime_batch_request("test.csv")
    validate_data_with_checkpoint = GreatExpectationsOperator(
        task_id="validate_data",
        data_context_root_dir='./great_expectations',
        checkpoint_name="valid_checkpoint",
        checkpoint_kwargs={
            "validations": [{"batch_request": runtime_batch_request}]
        },
        fail_task_on_validation_failure=False,
        validation_failure_callback=(
            lambda x: logger.info("Callback successfully run", x)
        ),
    )

    logger.warning("-------------------------------------------------------")
    try:
        validate_data_with_checkpoint
        logger.error(
            "done -------------------------------------------------------")
    except Exception as e:
        print(e.print_stack_trace())
        logger.error(e.print_stack_trace())

(
    validate_data_with_checkpoint
)
