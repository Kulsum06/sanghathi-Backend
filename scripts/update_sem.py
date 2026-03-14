
from pymongo import MongoClient

client = MongoClient("mongodb+srv://emithru:emith56cmrit@emithru.zv3i9.mongodb.net/?retryWrites=true&w=majority&appName=emithru")

db = client["cmrit_test"]

collection = db["studentprofiles"]

skip_sems = [8]

query = {"sem": {"$nin": skip_sems}}

update = {"$inc": {"sem": 1}}

result = collection.update_many(query, update)

print("Profiles updated:", result.modified_count)
