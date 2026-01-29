def load_text(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # simple chunking
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    return chunks
