from telegram.ext import (
    Application,
    CommandHandler
)

from config import BOT_TOKEN, ADMIN_IDS
from database import create_db, add_user
from buttons import main_menu
from admin_panel import admin_menu
from user_panel import user_panel


async def start(update, context):

    user = update.effective_user

    add_user(
        user.id,
        user.username
    )

    await update.message.reply_text(
        "سلام 👋\nبه ربات خوش آمدید",
        reply_markup=main_menu()
    )


async def admin(update, context):

    user_id = update.effective_user.id

    if user_id not in ADMIN_IDS:
        await update.message.reply_text(
            "⛔ دسترسی ندارید"
        )
        return

    await admin_menu(
        update,
        context
    )


async def panel(update, context):

    await user_panel(
        update,
        context
    )


def main():

    create_db()

    app = Application.builder().token(
        BOT_TOKEN
    ).build()


    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        CommandHandler(
            "admin",
            admin
        )
    )

    app.add_handler(
        CommandHandler(
            "panel",
            panel
        )
    )


    app.run_polling()


if __name__ == "__main__":
    main()
