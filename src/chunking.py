from langchain_text_splitters import RecursiveCharacterTextSplitter


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


documents = []

for text in sample_df["clean_complaint"]:
    chunks = text_splitter.split_text(text)
    documents.extend(chunks)


len(documents)

import pickle

with open(
    "data/vectorstore/documents.pkl",
    "wb"
) as f:
    pickle.dump(documents, f)