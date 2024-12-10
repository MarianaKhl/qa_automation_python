from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def get_error_message(driver, xpath):
    try:
        error_message_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return error_message_element.text.strip()
    except TimeoutException:
        return "No error message found"


def validate_registration_errors(driver):
    errors = {}
    errors['name'] = get_error_message(driver, "//input[@name='name']/following-sibling::div[@class='invalid-feedback']/p")
    errors['email'] = get_error_message(driver, "//input[@name='email']/following-sibling::div[@class='invalid-feedback']/p")
    errors['password'] = get_error_message(driver, "//input[@name='password']/following-sibling::div[@class='invalid-feedback']/p")
    errors['repeat_password'] = get_error_message(driver, "//input[@id='signupRepeatPassword']/following-sibling::div[@class='invalid-feedback']/p")
    errors['general'] = get_error_message(driver, "//div[@class='alert alert-danger']")
    return errors


def get_invalid_registration_data():
    return {
        "name": "",
        "email": "invalid-email",
        "password": "123",
        "repeat_password": "123",
    }
