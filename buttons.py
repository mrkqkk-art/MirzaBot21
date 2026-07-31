from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():

    buttons = [
        [
            InlineKeyboardButton(
                "👤 حساب من",
                callback_data="profile"
            )
        ],
        [
            InlineKeyboardButton(
                "📞 پشتیبانی",
                callback_data="support"
            )
        ]
    ]

    return InlineKeyboardMarkup(buttons)
