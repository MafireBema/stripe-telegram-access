import stripe
import os
import sqlite3

# Stripe-Webhook-Signatur
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

# Telegram
import requests
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_GROUP_ID = os.getenv("TELEGRAM_GROUP_ID")

def add_user(email):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (email) VALUES (?)", (email,))
    conn.commit()
    conn.close()

def stripe_webhook(request):
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature", "")
    
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except Exception as e:
        return f"⚠️ Fehler beim Verifizieren: {e}", 400

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        customer_email = session["customer_details"]["email"]
        add_user(customer_email)

        # Telegram-Benachrichtigung
        message = f"✅ Neuer Zugriff für: {customer_email}"
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            data={"chat_id": TELEGRAM_GROUP_ID, "text": message}
        )
        return "Success", 200

    return "Unhandled Event", 200
