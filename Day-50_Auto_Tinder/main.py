import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# for tinder
EMAIL = ""
PASSWORD = ""

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

URl = "https://tinder.com/"

driver.get(URl)
time.sleep(2)

log_in = driver.find_element(By.XPATH, '//*[@id="u1469494057"]/div/div[1]/div/main/div['
                                       '1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()

time.sleep(5)

facebook = driver.find_element(By.XPATH, '//*[@id="u-258887019"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div['
                                         '2]/button')
facebook.click()

time.sleep(10)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
# print(driver.title)

email = driver.find_element(By.ID, "email")
email.send_keys(EMAIL)

password = driver.find_element(By.ID, "pass")
password.send_keys(PASSWORD)

driver.find_element(By.NAME, "login").click()

driver.switch_to.window(base_window)

time.sleep(8)

driver.find_element(By.XPATH, '//*[@id="u-258887019"]/main/div[2]/div/div/div[1]/div[1]/button').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="u-258887019"]/main/div[1]/div/div/div[3]/button[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="u-258887019"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
time.sleep(2)

LIKE_URL = '# //*[@id="u1469494057"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button/span/span/svg'


for n in range(100):
    print("called")
    time.sleep(2)
    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            print("Loading")
            time.sleep(2)

    time.sleep(3)


