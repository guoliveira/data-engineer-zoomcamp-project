# Data pipeline 🤖

The main goal of my pipeline was to extract data from NOAA dataset into GCP Storage in the raw format and refined format (after transformation)

Therefore, according to the project objectives, I build two data pipelines for:
1. To load the data of the Portuguese weather station. And all weather stations in the raw format.
2. Load data of the weather dataset of last 20 years in raw format. And load Portuguese temperature data of the last 20 years.

## Portuguese weather stations

The objective of this pipeline is to extract the .txt file from the NOAA/Aws repository, load the txt file into the GCP raw storage, transform this file into a parquet file and load into GCP refined storage.

Hence, the tasks developed are:
1. Download of the txt file using ...
2. Load the previous file into BUCKET/raw/weather_stations/
3. Transform the txt file into a parquet file using the following rules:
* Extract attributes code, lat an long
* Filter by stations with code starting PO (Portugal)



