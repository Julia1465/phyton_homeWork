import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

FORM_DATA = {
    "first-name": "Иван",
    "last-name": "Петров",
    "address": "Ленина, 55-3",
    "e-mail": "test@skypro.com",
    "phone": "+7985899998787",
    "zip-code": "",
    "city": "Москва",
    "country": "Россия",
    "job-position": "QA",
    "company": "SkyPro",
}

GREEN_FIELD_IDS = [
    "first-name",
    "last-name",
    "address",
    "e-mail",
    "phone",
    "city",
    "country",
    "job-position",
    "company",
]


@pytest.fixture
def driver():
    drv = webdriver.Edge()
    drv.maximize_window()
    yield drv
    drv.quit()


def test_edge(driver):
    wait = WebDriverWait(driver, 15)

    driver.get(URL)
    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    for name, value in FORM_DATA.items():
        field = wait.until(EC.presence_of_element_located((By.NAME, name)))
        field.send_keys(value)

    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )
    submit_button.click()

    zip_code_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code_field.get_attribute("class"), (
        "Поле Zip code должно быть подсвечено красным"
    )

    for field_id in GREEN_FIELD_IDS:
        field = driver.find_element(By.ID, field_id)
        field_classes = field.get_attribute("class")
        assert "alert-success" in field_classes, (
            f"Поле {field_id} должно быть подсвечено зелёным, "
            f"классы: {field_classes}"
        )
