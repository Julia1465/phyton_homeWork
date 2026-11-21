import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"
FIRST_NAME = "Юлия"
LAST_NAME = "Вихарева"
POSTAL_CODE = "457351"
EXPECTED_TOTAL = "Total: $58.29"
WAIT_TIMEOUT = 10

CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
CHECKOUT_BUTTON = (By.ID, "checkout")
FIRST_NAME_INPUT = (By.ID, "first-name")
LAST_NAME_INPUT = (By.ID, "last-name")
POSTAL_CODE_INPUT = (By.ID, "postal-code")
CONTINUE_BUTTON = (By.ID, "continue")
TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

ITEMS_TO_ADD = (
    "sauce-labs-backpack",
    "sauce-labs-bolt-t-shirt",
    "sauce-labs-onesie",
)


@pytest.fixture
def driver():
    drv = webdriver.Firefox()
    drv.maximize_window()
    yield drv
    drv.quit()


def test_shop(driver):
    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    driver.get(BASE_URL)

    user_name_input = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    user_name_input.send_keys(LOGIN)

    password_input = wait.until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.send_keys(PASSWORD)

    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    for item_slug in ITEMS_TO_ADD:
        add_button = wait.until(
            EC.element_to_be_clickable((By.ID, f"add-to-cart-{item_slug}"))
        )
        add_button.click()

    cart_link = wait.until(EC.element_to_be_clickable(CART_LINK))
    cart_link.click()

    checkout_button = wait.until(
        EC.element_to_be_clickable(CHECKOUT_BUTTON)
    )
    checkout_button.click()

    first_name_input = wait.until(
        EC.visibility_of_element_located(FIRST_NAME_INPUT)
    )
    first_name_input.send_keys(FIRST_NAME)

    last_name_input = wait.until(
        EC.visibility_of_element_located(LAST_NAME_INPUT)
    )
    last_name_input.send_keys(LAST_NAME)

    postal_code_input = wait.until(
        EC.visibility_of_element_located(POSTAL_CODE_INPUT)
    )
    postal_code_input.send_keys(POSTAL_CODE)

    continue_button = wait.until(
        EC.element_to_be_clickable(CONTINUE_BUTTON)
    )
    continue_button.click()

    total_element = wait.until(
        EC.visibility_of_element_located(TOTAL_LABEL)
    )
    total_text = total_element.text.strip()
    print(f"Итоговая стоимость со страницы: {total_text!r}")

    assert total_text == EXPECTED_TOTAL, (
        f"Ожидалось '{EXPECTED_TOTAL}', но получено: {total_text}"
    )
