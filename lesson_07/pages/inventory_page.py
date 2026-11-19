from selenium.webdriver.common.by import By


class InventoryPage:
    ADD_TO_CART_ID = "add-to-cart-{slug}"
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    BACKPACK = "sauce-labs-backpack"
    BOLT_TSHIRT = "sauce-labs-bolt-t-shirt"
    ONESIE = "sauce-labs-onesie"

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, slug: str):
        self.driver.find_element(
            By.ID, self.ADD_TO_CART_ID.format(slug=slug)
        ).click()

    def add_products(self, slugs: list):
        for slug in slugs:
            self.add_to_cart(slug)

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
