# Prediction Job

## Installation

Activate your environment

Install airflow
```bash
# Skip if you are already in the Prediction-Job directory
cd Prediction-Job
pip install -r requirements.txt
```

## Initialization
```bash
airflow db init
# After running this command you will be asked to enter a password, 
# you can use "admin" to keep it simple
airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@admin.com
```

## Setup environment
Add our pipeline to the airflow main directory

Copy the /dags file to ~/airflow 
```bash
cp -R ./dags ~/airflow
```

## Start airflow

```bash
airflow webserver --port 7000 --workers 1 -D
airflow scheduler -S ./dags -D
```

## View the UI
[UI](http://localhost:7000)

## License
[MIT](https://choosealicense.com/licenses/mit/)
