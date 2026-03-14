import os, json, sys
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_CONNECTION_URL = os.getenv("MONGO_DB_USER_URL")
# print(MONGO_DB_CONNECTION_URL)




import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            # .T ==> for to convert the DataFramer(tabular Data) Data in to Json
            # .to_json() ==> convert that values in to the json stringified json
            # Json.loads() ==> is used to convert the stringified json to python dictionary
            # .values() ==> will return the dict values
            # list() ==> typecasting dict values in to the list
            # ###### As a result we now we got list of dicts  
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_CONNECTION_URL)
            self.database = self.mongo_client[self.database] # selecting the DataBase, while posting/pushing new Data, create a database if there is no such database
            
            self.collection=self.database[self.collection] # selecting the Collection/Table, while posting/pushing new Data, create a Collection/Table if there is no such Collection/Table
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="AnilDB"            # DataBase Name
    Collection="NetworkData"      # tabe Name
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    # print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)
        


