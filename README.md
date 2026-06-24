# Task 2 Report: Text Chunking, Embedding, and Vector Store Indexing

## Objective

The objective of Task 2 was to transform cleaned complaint narratives into a format suitable for semantic search using text chunking, embeddings, and vector indexing.

---

## 1. Dataset Preparation

The complaint dataset was loaded and filtered to keep only:

- Product
- Consumer complaint narrative

Empty complaint narratives were removed.

Because the available processed dataset contained limited valid narratives, the available records were used for experimentation.

---

## 2. Text Chunking

The complaint narratives were split into smaller overlapping chunks using:

- Tool: RecursiveCharacterTextSplitter
- Chunk size: 500 characters
- Chunk overlap: 50 characters

This improves retrieval performance because long complaints can be searched at a more detailed level.

Example:

Input:

"Customer reported unauthorized transactions..."

Output:

Chunk 1:
"Customer reported unauthorized transactions..."

Chunk 2:
"Transactions continued after contacting support..."

---

## 3. Embedding Generation

Text chunks were converted into numerical vectors using:

Model:

all-MiniLM-L6-v2

Library:

Sentence Transformers

Each text chunk was represented as a 384-dimensional vector.

Example output:

(number_of_chunks, 384)

---

## 4. Vector Store Indexing

FAISS was used as the vector database.

Process:

1. Convert embeddings into float32 arrays.
2. Create FAISS IndexFlatL2 index.
3. Store complaint embeddings.
4. Save index for future semantic search.

Files generated:


data/vectorstore/
│
├── complaints.index
└── documents.pkl


---

## 5. Results

The pipeline successfully transformed raw complaint narratives into searchable vector representations.

The output can now support semantic retrieval for the RAG chatbot.

---

## Conclusion

Task 2 successfully completed:

✓ Complaint chunking  
✓ Text embedding generation  
✓ FAISS vector indexing  
✓ Persistent vector store creation