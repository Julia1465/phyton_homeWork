import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
EXPECTED_TOTAL = "Total: $58.29"


@pytest.fixture
def shop(firefox_driver):
    login = LoginPage(firefox_driver)
    login.open(URL)
    return {
        "login": login,
        "inventory": InventoryPage(firefox_driver),
        "cart": CartPage(firefox_driver),
        "checkout": CheckoutPage(firefox_driver),
    }


def test_full_purchase_flow(shop):
    login = shop["login"]
    inventory = shop["inventory"]
    cart = shop["cart"]
    checkout = shop["checkout"]

    login.login(USERNAME, PASSWORD)

    inventory.add_products([
        inventory.BACKPACK,
        inventory.BOLT_TSHIRT,
        inventory.ONESIE,
    ])

    inventory.open_cart()
    items_count = cart.get_items_count()
    assert items_count == 3, f"В корзине {items_count} товаров, ожидали 3"

    cart.click_checkout()

    checkout.fill_form("Иван", "Иванов", "630000")
    checkout.click_continue()

    total = checkout.get_total()
    assert total == EXPECTED_TOTAL, (
        f"Ожидали '{EXPECTED_TOTAL}', на странице: '{total}'"
    )
