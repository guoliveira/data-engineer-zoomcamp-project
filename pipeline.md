# Data pipeline 🤖

The main goal of my pipeline was to extract data from NOAA dataset into GCP Storage in the raw format and refined format (after transformation)

Therefore, according to the project objectives, I build two data pipelines for:
1. To load the data of the Portuguese weather station. And all weather stations in the raw format.
2. Load data of the weather dataset of last 20 years in raw format. And load Portuguese temperature data of the last 20 years.

## Portuguese weather stations

The objective of this pipeline was to extract the .txt file from the NOAA/AWS repository, load the txt file into the GCP raw storage, transform this file into a parquet file and load into GCP refined storage.

Hence, the tasks developed are:
1. Download of the .txt file using a bash operator using curl;
2. Load the previous file into BUCKET/raw/weather_stations/;

4. Transform the txt file into a parquet file using the following rules:
* Extract attributes code, lat an long
* Filter by stations with code starting PO (Portugal)
* According with the latitude and longitude it was created two columns one to say if it was Portugues Mainland ("Continente") or one of the Islands ("Madeira" or "Açores") and another column indicating the area of the Mainland - North, Center or South ("Norte", "Centro" and "Sul").
* Performed one small correction on one weather station;
*  Converted the dataset into parquet file;
5. Load the previous file into BUCKET/refined/weather_stations/
6. Deleted the .txt file from local

This pipeline was only run once.

## Historical Portuguese average temperature

The objective of this pipeline was to extract all the 20 .csv.gz files from the NOAA/AWS repository, load the raw files into the GCP raw storage, transform these files into parquet and load them into GCP refined storage.

Hence, the tasks developed are:
1. Download of the .csv.gz file using a bash operator using curl;
2. Load the previous file into BUCKET/raw/weather_data/;
3. Transform the .csv.gz file into a parquet file using pySpark and the following rules:
* Converted the .csv.gz dataset into a dataframe;
* Converted the previous dataframe into a temp SQL table;
* Converted the weather_stations parquet file into a temp SQL table;
* Using a query it was extracted only the Portuguese data and the Average Temperature (that needed to be divided by 10)
* From the previous result it was performed a pivot to get the Average temperature as an attribute;
* Converted the dataset into parquet file in <local>/data/<YYYY>;
5. Rename the parquet into <local>/data/<YYYY>/pt_avg_temp.snappy.parquet
6. Load the previous file into BUCKET/refined/weather_data/year=<YYYY>/
7. Deleted the .csv.gz file from local
  
 This pipeline was set to run 20 times in order to get data from 2000 to 2020, therefore the execution date started in 2000 and ended at 2020.
