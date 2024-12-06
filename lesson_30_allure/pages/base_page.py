import logging
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Waiting for visibility of element: {locator}")
    def wait_for_element_visibility(self, locator, timeout=10):
        try:
            logging.info(f"Waiting for visibility of element: {locator}")
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="visibility_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(
                f"Element with locator {locator} did not become visible within {timeout} seconds."
            )

    @allure.step("Filling field: {locator} with value: {value}")
    def fill_field(self, locator, value, timeout=10):
        try:
            logging.info(f"Filling field {locator} with value: {value}")
            field = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            field.clear()
            field.send_keys(value)
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="fill_field_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(
                f"Field with locator {locator} was not clickable within {timeout} seconds."
            )

    @allure.step("Waiting for an element: {locator}")
    def wait_for_element(self, by, locator, timeout=10):
        logging.info(f"Waiting for an element: {locator}")
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    @allure.step("Waiting for an element: {locator}")
    def click_element(self, by, locator, timeout=10):
        element = self.wait_for_element(by, locator, timeout)
        logging.info(f"Click on an element: {locator}")
        element.click()

    @allure.step("Waiting for the registration modal to disappear")
    def wait_for_registration_to_complete(self, timeout=10):
        try:
            logging.info("Waiting for the registration modal to disappear.")
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "modal-body"))
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="registration_modal_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(
                "The registration modal did not disappear within the expected time."
            )

    @allure.step("Waiting for element to become invisible: {locator}")
    def wait_for_element_invisibility(self, locator, timeout=10):
        try:
            logging.info(f"Waiting for element to become invisible: {locator}")
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="invisibility_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(
                f"Element with locator {locator} did not become invisible within {timeout} seconds."
            )

    @allure.step("Waiting for error message with locator: {locator}")
    def wait_for_error_message(self, locator, timeout=10):
        try:
            logging.info(f"Waiting for error message with locator: {locator}")
            error_element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return error_element.text.strip()
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="error_message_timeout",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(
                f"Error message with locator {locator} did not appear within {timeout} seconds."
            )

    @allure.step("Getting error message with locator: {locator}")
    def get_error_message(self, locator, timeout=10):
        return self.wait_for_error_message(locator, timeout)

    @allure.step("Trigger blur on the active field")
    def trigger_field_blur(self):
        try:
            logging.info("Triggering blur event on the active field.")
            self.driver.execute_script("document.activeElement.blur();")
        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="trigger_blur_failure",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Failed to trigger blur event: {str(e)}")

