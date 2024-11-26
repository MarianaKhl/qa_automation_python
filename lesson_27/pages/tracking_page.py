from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_27.pages.base_page import BasePage

class TrackingPage(BasePage):
    input_locator = (By.ID, "en")
    button_locator = (By.ID, "np-number-input-desktop-btn-search-en")
    error_locator = (By.CSS_SELECTOR, "div.tracking__error-text")
    ok_button_locator = (By.CSS_SELECTOR, "span.v-btn__content")

    def enter_tracking_number(self, tracking_number):
        self.enter_text(self.input_locator, tracking_number)

    def click_search_button(self):
        self.click_element(self.button_locator)

    def get_error_message(self):
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.error_locator)
            )
            return error_element.text
        except TimeoutException as e:
            print(f"Error message not found within timeout: {e}")
            return None

    def click_ok_button(self):
        try:
            self.click_element(self.ok_button_locator)
            return True
        except TimeoutException:
            return False
