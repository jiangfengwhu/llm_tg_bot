from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from ui.btn import group_join_btn
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I am an avatar-generating bot. Please upload a photo with your face included!!!",
        reply_markup=group_join_btn(),
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = llm.invoke("".join(context.args))
    try:
        await update.message.reply_text(result.content, parse_mode="MarkdownV2")
    except Exception as e:
        await update.message.reply_text(result.content)


start_handler = CommandHandler("start", start)
chat_handler = CommandHandler("chat", chat)
