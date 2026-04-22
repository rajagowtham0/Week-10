from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["ccms_ai"]
collection = db["patientrecording"]
# Step 1: Remove all existing documents
delete_result = collection.delete_many({})
print(f"Deleted {delete_result.deleted_count} existing documents.")
# Step 2: Load new dataset
with open("mongo_insert.json") as f:
    data = json.load(f)
# Step 3: Insert new documents
insert_result = collection.insert_many(data)
print(f"Inserted {len(insert_result.inserted_ids)} new documents successfully!")