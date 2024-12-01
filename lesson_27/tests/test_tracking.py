import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


class TestTrackingStatus:
    def test_tracking_status_found(self, tracking_page):
        tracking_page.enter_tracking_number("59500002864036")
        tracking_page.click_search_button()

        status_text = tracking_page.get_status_text()
        assert status_text == "Отримана", f"Expected status 'Oтримана', but got '{status_text}'"

    def test_tracking_status_not_found(self, tracking_page):
        tracking_page.enter_tracking_number("50000010864030")
        tracking_page.click_search_button()

        error_message = tracking_page.get_error_message()
        assert error_message is not None, "Expected error message, but none was found"
        assert ("Ми не знайшли посилку за таким номером. Можливо, вона ще не передана для відправлення, або номер "
                "некоректний. Перевірте, чи відповідає вказаний номер можливому формату: 59500000031324 або "
                "AENM0002497278NPI.") in error_message, f"Unexpected error message: {error_message}"
