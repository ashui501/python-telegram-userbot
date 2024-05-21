

# nandha/plugins/main.py

from telegram import Update, constants, helpers, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ContextTypes
from nandha import app

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    user_name = update.effective_user.first_name
    mention = helpers.mention_markdown(user_id, user_name)

    keyboard = [
        [
            InlineKeyboardButton("Group 🌟", url="NandhaChat.t.me"),
            InlineKeyboardButton("Channel 💫", url="NandhaBots.t.me"),
        ],
        [
            InlineKeyboardButton("Nandha 💀", url=f"tg://user?id={user_id}")
        ]
    ]

    buttons = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(f"*Hello there {mention}, I'm Simple bot made by @NandhaBots using [Python Telegram Bot](https://docs.python-telegram-bot.org) Library.*"),
        parse_mode=constants.ParseMode.MARKDOWN,
        reply_markup=buttons)

start_handler = CommandHandler('start', start)
app.add_handler(start_handler)
