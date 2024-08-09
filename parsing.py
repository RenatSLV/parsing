import requests
import os

API_KEY = '45304021-20a89eb93c88fdab9b6179976'
url = f"https://pixabay.com/api/?key={API_KEY}&q=nature&image_type=photo&per_page=10"

# Директория для сохранения изображений
general_dir = "images"
os.makedirs(general_dir, exist_ok=True)

response = requests.get(url)
data = response.json()

for i, hit in enumerate(data['hits']):
    image_url = hit['largeImageURL']
    image_response = requests.get(image_url)
    if image_response.status_code == 200:

        image_dir = os.path.join(general_dir, f"image_{i}")
        os.makedirs(image_dir, exist_ok=True)

        with open(os.path.join(image_dir, f"image_{i}.jpg"), "wb") as file:
            file.write(image_response.content)

        print(f"Скачано image_{i}.jpg")
    else:
        print(f"Не удалось скачать изображение {i}, статус код: {image_response.status_code}")