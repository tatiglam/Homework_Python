from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")

    time.sleep(1)

    xpath = ("//button[contains(concat(' ', normalize-space(@class), ' '), "
             "' btn-primary ')]")

    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )

    blue_button.click()

    WebDriverWait(driver, 3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    time.sleep(0.5)

    print("Успешно: клик по синей кнопке и подтверждение alert выполнены")

finally:
    driver.quit()
