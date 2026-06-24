import faiss
import pickle
from sentence_transformers import SentenceTransformer


class ComplaintRetriever:

    def __init__(
        self,
        index_path="vectorstore/complaints.index",
        documents_path="vectorstore/documents.pkl"
    ):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.index = faiss.read_index(
            index_path
        )

        with open(documents_path, "rb") as f:
            self.documents = pickle.load(f)


    def search(self, query, k=5):

        query_embedding = self.model.encode(
            [query]
        )

        query_embedding = query_embedding.astype(
            "float32"
        )

        distances, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for idx, distance in zip(
            indices[0],
            distances[0]
        ):
            results.append({
                "text": self.documents[idx],
                "distance": float(distance)
            })

        return results