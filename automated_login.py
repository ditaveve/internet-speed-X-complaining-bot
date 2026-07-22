from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

class AutomatedLogin:

    def __init__(self, driver):
        self.driver=driver
        load_dotenv()

    def open_browser(self):
        self.driver.get(os.getenv("Y_LOGIN_URL"))

    def enter_email(self):
        email_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='email']")))
        email_input.send_keys(os.getenv("EMAIL"))

    def enter_pass(self):
        pass_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='password']")))
        pass_input.send_keys(os.getenv("PASSWORD"))

    def submit_login(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login_button.click()

    def login(self):
        self.open_browser()
        self.enter_email()
        self.enter_pass()
        self.submit_login()