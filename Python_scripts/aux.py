import polars as pl


def pl_read_csv(path, ):
    """
    Converting csv file into Pandas dataframe
    """
    df= pl.read_csv(path,)
    return df


def loading_into_parquet(df_pl):
    """
    Save dataframe in parquet
    """
    df_pl.write_parquet(f'taxi+_zone_lookup.parquet')


def main():
    path2="taxi+_zone_lookup.csv"
    df_zone= pl_read_csv(path2, )
    
    loading_into_parquet(df_zone)

if __name__ == "__main__":
    
    main()
