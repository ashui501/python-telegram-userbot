

# nandha/plugins/main.py

from telegram import Update, constants
from telegram.ext import CommandHandler, ContextTypes
from nandha import app

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    user_name = update.effective_user.first_name
    mention = f'[{user_name}](tg://user?id={user_id})'

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(f"**Hello there {mention}, I'm Simple bot made by @NandhaBots using [Python Telegram Bot](https://docs.python-telegram-bot.org) Library\.**"),
        parse_mode=constants.ParseMode.MARKDOWN_V2)

start_handler = CommandHandler('start', start)
app.add_handler(start_handler)
