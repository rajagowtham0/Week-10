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
