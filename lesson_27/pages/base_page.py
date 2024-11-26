from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def click_element(self, locator):
        element = self.wait_for_element(locator, EC.element_to_be_clickable)
        element.click()

    def enter_text(self, locator, text):
        input_field = self.wait_for_element(locator, EC.presence_of_element_located)
        input_field.clear()
        input_field.send_keys(text)
