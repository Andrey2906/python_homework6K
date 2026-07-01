from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 45)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator."
            "html")

        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        btn_7 = driver.find_element(By.XPATH, "//button[text()='7']")
        btn_plus = driver.find_element(By.XPATH, "//button[text()='+']")
        btn_8 = driver.find_element(By.XPATH, "//button[text()='8']")
        btn_equals = driver.find_element(By.XPATH, "//button[text()='=']")

        btn_7.click()
        btn_plus.click()
        btn_8.click()
        btn_equals.click()

        result_element = wait.until(
            EC.visibility_of_element_located((By.ID, "result")))

        assert result_element.text
        "" == "15", "Ожидался результат '15', но получено:"
        "{result_element.text}"

    finally:
        driver.quit()
