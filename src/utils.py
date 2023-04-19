from src.logger import logging
from src.exception import CustomException
import sys
from pymongo import MongoClient
import certifi
import pandas as pd

def read_mongodb(connection):
    try:
        client= MongoClient(connection,tlsCAFile=certifi.where())
        db=client['Data']
        database=db.Spotify_Dataset
        cursor=database.find()
        list_cur = list(cursor)
        df = pd.DataFrame(list_cur)
        df=df.drop(['_id'],axis='columns')
        return df
    except Exception as E:
        raise CustomException(E,sys)