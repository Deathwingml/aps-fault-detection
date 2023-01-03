import pymongo
import pandas as pd
import json

#Data file path
data_file_path = "/config/workspace/aps_failure_training_set1.csv"


# Provide the mongodb localhost url to connect python to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Creating the database and collection
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"


if __name__ == "__main__":
    df = pd.read_csv(data_file_path)
    print(f"Number of Rows and Columns: {df.shape}")

    # Convert dataframe into JSON to dump the records in MongoDB
    df.reset_index(drop= True, inplace= True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[2])
    
    #insert converted json record to MongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


