from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

COOKIE_USER_1 = {
    "name": "SESSION",
    "value": "ZmI1MGQzNDktY2M5ZS00YTFlLTlhZmEtYjA3OTE1NWNlOWMy"
    }
COOKIE_USER_2 = {
    "name": "SESSION",
    "value": "ZDM1ZTBmYzYtNDA4MC00OGNlLWFjOGYtY2YxZWUxNmVhN2Y1"
    }

USER_1_URL = "https://gitflic.ru/user/juli1234"
USER_2_URL = "https://gitflic.ru/user/juli5678"


def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get("https://gitflic.ru/")
    driver.add_cookie(COOKIE_USER_1)
    driver.refresh()
    driver.get(USER_1_URL)

    wait = WebDriverWait(driver, 10)
    wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "h1"), "juli1234"
            )
        )

    url_user_1 = driver.current_url

    driver.delete_all_cookies()

    driver.add_cookie(COOKIE_USER_2)
    driver.refresh()
    driver.get(USER_2_URL)

    wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "h1"), "juli5678"
            )
        )

    url_user_2 = driver.current_url

    assert url_user_1 != url_user_2, (
        f"URL не различаются: {url_user_1} == {url_user_2}"
    )

    driver.quit()
