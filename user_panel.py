from buttons import user_menu
from database import get_user_services


async def show_user_panel(update, context):

    await update.message.reply_text(
        "👤 پنل کاربری\n\n"
        "یکی از گزینه‌ها را انتخاب کنید:",
        reply_markup=user_menu()
    )


async def my_services(update, context):

    query = update.callback_query
    user_id = query.from_user.id

    services = get_user_services(user_id)

    if not services:
        await query.message.reply_text(
            "📦 شما هنوز سرویسی ندارید."
        )
        return

    text = "📦 سرویس‌های شما:\n\n"

    for s in services:
        text += (
            f"🔹 نام: {s[2]}\n"
            f"📊 حجم: {s[4]}\n"
            f"⏳ مدت: {s[5]} روز\n\n"
        )

    await query.message.reply_text(text)
