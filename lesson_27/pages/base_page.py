from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        # finds an element
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        # click on the element
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self, locator):
        # return element's text
        element = self.find_element(locator)
        return element.text
