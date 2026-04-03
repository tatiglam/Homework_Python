from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


def test_calculator():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        page = CalculatorPage(driver)
        page.open()
        page.set_delay("45")
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")
        page.wait_for_result("15", 60)
        result = page.get_result()
        assert result == "15"
        print("✅ Тест пройден!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator()
