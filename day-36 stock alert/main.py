import requests
import smtplib

COMPANY_TICKER = "TSLA"
COMPANY_NAME = "Tesla"
AUTOMATIC_MAIL_ADDRESS = "ABC"
AUTOMATIC_MAIL_PASSWORD = '***'
MAIL_RECIPIENT = "XYZ"

endpoint1 = "https://www.alphavantage.co/query"
params1 = {
    "function": "TIME_SERIES_DAILY",
    "apikey": "123",
    "symbol": COMPANY_TICKER
}

endpoint2 = "https://newsapi.org/v2/everything"
params2 = {
    "apiKey":"123",
    "qInTitle":COMPANY_NAME,
    "pageSize":3,
    "page":1
}

request1 = requests.get(endpoint1,params=params1)
price_data = request1.json()["Time Series (Daily)"]
data_list = [value for (key,value) in price_data.items()]

last_date_price=data_list[0]["4. close"]
day_before_last_date_price = data_list[1]["4. close"]

price_change_percentage = float(last_date_price)/ float(day_before_last_date_price)
if price_change_percentage != 0:
    nice_percentage_value = f"{((price_change_percentage - 1) * 100):.2f}%"
else:
    nice_percentage_value = "0.00%"

if price_change_percentage < 0.95 or price_change_percentage > 1.05:
    request2 = requests.get(endpoint2, params=params2)
    news_data = request2.json()
    articles = news_data["articles"]
    three_articles = articles[:3]
    formatted_articles = [article['title'] for article in three_articles]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=AUTOMATIC_MAIL_ADDRESS, password=AUTOMATIC_MAIL_PASSWORD)
        connection.sendmail(from_addr=AUTOMATIC_MAIL_ADDRESS, to_addrs=MAIL_RECIPIENT,
                            msg=f"Subject: {COMPANY_NAME} stock news headlines update\n\n{formatted_articles[0]}\n{formatted_articles[1]}\nLast day price change:{nice_percentage_value}")
else:
    print("Nothing important happened, news not needed")



