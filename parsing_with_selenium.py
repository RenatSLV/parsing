from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Установите драйвер Chrome
driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

try:

    url = 'https://investfunds.ru/indexes/129/'
    driver.get(url)
    
    time.sleep(5)
    
    value_elements = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[8]/div[2]/div[1]/div[1]')

    print("USD/KZT")

    for i in value_elements:
        print(i.text)
finally:

    driver.quit()