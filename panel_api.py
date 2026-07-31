import aiohttp


async def get_panel_status(url, token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        async with aiohttp.ClientSession() as session:

            async with session.get(
                url,
                headers=headers
            ) as response:

                return await response.json()

    except Exception as e:
        return {
            "error": str(e)
        }
