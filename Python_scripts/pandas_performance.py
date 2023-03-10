import pandas as pd
import time
import pyarrow as pa


def pd_read_csv(path, engine_pd,):
    """
    Converting csv file into Pandas dataframe
    """
    df= pd.read_csv(path, engine=engine_pd)
    return df

def pd_read_parquet(path, ):
    """
    Converting parquet file into Pandas dataframe
    """
    df= pd.read_parquet(path,)
    return df

def mean_test_speed_pd(df_pd):
    """
    Getting Mean per PULocationID
    """
    df_pd = df_pd[['PULocationID', 'trip_distance']]
    df_pd["PULocationID_column"] = df_pd[['PULocationID']].astype(int)
    df_pd=df_pd.groupby('PULocationID').mean()
    return df_pd

def endwith_test_speed_pd(df_pd):
    """
    Only getting Zones that end with East
    """

    df_pd = df_pd[df_pd.Zone.str.endswith('East')]

    return df_pd


def loading_into_parquet(df_pd, engine):
    """
    Save dataframe in parquet
    """
    df_pd.to_parquet(f'yellow_tripdata_2021-01_pd_v{pd.__version__}.parquet',engine)


def main():

    if pd.__version__ =='2.0.0rc0':
        pd.options.mode.dtype_backend = 'pyarrow'
    engine_pd='pyarrow'
    
    print(f'Starting ETL for Pandas version {pd.__version__}')
    start_time = time.perf_counter()

    print('Extracting...')
    path1="yellow_tripdata_2021-01.parquet"
    df_trips= pd_read_parquet(path1,)
    path2 = "taxi+_zone_lookup.csv"
    df_zone = pd_read_csv(path2, engine_pd)
    end_extract = time.perf_counter() 
    time_extract =end_extract- start_time
    print(f'Extraction Parquet end in {round(time_extract,3)} seconds')

    print('Transforming...')
    df_trips= mean_test_speed_pd(df_trips)
    df = pd.merge(df_trips,df_zone,how="inner", left_on="PULocationID_column", right_on="LocationID",)
    df = df[["Borough","Zone","trip_distance"]]
    df = endwith_test_speed_pd(df)
    end_transform = time.perf_counter() 
    time_transformation =time.perf_counter() - end_extract
    print(f'Transformation end in {round(time_transformation,3)} seconds')

    print('Loading...')
    loading_into_parquet(df, engine_pd)
    load_transformation =time.perf_counter() - end_transform
    print(f'Loading end in {round(load_transformation,3)} seconds')

    print(f'End ETL for Pandas version {pd.__version__}')

if __name__ == "__main__":
    
    main()
