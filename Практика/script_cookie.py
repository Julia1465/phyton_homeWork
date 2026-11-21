from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("https://gitflic.ru/")
sleep(2)


# Получаем все cookies
cookies = driver.get_cookies()

for cookie in cookies:
   print(f"{cookie['name']}: {cookie['value']}")

driver.quit()