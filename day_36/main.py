from datetime import date, timedelta
import os
from typing import Dict, List
import requests
from dotenv import load_dotenv

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MAX_DIFFERENCE = 3

load_dotenv()


def get_stock_price(str_day_before: str, str_yesterday: str) -> tuple[float, float]:
    request_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": os.getenv("STOCKS_API_KEY")
    }
    request = requests.get(os.getenv("STOCKS_BASE_URL"), params=request_params)
    request.raise_for_status()

    data = request.json()
    series = data["Time Series (Daily)"]

    yesterday_price = float(series[str_yesterday]["4. close"])
    day_before_price = float(series[str_day_before]["4. close"])
    return (day_before_price, yesterday_price)


def calc_difference(day_before_price: float, yesterday_price: float) -> float:
    difference = yesterday_price - day_before_price
    percentage = (difference * 100) / day_before_price
    return percentage


def get_news(from_date: str) -> List[Dict[str, str]]:

    params = {
        "q": STOCK.lower(),
        "from": from_date,
        "sortBy": "publishedAt",
        "pageSize": 3,
        "apiKey": os.getenv("NEWS_API_KEY")
    }
    request = requests.get(os.getenv("NEWS_BASE_URL"), params=params)
    request.raise_for_status()
    data = request.json()
    articles = []
    for article in data["articles"]:
        articles.append(
            {"title": article["title"], "description": article["description"]})

    return articles


def format_message(difference: float, news: List[Dict[str, str]]) -> str:
    message = f"{STOCK}: "
    if difference >= 0:
        message += "🔺"
    else:
        message += "🔻"

    message += f"{round(difference,2)}%\n"
    for article in news:
        message += f"Headline: {article['title']}\n"
        message += f"Brief: {article['description']}\n\n"

    return message


def send_message(message: str) -> None:
    """
    This method sends the message received as param to the telegram bot
    """
    url = os.getenv("TELEGRAM_BOT_BASE_URL")
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    send_message_url = f"{url}{token}/sendMessage"
    send_message_params = {
        "chat_id": os.getenv("TELEGRAM_BOT_CHAT_ID"),
        "parse_mode": "Markdown",
        "text": message
    }
    response = requests.get(send_message_url, params=send_message_params)
    response.raise_for_status()


str_today = date.today().strftime("%Y-%m-%d")
yesterday = date.today() - timedelta(days=1)
str_yesterday = yesterday.strftime("%Y-%m-%d")
day_before = date.today() - timedelta(days=2)
str_day_before = day_before.strftime("%Y-%m-%d")

(day_before_price, yesterday_price) = get_stock_price(
    str_day_before, str_yesterday)
difference = calc_difference(day_before_price, yesterday_price)
print("yesterday price: ", yesterday_price,
      "day before price: ", day_before_price,
      "difference", difference)

if abs(difference) > MAX_DIFFERENCE:
    news = get_news(str_today)
    message = format_message(difference, news)
    send_message(message)
