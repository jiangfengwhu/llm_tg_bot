from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from ui.btn import group_join_btn


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I am an avatar-generating bot. Please upload a photo with your face included!!!",
        reply_markup=group_join_btn(),
    )


start_handler = CommandHandler("start", start)
