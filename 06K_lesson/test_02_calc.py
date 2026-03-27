from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_calculator():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

        wait = WebDriverWait(driver, 10)

        delay_input = wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        buttons = {
            "7": "//span[text()='7']",
            "+": "//span[text()='+']",
            "8": "//span[text()='8']",
            "=": "//span[text()='=']"
        }

        for button_text, xpath in buttons.items():
            button = driver.find_element(By.XPATH, xpath)
            button.click()

        wait_result = WebDriverWait(driver, 50)
        wait_result.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        result = driver.find_element(By.CLASS_NAME, "screen").text
        assert result == "15"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator()
