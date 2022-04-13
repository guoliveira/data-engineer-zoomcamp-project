# Weather in Portugal in the last 30 years 😎
## Data Engineer Zoomcamp Capstone Project

This captstone project was developed under the scope of the [Data Engineer Zoomcamp by DataTalksClub](https://github.com/DataTalksClub/data-engineering-zoomcamp) (the biggest Data community in the internet - [DTC](https://datatalks.club/)).

The above zoomcamp had the following main topics/tools:
- Docker and docker-compose;
- Google Cloud Platform;
- Terraform;
- Airflow;
- Data Warehouse with Big Query;
- Analytics Engineering with Data Build Tool (DBT);
- Batch streaming with Spark;
- Streaming streaming with Kafka.

The zoomcamp is completed with a personal [Project](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_7_project) envolving some of those tools/topics.

For my project I decided to analyse the historical weather in Portugal in the last 30 years. More specifically, I decided to analyse average temperature from 1990 to 2020. (It was decided to avoid 2021 due possible mistakes and 2022 since it is incomplete).
**With this project I intend to see if there were any changes in temperature over the last 30 years showing it in a chart.**

In terms of dataset I had many choices but I decided to use the [NOAA dataset](https://registry.opendata.aws/noaa-ghcn/) available in the AWS Open Data.

This dataset has the following description:

*Global Historical Climatology Network - Daily is a dataset from NOAA that contains daily observations over global land areas. It contains station-based measurements from land-based stations worldwide, about two thirds of which are for precipitation measurement only. Other meteorological elements include, but are not limited to, daily maximum and minimum temperature, temperature at the time of observation, snowfall and snow depth. It is a composite of climate records from numerous sources that were merged together and subjected to a common suite of quality assurance reviews. Some data are more than 175 years old. The data is in CSV format. Each file corresponds to a year from 1763 to present and is named as such.*

## Technologies 🔨

For this project it was decided to use the following tools:
- Docker - to proceed to the containerization of other technologies;
- Airflow - for the orchestration of the full pipeline;
- Terraform - As a Infrastructure-as-Code (IaC) tool;
- Google Cloud Storage (GCS) - for storage as Data Lake;
- BigQuery: for the project Data Warehouse;
- Spark: for the transformation of raw data in refined data.

**It is possible to see the developed data pipeline (high-level ETL/ELT process) of the project at [the following link.](pipeline.md)**

**All the general development steps made in this project are mention [here.](https://github.com/guoliveira/data-engineer-zoomcamp-project/blob/main/development_steps.md)**

