from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


FORM_DATA = {
    "first-name": "Иван",
    "last-name": "Петров",
    "address": "Ленина, 55-3",
    "e-mail": "test@skypro.com",
    "phone": "+7985899998787",
    "zip-code": "",
    "city": "Москва",
    "country": "Россия",
    "job-position": "QA",
    "company": "SkyPro"
}

FIELD_SELECTORS = {
    "first-name": "input[name='first-name']",
    "last-name": "input[name='last-name']",
    "address": "input[name='address']",
    "e-mail": "input[name='e-mail']",
    "phone": "input[name='phone']",
    "zip-code": "input[name='zip-code']",
    "city": "input[name='city']",
    "country": "input[name='country']",
    "job-position": "input[name='job-position']",
    "company": "input[name='company']"
}


def test_form_validation():
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[name='first-name']")
            )
        )

        for field_name, value in FORM_DATA.items():
            selector = FIELD_SELECTORS[field_name]
            field = driver.find_element(By.CSS_SELECTOR, selector)
            field.clear()
            if value:
                field.send_keys(value)

        submit_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        submit_button.click()

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        page_text = driver.find_element(By.TAG_NAME, "body").text

        assert "Zip code\nN/A" in page_text or "Zip code: N/A" in page_text

        checks = {
            "First name": "Иван",
            "Last name": "Петров",
            "Address": "Ленина, 55-3",
            "City": "Москва",
            "Country": "Россия",
            "E-mail": "test@skypro.com",
            "Phone number": "+7985899998787",
            "Job position": "QA",
            "Company": "SkyPro"
        }

        for field_name, expected_value in checks.items():
            assert (
                f"{field_name}\n{expected_value}" in page_text
                or f"{field_name}: {expected_value}" in page_text
            )

    finally:
        driver.quit()


if __name__ == "__main__":
    test_form_validation()
