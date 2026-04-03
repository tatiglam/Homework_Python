import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@allure.title("Проверка калькулятора: 7 + 8 = 15 с задержкой 45 сек")
@allure.description(
    "Тест проверяет работу калькулятора с установленной задержкой"
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator():
    with allure.step("Настройка драйвера"):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    try:
        page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            page.open()

        with allure.step("Установить задержку 45 секунд"):
            page.set_delay("45")

        with allure.step("Ввести выражение 7 + 8"):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")

        with allure.step("Нажать ="):
            page.click_button("=")

        with allure.step("Ожидать результат 15"):
            page.wait_for_result("15", 60)

        with allure.step("Проверить результат"):
            result = page.get_result()
            assert result == "15"
            print("✅ Тест пройден!")

    finally:
        with allure.step("Закрыть браузер"):
            driver.quit()


if __name__ == "__main__":
    test_calculator()
