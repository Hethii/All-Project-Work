from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(executable_path=CHROME_DRIVER_PATH)

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfzy7ji4qmyfR8dZR8NQgYhMqolw83eYcV9WibTF8gQIy38fQ/viewform?usp=sf_link"
driver = webdriver.Chrome(service=service, options=chrome_options)

URL = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A37' \
      '.842914%2C%22east%22%3A-122.32992%2C%22south%22%3A37.707608%2C%22west%22%3A-122.536739%7D%2C%22mapZoom%22%3A12' \
      '%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A' \
      '%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22' \
      '%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C' \
      '%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22' \
      '%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C' \
      '%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

# research = soup.select("div ul li")
# house = soup.find_all(name="div", class_="StyledCard-c11n-8-84-3__sc-rmiu6p-0")
house_price = soup.find_all(name="span", class_="iMKTKr")
house_info = soup.find_all(name="a", class_="jnnxAW")
# house_link = soup.find_all(name="a", class_="jnnxAW")

house_address = []
house_link_list = []
for n in house_info:
    text = n.get_text().split("|")
    house_address.append(text[-1].strip(" "))

    link = n.get("href")
    if "https://www.zillow.com" not in link:
        link_join = "https://www.zillow.com" + link
        house_link_list.append(link_join)
    else:
        house_link_list.append(link)

# print(house_address)
# print(house_link_list)

house_price_list = [price_list.getText().split("+")[0].split("/")[0] for price_list in house_price]
# print(house_price_list)

driver.get(FORM_URL)

for runs in range(len(house_address)):
    # print(house_price_list[runs])
    sleep(5)
    address = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div['
                                            '2]/div/div[1]/div/div[1]/input')
    address.send_keys(house_address[runs])
    sleep(1)
    price = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                          '1]/div/div[1]/input')
    price.send_keys(house_price_list[runs])
    sleep(1)
    property_link = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div['
                                                  '2]/div/div[1]/div/div[1]/input')

    property_link.send_keys(house_link_list[runs])
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
