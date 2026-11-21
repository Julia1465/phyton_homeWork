from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://gitflic.ru")

sleep(2)

click_button = driver.find_element(By.CLASS_NAME, "button-start")
click_button.click()
sleep(2)

input_login = driver.find_element(By.ID, "email")
input_login.send_keys("in6vq@airsworld.net")

input_password = driver.find_element(By.ID, "passwordBasic")
input_password.send_keys("12345Qwerty")

submit_button = driver.find_element(By.CLASS_NAME, "btn-success")
submit_button.click()
sleep(5)

driver.quit()
