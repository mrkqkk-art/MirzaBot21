from buttons import main_menu


async def user_panel(update, context):

    await update.message.reply_text(
        "👤 پنل کاربری\n\n"
        "از منوی زیر استفاده کنید:",
        reply_markup=main_menu()
    )
