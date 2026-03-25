from pathlib import Path

docs_path = Path(__file__).resolve().parent / "docs.txt"

with open(docs_path, "r", encoding="utf-8") as f:
    text = f.read()

print(text)
