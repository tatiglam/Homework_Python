from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from shop_pages import LoginPage, InventoryPage, CartPage, CheckoutPage


def test_shop():
    firefox_options = Options()
    firefox_options.binary_location = (
        "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    )

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=firefox_options)

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart("sauce-labs-backpack")
        inventory_page.add_to_cart("sauce-labs-bolt-t-shirt")
        inventory_page.add_to_cart("sauce-labs-onesie")
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_info("Татьяна", "Кочеткова", "392000")

        total = checkout_page.get_total()
        assert total == "58.29"
        print("✅ Тест пройден!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shop()
