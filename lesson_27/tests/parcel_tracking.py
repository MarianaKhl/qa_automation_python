import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup_browser():
    # browser initialization
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


def enter_tracking_number(driver, tracking_number, input_locator, button_locator):
    WebDriverWait(driver, 10).until(
        lambda drv: drv.execute_script("return document.readyState") == "complete"
    )

    # enter parcel number
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(input_locator)
    ).clear()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(input_locator)
    ).send_keys(tracking_number)

    # wait and click on the button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(button_locator)
    ).click()


class TestTrackingStatus:
    def test_tracking_status_found(self, setup_browser):
        driver = setup_browser
        driver.get("https://tracking.novaposhta.ua/#/uk")

        tracking_number = "59500002864036"
        input_locator = ("id", "en")  # input field locator
        button_locator = ("id", "np-number-input-desktop-btn-search-en")  # search field locator

        enter_tracking_number(driver, tracking_number, input_locator, button_locator)

    def test_tracking_status_not_found(self, setup_browser):
        driver = setup_browser
        driver.get("https://tracking.novaposhta.ua/#/uk")

        tracking_number = "50000010864030"
        input_locator = ("css selector", "input#en")  # input field locator
        button_locator = ("css selector", "input#np-number-input-desktop-btn-search-en")  # search field locator
        error_locator = ("css selector", "span[data-v-1c645ccd]")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(input_locator)
        ).send_keys(tracking_number)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        ).click()

        # check if an error message appears or an additional payment window opens
        try:
            error_message_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-v-1c645ccd]"))
            )
            error_message = error_message_element.text
            print("Message from the Nova Poshta website:", error_message)
        except TimeoutException:
            print("Your parcel has been found in the database.")

            # click the "OK" button if it appears.
            try:
                ok_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "span.v-btn__content"))
                )
                ok_button.click()
                print("The 'OK' button was successfully pressed.")
            except TimeoutException:
                print("The 'OK' button did not appear.")