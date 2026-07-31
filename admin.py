from database import users_count


async def admin_panel(update, context):

    count = users_count()

    await update.message.reply_text(
        f"👑 پنل مدیریت\n\n"
        f"👥 کاربران: {count}"
    )
