import logging
import os

from telegram.ext import (
    ApplicationBuilder,
    Defaults,
)

from handlers.commands import start_handler, chat_handler
from handlers.media import img_handler
from handlers.query import tpl_sel_handler
from t2i.utils import query_tpl

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

token = os.environ.get("BOT_TOKEN", "")
PAYMENT_PROVIDER_TOKEN = os.environ.get("PAY_TOKEN", "")


if __name__ == "__main__":
    query_tpl()
    application = (
        ApplicationBuilder().token(token).defaults(Defaults(block=False)).build()
    )

    application.add_handler(start_handler)
    application.add_handler(chat_handler)
    application.add_handler(img_handler)
    application.add_handler(tpl_sel_handler)

    application.run_polling()
