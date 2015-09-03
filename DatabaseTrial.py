from pymongo import MongoClient
import datetime

client = MongoClient()
db = client['test_database']
collection = db['test_collection']

post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}

collection.insert_one(post)
