from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import yaml

from tasks.trainer import trainer
from tasks.test_predict import test_predict

default_args = {
    'owner': 'Yuki',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with open("ml_config.yml", "r") as f:
    config = yaml.safe_load(f)

dag = DAG('pipeline', default_args=default_args,
          schedule_interval=timedelta(days=1))

t_trainer = PythonOperator(
    task_id='trainer',
    provide_context=True,
    python_callable=trainer,
    op_kwargs={'config': config},
    dag=dag)

t_test_predict = PythonOperator(
    task_id='test_predict',
    provide_context=True,
    python_callable=test_predict,
    op_kwargs={'config': config},
    dag=dag)


t_trainer > t_test_predict
