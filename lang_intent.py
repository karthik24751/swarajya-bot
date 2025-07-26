from langdetect import detect
import re
import spacy

# For more advanced intent extraction, spaCy/NLTK can be added later

# Simple keyword mapping for demo
SCHEME_KEYWORDS = {
    'ration': [
        'ration', # English
        'राशन',   # Hindi
        'బియ్యం', # Telugu
        'রেশন',   # Bengali
        'ரேஷன்',  # Tamil
        'ರೇಷನ್',  # Kannada
        'రేషన్',  # Telugu (alt)
        'రేషన్ కార్డు', # Telugu (phrase)
        'റേഷൻ',  # Malayalam
        'રેશન',   # Gujarati
        'ਰਾਸ਼ਨ',   # Punjabi
        'ରାସନ୍',   # Odia
        'রেশন কার্ড', # Bengali (phrase)
        'राशन কार्ड', # Hindi (phrase)
        'راشن',    # Urdu
        'ৰেচন',    # Assamese
        'ರೇಷನ್ ಕಾರ್ಡ್', # Kannada (phrase)
    ],
    'pension': [
        'pension', # English
        'पेंशन',   # Hindi
        'పెన్షన్',  # Telugu
        'পেনশন',   # Bengali
        'பென்ஷன்', # Tamil
        'ಪಿಂಚಣಿ',  # Kannada
        'പെൻഷൻ',  # Malayalam
        'પેન્શન',  # Gujarati
        'ਪੈਨਸ਼ਨ',   # Punjabi
        'ପେନ୍ସନ୍', # Odia
        'পেনশন কার্ড', # Bengali (phrase)
        'पेंशन कार्ड', # Hindi (phrase)
        'پنشن',    # Urdu
        'পেঞ্চন',  # Assamese
    ],
    'aadhar': [
        'aadhar', # English
        'आधार',   # Hindi
        'ఆధార్',  # Telugu
        'আধার',   # Bengali
        'ஆதார்',  # Tamil
        'ಆಧಾರ್',  # Kannada
        'ആധാർ',  # Malayalam
        'આધાર',   # Gujarati
        'ਆਧਾਰ',   # Punjabi
        'ଆଧାର',   # Odia
        'আধার কার্ড', # Bengali (phrase)
        'आधार কार्ड', # Hindi (phrase)
        'آدھار',   # Urdu
        'আধাৰ',   # Assamese
    ],
}

# Load spaCy English model for entity/intent extraction
try:
    nlp_en = spacy.load('en_core_web_sm')
except Exception:
    nlp_en = None

def detect_language(text):
    try:
        lang = detect(text)
    except Exception:
        lang = 'unknown'
    return lang


def extract_keywords(text):
    text = text.lower()
    found = []
    for scheme, keywords in SCHEME_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text:
                found.append(scheme)
    print(f"[DEBUG] Input: {text} | Found keywords: {found}")
    return list(set(found))


def extract_entities_and_intent(text, lang='en'):
    """
    Use spaCy to extract entities and try to infer intent for English (fallback for others).
    Returns: (intent, entities)
    """
    if lang == 'en' and nlp_en:
        doc = nlp_en(text)
        entities = [(ent.label_, ent.text) for ent in doc.ents]
        # Simple intent inference: look for scheme-related nouns
        intent = None
        for token in doc:
            if token.lemma_.lower() in SCHEME_KEYWORDS:
                intent = token.lemma_.lower()
                break
        return intent, entities
    return None, []


def clarification_question(text, lang='en'):
    """
    Generate a clarification question if intent is unclear.
    """
    if lang == 'en':
        return "Sorry, I couldn't understand your request. Could you please specify which scheme you need help with (e.g., ration, pension, aadhar)?"
    # For other languages, fallback to English for now
    return "Sorry, I couldn't understand your request. Please specify the scheme (ration, pension, aadhar)." 