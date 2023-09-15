from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# from linkedIn:
EMAIL = ""
PASSWORD = ""
PHONE_NUMBER = ""

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
# options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=chrome_options)

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3680043605&distance=25&f_AL=true&geoId=105693087&keywords" \
      "=python%20developer&location=Lagos%2C%20Lagos%20State%2C%20Nigeria&refresh=true&sortBy=R"

driver.get(URL)
time.sleep(2)

driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()

time.sleep(2)
email = driver.find_element(By.NAME, "session_key")
email.send_keys(EMAIL)
password = driver.find_element(By.NAME, "session_password")
password.send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button").click()

time.sleep(5)

all_job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for listing in all_job_listings:
    print("Called \n")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone_number = driver.find_element(By.CSS_SELECTOR, ".artdeco-text-input--container input")
        if phone_number.text == "":
            phone_number.send_keys(PHONE_NUMBER)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        if submit_button.get_attribute("aria-label") == "Continue to next step":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()


# driver.find_element(By.CSS_SELECTOR, ".display-flex button span").click()
# driver.find_element(By.CSS_SELECTOR, ".display-flex button span").click()
