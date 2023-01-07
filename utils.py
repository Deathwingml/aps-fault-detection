import pandas as pd
import os, sys
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client


def get_collection_as_dataframe(database_name: str, collection_name:str)->pd.DataFrame:
    """
    Description: This function returns collection as a pandas DataFrame
    ===================================================================
    Params:
    database_name: database name
    collection_name: collection name
    ===================================================================
    return Pandas dataframe of a collection
    """
    
    try:
        logging.info(f"Reading data from database: {database_name} and collection : {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in columns:  #MongoDB addes a _id columns which is not necessary in our dataframe
            logging.info(f"Dropping column: _id")
            df = df.drop("_id", axis = 1)
        logging.info(f"Rows and Columns in df: {df.shape}")
        return df
    
    except Exception as e:
        raise SensorException(e, sys)