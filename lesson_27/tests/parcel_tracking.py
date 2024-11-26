import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from lesson_27.pages.tracking_page import TrackingPage


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


class TestTrackingStatus:
    def test_tracking_status_found(self, setup_browser):
        driver = setup_browser
        driver.get("https://tracking.novaposhta.ua/#/uk")

        page = TrackingPage(driver)
        page.enter_tracking_number("59500002864036")
        page.click_search_button()

        error_message = page.get_error_message()
        if error_message:
            print("Message from the Nova Poshta website:", error_message)
        else:
            print("Your parcel has been found in the database.")
            if page.click_ok_button():
                print("The 'Добре' button was clicked successfully.")
            else:
                print("The 'Добре' button did not appear.")

    def test_tracking_status_not_found(self, setup_browser):
        driver = setup_browser
        driver.get("https://tracking.novaposhta.ua/#/uk")

        page = TrackingPage(driver)
        page.enter_tracking_number("50000010864030")
        page.click_search_button()

        # logging for debugging
        print(driver.page_source)
        driver.save_screenshot("error_state.png")

        # waiting and checking for an error message
        error_message = page.get_error_message()
        assert error_message, "Expected error message to appear, but it did not."
