from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_elements():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://httpbin.qa-territory.online/links/10")

        links = wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
        )

        assert len(links) == 9, (
            f"Ожидалось 9 ссылок, но найдено: {len(links)}"
        )

        for i, link in enumerate(links):
            assert link.is_displayed(), (
                f"Ссылка №{i + 1} не отображается на странице"
            )

        assert "1" in links[0].text, (
            f"Текст первой ссылки не содержит '1': '{links[0].text}'"
        )

    finally:
        driver.quit()


if __name__ == "__main__":
    test_multiple_elements()
