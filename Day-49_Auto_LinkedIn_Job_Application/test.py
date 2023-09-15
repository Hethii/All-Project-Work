from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""
PHONE = ""

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
# options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=chrome_options)

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3680043605&distance=25&f_AL=true&geoId=105693087&keywords" \
      "=python%20developer&location=Lagos%2C%20Lagos%20State%2C%20Nigeria&refresh=true&sortBy=R"

driver.get(URL)

time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
# password_field.send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button").click()

time.sleep(5)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called \n")
    # print(listing.text)
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
#     try:
#         apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
#         apply_button.click()
#         time.sleep(5)
#
#         # If phone field is empty, then fill your phone number.
#         phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
#         if phone.text == "":
#             phone.send_keys(PHONE)
#
#         submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
#
#         # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
#             close_button.click()
#             time.sleep(2)
#             discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
#             discard_button.click()
#             print("Complex application, skipped.")
#             continue
#         else:
#             submit_button.click()
#
#         # Once application completed, close the pop-up window.
#         time.sleep(2)
#         close_button = driver.find_element(By.CLASS_NAME "artdeco-modal__dismiss")
#         close_button.click()
#
#     # If already applied to job or job is no longer accepting applications, then skip.
#     except NoSuchElementException:
#         print("No application button, skipped.")
#         continue
#
# time.sleep(5)
# driver.quit()
