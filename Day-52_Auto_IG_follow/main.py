from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)

# for INSTAGRAM
SIMILAR_ACCOUNTS = "PREFERED ACCOUNT USERNAME"
USERNAME = ''
PASSRWORD = ''


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path, options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSRWORD)
        password.send_keys(Keys.ENTER)

        sleep(8)

        self.driver.find_element(By.CSS_SELECTOR, 'section button').click()
        sleep(8)
        self.driver.find_element(By.CLASS_NAME, '_a9_0').click()

    def find_followers(self):
        self.driver.get("https://www.instagram.com/wealth/")
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, 'div ul li a').click()

        sleep(5)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div['
                                                   '2]/div/div/div/div/div[2]/div/div/div[2]')
        for n in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        followers_list = self.driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div['
                                                             '1]/div/div[2]/div/div/div/div/div[2]/div/div/div['
                                                             '2]/div[2]/div/div/div/div/div/div[3]/div/button')
        for n in followers_list:
            try:
                n.click()
                sleep(2)
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div['
                                                   '2]/div/div/div/div/div/div/button[2]').click()
                sleep(1)


bot = InstaFollower(service)
bot.login()
bot.find_followers()
bot.follow()
