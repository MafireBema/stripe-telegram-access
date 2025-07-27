from flask import Flask, request
from webhook import stripe_webhook
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Stripe Telegram Access läuft!"

@app.route("/webhook", methods=["POST"])
def webhook():
    return stripe_webhook(request)

if __name__ == "__main__":
    app.run(debug=True)
