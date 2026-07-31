from telegram.ext import (
    Application,
    CommandHandler
)

from config import BOT_TOKEN, ADMIN_IDS
from database import create_db, add_user
from buttons import main_menu
from admin import admin_panel


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
            admin_panel
        )
    )


    app.run_polling()


if __name__ == "__main__":
    main()
