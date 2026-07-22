from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
from time import sleep

class InternetSpeedTwitterBot:

    def __init__(self, driver):
        self.driver = driver
        self.down = None
        self.up = None
        load_dotenv()

    def open_browser(self):
        self.driver.get(os.getenv("INTERNET_SPEED_URL"))

    def accept_cookies(self):
        accept_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='onetrust-accept-btn-handler']")))
        accept_button.click()

    def click_start(self):
        start_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='start speed test - connection type multi']")))
        start_button.click()

    def check_for_popup(self):
        ok = False
        while not ok:
            try:
                popup_active =  self.driver.find_element(By.CSS_SELECTOR, "button[class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeSmall !absolute !top-3 !right-3 !size-6 css-9b8ioq']")
                popup_active.click()
                ok = True
            except Exception:
                sleep(0.5)
                pass

    def get_internet_speed(self):
        self.open_browser()
        self.accept_cookies()
        self.click_start()
        self.check_for_popup()
        collected_data = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3[class='py-2 font-mono text-5xl MuiBox-root css-s31qlv']")))
        self.down = collected_data[0].text
        self.up = collected_data[1].text
        print(f"Download speed: {self.down}")
        print(f"Upload speed: {self.up}")
        self.driver.quit()


    def tweet_at_provider(self):
        pass