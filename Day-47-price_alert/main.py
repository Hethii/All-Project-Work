import smtplib
import lxml
import requests
from bs4 import BeautifulSoup

MY_EMAIL = ""
MY_PASSWORD = ""

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url, headers=headers)

# print(response.content)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
# print(price_as_float)

trial_price = 200.0
product_name = soup.find(id="productTitle").getText().strip()
# print(f"{product_name}")


if price_as_float < trial_price:
    message = f"{product_name} is now ${price_as_float}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="ezerowoeye@yahoo.com",
                            msg=f"Subject: Price Alert!\n\n{message}\n{url}".encode("utf8"))
