from src.logger import logging
from src.exception import CustomException
import sys
from pymongo import MongoClient
import certifi
import pandas as pd 
import os
import dill
import numpy as np
from typing import List
import math
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
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
def emotion_average(file_path:str)->List[str]:
    emotion=[]
    try:
        with open(file_path) as file_obj:
            emotion=file_obj.readlines()
            int_list=[]
            emotion=[em.replace("\n",'') for em in emotion]
            for string in emotion:
                integer = int(string)
                int_list.append(integer)
            eavg= math.floor(sum(int_list) / len(int_list))
            if eavg==0 or eavg==1 or eavg==2 or eavg==4:
                return 0
            return 1
    except Exception as e:
        raise CustomException(e,sys)
def normalize(x):
    try:
        y = (x - np.mean(x))
        y/=np.std(x)
        return y
    except Exception as e:
        raise CustomException(e,sys)
def string(r):
    try:
        k=str(r['id'])

        tokens = k.split()

        # extract the second token
        id_string = tokens[1]

        # print the extracted string
        return id_string
    except Exception as e:
        raise CustomException(e,sys)
    