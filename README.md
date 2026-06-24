## Task 3: Semantic Retrieval with FAISS

### Objective
Implement semantic search to retrieve the most relevant complaint chunks based on a user query.

### Implementation
- Loaded the FAISS vector index created in Task 2.
- Loaded stored complaint text chunks.
- Converted user queries into embeddings using the `all-MiniLM-L6-v2` sentence transformer model.
- Performed similarity search using FAISS.
- Retrieved the top-k most relevant complaint chunks for a given query.

### Output
The retrieval pipeline successfully returns relevant complaint narratives based on semantic similarity rather than keyword matching.

### Files Added
- `notebooks/task3_retrieval.ipynb`
- `src/retrieval.py` (if created)

### Technologies Used
- Sentence Transformers
- FAISS Vector Database
- NumPy
- Python