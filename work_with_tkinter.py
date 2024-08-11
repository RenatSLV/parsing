"""программа котороя дергает с сайта инфу и записывает ее в папку"""
from tkinter import *
import requests
import os

def parsing():
    """
    функция не чего не принимает она просто ввыполняет скрипт в себе
    """
    #нужные переменые
    folder_path = "file/"
    file_name = "file.txt"
    post_id = 1
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response = requests.get(url) #дёргает инфу
    #проверка на ошибку
    if response.status_code == 200:
        post_data = response.json()

        print("Post data:")
        print(f"Title: {post_data['title']}")
        print(f"Body: {post_data['body']}")

        post_data_str = str(post_data) #преоброзуем чтобы сохронить в файл

        if not os.path.exists(folder_path): #проверяем есть ли папка
            os.makedirs(folder_path)

        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'w', encoding='utf-8') as file: #записывает файл в папку
            file.write(post_data_str)
    else:
        print("Чтото пошло не так ", response.status_code)
    
# программа
window = Tk()
window.title("Добро пожаловать в моё приложение для парсинга!!!!!")
window.geometry('500x500')
lbl = Label(window, text="Что бы спарсить данные нажми на кнопку", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)
btn = Button(window, text="кнопка", command=parsing, font=("Arial Bold", 15))
btn.grid(column=1, row=0)
window.mainloop()