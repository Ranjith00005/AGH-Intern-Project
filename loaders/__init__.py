from .json_loader import load_json
from .text_loader import load_text
from .pdf_loader import load_pdf
from .js_loader import load_js

def load_file(path: str) -> list[str]:
    if path.endswith(".json"):
        return load_json(path)
    elif path.endswith(".txt"):
        return load_text(path)
    elif path.endswith(".pdf"):
        return load_pdf(path)
    elif path.endswith(".js"):
        return load_js(path)
    else:
        raise ValueError(f"Unsupported file type: {path}")
