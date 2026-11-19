from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")
    SUBTOTAL_LABEL = (By.CSS_SELECTOR, ".summary_subtotal_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, value: str):
        self.driver.find_element(*self.FIRST_NAME).send_keys(value)

    def enter_last_name(self, value: str):
        self.driver.find_element(*self.LAST_NAME).send_keys(value)

    def enter_postal_code(self, value: str):
        self.driver.find_element(*self.POSTAL_CODE).send_keys(value)

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_total(self) -> str:
        self.wait.until(
            lambda d: self.driver.find_element(*self.TOTAL_LABEL).text
        )
        return self.driver.find_element(*self.TOTAL_LABEL).text

    def get_subtotal(self) -> str:
        return self.driver.find_element(*self.SUBTOTAL_LABEL).text
