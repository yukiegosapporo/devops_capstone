
initdb:
	airflow initdb

server:
	airflow webserver -p 8080

scheduler:
	airflow scheduler

pipeline:
	airflow run pipeline test_predict 2020-01-01T10:20:00 --force=true

install:
	pip install -r requirements.txt