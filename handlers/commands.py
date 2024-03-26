from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="我是一个头像生成机器人，请先上传您带头像的照片",
    )


start_handler = CommandHandler("start", start)
