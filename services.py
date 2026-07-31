from database import add_service, get_user_services


def create_service(
    user_id,
    name,
    config,
    volume,
    days
):
    add_service(
        user_id,
        name,
        config,
        volume,
        days
    )


def user_services(user_id):

    return get_user_services(
        user_id
    )


def format_services(services):

    if not services:
        return "📦 هیچ سرویسی وجود ندارد."

    text = "📦 سرویس‌ها:\n\n"

    for service in services:

        text += (
            f"🔹 نام: {service[2]}\n"
            f"🌐 کانفیگ: {service[3]}\n"
            f"📊 حجم: {service[4]}\n"
            f"⏳ مدت: {service[5]} روز\n"
            f"📌 وضعیت: {service[6]}\n\n"
        )

    return text
