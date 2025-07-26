from fastapi import FastAPI, Query
from pydantic import BaseModel
from nlp.lang_intent import detect_language, extract_keywords
from db.query import find_scheme

app = FastAPI()

class SchemeRequest(BaseModel):
    text: str
    language: str = None  # Optional, auto-detect if not provided

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/scheme-info")
def scheme_info(req: SchemeRequest):
    lang = req.language or detect_language(req.text)
    keywords = extract_keywords(req.text)
    if not keywords:
        return {"error": "No relevant scheme keywords found.", "language": lang}
    scheme = find_scheme(keywords, lang)
    if scheme:
        return {"language": lang, **scheme}
    else:
        return {"error": "No matching scheme found.", "language": lang} 