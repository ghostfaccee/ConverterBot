from config import API_TOKEN
import aiohttp

async def get_exchage_rate() -> dict:
    url = f'https://v6.exchangerate-api.com/v6/{API_TOKEN}/latest/USD'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {'Error': 'API недоступен'}
    except Exception:
        return {'Error': 'Ошибка соединения'}
