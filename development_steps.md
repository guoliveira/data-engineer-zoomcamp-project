## Development Steps

This capstone followed these general development steps:

1. Started a Google Cloud Platform free account (this step was skipped since we already built before for the zoomcamp);

2. Creation of GCP project with the name "Capstone-Luis-Oliveira" and followed the advanced steps in [here](https://github.com/guoliveira/data-engineer-zoomcamp-project/tree/main/GCP_Terraform)

3. Creation of a GCP infrastructure using Terraform. This infrastructure includes Big Query and Storage.  The steps can be seen [here](https://github.com/guoliveira/data-engineer-zoomcamp-project/blob/main/GCP_Terraform/Readme.md#creation-of-a-gcp-infrastructure);

4. [Development of DockerFile and Docker-Compose structure to run Airflow.](setup_docker.md)

5. [Start to run Airflow inside a container](Airflow/README.md) and [development of two DAG for the pipeline data.](Airflow/dags)

6. Ran the two Dags in order get the raw files and refined (after transformation) files in GCP Storage. The data pipeline is presented ...

7. Creation of two tables in BigQuery using DDL. One table with Portuguese weather station information (code, latitude, longitude, region and location) and one partitioned table with the average temperature by day and by station (this table was partition by year).
*It was decided to ran a DDL Query in BigQuery because it was going to be done once (it was unnecessary to set it in Airflow)*

8. Development of a visualization using ...
