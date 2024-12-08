import pytest
import allure
import sys
import os
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

@pytest.fixture(scope="function")
def driver():
    # driver initialization
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver

    driver.quit()

@allure.feature("Registration")
@pytest.fixture(scope="function")
def navigate_to_site(driver):
    url = "https://guest:welcome2qauto@qauto2.forstudy.space/"
    driver.get(url)
    return driver

@allure.feature("Registration")
@pytest.mark.usefixtures("driver")
def test_registration_error_messages(driver):
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-body"))
    )

    fields = [
        {
            "field_selector": (By.ID, "signupName"),
            "error_selector": (By.CSS_SELECTOR, "#signupName + .invalid-feedback"),
            "input_value": "",
            "expected_error": "Name required",
        },
        {
            "field_selector": (By.ID, "signupEmail"),
            "error_selector": (By.CSS_SELECTOR, "#signupEmail + .invalid-feedback"),
            "input_value": "invalid-email",
            "expected_error": "Email is incorrect",
        },
        {
            "field_selector": (By.ID, "signupPassword"),
            "error_selector": (By.CSS_SELECTOR, "#signupPassword + .invalid-feedback"),
            "input_value": "short",
            "expected_error": (
                "Password has to be from 8 to 15 characters long and contain at least one integer, "
                "one capital, and one small letter"
            ),
        },
        {
            "field_selector": (By.ID, "signupRepeatPassword"),
            "error_selector": (
                By.CSS_SELECTOR,
                "#signupRepeatPassword + .invalid-feedback",
            ),
            "input_value": "short",
            "expected_error": (
                "Password has to be from 8 to 15 characters long and contain at least one integer, "
                "one capital, and one small letter"
            ),
        },
    ]

    for field in fields:
        driver.find_element(*field["field_selector"]).clear()
        driver.find_element(*field["field_selector"]).send_keys(field["input_value"])
        driver.find_element(By.TAG_NAME, "body").click()
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(field["error_selector"])
        )
        actual_error = error_element.text

        assert actual_error == field["expected_error"], (
            f"For field {field['field_selector']} expected: '{field['expected_error']}', "
            f"but received: '{actual_error}'"
        )

    driver.find_element(By.ID, "signupEmail").clear()
    driver.find_element(By.ID, "signupEmail").send_keys("test@example.com")
    driver.find_element(By.ID, "signupPassword").send_keys("TestPassword123")
    driver.find_element(By.ID, "signupRepeatPassword").send_keys("TestPassword123")
    driver.find_element(By.XPATH, "//button[text()='Register']").click()

    general_error_selector = (By.CLASS_NAME, "alert-danger")
    general_error_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(general_error_selector)
    )
    general_error_text = general_error_element.text
    assert general_error_text == "User already exists", (
        f"Expected message: 'User already exists', but received: '{general_error_text}'"
    )


@pytest.fixture
def name():
    return "John"


@pytest.fixture
def last_name():
    return "Doe"


@pytest.fixture
def email():
    return "johndoe@example.com"


@pytest.fixture
def password():
    return "Password123"


@pytest.fixture
def register_user(driver):
    def _register(first_name, last_name, email, password):
        driver.find_element(By.ID, "signupFirstName").send_keys(first_name)
        driver.find_element(By.ID, "signupLastName").send_keys(last_name)
        driver.find_element(By.ID, "signupEmail").send_keys(email)
        password_field = driver.find_element(By.ID, "signupPassword")
        password_field.send_keys(password)

        password_field.click()

        driver.execute_script("document.activeElement.blur();")

        driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".invalid-feedback"))
            )
            error_messages = {}
            try:
                error_message = driver.find_element(By.CSS_SELECTOR, "#signupPassword + .invalid-feedback")
                error_messages["password"] = error_message.text
            except NoSuchElementException:
                pass
            return {"status": "error", "messages": error_messages}
        except TimeoutException:
            return {"status": "success", "messages": {"info": "Registration successful"}}

    return _register


def fill_field(self, field_locator, value):
    field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(field_locator))
    field.clear()
    field.send_keys(value)

