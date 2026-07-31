from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from database import users_count


async def admin_menu(update, context):

    count = users_count()

    buttons = [
        [
            InlineKeyboardButton(
                "📊 آمار کاربران",
                callback_data="stats"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 ارسال همگانی",
                callback_data="broadcast"
            )
        ]
    ]

    await update.message.reply_text(
        f"👑 پنل مدیریت\n\n"
        f"👥 تعداد کاربران: {count}",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
