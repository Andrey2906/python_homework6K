from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_checkout():
    options = Options()
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 30)

    try:
        driver.get("https://www.saucedemo.com/")

        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, ".btn_action")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for product_name in products_to_add:
            product_card = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains("
                     "@class,'inventory_item') and .//div[text()='"
                     "{product_name}']]"))
            )
            add_to_cart_btn = product_card.find_element(
                By.CSS_SELECTOR, ".btn_inventory")
            add_to_cart_btn.click()

        cart_link = driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_container a")
        cart_link.click()

        checkout_btn = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, ".checkout_button")))
        checkout_btn.click()

        first_name_input = wait.until(
            EC.visibility_of_element_located((By.ID, "first-name")))
        last_name_input = driver.find_element(By.ID, "last-name")
        postal_code_input = driver.find_element(By.ID, "postal-code")

        first_name_input.send_keys("Иван")
        last_name_input.send_keys("Петров")
        postal_code_input.send_keys("123456")

        continue_btn = driver.find_element(
            By.CSS_SELECTOR, ".cart_button")
        continue_btn.click()

        total_element = wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text  # например: "Total: $58.29"

        total_value = total_text.replace("Total: ", "").strip()

        assert total_value == "$58.29", ""
        "Ожидалась сумма $58.29, но получено: {total_value}"

    finally:
        driver.quit()
