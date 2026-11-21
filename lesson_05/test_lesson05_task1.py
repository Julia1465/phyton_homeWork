import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://httpbin.qa-territory.online")
        time.sleep(3)
        start_url = driver.current_url
        print(f"Стартовый URL: {start_url}")

        link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "HTML Form"))
            )
        time.sleep(3)
        link.click()

        time.sleep(3)
        current_url = driver.current_url
        assert "/forms/post" in current_url, (
            f"Ожидался URL с /forms/post, но получен: {current_url}"
        )
        print("URL успешно изменился на /forms/post")

        driver.back()

        time.sleep(3)
        back_url = driver.current_url
        assert back_url == start_url, (
            f"Не вернулись на исходную страницу. "
            f"Текущий URL: {back_url}, исходный: {start_url}"
        )
        print("Успешно вернулись на главную страницу")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_navigation()
