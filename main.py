from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler
)

from config import BOT_TOKEN, ADMIN_IDS
from database import create_db, add_user
from buttons import user_menu
from user_panel import my_services
from admin_panel import show_admin_panel, admin_stats


async def start(update, context):

    user = update.effective_user

    add_user(
        user.id,
        user.username
    )

    await update.message.reply_text(
        "سلام 👋\n"
        "به ربات خوش آمدید",
        reply_markup=user_menu()
    )


async def admin(update, context):

    user_id = update.effective_user.id

    if user_id not in ADMIN_IDS:
        await update.message.reply_text(
            "⛔ دسترسی ندارید"
        )
        return

    await show_admin_panel(
        update,
        context
    )


async def buttons_handler(update, context):

    query = update.callback_query

    await query.answer()

    if query.data == "my_services":
        await my_services(
            update,
            context
        )

    elif query.data == "stats":

        if query.from_user.id in ADMIN_IDS:
            await admin_stats(
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
        CallbackQueryHandler(
            buttons_handler
        )
    )


    app.run_polling()


if __name__ == "__main__":
    main()
