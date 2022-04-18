import os
import pandas as pd

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from google.cloud import storage

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")

path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")


def extract_portuguese_stations(parquet_file):
    """
    This function perform transformations at the weather stations
    :param parquet_file:
    :return:
    """
    df = pd.DataFrame()

    code = []
    lat = []
    long = []
    with open("ghcnd-stations.txt", "r") as f:
        for x in f:
            y = x.split("  ", 6)
            if y[0] == 'POW00013201':
                code.append(y[0])
                lat.append(float(y[1]))
                l = y[2].split(' ', 2)
                long.append(float(l[0]))
            elif y[0][:2] == 'PO':
                code.append(y[0])
                lat.append(float(y[1]))
                long.append(float(y[2]))

    df['code'] = code
    df['lat'] = lat
    df['long'] = long

    df.loc[(df['long']) > -10, 'Region'] = 'Continente'
    df.loc[df['long'] <= -10, 'Region'] = 'Madeira'
    df.loc[(df['long']) <= -20, 'Region'] = 'Açores'

    df.loc[((df['Region']) == 'Continente') & (df['lat'] > 38), 'Area'] = 'Centro'
    df.loc[((df['Region']) == 'Continente') & (df['lat'] > 40), 'Area'] = 'Norte'
    df.loc[((df['Region']) == 'Continente') & (df['lat'] < 38), 'Area'] = 'Sul'

    print(df.head())

    df.to_parquet(parquet_file)


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
    dag_id="stations_ingest_process",
    schedule_interval=None,
    default_args=default_args,
    catchup=True,
    max_active_runs=1,
    tags=['dtc-de'],
    start_date=days_ago(1)
) as dag:

    dataset_file = 'ghcnd-stations.txt'
    dataset_url = f"https://noaa-ghcn-pds.s3.amazonaws.com"
    parquet_dataset = 'rfn_ghcnd_stations.parquet'

    download_dataset_task = BashOperator(
        task_id="download_dataset_task",
        bash_command=f"curl -sSLf {dataset_url}/{dataset_file} > {path_to_local_home}/{dataset_file}"
    )

    local_to_raw_gcs = PythonOperator(
        task_id="local_to_raw_gcs",
        python_callable=upload_to_gcs,
        op_kwargs={
            "bucket": BUCKET,
            "object_name": f"raw/stations/{dataset_file}",
            "local_file": f"{path_to_local_home}/{dataset_file}",
        },
    )

    process_data_stations = PythonOperator(
        task_id='process_stations',
        python_callable = extract_portuguese_stations,
                op_kwargs={"parquet_file":f"{path_to_local_home}/{parquet_dataset}"}
    )

    local_to_refined_gcs = PythonOperator(
        task_id="local_to_refined_gcs",
        python_callable=upload_to_gcs,
        op_kwargs={
            "bucket": BUCKET,
            "object_name": f"refined/stations/{parquet_dataset}",
            "local_file": f"{path_to_local_home}/{parquet_dataset}",
        },
    )

    remove_dataset_task = BashOperator(
        task_id="remove_dataset_txt",
        bash_command=f"rm {path_to_local_home}/{dataset_file}"
    )

    download_dataset_task >> local_to_raw_gcs >> process_data_stations
    process_data_stations >> local_to_refined_gcs >> remove_dataset_task
