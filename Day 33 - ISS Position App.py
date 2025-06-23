import requests, smtplib, time
from datetime import datetime

MY_LAT = 31.457581 # Your latitude
MY_LONG = -109.593224 # Your longitude
MY_EMAIL = "gordon.freeman.MIT1999@gmail.com"
MY_PASSWORD = "Password123"

#Your position is within +5 or -5 degrees of the ISS position.
def positionCheck():
    responseISS = requests.get(url="http://api.open-notify.org/iss-now.json")
    responseISS.raise_for_status()
    dataISS = responseISS.json()

    issLatitude = float(dataISS["iss_position"]["latitude"])
    issLongitude = float(dataISS["iss_position"]["longitude"])

    print(f"\nThe current time is {hourMinFormatted}")
    print(f"Sunrise for Charlotte Douglas International Airport occurs at {sunriseFormatted}")
    print(f"Sunset for Charlotte Douglas International Airport occurs at {sunsetFormatted}")
    print(f"\nLatitude and longitude of Charlotte Douglas International Airport: {MY_LAT} and {MY_LONG}")
    print(f"Current ISS latitude and longitude: {issLatitude} and {issLongitude}")
    if issLatitude == (MY_LAT + 5) or issLatitude == (MY_LAT - 5):
        if issLongitude == (MY_LONG + 5) or issLongitude == (MY_LONG - 5):
            print(f"\nThe ISS is near Charlotte Douglas International Airport!")
            return True
    print(f"\nThe ISS is NOT near Charlotte Douglas International Airport!")
    return None

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "America/New_York"
}

responseSun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
responseSun.raise_for_status()
dataSun = responseSun.json()
sunrise = dataSun["results"]["sunrise"].split("T")[1].split("-")[0].split(":")[0:2]
sunset = dataSun["results"]["sunset"].split("T")[1].split("-")[0].split(":")[0:2]
sunriseFormatted = f"{sunrise[0]}:{sunrise[1]}"
sunsetFormatted = f"{sunset[0]}:{sunset[1]}"

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    currentTime = datetime.now()
    currentHour = str(currentTime).split(" ")[1].split(":")[0]
    currentMin = str(currentTime).split(" ")[1].split(":")[1]
    hourMinFormatted = f"{currentHour}:{currentMin}"
    isNear = positionCheck()
    if isNear:
        if hourMinFormatted == sunsetFormatted:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                to_addrs="JohnSmith@cia.gov",
                msg=f"Subject:Look up!!!\n\nThe ISS is overhead!")
                connection.close()