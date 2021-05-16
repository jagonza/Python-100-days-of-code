import os
from dotenv import load_dotenv
import datetime
import requests


def ask_for_wather() -> None:
    """
    This is the main method. Request the wather forecast
    and call the method to send de message to the telegram bot
    """

    weather_params = {
        "lat": 40.488345231500176,
        "lon": -3.6109706895784655,
        "units": "metric",
        "exclude": "current,minutely,daily",
        "appid": os.getenv("OWM_API_KEY")
    }
    response = requests.get(os.getenv("OWM_BASE_URL"), params=weather_params)
    response.raise_for_status()
    response_data = response.json()

    hourly_forecast = response_data["hourly"]
    weather_message = ""
    for i in range(0, 12):
        hour_data = hourly_forecast[i]
        day_information = datetime.datetime.fromtimestamp(
            hour_data["dt"]).strftime('%Hh')

        hour_weather_conditions = hour_data["weather"]
        for weather_condition in hour_weather_conditions:
            condition_id = weather_condition["id"]
            weather_icon = get_icon(condition_id)
            day_information += f" {weather_icon} "

        day_information += "\n"
        weather_message += day_information

    send_message(weather_message)


def get_icon(code: int) -> str:
    """
    This method takes the code that receives as param
    and return the corresponding weather icon
    """

    if code >= 200 and code < 300:
        return "⛈"
    elif code >= 300 and code < 400:
        return "🌦"
    elif code >= 500 and code < 600:
        return "🌧"
    elif code >= 600 and code < 700:
        return "❄️"
    elif code == 800:
        return "☀️"
    elif code == 801:
        return "🌤"
    elif code == 802:
        return "⛅️"
    elif code == 803:
        return "🌥"
    elif code == 804:
        return "☁️"


def send_message(message):
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


load_dotenv()

ask_for_wather()
