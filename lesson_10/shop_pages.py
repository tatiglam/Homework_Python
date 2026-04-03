from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """Открывает страницу логина.

        Returns:
            None
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """Выполняет вход с указанными данными.

        Args:
            username: Имя пользователя
            password: Пароль

        Returns:
            None
        """
        self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_id: str) -> None:
        """Добавляет товар в корзину.

        Args:
            product_id: ID товара (например, "sauce-labs-backpack")

        Returns:
            None
        """
        button = (By.ID, f"add-to-cart-{product_id}")
        self.wait.until(EC.element_to_be_clickable(button)).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину.

        Returns:
            None
        """
        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self) -> None:
        """Нажимает кнопку Checkout.

        Returns:
            None
        """
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_info(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """Заполняет форму оформления заказа.

        Args:
            first_name: Имя
            last_name: Фамилия
            postal_code: Почтовый индекс

        Returns:
            None
        """
        self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        """Возвращает итоговую сумму заказа.

        Returns:
            str: Итоговая сумма (например, "58.29")
        """
        locator = (By.CLASS_NAME, "summary_total_label")
        total_element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        return total_element.text.split("$")[1]
