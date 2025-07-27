import telegram
import sqlite3

# Deinen Bot-Token hier einfügen (von @BotFather bekommen)
BOT_TOKEN = 7814998262:AAHXM-3U5CdGe19HNPfNNdAG8SIMJEFoWLk
CHANNEL_LINK = https://t.me/+uuDDefbXyzRiMmYy

bot = telegram.Bot(token=BOT_TOKEN)

def send_access_email(email):
    try:
        # Sende dem Nutzer eine Nachricht oder mach etwas mit Telegram
        bot.send_message(chat_id=email, text=f"Willkommen! Dein Zugang: {CHANNEL_LINK}")
        print(f"Zugang an {email} gesendet.")
    except Exception as e:
        print(f"Fehler beim Senden: {e}")
