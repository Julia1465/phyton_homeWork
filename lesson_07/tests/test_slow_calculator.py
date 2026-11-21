import pytest

from pages.calculator_page import CalculatorPage

URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


@pytest.fixture
def calculator_page(driver):
    page = CalculatorPage(driver)
    page.open(URL)
    return page


def test_slow_calculator_addition(calculator_page):
    calculator_page.set_delay("45")
    calculator_page.press_expression("7+8=")
    result = calculator_page.get_result("15")
    assert result == "15", f"Ожидали '15', на экране: '{result}'"
