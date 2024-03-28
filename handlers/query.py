import asyncio
from urllib.parse import urljoin

import requests
from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

from config.t2i import baseUrl
from t2i.utils import queue_prompt


async def get_img(url: str):
    resp = requests.get(url)
    if resp.status_code == 404:
        await asyncio.sleep(10)
        return await get_img(url)
    else:
        return resp.content


async def handle_tpl_sel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    [tpl, input_name] = query.data.split("$")
    await query.edit_message_text(f"template: {tpl}")
    job = queue_prompt(input_name, tpl)
    output_name = job.get("data", {}).get("output_prefix", "")
    if output_name:
        await context.bot.send_message(
            update.effective_chat.id,
            f"Task submission successful! template：{tpl}, task number is {output_name}",
        )
        img_data = await get_img(urljoin(baseUrl, "res/" + output_name + "_0001.jpg"))
        await context.bot.send_photo(update.effective_chat.id, img_data)
    else:
        await context.bot.send_message(
            update.effective_chat.id, "Task submission failed"
        )


tpl_sel_handler = CallbackQueryHandler(handle_tpl_sel)
