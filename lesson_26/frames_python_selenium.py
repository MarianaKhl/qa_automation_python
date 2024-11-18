from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver initialization
driver = webdriver.Chrome()

# opening the main HTML page, start server the first in the console = python3 -m http.server 8000
driver.get("http://localhost:8000/dz.html")

try:
    # go to the first frame
    WebDriverWait(driver, timeout=10).until(
        EC.frame_to_be_available_and_switch_to_it("frame1")
    )
    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")
    button1 = driver.find_element(By.TAG_NAME, "button")
    button1.click()

    # checking the message in the dialog box
    alert1 = Alert(driver)
    assert "Верифікація пройшла успішно!" in alert1.text
    print("Frame1 verification successful")
    alert1.accept()

    # return to the main context
    driver.switch_to.default_content()

    # go to the second frame
    WebDriverWait(driver, timeout=10).until(
        EC.frame_to_be_available_and_switch_to_it("frame2")
    )
    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")
    button2 = driver.find_element(By.TAG_NAME, "button")
    button2.click()

    alert2 = Alert(driver)
    assert "Верифікація пройшла успішно!" in alert2.text
    print("Frame2 verification successful")
    alert2.accept()

except Exception as e:
    import traceback
    print(f"An error occurred: {e}")
    traceback.print_exc()

finally:
    # closing the browser
    driver.quit()

