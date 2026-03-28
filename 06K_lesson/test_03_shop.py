from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def test_shop():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        driver.get("https://www.saucedemo.com/")

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        items = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie"
        }

        for item_name, button_id in items.items():
            wait.until(EC.element_to_be_clickable((By.ID, button_id))).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys("Татьяна")
        driver.find_element(By.ID, "last-name").send_keys("Кочеткова")
        driver.find_element(By.ID, "postal-code").send_keys("392000")

        driver.find_element(By.ID, "continue").click()

        total_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_text = total_element.text
        total_value = total_text.split("$")[1]

        assert total_value == "58.29"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shop()
