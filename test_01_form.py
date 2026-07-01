from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 20)

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name, value in fields.items():
        field = wait.until(EC.presence_of_element_located((By.NAME, name)))
        field.send_keys(value)

    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".invalid")))

    zip_code_field = driver.find_element(By.ID, "zip-code")
    assert "invalid" in zip_code_field.get_attribute("class"), \
        f"Ожидался класс 'invalid' у zip-code, получили: '{
            zip_code_field.get_attribute('class')}'"

    valid_fields = [
        (By.NAME, "first-name"),
        (By.NAME, "last-name"),
        (By.NAME, "address"),
        (By.NAME, "e-mail"),
        (By.NAME, "phone"),
        (By.NAME, "city"),
        (By.NAME, "country"),
        (By.NAME, "job-position"),
        (By.NAME, "company"),
    ]

    for locator in valid_fields:
        field = driver.find_element(*locator)
        assert "valid" in field.get_attribute("class"), \
            f"Поле {locator[1]}: ожидался класс 'valid', получили '{
                field.get_attribute('class')}'"

    driver.quit()
