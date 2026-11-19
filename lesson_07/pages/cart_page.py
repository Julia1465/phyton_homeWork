from selenium.webdriver.common.by import By


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAMES = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def get_items_count(self) -> int:
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_items_names(self) -> list:
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [element.text for element in elements]
