from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Starting the WebDriver
driver = webdriver.Chrome()

# Login to the site with authorization
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

try:
    # Waiting for the "Sign In" button to appear and clicking it
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(@class, 'btn-outline-white') and contains(@class, 'header_signin') and text()='Sign In']")
        )
    )
    sign_in_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-outline-white') and contains(@class, 'header_signin') and text()='Sign In']")
    sign_in_button.click()
    print("The button 'Sign In' was found and clicked!")

    # Filling in the email field
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='email' and @type='text']"))
    )
    email_field = driver.find_element(By.XPATH, "//input[@name='email' and @type='text']")
    email_field.send_keys("guest")

    # Filling in the password field
    password_field = driver.find_element(By.XPATH, "//input[@name='password' and @type='password']")
    password_field.send_keys("welcome2qauto")

    # Clicking the "Login" button
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_button.click()
    print("Authorization completed successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Closing the browser after execution
    driver.quit()

