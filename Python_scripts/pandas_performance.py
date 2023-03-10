import pandas as pd
import time


def pd_read_csv():
    """
    Converting csv file into Pandas dataframe
    """
    df= pd.read_csv("yellow_tripdata_2021-01.csv.gz")
    return df


def main():

    if pd.__version__ =='2.0.0rc0':
        pd.options.mode.dtype_backend = 'pyarrow'
    
    print(f'Starting ETL for Pandas version {pd.__version__}')
    start_time = time.perf_counter()

    df= pd_read_csv()

    print(time.perf_counter() - start_time)

if __name__ == "__main__":
    
    main()
