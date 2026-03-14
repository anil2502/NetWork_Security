
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
load_dotenv() ################### need to know why we are calling this function right after importing ??????

MONGO_DB_CONNECTION_URL = os.getenv("MONGO_DB_USER_URL")

# Create a new client and connect to the server
client = MongoClient(MONGO_DB_CONNECTION_URL, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)