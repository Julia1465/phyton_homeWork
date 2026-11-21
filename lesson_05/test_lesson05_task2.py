import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    try:
        driver.get("https://httpbin.qa-territory.online/forms/post")
        time.sleep(2)
        start_url = driver.current_url

        custname_field = wait.until(
            EC.element_to_be_clickable((By.NAME, "custname"))
        )
        custname_field.click()
        time.sleep(0.5)
        custname_field.clear()

        name_to_enter = "Юлия"
        time.sleep(2)
        custname_field.send_keys(name_to_enter)

        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Submit')]")
            )
        )
        time.sleep(2)
        submit_button.click()

        time.sleep(2)
        new_url = driver.current_url

        assert new_url != start_url, "URL не изменился после отправки формы!"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_form_submission()
