import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os
#connecting to MongoDB as localhost

@dataclass
class EnvironmentVariable:
    mongo_db_url: str = os.getenv("Mongo_DB_URL")


env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient()