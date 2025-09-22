from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_shipping_info(self, first_name, last_name, zip_code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        ).send_keys(first_name)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "last-name"))
        ).send_keys(last_name)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "postal-code"))
        ).send_keys(zip_code)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()
