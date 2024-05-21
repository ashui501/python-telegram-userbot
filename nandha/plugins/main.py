

from nandha import app
from telegram.ext import CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )



start_handler = CommandHandler('start', start)
app.add_handler(start_handler)
