from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    url = "https://kaspi.kz/shop/c/computers/?utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_sports&gclid=Cj0KCQjwtsy1BhD7ARIsAHOi4xb0paM6QMyH9Fwdz2vNRKmOKJoU3DJtOvWwekqLPyL-8fqy_O_jveoaAmWgEALw_wcB"
    driver.get(url)

    time.sleep(5)

    block = driver.find_element(By.CLASS_NAME, "item-cards-grid__cards")
    all_price = block.find_elements(By.CLASS_NAME, "item-card__prices-price")

    for i in all_price:
        print(i.text)
finally:

    driver.quit()
