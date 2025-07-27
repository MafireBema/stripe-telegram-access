import os
import sqlite3
import stripe
from flask import Flask, request
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")
webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
channel_id = os.getenv("CHANNEL_ID")

app = Flask(__name__)

def get_all_users():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT user_id FROM users")
    users = c.fetchall()
    conn.close()
    return [uid[0] for uid in users]

@app.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get("stripe-signature")
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except Exception as e:
        return f"⚠️ Error: {str(e)}", 400

    if event["type"] == "checkout.session.completed":
        for uid in get_all_users():
            try:
                bot.invite_chat_member(chat_id=channel_id, user_id=uid)
            except Exception as e:
                print(f"❌ Fehler beim Einladen von {uid}: {e}")
    return "✅ OK", 200

if __name__ == "__main__":
    app.run(port=4242)
