import logging
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28_page_object.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_signup_button(self):
        signup_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']"))
        )
        signup_button.click()

    def fill_form(self, name, last_name, email, password, repeat_password):
        self.fill_field((By.ID, "signupName"), name)
        self.fill_field((By.ID, "signupLastName"), last_name)
        self.fill_field((By.ID, "signupEmail"), email)
        self.fill_field((By.ID, "signupPassword"), password)
        self.fill_field((By.ID, "signupRepeatPassword"), repeat_password)

    def fill_field(self, field_locator, value):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(field_locator)
        )
        field.clear()
        field.send_keys(value)

    def submit_form(self):
        register_button = self.driver.find_element(By.XPATH, "//button[text()='Register']")
        register_button.click()

    def wait_for_element_visibility(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} did not become visible within {timeout} seconds.")

    def wait_for_registration_to_complete(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "modal-body"))
        )

    def check_redirect_to_profile(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.url_contains("/panel/garage")
            )
        except TimeoutException:
            raise AssertionError("After registration, there was no redirection to the user profile.")

    def wait_for_error_message(self, error_selector):
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(error_selector)
            )
            return error_element.text
        except TimeoutException:
            raise AssertionError("The error message did not appear on the page.")

    def is_error_message_displayed(self, error_selector):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(error_selector)
            )
            return True
        except TimeoutException:
            return False
