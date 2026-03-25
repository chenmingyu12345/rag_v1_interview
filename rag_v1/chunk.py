from pathlib import Path


def split_text(text, chunk_size=100):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


docs_path = Path(__file__).resolve().parent / "docs.txt"

with open(docs_path, "r", encoding="utf-8") as f:
    text = f.read()

chunks = split_text(text)

print(chunks)
