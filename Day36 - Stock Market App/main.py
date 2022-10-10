import requests
import datetime as dt
from twilio.rest import Client

# To jest do twilio
account_sid = "AC4d1a0b54cc08ca9c1bc68f0295a9906a"
auth_token = "875812ca149039517660b28358ae5235"

# Uzyskanie daty wczorajszej i przedwczorajszej
today = dt.date.today()
yesterday = dt.datetime.strftime(today - dt.timedelta(1), '%Y-%m-%d')
before_yesterday = dt.datetime.strftime(today - dt.timedelta(2), '%Y-%m-%d')
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_app_id = "0H5MP1SI7K8GW0VD"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_app_id = "a91c9be56b444c2488fa11793518744c"


# STEP 1: Use https://newsapi.org/docs/endpoints/everything
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_app_id,
}
response_stock = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response_stock.raise_for_status()
raw_stock_data = response_stock.json()

stock_data = raw_stock_data["Time Series (Daily)"]
yesterday_stock = float(stock_data[yesterday]["4. close"])
two_days_stock = float(stock_data[before_yesterday]["4. close"])

value_diff = round(yesterday_stock - two_days_stock, 2)
percentage_diff = round(((yesterday_stock - two_days_stock) / two_days_stock) * 100, 2)


# STEP 2: Use https://newsapi.org/docs/endpoints/everything
news_parameters = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "sortBy": "relevancy",
    "apiKey": news_app_id,
}
response_news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
response_news.raise_for_status()

raw_news_data = response_news.json()
news_data = raw_news_data["articles"][:3]
print(news_data)


# STEP 3: Use twilio.com/docs/sms/quickstart/python
client = Client(account_sid, auth_token)
for news in news_data:
    if value_diff > 0:
        message = f"""
        TSLA: 🔺{percentage_diff}%
        Headline: {news["title"]}
        Brief: {news["description"]}
        """
        message = client.messages \
            .create(
                body=message,
                from_='+48732106918',
                to='+48666532414'
            )
    else:
        message = f"""
                TSLA: 🔻{percentage_diff}%
                Headline: {news["title"]}
                Brief: {news["description"]}
                """
        message = client.messages \
            .create(
                body=message,
                from_='+48732106918',
                to='+48666532414'
            )
