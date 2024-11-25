from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# function to check the validity of the invoice number
def is_valid_tracking_number(tracking_number):
    return len(tracking_number) == 14 and tracking_number.isdigit()

tracking_number = "59500002864036"

if not is_valid_tracking_number(tracking_number):
    print("The invoice number must contain 14 digits.")
else:
    # Browser initialization
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())  # automatically download chromedriver
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # open page
        driver.get("https://tracking.novaposhta.ua/#/uk")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "en")))

        # find the field for entering the invoice number
        input_field = driver.find_element(By.ID, "en")
        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.RETURN)

        try:
            # check for an error message
            error_message_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "span[data-v-1c645ccd]"))
            )
            error_message = error_message_element.text
            print("Message from the Nova Poshta website:", error_message)
        except TimeoutException:
            print("Your parcel has been found in the database.")

            # click on the button 'Добре'
            try:
                ok_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "span.v-btn__content"))
                )
                ok_button.click()

                # waiting for information from the "header__status-text" field
                header_status_element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header__status-text"))
                )
                header_status_text = header_status_element.text
                print("Parcel status information:", header_status_text)
            except TimeoutException:
                print("Could not find the required information.")
    except NoSuchElementException as e:
        print(f"Item not found: {e}")
    finally:
        # сlose the browser
        driver.quit()
