from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    # Ожидание появления поля ввода и ввод текста
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.send_keys("SkyPro")

    # Ожидание появления кнопки и клик
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    button.click()

    # Ожидание изменения текста на кнопке и получение текста
    updated_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "updatingButton"))
    )
    # Дополнительное ожидание, чтобы текст обновился
    WebDriverWait(driver, 10).until(
        lambda d: updated_button.text == "SkyPro"
    )

    # Вывод текста кнопки в консоль
    print(updated_button.text)

finally:
    driver.quit()
