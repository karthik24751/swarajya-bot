import os
import sys

# Add current directory to sys.path to allow relative imports
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from nlp.lang_intent import detect_language, extract_keywords
from db.query import find_scheme

# Initialize FastAPI app
app = FastAPI(
    title="Government Scheme Info API",
    description="Detects language, extracts keywords, and retrieves matching government schemes.",
    version="1.0.0"
)

# Enable CORS (important if accessed from browser or Telegram bot)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class SchemeRequest(BaseModel):
    text: str
    language: str = None  # Optional – auto-detect if not provided

# Health check route
@app.get("/health")
def health():
    return {"status": "ok"}

# Main route
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
