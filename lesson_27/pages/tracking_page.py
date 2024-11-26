from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TrackingPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_tracking_number(self, tracking_number):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "en"))
        )
        input_field.clear()
        input_field.send_keys(tracking_number)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "np-number-input-desktop-btn-search-en"))
        )
        search_button.click()

    def get_error_message(self):
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "track__form-error"))
        )
        return error_message.text
