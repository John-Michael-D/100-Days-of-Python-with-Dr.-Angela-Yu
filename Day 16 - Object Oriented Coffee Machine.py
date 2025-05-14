from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMenu = Menu()
coffeeMachine = CoffeeMaker()
coffeeCoins = MoneyMachine()

while True:
    question = input(f"What would you like? {coffeeMenu.get_items()}/\n>").strip().lower()

    if question == "report":
        coffeeMachine.report()
        coffeeCoins.report()
    elif question == "off":
        break
    else:
        userChoice = coffeeMenu.find_drink(question)
        resourceCheck = coffeeMachine.is_resource_sufficient(userChoice)

        if resourceCheck == True:
            inputCoins = coffeeCoins.make_payment(userChoice.cost)
            if inputCoins == True:
                coffeeMachine.make_coffee(userChoice)