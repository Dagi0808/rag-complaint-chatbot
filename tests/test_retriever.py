from src.retriever import ComplaintRetriever


retriever = ComplaintRetriever()


results = retriever.search(
    "I was charged an incorrect fee",
    k=3
)


for r in results:
    print("----------------")
    print(r["text"])