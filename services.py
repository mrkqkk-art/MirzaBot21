services = []


def add_service(
    user_id,
    username,
    volume,
    days
):

    services.append({
        "user": user_id,
        "username": username,
        "volume": volume,
        "days": days
    })


def get_services():

    return services
