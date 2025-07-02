import requests, os
from datetime import *
from requests.auth import HTTPBasicAuth

os.system("clear")

NUTRIONIX_API_ID = os.environ["DAY_38_NUTRIONIX_ID"]
NUTRIONIX_API_KEY = os.environ["DAY_38_NUTRIONIX_API_KEY"]
SHEETY_PASSWORD = os.environ["DAY_38_SHEETY_PASSWORD"]

todayDate = datetime.now().strftime("%d/%m/%Y")
nowTime = datetime.now().strftime("%X")

nutrionixConfig = {
    "url" : "https://trackapi.nutritionix.com/v2/natural/exercise",
    "headers" : {
        "Content-Type" : "application/json",
        "x-app-id" : NUTRIONIX_API_ID,
        "x-app-key" : NUTRIONIX_API_KEY
    },
    "body" : {
        "query" : input("What did you do for exercise today?\n>")
    }
}

nutrionixResponse = requests.post(url=nutrionixConfig["url"], json=nutrionixConfig["body"], headers=nutrionixConfig["headers"])
nutrionixResponse.raise_for_status()
nutrionixJSON = nutrionixResponse.json()

headers = {"Authorization" : f"Basic {SHEETY_PASSWORD}"}

for i in nutrionixJSON["exercises"]:
    sheetInputs = {
        "date" : todayDate,
        "time" : nowTime,
        "exercise" : str(i["user_input"]).title(),
        "duration" : i["duration_min"],
        "calories" : i["nf_calories"],
    }
    sheetyConfig = {
        "url": "https://api.sheety.co/a784f4b5f6bd284b401909679f7cb987/myWorkouts/sheet1",
    }
    sheetyResponse = requests.post(url=sheetyConfig["url"], json={"sheet1": sheetInputs}, headers=headers)
    sheetyResponse.raise_for_status()
    sheetyJSON = sheetyResponse.json()
    print(f"\nYou {i['user_input']} for {i['duration_min']} minutes and burned {i['nf_calories']} calories!")
