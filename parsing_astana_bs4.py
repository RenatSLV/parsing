import requests
from bs4 import BeautifulSoup


url = 'https://www.hmn.ru/index.php?index=50&value=35188'

response = requests.get(url)
html_response = response.text

with open("file.html", "w", encoding="utf-8") as file:
    file.write(html_response)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    

    temperature = soup.find("<span>", id='bcde190')
    description = soup.find('<h2><b><a href="index.php?index=28&value=35188" class_="imp"></a>')
    
    if temperature and description:

        temp_text = temperature.get_text()
        desc_text = description.get_text()
        print(f'Погода в Астане: {temp_text}, {desc_text}')
    else:
        print('Не удалось найти информацию о погоде на странице')
else:
    print(f'Не удалось загрузить страницу. Статус код: {response.status_code}')