import requests
from datetime import datetime
import time

MY_LAT = 40.416729
MY_LONG = -3.703339

iss_latitude = 0
iss_longitude = 0
hour_now = 0
sunrise = 0
sunset = 0


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    global iss_latitude
    iss_latitude = float(data["iss_position"]["latitude"])
    global iss_longitude
    iss_longitude = float(data["iss_position"]["longitude"])


def get_sunset_sunrise():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json",
        params=parameters)
    response.raise_for_status()
    data = response.json()
    global sunrise
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    global sunset
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


def get_hour_now():
    time_now = datetime.now()
    global hour_now
    hour_now = time_now.isoformat().split("T")[1].split(":")[0]


def check_iss_position():
    get_hour_now()
    get_sunset_sunrise()
    get_iss_position()
    print(f"Your position is: lat = {MY_LAT} long = {MY_LONG}")
    print(f"ISS position is: lat = {iss_latitude} long = {iss_longitude}")
    print(
        f"It's {hour_now} and the sunset is at {sunset} and the sunrise is at {sunrise}")
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG):
        if hour_now >= sunset and hour_now <= sunrise:
            print("WATCH THE ISS OVER YOUR HEAD")


while True:
    check_iss_position()
    time.sleep(60)
