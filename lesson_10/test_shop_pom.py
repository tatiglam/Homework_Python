import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from shop_pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@allure.title("Проверка интернет-магазина: оформление заказа")
@allure.description(
    "Тест добавляет 3 товара в корзину и проверяет итоговую сумму"
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    with allure.step("Настройка драйвера Firefox"):
        firefox_options = Options()
        firefox_options.binary_location = (
            "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        )
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)

    try:
        with allure.step("Открыть страницу логина и выполнить вход"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить 3 товара в корзину"):
            inventory_page = InventoryPage(driver)
            inventory_page.add_to_cart("sauce-labs-backpack")
            inventory_page.add_to_cart("sauce-labs-bolt-t-shirt")
            inventory_page.add_to_cart("sauce-labs-onesie")

        with allure.step("Перейти в корзину и нажать Checkout"):
            inventory_page.go_to_cart()
            cart_page = CartPage(driver)
            cart_page.checkout()

        with allure.step("Заполнить форму оформления заказа"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_info("Татьяна", "Кочеткова", "392000")

        with allure.step("Проверить итоговую сумму"):
            total = checkout_page.get_total()
            assert total == "58.29"
            print("✅ Тест пройден!")

    finally:
        with allure.step("Закрыть браузер"):
            driver.quit()


if __name__ == "__main__":
    test_shop()
