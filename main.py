import os
import sys

# Ensure the current directory is in the path so submodules can be imported
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from nlp.lang_intent import detect_language, extract_keywords
from db.query import find_scheme

# Initialize the FastAPI app
app = FastAPI(
    title="Government Scheme Info API",
    description="API to detect language, extract keywords, and find relevant government schemes.",
    version="1.0.0"
)

# Optional: Add CORS middleware if you plan to access this API from a frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class SchemeRequest(BaseModel):
    text: str
    language: str = None  # Optional – will auto-detect if not given

# Health check route
@app.get("/health")
def health():
    return {"status": "ok"}

# Main scheme info route
@app.post("/scheme-info")
def scheme_info(req: SchemeRequest):
    try:
        lang = req.language or detect_language(req.text)
        keywords = extract_keywords(req.text)

        if not keywords:
            return {
                "error": "No relevant scheme keywords found.",
                "language": lang,
                "keywords": []
            }

        scheme = find_scheme(keywords, lang)
        if scheme:
            return {
                "language": lang,
                "keywords": keywords,
                **scheme
            }
        else:
            return {
                "error": "No matching scheme found.",
                "language": lang,
                "keywords": keywords
            }

    except Exception as e:
        return {"error": f"Internal error: {str(e)}"}
