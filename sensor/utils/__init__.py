import pandas as pd
from sensor.config import mongo_client
from sensor.exception import SensorException
from sensor.logger import logging

def get_collection_as_dataframe(database_name, collection_name:str)->pd.DataFrame:
    """
    This function returns collection as Dataframe
    database_name: database name
    collection_name: collectionname
    =============================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id")
            df = df.drop("_id", axis = 1)
            logging.info(f"Rows and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e,sys)
