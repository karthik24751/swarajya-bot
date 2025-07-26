import os
import tempfile
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from nlp.lang_intent import detect_language, extract_keywords, extract_entities_and_intent, clarification_question
from db.query import find_scheme
from tts.tts import text_to_speech
import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN') or '8378297028:AAG_BLlEEIZ1SG_5ZG7pDNS6Grc5OLMnI64'

try:
    import whisper
    whisper_model = whisper.load_model('base')
except ImportError:
    whisper = None
    whisper_model = None

LANG_MAP = {
    'hi': 'hi',   # Hindi
    'te': 'te',   # Telugu
    'bn': 'bn',   # Bengali
    'mr': 'mr',   # Marathi
    'ta': 'ta',   # Tamil
    'gu': 'gu',   # Gujarati
    'kn': 'kn',   # Kannada
    'ml': 'ml',   # Malayalam
    'or': 'or',   # Odia
    'pa': 'pa',   # Punjabi
    'as': 'as',   # Assamese
    'ur': 'ur',   # Urdu
}

def get_lang_code(lang):
    return LANG_MAP.get(lang, 'hi')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Namaste! I am Swarajya, your welfare scheme assistant. Send me a text or voice message to get started.')

async def process_message(text, update):
    lang = detect_language(text)
    print(f"[DEBUG] Detected language: {lang}")
    keywords = extract_keywords(text)
    print(f"[DEBUG] Keywords after extraction: {keywords}")
    if not keywords:
        # Try spaCy-based intent extraction for English
        intent, entities = extract_entities_and_intent(text, lang=lang)
        print(f"[DEBUG] spaCy intent: {intent}, entities: {entities}")
        if intent:
            keywords = [intent]
        else:
            await update.message.reply_text(clarification_question(text, lang=lang))
            return
    scheme = find_scheme(keywords, lang)
    print(f"[DEBUG] Scheme found: {scheme}")
    if scheme:
        response = f"\U0001F4C4 {scheme['name']}\nEligibility: {scheme['eligibility']}\nDocuments: {scheme['documents']}\nSteps: {scheme['steps']}\nContact: {scheme['contact']}"
        if scheme.get('apply_links'):
            links = scheme['apply_links'].split(';')
            response += "\n\n\U0001F517 Official Apply Link(s):\n"
            for link in links:
                response += f"{link.strip()}\n"
        if scheme.get('video_url'):
            video_url = scheme['video_url']
            if 'youtube.com' in video_url or 'youtu.be' in video_url:
                import re
                yt_id = None
                match = re.search(r'(?:v=|be/)([\w-]{11})', video_url)
                if match:
                    yt_id = match.group(1)
                if yt_id:
                    thumb_url = f'https://img.youtube.com/vi/{yt_id}/hqdefault.jpg'
                    keyboard = InlineKeyboardMarkup([
                        [InlineKeyboardButton("\ud83d\udcfa Watch how to apply", url=video_url)]
                    ])
                    try:
                        # Download thumbnail and send as file
                        with requests.get(thumb_url, stream=True, timeout=10) as r:
                            r.raise_for_status()
                            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_img:
                                for chunk in r.iter_content(chunk_size=8192):
                                    tmp_img.write(chunk)
                                tmp_img_path = tmp_img.name
                        with open(tmp_img_path, 'rb') as img_file:
                            await update.message.reply_photo(img_file, caption=response, reply_markup=keyboard)
                        os.remove(tmp_img_path)
                        # Also send audio
                        try:
                            lang_code = get_lang_code(lang)
                            audio_path = text_to_speech(response, lang_code=lang_code)
                            with open(audio_path, 'rb') as audio_file:
                                await update.message.reply_voice(audio_file)
                            os.remove(audio_path)
                        except Exception as e:
                            await update.message.reply_text(f"(Audio unavailable: {e})")
                        return
                    except Exception as e:
                        import traceback
                        print(f"[DEBUG] Failed to download/send thumbnail: {e}")
                        traceback.print_exc()
            # fallback: just send link if thumbnail fails or not YouTube
            response += f"\n\n\U0001F4FA [Watch how to apply]({video_url})"
        await update.message.reply_text(response, disable_web_page_preview=False, parse_mode='Markdown')
        # Send audio reply (if not already sent with photo)
        if not scheme.get('video_url') or not yt_id: # Only send audio if no video or video failed
            try:
                lang_code = get_lang_code(lang)
                audio_path = text_to_speech(response, lang_code=lang_code)
                with open(audio_path, 'rb') as audio_file:
                    await update.message.reply_voice(audio_file)
                os.remove(audio_path)
            except Exception as e:
                await update.message.reply_text(f"(Audio unavailable: {e})")
    else:
        await update.message.reply_text(clarification_question(text, lang=lang))

async def echo_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_message(update.message.text, update)

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not whisper_model:
        await update.message.reply_text('Voice transcription is not available (Whisper not installed).')
        return
    voice = update.message.voice
    file = await context.bot.get_file(voice.file_id)
    with tempfile.NamedTemporaryFile(suffix='.ogg') as temp_audio:
        await file.download_to_drive(temp_audio.name)
        # Try to detect language from user profile or fallback to 'en'
        user_lang = update.effective_user.language_code if update.effective_user and update.effective_user.language_code else 'en'
        whisper_lang = user_lang if user_lang in LANG_MAP else 'en'
        try:
            result = whisper_model.transcribe(temp_audio.name, language=whisper_lang)
            transcription = result['text']
        except Exception as e:
            transcription = f"Error during transcription: {e}"
    await update.message.reply_text(f'Transcription: {transcription}')
    await process_message(transcription, update)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "\U0001F916 Swarajya Bot Help\n"
        "\n"
        "Send me a text or voice message about any government welfare scheme.\n"
        "I support all major Indian languages (Hindi, Telugu, Bengali, Marathi, Tamil, Gujarati, Kannada, Malayalam, Odia, Punjabi, Assamese, Urdu).\n"
        "\n"
        "Examples:\n"
        "- 'मुझे राशन कार्ड के लिए अप्लाई करना है'\n"
        "- 'నేను పెన్షన్ కోసం అప్లై చేయాలి'\n"
        "- 'I want to apply for aadhar card'\n"
        "\n"
        "I will reply with eligibility, documents, steps, and contact info—plus an audio summary!\n"
        "\n"
        "Commands:\n"
        "/start — Welcome message\n"
        "/help — Show this help\n"
        "/about — About this bot\n"
    )
    await update.message.reply_text(help_text)

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = (
        "\U0001F4E2 Swarajya: Indian Welfare Scheme Assistant\n"
        "\n"
        "Created to help all citizens—especially the elderly and underserved—access government scheme info in their language.\n"
        "\n"
        "Built with ❤️ using Python, Telegram, Whisper, gTTS, spaCy, and open data.\n"
        "\n"
        "Source: (private)\n"
        "Contact: @SwarajyaSupport\n"
    )
    await update.message.reply_text(about_text)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('about', about_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_text))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.run_polling()

if __name__ == '__main__':
    main() 