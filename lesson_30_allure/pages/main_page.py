import logging
import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_30_allure.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click on the button 'Registration'")
    def click_signup_button(self):
        signup_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']"))
        )
        signup_button.click()

    @allure.step("Fill in the form of registration.")
    def fill_form(self, name, last_name, email, password, repeat_password):
        self.fill_field((By.ID, "signupName"), name)
        self.fill_field((By.ID, "signupLastName"), last_name)
        self.fill_field((By.ID, "signupEmail"), email)
        self.fill_field((By.ID, "signupPassword"), password)
        self.fill_field((By.ID, "signupRepeatPassword"), repeat_password)

    @allure.step("Fill in the field of registration.")
    def fill_field(self, field_locator, value):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(field_locator)
        )
        field.clear()
        field.send_keys(value)

    @allure.step("Click on the button of registration.")
    def submit_form(self):
        register_button = self.driver.find_element(By.XPATH, "//button[text()='Register']")
        register_button.click()

    @allure.step("Waiting for element to visibility.")
    def wait_for_element_visibility(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} did not become visible within {timeout} seconds.")

    @allure.step("Waiting for registration to complete.")
    def wait_for_registration_to_complete(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "modal-body"))
        )

    @allure.step("Check redirect to profile.")
    def check_redirect_to_profile(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.url_contains("/panel/garage")
            )
        except TimeoutException:
            raise AssertionError("After registration, there was no redirection to the user profile.")

    @allure.step("Waiting for error message.")
    def wait_for_error_message(self, error_selector):
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(error_selector)
            )
            return error_element.text
        except TimeoutException:
            raise AssertionError("The error message did not appear on the page.")

    @allure.step("Is error message displays.")
    def is_error_message_displayed(self, error_selector):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(error_selector)
            )
            return True
        except TimeoutException:
            return False

