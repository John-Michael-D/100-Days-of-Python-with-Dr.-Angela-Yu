import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}

def mainLoop():
    """This is the main function containing the other functions for the coffee machine."""

    def deactivateMachine():
        """This function will allow the user to turn off the coffee machine."""

        sys.exit()

    def resourceReport():
        """This function provides a report of the machine's resources."""

        waterAmount = resources["water"]
        milkAmount = resources["milk"]
        coffeeAmount = resources["coffee"]
        moneyAmount = resources["money"]

        print(f"Water: {waterAmount}ml")
        print(f"Milk: {milkAmount}ml")
        print(f"Coffee: {coffeeAmount}g")
        print(f"Money: ${moneyAmount:.2f}")

    def coffeeOrder(order):
        """This function will process the user's order and check the order against the machine's resources."""

        if order == "espresso":
            if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                return True
            elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                print("Sorry, there's not enough water in the machine.")
                return False
            elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                print("Sorry, there's not enough coffee in the machine.")
                return False

        elif order == "latte":
            if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                return True
            elif resources["water"] < MENU["latte"]["ingredients"]["water"]:
                print("Sorry, there's not enough water in the machine.")
                return False
            elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
                print("Sorry, there's not enough milk in the machine.")
                return False
            elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
                print("Sorry, there's not enough coffee in the machine.")
                return False

        elif order == "cappuccino":
            if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                return True
            elif resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
                print("Sorry, there's not enough water in the machine.")
                return False
            elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
                print("Sorry, there's not enough milk in the machine.")
                return False
            elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
                print("Sorry, there's not enough coffee in the machine.")
                return False

    def coinProccess(order):
        """This function processes the coins input to the machine, checks it against the cost of the order, and returns change if needed."""

        totalInput = 0.00

        print("Please insert coins.")

        while True:
            try:
                amountQuarters = int(input("How many quarters?\n>"))
                if amountQuarters >= 0:
                    totalInput += amountQuarters * 0.25
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid entry. Try again!")

        while True:
            try:
                amountDimes = int(input("How many dimes?\n>"))
                if amountDimes >= 0:
                    totalInput += amountDimes * 0.10
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid entry. Try again!")

        while True:
            try:
                amountNickels = int(input("How many nickels?\n>"))
                if amountNickels >= 0:
                    totalInput += amountNickels * 0.05
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid entry. Try again!")

        while True:
            try:
                amountPennies = int(input("How many pennies?\n>"))
                if amountPennies >= 0:
                    totalInput += amountPennies * 0.05
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid entry. Try again!")

        if totalInput == MENU[order]["cost"]:
            resources["money"] += totalInput
            return True
        elif totalInput > MENU[order]["cost"]:
            totalChange = totalInput - MENU[order]["cost"]
            totalInput = totalInput - totalChange
            resources["money"] += totalInput
            print(f"Your change is: ${totalChange:.2f}")
            return True
        else:
            print(f"Sorry, that's not enough money. Input coins refunded.")
            return False

    while True:
        try:
            question = input("What would you like? (espresso/latte/cappuccino):\n>").strip().lower()

            if question == "off":
                deactivateMachine()
            elif question == "report":
                resourceReport()
            elif question in ["espresso", "latte", "cappuccino"]:
                result1 = coffeeOrder(question)
                if result1 == True:
                    result2 = coinProccess(question)
                    if result2 == True:
                        print(f"Here's your {question}. Enjoy!")
            else:
                raise ValueError
        except ValueError:
            print("Invalid entry.")

mainLoop()