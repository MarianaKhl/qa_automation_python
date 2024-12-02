import pytest
from selenium.webdriver.common.by import By
from lesson_28_page_object.pages.main_page import MainPage
from lesson_28_page_object.tests.conftest import register_user
from lesson_28_page_object.tests.conftest import navigate_to_site, driver


@pytest.mark.usefixtures("navigate_to_site")
def test_successful_registration(driver, register_user):
    main_page = MainPage(driver)

    main_page.click_signup_button()

    # waiting for the registration form to appear.
    main_page.wait_for_element_visibility((By.CLASS_NAME, "modal-body"))

    main_page.fill_form("Test", "User", "k7buser@example.com", "ValidPass123", "ValidPass123")

    # submitting the form
    main_page.submit_form()

    main_page.wait_for_registration_to_complete()

    # checking the redirect to the profile
    main_page.check_redirect_to_profile()


@pytest.mark.usefixtures("navigate_to_site")
def test_existing_user_registration(driver, register_user):
    main_page = MainPage(driver)

    main_page.click_signup_button()

    main_page.wait_for_element_visibility((By.CLASS_NAME, "modal-body"))

    main_page.fill_form("Test", "User", "existing@example.com", "ValidPass123", "ValidPass123")

    main_page.submit_form()

    error_selector = (By.CLASS_NAME, "alert-danger")
    error_message = main_page.wait_for_error_message(error_selector)

    assert error_message == "User already exists", (
        f"Expected error message: 'User already exists', but received: '{error_message}'"
    )


@pytest.mark.usefixtures("navigate_to_site")
def test_invalid_name_registration(driver):
    main_page = MainPage(driver)

    main_page.click_signup_button()

    main_page.wait_for_element_visibility((By.CLASS_NAME, "modal-body"))

    main_page.fill_field((By.ID, "signupName"), "")

    driver.find_element(By.TAG_NAME, "body").click()

    error_selector = (By.CSS_SELECTOR, "#signupName + .invalid-feedback")
    actual_error = main_page.wait_for_error_message(error_selector)

    assert actual_error == "Name required", (
        f"Expected message: 'Name required', but received: '{actual_error}'"
    )


@pytest.mark.usefixtures("navigate_to_site")
def test_invalid_email_registration(driver, email, password):
    main_page = MainPage(driver)

    main_page.click_signup_button()

    main_page.wait_for_element_visibility((By.CLASS_NAME, "modal-body"))

    main_page.fill_field((By.ID, "signupEmail"), "invalid-email")

    driver.execute_script("document.activeElement.blur();")

    error_selector = (By.CSS_SELECTOR, "#signupEmail + .invalid-feedback")
    actual_error = main_page.wait_for_error_message(error_selector)

    assert actual_error == "Email is incorrect", (
        f"Expected message: 'Email is incorrect', but received: '{actual_error}'"
    )


@pytest.mark.usefixtures("navigate_to_site")
def test_short_password_registration(driver):
    main_page = MainPage(driver)

    main_page.click_signup_button()

    main_page.wait_for_element_visibility((By.CLASS_NAME, "modal-body"))

    main_page.fill_field((By.ID, "signupPassword"), "123")

    driver.execute_script("document.activeElement.blur();")

    error_selector = (By.CSS_SELECTOR, "#signupPassword + .invalid-feedback")
    actual_error = main_page.wait_for_error_message(error_selector)

    expected_error = "Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter"

    assert actual_error == expected_error, (
        f"Message expected: '{expected_error}', but received: '{actual_error}'"
    )

@pytest.mark.usefixtures("navigate_to_site")
def test_invalid_repeat_password_registration(driver, register_user):
    main_page = MainPage(driver)

    main_page.click_signup_button()

    main_page.wait_for_element_visibility((By.CLASS_NAME, "modal-body"))

    main_page.fill_field((By.ID, "signupPassword"), "short")

    main_page.fill_field((By.ID, "signupRepeatPassword"), "short")

    driver.execute_script("document.activeElement.blur();")

    error_selector = (By.CSS_SELECTOR, "#signupRepeatPassword + .invalid-feedback")
    actual_error = main_page.wait_for_error_message(error_selector)

    expected_error = "Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter"

    assert actual_error == expected_error, (
        f"Expected message: '{expected_error}', but received: '{actual_error}'"
    )
