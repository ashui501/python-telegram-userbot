

# nandha/plugins/main.py

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from nandha import app

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )

start_handler = CommandHandler('start', start)
app.add_handler(start_handler)
