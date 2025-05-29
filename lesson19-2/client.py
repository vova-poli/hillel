import requests
import os

BASE_URL = 'http://127.0.0.1:8080'
IMAGE_PATH = 'test.jpg'
FILENAME = os.path.basename(IMAGE_PATH)

# 1. POST /upload
with open(IMAGE_PATH, 'rb') as image_file:
    files = {'image': image_file}
    resp = requests.post(f'{BASE_URL}/upload', files=files)

if resp.status_code == 201:
    uploaded_url = resp.json()['image_url']
    print(f"[UPLOAD] Успішно: {uploaded_url}")
else:
    print(f"[UPLOAD] Помилка: {resp.text}")
    exit(1)

# 2. GET /image/<filename> з заголовком Content-Type: text
headers = {'Content-Type': 'text'}
resp = requests.get(f'{BASE_URL}/image/{FILENAME}', headers=headers)

if resp.status_code == 200:
    print(f"[GET] URL зображення: {resp.json()['image_url']}")
else:
    print(f"[GET] Помилка: {resp.text}")
    exit(1)

# 3. DELETE /delete/<filename>
resp = requests.delete(f'{BASE_URL}/delete/{FILENAME}')

if resp.status_code == 200:
    print(f"[DELETE] Успішно: {resp.json()['message']}")
else:
    print(f"[DELETE] Помилка: {resp.text}")
