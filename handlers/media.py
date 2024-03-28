from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ChatMemberStatus
from telegram.ext import (
    ContextTypes,
    MessageHandler,
    filters,
)

from config.t2i import get_templates
from t2i.utils import upload_image
from ui.btn import group_join_btn


def split_list(lst, sz):
    return [lst[i : i + sz] for i in range(0, len(lst), sz)]


async def handle_img(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user = await ctx.bot.getChatMember(-1002050415896, update.message.from_user.id)
    if user.status in [
        ChatMemberStatus.MEMBER,
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.OWNER,
    ]:
        new_file = await update.message.effective_attachment[-1].get_file()
        blob = await new_file.download_as_bytearray()
        await update.message.reply_text("Uploading...")
        input_name = new_file.file_unique_id + ".jpg"
        upload_image(input_name, blob=blob)
        reply_markup = InlineKeyboardMarkup(
            split_list(
                list(
                    map(
                        lambda x: InlineKeyboardButton(
                            x, callback_data="$".join([x, input_name])
                        ),
                        get_templates(),
                    )
                ),
                3,
            )
        )
        await update.message.reply_text(
            "Upload done, please select template", reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            "Press Button to join the group", reply_markup=group_join_btn()
        )


img_handler = MessageHandler(filters.PHOTO, handle_img)
