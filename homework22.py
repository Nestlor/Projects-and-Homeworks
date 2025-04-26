import requests
import os
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Загружено {len(data)} объектов.")
else:
    print(f"Ошибка загрузки: {response.status_code}")

folder_name = "json_files"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for i, item in enumerate(data):
    with open(os.path.join(folder_name, f"post_{i+1}.json"), 'w') as f:
        json.dump(item, f, indent=4)

print(f"Данные сохранены в папке {folder_name}.")
