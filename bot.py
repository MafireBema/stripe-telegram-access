import os
import sqlite3
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

app = ApplicationBuilder().token(BOT_TOKEN).build()

def add_user(user_id):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    add_user(user_id)
    await context.bot.send_message(chat_id=user_id, text="Danke für den Start! Du wirst bald freigeschaltet.")

app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    import asyncio
    asyncio.run(app.run_polling())
