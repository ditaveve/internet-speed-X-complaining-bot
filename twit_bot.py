from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

class TwitBot:

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

    def start_post(self):
        post_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button'][class='y-btn-primary x-post-cta']")))
        post_button.click()

    def write_complaint(self, down_speed, up_speed):
        msg = f"Hey Internet Provider, why is my internet speed {down_speed}down/{up_speed}up when I pay for {os.getenv("PROMISED_DOWN")}down/{os.getenv("PROMISED_UP")}up?"
        text_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#modal-compose")))
        text_input.click()
        text_input.send_keys(msg)

    def upload_post(self):
        post_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='post-button']")))
        post_button.click()

    def decide_complain(self, down_speed, up_speed):
        if (float(down_speed) < float(os.getenv("PROMISED_DOWN"))) or (float(up_speed) < float(os.getenv("PROMISED_UP"))):
            self.login()
            self.start_post()
            self.write_complaint(down_speed, up_speed)
            self.upload_post()
        else:
            print("Internet Speed in parameters.")