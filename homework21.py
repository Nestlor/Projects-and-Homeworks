# 1)

# import os
# import requests

# os.chdir('d:/DEV/PYTHON/lesson21/')

# def download_with_requests():
#     folder = "requests_images"
    
#     for i in range(10):
#         try:
#             url = f"https://picsum.photos/200/300?random={i}"
#             response = requests.get(url, stream=True)
            
#             if response.status_code == 200:
#                 with open(f"{folder}/image_{i}.jpg", "wb") as file:
#                     for chunk in response.iter_content(1024):
#                         file.write(chunk)
#                 print(f"[Requests] Изображение {i} загружено")
#             else:
#                 print(f"[Requests] Ошибка {response.status_code}")
#         except Exception as e:
#             print(f"[Requests] Ошибка: {e}")

# download_with_requests()

# 2)

# import os
# import aiohttp

# os.chdir('d:/DEV/PYTHON/lesson21/')

# async def download_with_aiohttp():
#     folder = "aiohttp_images"
    
#     async with aiohttp.ClientSession() as session:
#         for i in range(10):
#             try:
#                 url = f"https://picsum.photos/200/300?random={i}"
#                 async with session.get(url) as response:
#                     if response.status == 200:
#                         data = await response.read()
#                         with open(f"{folder}/image_{i}.jpg", "wb") as file:
#                             file.write(data)
#                         print(f"[Aiohttp] Изображение {i} загружено")
#                     else:
#                         print(f"[Aiohttp] Ошибка {response.status}")
#             except Exception as e:
#                 print(f"[Aiohttp] Ошибка: {e}")

# import asyncio
# asyncio.run(download_with_aiohttp())
