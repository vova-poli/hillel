import requests

# Початкові дані
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,           # Сол (марсіанський день)
    'camera': 'fhaz',      # Фронтальна камера
    'api_key': 'DEMO_KEY'  # Публічний ключ NASA
}

# JSON з посиланнями на фото
response = requests.get(url, params=params)
data = response.json()

# Перевіримо, чи є фото
photos = data.get('photos', [])
if not photos:
    print("Фото не знайдено за заданими параметрами.")
else:
    print(f"Знайдено {len(photos)} фото. Завантаження...")

    for i, photo in enumerate(photos[:10], start=1):
        img_url = photo['img_src']
        img_data = requests.get(img_url).content

        filename = f'mars_photo{i}.jpg'

        with open(filename, 'wb') as f:
            f.write(img_data)

        print(f"Збережено {filename}")

    print("Завантаження завершено.")
