from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, seconds: str):
        field = self.driver.find_element(*self.DELAY_INPUT)
        field.clear()
        field.send_keys(seconds)

    def press_button(self, value: str):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']"
        ).click()

    def press_expression(self, expression: str):
        for char in expression:
            self.press_button(char)

    def get_result(self, expected: str) -> str:
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )
        return self.driver.find_element(*self.SCREEN).text
