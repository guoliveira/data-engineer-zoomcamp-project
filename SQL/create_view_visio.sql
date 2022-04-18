  CREATE VIEW `capstone-luis-oliveira-347008.weather_historical_data.weather_data_visio` AS
    SELECT
      wd.date
      , wd.TAVG as temp_avg
      , wd.year
      , ws.lat
      , ws.long
      , if(ws.Region='Continente', concat(ws.Area,' - ',ws.Region),ws.Region ) as portuguese_region
    FROM
      `capstone-luis-oliveira-347008.weather_historical_data.weather_data` wd
    INNER JOIN `capstone-luis-oliveira-347008.weather_historical_data.weather_stations` ws
    on wd.stations_code=ws.code
