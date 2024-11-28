import pytest
import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28_page_object.pages.main_page import MainPage
from lesson_28_page_object.tests.conftest import register_user
from lesson_28_page_object.tests.conftest import navigate_to_site, driver


@pytest.mark.usefixtures("navigate_to_site")
def test_successful_registration(driver, register_user):
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

    # waiting for the registration form
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-body"))
        )
    except TimeoutException:
        raise AssertionError("The registration form did not appear on the page.")

    # filling in the registration form fields
    name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupName"))
    )
    name_field.clear()
    name_field.send_keys("Test")

    last_name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupLastName"))
    )
    last_name_field.clear()
    last_name_field.send_keys("User")

    email_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupEmail"))
    )
    email_field.clear()
    email_field.send_keys("kwuser@example.com")

    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupPassword"))
    )
    password_field.clear()
    password_field.send_keys("ValidPass123")

    repeat_password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupRepeatPassword"))
    )
    repeat_password_field.clear()
    repeat_password_field.send_keys("ValidPass123")

    # clicking the "Register" button to submit the form
    register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
    register_button.click()

    # expecting the registration form to be closed
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "modal-body"))
    )

    # Checking the redirect to the profile
    try:
        WebDriverWait(driver, 15).until(
            EC.url_contains("/panel/garage")
        )
    except TimeoutException:
        raise AssertionError("After registration, there was no redirection to the user profile.")


@pytest.mark.usefixtures("navigate_to_site")
def test_existing_user_registration(driver, register_user):
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-body"))
        )
    except TimeoutException:
        raise AssertionError("The registration form did not appear on the page..")

    name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupName"))
    )
    name_field.clear()
    name_field.send_keys("Test")

    last_name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupLastName"))
    )
    last_name_field.clear()
    last_name_field.send_keys("User")

    email_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupEmail"))
    )
    email_field.clear()
    email_field.send_keys("existing@example.com")  # email that already exists

    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupPassword"))
    )
    password_field.clear()
    password_field.send_keys("ValidPass123")

    repeat_password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupRepeatPassword"))
    )
    repeat_password_field.clear()
    repeat_password_field.send_keys("ValidPass123")

    # clicking the "Register" button to submit the form
    register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
    register_button.click()

    # delay for interface update
    time.sleep(3)

    # check the error message
    error_selector = (By.CLASS_NAME, "alert-danger")

    try:
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(error_selector)
        )
        assert error_element.is_displayed(), "No error message is displayed."
        print("Error found: ", error_element.text)
    except TimeoutException:
        print("No error message appeared.")
        raise AssertionError("The error message did not appear on the page.")


@pytest.mark.usefixtures("navigate_to_site")
def test_invalid_name_registration(driver):
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-body"))
    )

    name_field = driver.find_element(By.ID, "signupName")
    name_field.clear()
    name_field.send_keys("")
    driver.find_element(By.TAG_NAME, "body").click()

    error_selector = (By.CSS_SELECTOR, "#signupName + .invalid-feedback")
    error_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(error_selector)
    )
    actual_error = error_element.text
    assert actual_error == "Name required", (
        f"Expected message: 'Name required', but received: '{actual_error}'"
    )


@pytest.mark.usefixtures("navigate_to_site")
def test_invalid_email_registration(driver, email, password):
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-body"))
        )
    except TimeoutException:
        raise AssertionError("The registration form did not appear on the page.")

    email_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupEmail"))
    )
    email_field.clear()
    email_field.send_keys("invalid-email")

    driver.execute_script("document.activeElement.blur();")

    error_selector = (By.CSS_SELECTOR, "#signupEmail + .invalid-feedback")

    try:
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(error_selector)
        )
    except TimeoutException:
        raise AssertionError("The error message did not appear on the page.")

    actual_error = error_element.text
    assert actual_error == "Email is incorrect", (
        f"Expected message: 'Email is incorrect', but received: '{actual_error}'"
    )


@pytest.mark.usefixtures("navigate_to_site")
def test_short_password_registration(driver):
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-body"))
        )
    except TimeoutException:
        raise AssertionError("The registration form did not appear on the page.")

    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupPassword"))
    )
    password_field.clear()
    password_field.send_keys("123")

    driver.execute_script("document.activeElement.blur();")

    error_selector = (By.CSS_SELECTOR, "#signupPassword + .invalid-feedback")

    try:
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(error_selector)
        )
    except TimeoutException:
        raise AssertionError("The error message did not appear on the page.")

    actual_error = error_element.text
    expected_error = "Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter"

    assert actual_error == expected_error, (
        f"Message expected: '{expected_error}', but received: '{actual_error}'"
    )


@pytest.mark.usefixtures("navigate_to_site")
def test_invalid_repeat_password_registration(driver, register_user):
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-body"))
        )
    except TimeoutException:
        raise AssertionError("The registration form did not appear on the page.")

    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupPassword"))
    )
    password_field.clear()
    password_field.send_keys("short")

    repeat_password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "signupRepeatPassword"))
    )
    repeat_password_field.clear()
    repeat_password_field.send_keys("short")

    driver.execute_script("document.activeElement.blur();")

    error_selector = (By.CSS_SELECTOR, "#signupRepeatPassword + .invalid-feedback")

    try:
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(error_selector)
        )
    except TimeoutException:
        raise AssertionError("The error message did not appear on the page.")

    actual_error = error_element.text
    expected_error = "Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter"

    assert actual_error == expected_error, (
        f"Expected message: '{expected_error}', but received: '{actual_error}'"
    )

