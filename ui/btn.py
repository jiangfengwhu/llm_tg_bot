from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def group_join_btn():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Join the group first", url="https://t.me/ai_avatar_ff"
                )
            ]
        ]
    )
