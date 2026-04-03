from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_id):
        button = (By.ID, f"add-to-cart-{product_id}")
        self.wait.until(EC.element_to_be_clickable(button)).click()

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_info(self, first_name, last_name, postal_code):
        self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total_element.text.split("$")[1]
