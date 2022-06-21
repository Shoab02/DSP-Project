# Prediction Job

## Installation

Activate your environment with python 3.8

Install airflow

```bash
# Skip if you are already in the Prediction-Job directory
cd Prediction-Job
pip install -r requirements.txt
```

## Initialization

```bash
# Navigate to the prediction job directory
cd Prediction-Job
export AIRFLOW_HOME=`pwd`
airflow db init
# After running this command you will be asked to enter a password,
# you can use "admin" to keep it simple
airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@admin.com
```

## Start airflow

```bash
airflow webserver --port 4000 --workers 1 -D
airflow scheduler -D
```

## View the UI

[UI](http://localhost:7000)

## License

[MIT](https://choosealicense.com/licenses/mit/)
