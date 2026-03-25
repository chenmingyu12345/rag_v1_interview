import os

os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Artificial Intelligence is the simulation of human intelligence.",
    "Machine learning is a subset of AI.",
]

embeddings = model.encode(sentences)

print(embeddings.shape)

query = "What is AI?"

query_embedding = model.encode([query])

similarity = cosine_similarity(query_embedding, embeddings)

print(similarity)
