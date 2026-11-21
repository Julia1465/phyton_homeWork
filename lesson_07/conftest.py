import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import (
    Options as FirefoxOptions,
)


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        try:
            driver.quit()
        except Exception:
            pass


@pytest.fixture
def firefox_driver():
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    try:
        yield driver
    finally:
        try:
            driver.quit()
        except Exception:
            pass
