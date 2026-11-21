import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = (
    "https://bonigarcia.dev/selenium-webdriver-java/"
    "slow-calculator.html"
)
DELAY = "45"
EXPECTED_RESULT = "15"
WAIT_TIMEOUT = 60

SCREEN = (By.CLASS_NAME, "screen")
DELAY_INPUT = (By.ID, "delay")


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    drv.quit()


def test_slow_calculator(driver):
    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    driver.get(BASE_URL)
    wait.until(EC.presence_of_element_located(DELAY_INPUT))

    delay_input = driver.find_element(*DELAY_INPUT)
    delay_input.clear()
    delay_input.send_keys(DELAY)

    for value in ("7", "+", "8", "="):
        xpath_expr = f"//span[normalize-space()='{value}']"
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_expr))
        )
        button.click()

    wait.until(
        EC.text_to_be_present_in_element(SCREEN, EXPECTED_RESULT)
    )

    screen_text = driver.find_element(*SCREEN).text.strip()
    assert screen_text == EXPECTED_RESULT, (
        f"Ожидался результат {EXPECTED_RESULT}, "
        f"получено: {screen_text}"
    )
