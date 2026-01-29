import json

def load_json(path: str) -> list[str]:
    """
    Load JSON file and convert each top-level object to text
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []

    if isinstance(data, dict):
        for key, value in data.items():
            documents.append(str(value))
    elif isinstance(data, list):
        for item in data:
            documents.append(str(item))

    return documents
