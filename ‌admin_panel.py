from buttons import admin_menu
from database import users_count


async def show_admin_panel(update, context):

    count = users_count()

    await update.message.reply_text(
        f"👑 پنل مدیریت\n\n"
        f"👥 تعداد کاربران: {count}\n\n"
        f"یکی از گزینه‌ها را انتخاب کنید:",
        reply_markup=admin_menu()
    )


async def admin_stats(update, context):

    query = update.callback_query

    count = users_count()

    await query.message.reply_text(
        f"📊 آمار ربات\n\n"
        f"👥 کاربران: {count}"
    )
