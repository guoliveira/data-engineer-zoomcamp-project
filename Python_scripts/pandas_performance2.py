import pandas as pd
import time
from cpu_ram import profile_mem, profile_cpu

@profile_cpu
@profile_mem
def extraction():
    path1="yellow_tripdata_2021-01.parquet"
    df_trips= pd_read_parquet(path1,)
    path2 = "taxi+_zone_lookup.parquet"
    df_zone = pd_read_parquet(path2,)

    return df_trips, df_zone


def pd_read_parquet(path, ):
    """
    Converting parquet file into Pandas dataframe
    """
    df= pd.read_parquet(path,)
    return df

@profile_cpu
@profile_mem
def transformation(df_trips, df_zone):
    df_trips= mean_test_speed_pd(df_trips)

    df = pd.merge(df_trips,df_zone,how="inner", left_on="PULocationID", right_on="LocationID",)
    df = df[["Borough","Zone","trip_distance"]]
    df = endwith_test_speed_pd(df)

    return df

def mean_test_speed_pd(df_pd):
    """
    Getting Mean per PULocationID
    """
    df_pd = df_pd[['PULocationID', 'trip_distance']]
    df_pd=df_pd.groupby('PULocationID').mean()
    return df_pd

def endwith_test_speed_pd(df_pd):
    """
    Only getting Zones that end with East
    """

    df_pd = df_pd[df_pd.Zone.str.endswith('East')]

    return df_pd

@profile_cpu
@profile_mem
def loading_into_parquet(df_pd, engine):
    """
    Save dataframe in parquet
    """
    df_pd.to_parquet(f'yellow_tripdata_2021-01_pd_v{pd.__version__}.parquet',engine)


def main():

    engine_pd='pyarrow'
    
    print(f'Starting ETL for Pandas version {pd.__version__}')
    print("\n")
    start_time = time.perf_counter()

    print('Extracting...')
    df_trips, df_zone =extraction()

    end_extract = time.perf_counter() 
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
    loading_into_parquet(df, engine_pd)
    load_transformation =time.perf_counter() - end_transform
    #print(f'Loading end in {round(load_transformation,3)} seconds')
    print("\n")
    print(f'End ETL for Pandas version {pd.__version__}')

if __name__ == "__main__":
    
    main()
