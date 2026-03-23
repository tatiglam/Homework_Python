from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:

    driver.get("http://uitestingplayground.com/dynamicid")

    time.sleep(1)

    xpath = "//button[text()='Button with Dynamic ID']"
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )

    blue_button.click()

    # Небольшая пауза для стабильности
    time.sleep(0.5)

    print("Успешно: клик по кнопке с динамическим ID выполнен")

finally:
    # Закрытие браузера
    driver.quit()
