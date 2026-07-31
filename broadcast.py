from database import get_users


async def send_broadcast(bot, text):

    users = get_users()

    for user in users:

        try:
            await bot.send_message(
                user[0],
                text
            )

        except:
            pass
