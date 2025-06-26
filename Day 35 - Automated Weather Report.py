import requests, os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OPEN_WEATHER_API = requests.get(f"https://api.openweathermap.org/data/2.5/"
f"forecast?lat={os.environ.get("day_35_lat")}&lon={os.environ.get("day_35_lon")}"
f"&appid={os.environ.get("day_35_api")}&units=imperial&cnt=8")
OPEN_WEATHER_API.raise_for_status()
OPEN_WEATHER_API_DATA = OPEN_WEATHER_API.json()
TWILIO_SID = os.environ.get("day_35_sid")
TWILIO_TOKEN = os.environ.get("day_35_token")
PROXY_CLIENT = TwilioHttpClient()
PROXY_CLIENT.session.proxies = {"https": os.environ["https_proxy"]}
CLIENT = Client(TWILIO_SID, TWILIO_TOKEN, http_client=PROXY_CLIENT)

messageBody = ""
def weatherReport():
    global messageBody
    counter = 0
    while counter <= 7:
        time = OPEN_WEATHER_API_DATA["list"][counter]["dt_txt"]
        temp = OPEN_WEATHER_API_DATA["list"][counter]["main"]["temp"]
        tempFeelsLike = OPEN_WEATHER_API_DATA["list"][counter]["main"]["feels_like"]
        conditions = OPEN_WEATHER_API_DATA["list"][counter]["weather"][0]["description"].title()

        if "Rain" in conditions:
            messageBody += f"{time}\nTemperature: {temp} degrees\nFeels like: {tempFeelsLike} degrees\nConditions: {conditions}\n***Dress accordingly!***\n\n"
        else:
            messageBody += f"{time}\nTemperature: {temp} degrees\nFeels like: {tempFeelsLike} degrees\nConditions: {conditions}\n\n"

        counter += 1

weatherReport()

message = CLIENT.messages.create(

    body=messageBody,

    from_=f"whatsapp:{os.environ.get("day_35_twilioNum")}",

    to=f"whatsapp:{os.environ.get("day_35_myNum")}",

)

print(message.status)