from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ''

service = Service(executable_path=CHROME_DRIVER_PATH)
X_URL = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input'


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path, options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/result/15118103633")
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()

        sleep(60)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                             '3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(8)
        email = self.driver.find_element(By.NAME, 'text')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        sleep(5)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(10)

        # click_first = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        #
        # tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div')
        # tweet.send_keys('Hello there')
        # tweet.send_keys(Keys.ENTER)

        tweet_compose = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                 '2]/div/div[2]/div[1]/div/div/div/div['
                                                 '2]/div[1]/div/div/div/div/div/div/div/div/div/div['
                                                 '1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for " \
                f"{PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                '2]/div/div[2]/div[1]/div/div/div/div['
                                                '2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        print(f'Hey Internet Provider, why is my internet speed {self.down}down{self.up}up when I pay '
              f'{PROMISED_DOWN}down/{PROMISED_UP}up')


# //*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span

bot = InternetSpeedTwitterBot(service)
bot.get_internet_speed()
bot.tweet_at_provider()
