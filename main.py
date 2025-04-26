import aiohttp
import asyncio
import os
import json

url = "https://jsonplaceholder.typicode.com/posts"

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Ошибка загрузки: {response.status}")
                return []

async def save_data():
    data = await fetch_data()
    if data:
        folder_name = "json_files_aio"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        for i, item in enumerate(data):
            with open(os.path.join(folder_name, f"post_{i+1}.json"), 'w') as f:
                json.dump(item, f, indent=4)

        print(f"Данные сохранены в папке {folder_name}.")

if __name__ == "__main__":
    asyncio.run(save_data())
