import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_PATH_FILE = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df = pd.read_csv(DATA_PATH_FILE)
    print(f"Rows and columns:{df.shape}")
    
    #Convert dataframe to json so that we can dump these recors in mongoDB
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json record to mongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    