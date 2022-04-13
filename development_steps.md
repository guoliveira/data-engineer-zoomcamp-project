## Development Steps

This capstone followed these general development steps:

1. Started a Google Cloud Platform free account (this step was skipped since we already built before for the zoomcamp);

2. Creation of GCP project with the name "Capstone-Luis-Oliveira" and followed the advanced steps in [here](https://github.com/guoliveira/data-engineer-zoomcamp-project/tree/main/GCP_Terraform)

3. Creation of a GCP infrastructure using Terraform. This infrastructure includes Big Query and Storage.  The steps can be seen [here](https://github.com/guoliveira/data-engineer-zoomcamp-project/blob/main/GCP_Terraform/Readme.md#creation-of-a-gcp-infrastructure);

4. [Development of DockerFile and Docker-Compose structure to run Airflow.](setup_docker.md)

5. [Start to run Airflow inside a container](Airflow/README.md) and [development of two DAG for the pipeline data.](Airflow/dags)