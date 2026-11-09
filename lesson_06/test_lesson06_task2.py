from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://gitflic.ru/"

USER_1_URL = "https://gitflic.ru/user/juli1234"
USER_2_URL = "https://gitflic.ru/user/juli5678"

COOKIE_USER_1 = {
    "name": "SESSION",
    "value": "ZDk5MDBkY2YtZDg4OS00ODlmLTg4OGYtNjEzOTI2OTI1Y2Nh",
    "domain": ".gitflic.ru",
    }

COOKIE_USER_2 = {
    "name": "SESSION",
    "value": "OWI1ZTY0OGItYzg4ZS00ODZjLWFjNjctNWM0MDZlNmI2YmZj",
    "domain": ".gitflic.ru",
    }


def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get(BASE_URL)
    driver.add_cookie(COOKIE_USER_1)
    driver.refresh()
    driver.get(USER_1_URL)

    wait = WebDriverWait(driver, 20)
    wait.until(EC.title_contains("juli1234"))
    url_user_1 = driver.current_url

    driver.delete_all_cookies()
    driver.execute_script(
        "window.localStorage.clear(); window.sessionStorage.clear();"
    )

    driver.add_cookie(COOKIE_USER_2)
    driver.refresh()
    driver.get(USER_2_URL)

    wait.until(EC.title_contains("juli5678"))
    url_user_2 = driver.current_url

    assert url_user_1 != url_user_2, (
        f"URL не различаются: {url_user_1} == {url_user_2}"
    )

    driver.quit()
