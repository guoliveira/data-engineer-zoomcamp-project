-- To create dimension table weather_stations
CREATE EXTERNAL TABLE `capstone-luis-oliveira-347008.weather_historical_data.weather_stations`
    OPTIONS (
      uris=['gs://dtc_data_lake_capstone-luis-oliveira-347008/refined/stations/*'],
      format=parquet,
      hive_partition_uri_prefix='gs://dtc_data_lake_capstone-luis-oliveira-347008/refined/stations'
    );
    
    
  -- To create fact table weather_data that is partitioned by Year  
   CREATE EXTERNAL TABLE `capstone-luis-oliveira-347008.weather_historical_data.weather_data`
    WITH PARTITION COLUMNS (
      year INT64
    )
    OPTIONS (
      uris=['gs://dtc_data_lake_capstone-luis-oliveira-347008/refined/weather_data/*'],
      format=parquet,
      hive_partition_uri_prefix='gs://dtc_data_lake_capstone-luis-oliveira-347008/refined/weather_data'
    );
