import asyncio

import requests
from telegram import Update
from telegram.ext import (
    ContextTypes,
    MessageHandler,
    filters,
)

from t2i.utils import upload_image, queue_prompt


async def get_img(url: str):
    resp = requests.get(url)
    print("get img")
    if resp.status_code == 404:
        await asyncio.sleep(10)
        return await get_img(url)
    else:
        return resp.content


async def handle_img(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    new_file = await update.message.effective_attachment[-1].get_file()
    blob = await new_file.download_as_bytearray()
    await update.message.reply_text("开始上传图片")
    input_name = new_file.file_unique_id + ".jpg"
    upload_image(input_name, blob=blob)
    await update.message.reply_text(text="上传图片完毕，开始生成")
    job = queue_prompt(input_name)
    output_name = job.get("data", {}).get("output_prefix", "")
    await update.message.reply_text("任务提交成功，任务编号：" + output_name)
    img_data = await get_img(
        "http://123.123.110.133:8099/res/" + output_name + "_0001.jpg"
    )
    await update.message.reply_photo(img_data)


img_handler = MessageHandler(filters.PHOTO, handle_img)
