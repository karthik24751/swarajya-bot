# Swarajya: Multilingual Welfare Scheme Voice Assistant Bot

Swarajya is a Telegram-based voice assistant that helps Indian citizens access information about government welfare schemes using voice or text in multiple Indian languages (starting with Hindi and Telugu).

## Features
- Accepts voice notes and text messages via Telegram
- Transcribes voice messages (Whisper/Vosk)
- Detects language and extracts intent
- Retrieves info from a welfare schemes database (SQLite)
- Responds with text and audio (gTTS)
- Multilingual support (Hindi, Telugu)

## Setup Instructions

1. **Clone the repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env` and add your Telegram bot token:
     ```
     TELEGRAM_TOKEN=your_telegram_bot_token_here
     ```

4. **Run the bot**
   ```bash
   python bot/bot.py
   ```

## FastAPI Backend

To run the FastAPI backend (for modularity or future expansion):

```bash
uvicorn api.main:app --reload
```

### Endpoints
- `GET /health` — Health check
- `POST /scheme-info` — Get scheme info
  - Request JSON: `{ "text": "message", "language": "hi" }` (language optional)
  - Response JSON: scheme info or error

## Project Structure
- `bot/` — Telegram bot logic
- `api/` — FastAPI backend (optional)
- `db/` — SQLite database and scripts
- `nlp/` — Language detection and intent extraction
- `tts/` — Text-to-speech utilities
- `stt/` — Speech-to-text utilities
- `tests/` — Unit and integration tests

## Next Steps
- Integrate voice transcription
- Add language detection and intent extraction
- Build and populate the welfare schemes database
- Implement text and audio responses

---

*Made with ❤️ for digital inclusion in India.* 