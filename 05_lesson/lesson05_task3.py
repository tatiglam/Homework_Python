from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Запуск браузера Firefox
driver = webdriver.Firefox()

try:

    driver.get("http://the-internet.herokuapp.com/inputs")

    css_selector = "input[type='number']"
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )

    # Ввести текст "12345"
    input_field.send_keys("12345")
    print("Введено: 12345")

    time.sleep(1)

    # Очистить поле
    input_field.clear()
    print("Поле очищено")

    time.sleep(1)

    # Ввести текст "54321"
    input_field.send_keys("54321")
    print("Введено: 54321")

    time.sleep(1)

    print("Успешно: все действия с полем ввода выполнены")

finally:
    # Закрытие браузера
    driver.quit()
