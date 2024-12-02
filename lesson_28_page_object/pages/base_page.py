import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, locator, timeout=10):
        logging.info(f"Waiting for an element: {locator}")
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def click_element(self, by, locator, timeout=10):
        element = self.wait_for_element(by, locator, timeout)
        logging.info(f"Click on an element: {locator}")
        element.click()
