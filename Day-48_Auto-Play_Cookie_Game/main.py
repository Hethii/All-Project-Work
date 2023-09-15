from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
driver.get("https://www.python.org/")

# price = driver.find_element(By.ID, "priceblock_ourprice")
# print(price.text)
# price = driver.find_element(By.XPATH, '//*[@id="corePrice_feature_div"]/div/span[1]/span[1]')

search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)

logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
#
# event = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]')
# print(event.text)

# events_dict = {}
# for numbers in range(5):
#     event = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{numbers + 1}]/time')
#     event_title = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{numbers + 1}]/a')
#     event_date = event.get_attribute('datetime').split("T")[0]
#
#     events_dict.update({numbers: {
#         'time': event_date,
#         'name': event_title.text
#     }
#     })
#
# print(events_dict)
#
# # another way
# event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].get_attribute('datetime').split("T")[0],
#         "name": event_names[n].text,
#     }
# print(events)


# driver.close()  # close the particular tab
driver.quit()  # closes all the tabs
