from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NovaPoshtaTracker:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open_page(self):
        self.driver.get(self.url)
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "en"))
        )

    def enter_ttn_number(self, ttn: str):
        input_field = self.driver.find_element(By.ID, "en")
        input_field.clear()
        input_field.send_keys(ttn)
        input_field.send_keys(Keys.ENTER)

    def get_status_text(self) -> str:
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
        )
        status_element = self.driver.find_element(By.CSS_SELECTOR, ".header__status-text")
        return status_element.text
