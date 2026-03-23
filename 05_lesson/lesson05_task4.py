from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Запуск браузера Firefox
driver = webdriver.Firefox()

try:
    # Переход на страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Ожидание загрузки страницы
    time.sleep(1)

    # Поиск поля username и ввод значения
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("tomsmith")
    print("Введен username: tomsmith")

    # Поиск поля password и ввод значения
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Введен password: SuperSecretPassword!")

    css_selector = "div.flash.success"
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )

    # Ожидание появления зеленой плашки (flash-сообщения об успехе)
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.flash.success"))
    )

    # Вывод текста зеленой плашки в консоль
    message_text = success_message.text
    print("\n=== Текст зеленой плашки ===")
    print(message_text)
    print("============================\n")

    # Небольшая пауза для наглядности
    time.sleep(1)

    print("Успешно: авторизация выполнена")

finally:
    # Закрытие браузера
    driver.quit()
