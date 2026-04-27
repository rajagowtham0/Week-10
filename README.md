# CCMS_AI Application

## Project overview
The CCMS AI system is designed to retrieve similar patient cases based on input symptoms and doctor notes. 
It uses embedding-based similarity and FAISS search to identify relevant past cases and generate structured insights.
## Project structure
ccms_ai/
1. data_processing/
1. database.py            # Handles MongoDB connection and data retrieval
2. models/
1. models.py              # Defines API request, response schemas, and top similar cases retrieval
3. retrieval/
1. retrieval_engine.py    # Core pipeline: retrieval + insight generation
2. vector_index.py        # FAISS index creation and similarity search
4. utils/
1. embedding.py           # Embedding generation, caching, and storage
2. config.py              # Configuration settings (DB, model, parameters)
5. app.py              # FastAPI application

## Module overview
### data_processing/database.py
Manages database operations, including fetching stored cases and embeddings.
### models/models.py
Defines structured request and response formats for the API.
### retrieval/retrieval_engine.py
Implements the main pipeline for retrieving similar cases and generating insights.
### retrieval/vector_index.py
Handles FAISS-based indexing and similarity search.
### utils/embedding.py
Generates embeddings and manages caching and storage.
### utils/config.py
Stores configuration variables such as database connection and model details.
### app.py
Serves as the main API layer connecting all components.

## Dummy data creation overview
Dataset Creation → MongoDB Storage → Embedding Generation → Vector Database
### Dataset_creation.py
Generates synthetic clinical case records for acne, pigmentation, 
and hair loss conditions with structured attributes.
### insert_data.py
Inserts the generated dataset into MongoDB (ccms_ai.patientrecording) 
after clearing existing records.
### vector_conversion.py
Transforms clinical text (symptoms + doctor notes) into dense vector embeddings using a SentenceTransformer model and stores them in ccms_embeddings.embedded_cases.
### mongo_insert.json
Intermediate dataset file used for batch insertion into MongoDB.

## Dependencies
### pip install fastapi uvicorn pymongo sentence-transformers faiss-cpu numpy
### FastAPI
Used to build the REST API for handling clinical query requests.
### Uvicorn
ASGI server required to run the FastAPI application.
### PyMongo
Enables interaction with MongoDB for fetching and storing clinical case data.
### Sentence-Transformers
Generates dense vector embeddings from clinical text for semantic similarity.
### FAISS (faiss-cpu)
Provides efficient vector indexing and fast nearest-neighbor search.
### NumPy
Handles numerical operations and embedding vector transformations.

## Running the API service
### Ensure MongoDB is running locally
1. The application depends on stored embeddings and case data.
2. Default connection: mongodb://localhost:27017
### Start the FastAPI server
uvicorn app:app --reload
### Access the API interface
http://127.0.0.1:8000/docs
1. Interactive Swagger UI will be available for testing endpoints.
2. The FAISS index and embeddings are initialized automatically at startup.
### API Request
{
  "symptoms": "hair thinning and excessive shedding",
  "doctor_notes": "telogen effluvium"
}
### API Response
{
  "similar_cases":
  [
    {
      "case_id": "HAIR_034",
      "similarity_score": 0.9043
    },
    {
      "case_id": "HAIR_002",
      "similarity_score": 0.903
    },
    {
      "case_id": "HAIR_011",
      "similarity_score": 0.9025
    },
    {
      "case_id": "HAIR_019",
      "similarity_score": 0.9008
    },
    {
      "case_id": "HAIR_010",
      "similarity_score": 0.9006
    }
  ]
  ,
  "symptoms": "The similarity is mainly due to shared symptoms such as hair, thinning",
  "treatment": "In similar past cases, patients well responded PRP therapy",
  "similarity_score": "Based on the 5 similar patients, the weighted confidence score obtained is 0.902"
}