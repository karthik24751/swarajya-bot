import os
import sys

# Ensure the current directory is in the path so submodules can be imported
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from fastapi import FastAPI
from pydantic import BaseModel
from nlp.lang_intent import detect_language, extract_keywords
from db.query import find_scheme

app = FastAPI()

class SchemeRequest(BaseModel):
    text: str
    language: str = None  # Optional – will auto-detect if not given

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/scheme-info")
def scheme_info(req: SchemeRequest):
    try:
        lang = req.language or detect_language(req.text)
        keywords = extract_keywords(req.text)

        if not keywords:
            return {"error": "No relevant scheme keywords found.", "language": lang}

        scheme = find_scheme(keywords, lang)
        if scheme:
            return {"language": lang, **scheme}
        else:
            return {"error": "No matching scheme found.", "language": lang}

    except Exception as e:
        return {"error": str(e)}
