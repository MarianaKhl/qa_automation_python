import logging
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28_page_object.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def get_error_message(self, locator):
        try:
            error_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
            return error_element.text.strip()
        except TimeoutException:
            logging.error("No error message found.")
            return "No error message found"

    def close_modal_if_present(self):
        try:
            modal_close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))
            )
            modal_close_button.click()
            logging.info("The modal window has been closed successfully.")
        except TimeoutException:
            logging.info("There is no modal window, let's continue.")

    def click_signup_button_with_js(self):
        try:
            signup_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Sign up']"))
            )
            self.driver.execute_script("arguments[0].click();", signup_button)
            logging.info("The 'Sign up' button was successfully clicked.")
        except TimeoutException as e:
            logging.error(f"Error when clicking the 'Sign up' button: {e}")
            raise

    def wait_for_registration_form(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "name"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "signupRepeatPassword"))
            )
            logging.info("The registration form has been successfully uploaded.")
        except Exception as e:
            logging.error(f"Error loading registration form: {e}")
            raise

    def is_success_message_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
            )
            logging.info("A message about successful registration has been found.")
            return True
        except TimeoutException:
            logging.error("A message about successful registration was NOT found.")
            return False

    def is_error_message_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
            )
            logging.info("Error message found.")
            return True
        except TimeoutException:
            logging.error("Error message NOT found.")
            return False
