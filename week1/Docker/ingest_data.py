#!/usr/bin/env python
# coding: utf-8

import os
import wget
import urllib.request
import argparse
import pandas as pd
from time import time
from sqlalchemy import create_engine

def connection(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'

    # Download CSV file
    #print(csv_name, url)
    urllib.request.urlretrieve(url,csv_name)


    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
  
    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')
    
    df.to_sql(name=table_name, con=engine, if_exists='append')
    
    while True:
        
        try:
            df = next(df_iter)        
            ts = time()    
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            df.to_sql(name=table_name, con=engine, if_exists='append')
            te = time()
            print('Another chunk has been inserted, took %.3f seconds' % (te-ts))
    
        except:
            print('All data has been uploaded to the table')
            break

    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres.')

    parser.add_argument('--user', help='username for Postgres')
    parser.add_argument('--password', help='password for Postgres')
    parser.add_argument('--host', help='host for Postgres')
    parser.add_argument('--port', help='post for Postgres')
    parser.add_argument('--db', help='database name for Postgres')
    parser.add_argument('--table_name', help='name of the table where the results will be written')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    connection(args)

