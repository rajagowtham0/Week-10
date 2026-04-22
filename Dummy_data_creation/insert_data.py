from pymongo import MongoClient
from bson import ObjectId
import json

# Connect
client = MongoClient("mongodb://localhost:27017")
db = client["ccms_ai"]
collection = db["patientrecording"]
# Step 1: Delete existing data
collection.delete_many({})
print("Old data deleted.")
# Step 2: Load JSON
with open("mongo_insert.json") as f:
    data = json.load(f)
# Step 3: FIX _id FIELD
for doc in data:
    if "_id" in doc and "$oid" in doc["_id"]:
        doc["_id"] = ObjectId(doc["_id"]["$oid"])
# Step 4: Insert
collection.insert_many(data)

print("Data inserted successfully!")