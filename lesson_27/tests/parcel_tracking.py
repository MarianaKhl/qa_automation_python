import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup_browser():
    """Fixture to initialize and clean up the browser."""
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


@pytest.fixture
def validate_tracking_number():
    """Helper fixture to validate tracking numbers."""
    def is_valid(tracking_number):
        return len(tracking_number) == 14 and tracking_number.isdigit()
    return is_valid


class TestNovaPoshtaTracking:
    def test_invalid_tracking_number(self, validate_tracking_number):
        """Test for invalid tracking numbers."""
        tracking_number = "134565332"  # Invalid tracking number
        assert not validate_tracking_number(tracking_number), "Tracking number validation failed for invalid input"

    def test_valid_tracking_number_not_found(self, setup_browser, validate_tracking_number):
        """Test case for a valid but non-existing tracking number."""
        tracking_number = "59500010864030"  # Valid but non-existing number
        assert validate_tracking_number(tracking_number), "Tracking number is not valid"

        driver = setup_browser
        driver.get("https://tracking.novaposhta.ua/#/uk")

        # Enter the tracking number
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "en")))
        input_field = driver.find_element(By.ID, "en")
        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.RETURN)

        # Verify the error message
        error_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-v-1c645ccd]"))
        )
        error_message = error_message_element.text
        assert "Ми не знайшли посилку за таким номером." in error_message, "Error message not found or incorrect"

    def test_valid_tracking_number_found(self, setup_browser, validate_tracking_number):
        """Test case for a valid existing tracking number."""
        tracking_number = "59500002864036"  # Replace with a valid tracking number
        assert validate_tracking_number(tracking_number), "Tracking number is not valid"

        driver = setup_browser
        driver.get("https://tracking.novaposhta.ua/#/uk")

        # Enter the tracking number
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "en")))
        input_field = driver.find_element(By.ID, "en")
        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.RETURN)

        # Handle popup and verify the status text - (header__status-text = Відправлення прямує до Братислава.)(header__status-header = Зараз:)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.v-btn__content"))).click()
        header_status_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header__status-text"))
        )
        header_status_text = header_status_element.text
        assert "Відправлення прямує до Братислава." in header_status_text, "Header status text not found or incorrect"
