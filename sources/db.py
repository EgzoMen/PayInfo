from pymongo import MongoClient, errors
from dotenv import load_dotenv
from os import getenv

load_dotenv()

connection = MongoClient('mongodb://localhost:27017')
db = connection.get_database(getenv('db_name'))
product_collection = db.get_collection(getenv('collection_name'))
