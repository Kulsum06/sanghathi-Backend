
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))

db = client["cmrit_test"]

collection = db["studentprofiles"]

skip_sems = [8]

query = {"sem": {"$nin": skip_sems}}

update = {"$inc": {"sem": 1}}

result = collection.update_many(query, update)

print("Profiles updated:", result.modified_count)
