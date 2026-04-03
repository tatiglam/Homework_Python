from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """Открывает страницу калькулятора.

        Returns:
            None
        """
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.driver.get(url)

    def set_delay(self, seconds: str) -> None:
        """Устанавливает задержку перед вычислением.

        Args:
            seconds: Задержка в секундах

        Returns:
            None
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, button_text: str) -> None:
        """Нажимает кнопку с указанным текстом.

        Args:
            button_text: Текст на кнопке (цифра или оператор)

        Returns:
            None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{button_text}']")
            )
        )
        button.click()

    def get_result(self) -> str:
        """Возвращает результат вычисления.

        Returns:
            str: Результат на экране калькулятора
        """
        result_element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "screen"))
        )
        return result_element.text

    def wait_for_result(self, expected_result: str, timeout: int = 60) -> None:
        """Ожидает появления ожидаемого результата.

        Args:
            expected_result: Ожидаемый результат
            timeout: Таймаут в секундах (по умолчанию 60)

        Returns:
            None
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected_result
            )
        )
