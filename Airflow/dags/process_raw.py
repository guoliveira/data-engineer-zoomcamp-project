import os
import pandas as pd
import pyspark
from pyspark.sql import SparkSession

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator

from google.cloud import storage

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")

path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")


def process_data_weather_fn(year_to_process):

    spark = SparkSession.builder.master("local[*]").appName('test').getOrCreate()
    df = spark.read.option("header", "false").csv(f'{year_to_process}.csv.gz')
    df.registerTempTable('weather_data')
    df_stations = spark.read.option("header", "true").parquet('rfn_ghcnd_stations.parquet')
    df_stations.registerTempTable('stations')

    portuguese_temperature = spark.sql("""
    SELECT
        _c0 as stations_code
      , _c1 as date
      , _c2 as variable
      , cast(_c3 as float)/10 as value
    FROM
        weather_data
    WHERE _c0 IN (SELECT code
                  FROM stations)
          and _c2 = 'TAVG'
    """)

    pivotDF = portuguese_temperature.groupBy("stations_code", "date").pivot("variable").sum("value")
    pivotDF.coalesce(1).write.parquet(f'{year_to_process}/', mode='overwrite')


def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    :param bucket: GCS bucket name
    :param object_name: target path & file-name
    :param local_file: source path & file-name
    :return:
    """
    # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # (Ref: https://github.com/googleapis/python-storage/issues/74)
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB
    # End of Workaround

    client = storage.Client()
    bucket = client.bucket(bucket)

    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="ingest_process_weather_data",
    schedule_interval=None,
    default_args=default_args,
    catchup=True,
    max_active_runs=1,
    tags=['dtc-de'],
    start_date=days_ago(1)
) as dag:

    baseurl="https://noaa-ghcn-pds.s3.amazonaws.com/csv.gz/"

    start_task = DummyOperator(task_id='start_task', dag=dag)


    for i in range(2000, 2002):
        dataset_file = f"{i}.csv.gz"

        download_dataset_task = BashOperator(
            task_id=f"download_dataset_{i}",
            bash_command=f"curl -sSLf {baseurl}{dataset_file} > {path_to_local_home}/{dataset_file}"
        )

        process_data_weather = PythonOperator(
            task_id=f'process_data_weather_{i}',
            python_callable = process_data_weather_fn,
            op_kwargs={
                "year_to_process": i,}
        )

        start_task >> download_dataset_task >> process_data_weather

        local_to_gcs_task = PythonOperator(
            task_id=f"local_to_gcs_year_{i}",
            python_callable=upload_to_gcs,
            op_kwargs={
                "bucket": BUCKET,
                "object_name": f"refined/weather_data/{dataset_file.replace('.csv.gz','.parquet')}",
                "local_file": f"{path_to_local_home}/{dataset_file.replace('.csv.gz','.parquet')}",
            },
        )

        remove_dataset_task = BashOperator(
            task_id=f"remove_dataset_year_{i}",
            bash_command=f"rm {path_to_local_home}/{dataset_file} {path_to_local_home}/{dataset_file.replace('.csv.gz','.parquet')} "
        )

        process_data_weather >> local_to_gcs_task >> remove_dataset_task

