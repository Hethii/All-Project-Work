import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Stock and twilio api. get inside file folders
STOCK_API_KEY = ""
api_key_newsapi = ""

account_sid = ""
auth_token = ""

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}


tsla_response = requests.get("https://www.alphavantage.co/query", params=parameters)
tsla_response.raise_for_status()
tsla_data = tsla_response.json()["Time Series (Daily)"]
tsla_data_list = [value for (key, value) in tsla_data.items()]

news_parameters = {
    "q": "tsla",
    "qInTitle": COMPANY_NAME,
    "apiKey": "news_api"
}
news_tesla_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_tesla_response.raise_for_status()
news_data = news_tesla_response.json()
# print(news_data)
yesterday = float(tsla_data_list[0]["4. close"])
day_before_yesterday = float(tsla_data_list[1]["4. close"])
#
#
percentage = 100 * (yesterday - day_before_yesterday) / yesterday
print(percentage)
final_percentage = '{:,.2f}'.format(abs(percentage))

up_down = None
if percentage > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

for news_index in range(3):
    if percentage >= 1:
        # print("Get News")
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f""""{STOCK}: {up_down}{final_percentage}%
            Headline: {news_data["articles"][news_index]["title"]}
            Brief: {news_data["articles"][news_index]["description"]}""",
            from_='twilio number',
            to='my number'
        )
        print(message.status)
