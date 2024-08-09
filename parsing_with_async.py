import aiohttp
import asyncio
import os

API_KEY = '45304021-20a89eb93c88fdab9b6179976'
url = f"https://pixabay.com/api/?key={API_KEY}&q=nature&image_type=photo&per_page=10"

# Основная директория для сохранения изображений
general_dir = "images_with_aiohttp"
os.makedirs(general_dir, exist_ok=True)

async def download_image(session, image_url, i):
    async with session.get(image_url) as response:
        if response.status == 200:
            content = await response.read()
            # Создание отдельной папки для каждого изображения
            image_dir = os.path.join(general_dir, f"image_{i}")
            os.makedirs(image_dir, exist_ok=True)

            with open(os.path.join(image_dir, f"image_{i}.jpg"), "wb") as file:
                file.write(content)
            print(f"Скачано и сохранено image_{i}.jpg в {image_dir}")
        else:
            print(f"Не удалось скачать изображение {i}, статус код: {response.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            tasks = []
            for i, hit in enumerate(data['hits']):
                image_url = hit['largeImageURL']
                tasks.append(download_image(session, image_url, i))
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
