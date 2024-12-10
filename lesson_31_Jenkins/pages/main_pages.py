import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_31_Jenkins.pages.base_page import BasePage


class MainPage(BasePage):
    MODAL_BODY = (By.CLASS_NAME, "modal-body")
    NAME_FIELD = (By.ID, "signupName")
    LAST_NAME_FIELD = (By.ID, "signupLastName")
    EMAIL_FIELD = (By.ID, "signupEmail")
    PASSWORD_FIELD = (By.ID, "signupPassword")
    REPEAT_PASSWORD_FIELD = (By.ID, "signupRepeatPassword")
    SIGNUP_BUTTON = (By.XPATH, "//button[text()='Sign up']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Register']")

    ERROR_NAME = (By.CSS_SELECTOR, "#signupName + .invalid-feedback")
    ERROR_EMAIL = (By.CSS_SELECTOR, "#signupEmail + .invalid-feedback")
    ERROR_PASSWORD = (By.CSS_SELECTOR, "#signupPassword + .invalid-feedback")

    @allure.step("Waiting for the registration modal to disappear")
    def wait_for_registration_to_complete(self, timeout=10):
        self.wait_for_element_invisibility(self.MODAL_BODY, timeout)

    @allure.step("Click on the 'Sign up' button")
    def click_signup_button(self):
        self.click_element(*self.SIGNUP_BUTTON)

    @allure.step("Wait for the registration modal to be visible")
    def wait_for_modal_to_appear(self):
        self.wait_for_element_visibility(self.MODAL_BODY)

    @allure.step("Fill the registration form")
    def fill_form(self, name, last_name, email, password, repeat_password):
        self.fill_field(self.NAME_FIELD, name)
        self.fill_field(self.LAST_NAME_FIELD, last_name)
        self.fill_field(self.EMAIL_FIELD, email)
        self.fill_field(self.PASSWORD_FIELD, password)
        self.fill_field(self.REPEAT_PASSWORD_FIELD, repeat_password)

    @allure.step("Submit the registration form")
    def submit_registration_form(self):
        self.click_element(*self.REGISTER_BUTTON)

    @allure.step("Check if redirected to profile page")
    def check_redirect_to_profile(self, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains("/panel/garage")
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="redirect_failure",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("No redirect to profile page after registration.")
