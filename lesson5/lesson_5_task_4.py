from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


options = webdriver.FirefoxOptions()
options.add_argument("--start-maximized")


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window

driver.get("http://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.CSS_SELECTOR, "#username")
username_field.send_keys("tomsmith")

password_field = driver.find_element(By.CSS_SELECTOR, "#password")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(
    By.CSS_SELECTOR, "button.radius")
login_button.click()

message = driver.find_element(By.CSS_SELECTOR, "#flash")
print("Сообщение после входа:", message.text.rstrip(' ×'))

driver.quit()
