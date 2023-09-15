from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
# options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# articles_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# articles_count.click()

# view_source = driver.find_element(By.LINK_TEXT, "View source")
# view_source.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# driver.get('http://secure-retreat-92358.herokuapp.com/')
# first_name = driver.find_element(By.NAME, "fName")
# first_name.send_keys("Ebenezer")
# last_name = driver.find_element(By.NAME, "lName")
# last_name.send_keys("Owoeye")
# email = driver.find_element(By.NAME, "email")
# email.send_keys("ezertobi@gmail.com")
# sign_up = driver.find_element(By.CLASS_NAME, "btn-lg")
# sign_up.click()

import time

driver.get('https://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

five_min = time.time() + 60 * 5
timeout = time.time() + 5
while True:

    cookie.click()
    if time.time() > timeout:
        cookie_amount = driver.find_element(By.ID, "money").text
        if "," in cookie_amount:
            cookie_amount = cookie_amount.replace(",", "")
        cookie_acquired = int(cookie_amount)

        upgrade_cost = driver.find_elements(By.CSS_SELECTOR, "#store b")
        # print(upgrade_cost)
        amount_needed = [int(amount.text.split("-")[1].strip().replace(",", "")) for amount in upgrade_cost if
                         amount.text != ""]

        cookie_upgrades = {}
        for n in range(len(amount_needed)):
            cookie_upgrades[amount_needed[n]] = item_ids[n]
        # print(cookie_upgrades)

        # # Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, the_id in cookie_upgrades.items():

            if cookie_count > cost:
                affordable_upgrades[cost] = the_id

        # print(affordable_upgrades)

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        # print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        # print(to_purchase_id)
        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5
    if time.time() > five_min:
        cookie_rate = driver.find_element(By.ID, "cps")
        text = cookie_rate.text
        print(text)
        break
# cookies/second : 49

# 0.1251|61773|27|251|9|245|1|550|0|2000|1|7701|1|55001|0|1000000|0|123456789
