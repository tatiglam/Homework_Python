from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(url)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ID, "image-container")
        )
    )

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#image-container img:nth-child(3)")
        )
    )

    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

    print(f"Найдено картинок: {len(images)}")

    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print(third_image_src)
    else:
        print("Не удалось получить 3-ю картинку")

finally:
    driver.quit()
