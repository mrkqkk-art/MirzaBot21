import aiohttp

from config import PASARGAD_URL, PASARGAD_TOKEN


async def pasargad_request(
    method,
    endpoint,
    data=None
):

    url = f"{PASARGAD_URL}/{endpoint}"

    headers = {
        "Authorization": f"Bearer {PASARGAD_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        async with aiohttp.ClientSession() as session:

            if method == "GET":

                async with session.get(
                    url,
                    headers=headers
                ) as response:

                    return await response.json()


            if method == "POST":

                async with session.post(
                    url,
                    headers=headers,
                    json=data
                ) as response:

                    return await response.json()

    except Exception as e:

        return {
            "error": str(e)
        }



async def get_panel_info():

    return await pasargad_request(
        "GET",
        "info"
    )



async def create_account(data):

    return await pasargad_request(
        "POST",
        "users",
        data
    )
