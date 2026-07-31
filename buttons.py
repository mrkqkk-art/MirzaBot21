from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def user_menu():

    buttons = [
        [
            InlineKeyboardButton(
                "🛒 خرید سرویس",
                callback_data="buy"
            )
        ],
        [
            InlineKeyboardButton(
                "📦 سرویس‌های من",
                callback_data="my_services"
            )
        ],
        [
            InlineKeyboardButton(
                "🔄 تمدید سرویس",
                callback_data="renew"
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



def admin_menu():

    buttons = [
        [
            InlineKeyboardButton(
                "📊 آمار کاربران",
                callback_data="stats"
            )
        ],
        [
            InlineKeyboardButton(
                "➕ ساخت سرویس",
                callback_data="create_service"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 ارسال همگانی",
                callback_data="broadcast"
            )
        ],
        [
            InlineKeyboardButton(
                "⚙️ تنظیمات پنل",
                callback_data="settings"
            )
        ]
    ]

    return InlineKeyboardMarkup(buttons)
