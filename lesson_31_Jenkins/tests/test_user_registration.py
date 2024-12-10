import allure
import pytest
from selenium.webdriver.common.by import By
from lesson_31_Jenkins.pages.main_pages import MainPage


@allure.feature("Registration")
@pytest.mark.usefixtures("navigate_to_site")
def test_successful_registration(driver):
    main_page = MainPage(driver)

    main_page.click_signup_button()
    main_page.wait_for_modal_to_appear()
    main_page.fill_form(
        name="Test",
        last_name="User",
        email="jjj94ppuser@example.com",
        password="ValidPass123",
        repeat_password="ValidPass123"
    )
    main_page.submit_registration_form()
    main_page.wait_for_registration_to_complete()
    main_page.check_redirect_to_profile()


@allure.feature("Registration")
@pytest.mark.usefixtures("navigate_to_site")
def test_existing_user_registration(driver):
    main_page = MainPage(driver)

    main_page.click_signup_button()
    main_page.wait_for_modal_to_appear()
    main_page.fill_form(
        name="Test",
        last_name="User",
        email="existing@example.com",
        password="ValidPass123",
        repeat_password="ValidPass123"
    )
    main_page.submit_registration_form()

    error_selector = (By.CLASS_NAME, "alert-danger")
    error_message = main_page.wait_for_error_message(error_selector)

    assert error_message == "User already exists", (
        f"Expected error message: 'User already exists', but received: '{error_message}'"
    )


@allure.feature("Registration")
@pytest.mark.usefixtures("navigate_to_site")
def test_invalid_name_registration(driver):
    main_page = MainPage(driver)
    main_page.click_signup_button()
    main_page.wait_for_modal_to_appear()
    main_page.fill_field(MainPage.NAME_FIELD, "")
    main_page.trigger_field_blur()

    error_message = main_page.get_error_message(MainPage.ERROR_NAME)
    assert error_message == "Name required", (
        f"Expected message: 'Name required', but received: '{error_message}'"
    )


@allure.feature("Registration")
@pytest.mark.usefixtures("navigate_to_site")
def test_invalid_email_registration(driver):
    main_page = MainPage(driver)
    main_page.click_signup_button()
    main_page.wait_for_modal_to_appear()
    main_page.fill_field(MainPage.EMAIL_FIELD, "invalid-email")
    main_page.trigger_field_blur()

    error_message = main_page.get_error_message(MainPage.ERROR_EMAIL)
    assert error_message == "Email is incorrect", (
        f"Expected message: 'Email is incorrect', but received: '{error_message}'"
    )


@allure.feature("Registration")
@pytest.mark.usefixtures("navigate_to_site")
def test_short_password_registration(driver):
    main_page = MainPage(driver)
    main_page.click_signup_button()
    main_page.wait_for_modal_to_appear()
    main_page.fill_field(MainPage.PASSWORD_FIELD, "123")
    main_page.trigger_field_blur()

    error_message = main_page.get_error_message(MainPage.ERROR_PASSWORD)
    expected_error = "Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter"

    assert error_message == expected_error, (
        f"Message expected: '{expected_error}', but received: '{error_message}'"
    )

