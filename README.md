# Average Temperature in Portugal in the last 20 years 😎
## Data Engineer Zoomcamp Capstone Project

This capstone project was developed under the scope of the [Data Engineer Zoomcamp by DataTalksClub](https://github.com/DataTalksClub/data-engineering-zoomcamp) (the biggest Data community in the internet - [DTC](https://datatalks.club/)).

The above zoomcamp had the following main topics/tools:
- Docker and docker-compose;
- Google Cloud Platform;
- Terraform;
- Airflow;
- Data Warehouse with Big Query;
- Analytics Engineering with Data Build Tool (DBT);
- Batch streaming with Spark;
- Streaming with Kafka.

The zoomcamp is completed with a personal [Project](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_7_project) envolving some of those tools/topics.

For my project I decided to analyse the historical temperature in Portugal in the last 20 years. 
More specifically, I decided to analyse the average temperature from 2000 to 2020. (It was decided to avoid 2021 due possible mistakes and 2022 since it is incomplete).

**With this project I intend to see if there were any temperature trend over the last 20 years**

In terms of dataset I had many choices, but I decided to use the [NOAA dataset](https://registry.opendata.aws/noaa-ghcn/) available in the AWS Open Data.

This dataset has the following description:

*Global Historical Climatology Network - Daily is a dataset from NOAA that contains daily observations over global land areas. It contains station-based measurements from land-based stations worldwide, about two thirds of which are for precipitation measurement only. Other meteorological elements include, but are not limited to, daily maximum and minimum temperature, temperature at the time of observation, snowfall and snow depth. It is a composite of climate records from numerous sources that were merged together and subjected to a common suite of quality assurance reviews. Some data are more than 175 years old. The data is in CSV format. Each file corresponds to a year from 1763 to present and is named as such.*

## Used Technologies 🔨

For this project it was decided to use the following tools:
- Docker - to proceed to the containerization of other technologies;
- Airflow - for the orchestration of the full pipeline;
- Terraform - As a Infrastructure-as-Code (IaC) tool;
- Google Cloud Storage (GCS) - for storage as Data Lake;
- BigQuery: for the project Data Warehouse;
- Spark: for the transformation of raw data in refined data.


## Development Steps 🚧

This capstone followed these general development steps:

1. Started a Google Cloud Platform free account (this step was skipped since we already built before for the zoomcamp);

2. Creation of GCP project with the name "Capstone-Luis-Oliveira" and [followed the advanced steps in here](https://github.com/guoliveira/data-engineer-zoomcamp-project/tree/main/GCP_Terraform)

3. Creation of a GCP infrastructure using Terraform. This infrastructure includes Big Query and Storage.  [The steps can be seen here](https://github.com/guoliveira/data-engineer-zoomcamp-project/blob/main/GCP_Terraform/Readme.md#creation-of-a-gcp-infrastructure);

4. [Development of DockerFile and Docker-Compose structure to run Airflow.](setup_docker.md)

5. [Start to run Airflow inside a container](Airflow/README.md) and [development of two DAG for the pipeline data.](Airflow/dags)

6. Ran the two Dags in order get the raw files and refined (after transformation) files in GCP Storage. [The data pipeline is presented here.](pipeline.md)

7. Creation of two tables in BigQuery using DDL. One table with Portuguese weather station information (code, latitude, longitude, region and location) and one partitioned table with the average temperature by day and by station (this table was partition by year).

***It was decided to run a DDL Query in BigQuery because it was going to be done only once (it was an unnecessary energy to set it in Airflow)***

The DDL queries are presented here.

8. Development of some "questions to the data" in order to perform an analyses.

9. Development of a visualization using ...


