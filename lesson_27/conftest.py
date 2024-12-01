import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from lesson_27.pages.main_page import TrackingPage

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def tracking_page(setup_browser):
    driver = setup_browser
    driver.get("https://tracking.novaposhta.ua/#/uk")
    return TrackingPage(driver)

