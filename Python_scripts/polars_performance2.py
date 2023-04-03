import polars as pl
import time
from cpu_ram import profile_mem, profile_cpu

@profile_cpu
@profile_mem
def extraction():
    path1="yellow_tripdata_2021-01.parquet"
    df_trips= pl_read_parquet(path1,)
    path2 = "taxi+_zone_lookup.parquet"
    df_zone = pl_read_parquet(path2,)

    return df_trips, df_zone

def pl_read_parquet(path, ):
    """
    Converting parquet file into Pandas dataframe
    """
    df= pl.read_parquet(path,)
    return df

@profile_cpu
@profile_mem
def transformation(df_trips, df_zone):
    df_trips= mean_test_speed_pl(df_trips)
    df = df_trips.join(df_zone,how="inner", left_on="PULocationID", right_on="LocationID",)
    df = df[["Borough","Zone","trip_distance"]]
    df = endwith_test_speed_pd(df)
    return df

def mean_test_speed_pl(df_pl):
    """
    Getting Mean per PULocationID
    """
    df_pl = df_pl[['PULocationID', 'trip_distance']].groupby('PULocationID').mean()
    return df_pl


def endwith_test_speed_pd(df_pl):
    """
    Only getting Zones that end with East
    """

    df_pl = df_pl.filter(pl.col("Zone").str.ends_with('East'))

    return df_pl

@profile_cpu
@profile_mem
def loading_into_parquet(df_pl):
    """
    Save dataframe in parquet
    """
    df_pl.write_parquet(f'yellow_tripdata_2021-01_pl.parquet')

def main():
    
    print(f'Starting ETL for Polars')
    print("\n")
    start_time = time.perf_counter()

    print('Extracting...')
    df_trips, df_zone =extraction()
       
    end_extract=time.perf_counter() 
    time_extract =end_extract- start_time

    #print(f'Extraction Parquet end in {round(time_extract,3)} seconds')
    
    print("\n")
    print('Transforming...')
    df = transformation(df_trips, df_zone)
    end_transform = time.perf_counter() 
    time_transformation =time.perf_counter() - end_extract
    #print(f'Transformation end in {round(time_transformation,3)} seconds')
    
    print("\n")
    print('Loading...')
    loading_into_parquet(df,)
    load_transformation =time.perf_counter() - end_transform
    #print(f'Loading end in {round(load_transformation,3)} seconds')
    print("\n")
    print(f'End ETL for Polars ')

if __name__ == "__main__":
    
    main()
