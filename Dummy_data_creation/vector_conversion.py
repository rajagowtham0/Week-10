# embedding_pipeline.py

from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
# CONFIG
MONGO_URI = "mongodb://localhost:27017"

SOURCE_DB = "ccms_ai"
SOURCE_COLLECTION = "patientrecording"

TARGET_DB = "ccms_embeddings"
TARGET_COLLECTION = "embedded_cases"

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDING_VERSION = "1.0"
# LOAD MODEL (ONLY ONCE)
print("Loading embedding model...")
model = SentenceTransformer(EMBEDDING_MODEL_NAME)
# CONNECT DB
client = MongoClient(MONGO_URI)
source_collection = client[SOURCE_DB][SOURCE_COLLECTION]
target_collection = client[TARGET_DB][TARGET_COLLECTION]
# STEP 1: DELETE OLD EMBEDDINGS
delete_result = target_collection.delete_many({})
print(f"Deleted {delete_result.deleted_count} old embedded records.")
# STEP 2: FETCH SOURCE DATA
records = list(source_collection.find())

if not records:
    raise RuntimeError("No source records found in MongoDB.")

print(f"Fetched {len(records)} records from source collection.")

documents = []
# STEP 3: GENERATE EMBEDDINGS
for idx, record in enumerate(records):

    case_id = record.get("case_id", "")
    symptoms = record.get("symptoms", "")
    notes = record.get("doctor_notes", "")
    treatment = record.get("treatment", "")

    # Combine text
    text = f"{symptoms}. {notes}".strip()

    # Generate embedding
    embedding = model.encode(text, convert_to_numpy=True)

    document = {
        "case_id": case_id,
        "symptoms": symptoms,
        "notes": notes,
        "treatment": treatment,
        "embedding": embedding.tolist(),
        "embedding_model": EMBEDDING_MODEL_NAME,
        "embedding_version": EMBEDDING_VERSION
    }

    documents.append(document)
# STEP 4: INSERT NEW EMBEDDINGS
if documents:
    insert_result = target_collection.insert_many(documents)
    print(f"Inserted {len(insert_result.inserted_ids)} embedded records successfully!")

print("Embedding pipeline completed successfully.")