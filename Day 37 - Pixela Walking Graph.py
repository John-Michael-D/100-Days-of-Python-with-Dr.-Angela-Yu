import requests
from datetime import *

authentication = input("Please enter your password.\n>")
print("Here's the link to your graph! https://pixe.la/v1/users/jmd1999/graphs/graph0.html")

TOKEN = authentication
USERNAME = "jmd1999"

pixelaEndpoint = "https://pixe.la/v1/users"
pixelaParams = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#pixelaResponse = requests.post(url=pixelaEndpoint, json=pixelaParams)
#print(pixelaResponse.text)

graphEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs"
graphConfig = {
    "id" : "graph0",
    "name" : "Walking Graph",
    "unit" : "Minutes",
    "type" : "int",
    "color" : "sora"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
#graphResponse = requests.post(url=graphEndpoint, json=graphConfig, headers=headers)
#print(graphResponse.text)

#All of the above code just initializes the user account and their graph.
while True:
    choiceDate = input("\nEnter the date in yyyyMMdd format that would like to input information for. "
                       "Type 'today' if you want to input information for the current day.\n>").strip().lower()
    if choiceDate == "today":
        currentDate = str(datetime.now()).split(" ")[0].split("-")
        currentDateFormatted = f"{currentDate[0]}{currentDate[1]}{currentDate[2]}"
        choiceDate = currentDateFormatted


    graphPixelEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs/{graphConfig['id']}/{choiceDate}"
    graphPixelConfig = {
        "quantity" : input(f"\nEnter how many minutes you walked during {choiceDate}.\n>")
    }

    graphPixelResponse = requests.put(url=graphPixelEndpoint, json=graphPixelConfig, headers=headers)
    print("\n", graphPixelResponse.text)
