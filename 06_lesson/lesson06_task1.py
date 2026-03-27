from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    # Ожидание, когда кнопка станет кликабельной, и клик
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )
    button.click()

    # Ожидание появления элемента и проверка, что текст не пустой
    success_label = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content p"))
    )

    # Ожидание, когда текст станет не пустым
    WebDriverWait(driver, 10).until(
        lambda d: success_label.text.strip() != ""
    )

    # Получение и вывод текста
    text = success_label.text
    print(text)

finally:
    driver.quit()
