import os, sys

os.system("clear")

def art(args):
    if args == 0:
        print(r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")
    elif args == 1:
        print(r"""
   █████████   ██████████   ██████████   █████ ███████████ █████    ███████    ██████   █████
  ███░░░░░███ ░░███░░░░███ ░░███░░░░███ ░░███ ░█░░░███░░░█░░███   ███░░░░░███ ░░██████ ░░███ 
 ░███    ░███  ░███   ░░███ ░███   ░░███ ░███ ░   ░███  ░  ░███  ███     ░░███ ░███░███ ░███ 
 ░███████████  ░███    ░███ ░███    ░███ ░███     ░███     ░███ ░███      ░███ ░███░░███░███ 
 ░███░░░░░███  ░███    ░███ ░███    ░███ ░███     ░███     ░███ ░███      ░███ ░███ ░░██████ 
 ░███    ░███  ░███    ███  ░███    ███  ░███     ░███     ░███ ░░███     ███  ░███  ░░█████ 
 █████   █████ ██████████   ██████████   █████    █████    █████ ░░░███████░   █████  ░░█████
░░░░░   ░░░░░ ░░░░░░░░░░   ░░░░░░░░░░   ░░░░░    ░░░░░    ░░░░░    ░░░░░░░    ░░░░░    ░░░░░ 
""")
    elif args == 2:
        print(r"""
  █████████  █████  █████ ███████████  ███████████ ███████████     █████████     █████████  ███████████ █████    ███████    ██████   █████
 ███░░░░░███░░███  ░░███ ░░███░░░░░███░█░░░███░░░█░░███░░░░░███   ███░░░░░███   ███░░░░░███░█░░░███░░░█░░███   ███░░░░░███ ░░██████ ░░███ 
░███    ░░░  ░███   ░███  ░███    ░███░   ░███  ░  ░███    ░███  ░███    ░███  ███     ░░░ ░   ░███  ░  ░███  ███     ░░███ ░███░███ ░███ 
░░█████████  ░███   ░███  ░██████████     ░███     ░██████████   ░███████████ ░███             ░███     ░███ ░███      ░███ ░███░░███░███ 
 ░░░░░░░░███ ░███   ░███  ░███░░░░░███    ░███     ░███░░░░░███  ░███░░░░░███ ░███             ░███     ░███ ░███      ░███ ░███ ░░██████ 
 ███    ░███ ░███   ░███  ░███    ░███    ░███     ░███    ░███  ░███    ░███ ░░███     ███    ░███     ░███ ░░███     ███  ░███  ░░█████ 
░░█████████  ░░████████   ███████████     █████    █████   █████ █████   █████ ░░█████████     █████    █████ ░░░███████░   █████  ░░█████
 ░░░░░░░░░    ░░░░░░░░   ░░░░░░░░░░░     ░░░░░    ░░░░░   ░░░░░ ░░░░░   ░░░░░   ░░░░░░░░░     ░░░░░    ░░░░░    ░░░░░░░    ░░░░░    ░░░░░ 
""")
    elif args == 3:
        print(r"""
 ██████   ██████ █████  █████ █████       ███████████ █████ ███████████  █████       █████   █████████    █████████   ███████████ █████    ███████    ██████   █████
░░██████ ██████ ░░███  ░░███ ░░███       ░█░░░███░░░█░░███ ░░███░░░░░███░░███       ░░███   ███░░░░░███  ███░░░░░███ ░█░░░███░░░█░░███   ███░░░░░███ ░░██████ ░░███ 
 ░███░█████░███  ░███   ░███  ░███       ░   ░███  ░  ░███  ░███    ░███ ░███        ░███  ███     ░░░  ░███    ░███ ░   ░███  ░  ░███  ███     ░░███ ░███░███ ░███ 
 ░███░░███ ░███  ░███   ░███  ░███           ░███     ░███  ░██████████  ░███        ░███ ░███          ░███████████     ░███     ░███ ░███      ░███ ░███░░███░███ 
 ░███ ░░░  ░███  ░███   ░███  ░███           ░███     ░███  ░███░░░░░░   ░███        ░███ ░███          ░███░░░░░███     ░███     ░███ ░███      ░███ ░███ ░░██████ 
 ░███      ░███  ░███   ░███  ░███      █    ░███     ░███  ░███         ░███      █ ░███ ░░███     ███ ░███    ░███     ░███     ░███ ░░███     ███  ░███  ░░█████ 
 █████     █████ ░░████████   ███████████    █████    █████ █████        ███████████ █████ ░░█████████  █████   █████    █████    █████ ░░░███████░   █████  ░░█████
░░░░░     ░░░░░   ░░░░░░░░   ░░░░░░░░░░░    ░░░░░    ░░░░░ ░░░░░        ░░░░░░░░░░░ ░░░░░   ░░░░░░░░░  ░░░░░   ░░░░░    ░░░░░    ░░░░░    ░░░░░░░    ░░░░░    ░░░░░ 
""")
    elif args == 4:
        print(r"""
 ██████████   █████ █████   █████ █████  █████████  █████    ███████    ██████   █████
░░███░░░░███ ░░███ ░░███   ░░███ ░░███  ███░░░░░███░░███   ███░░░░░███ ░░██████ ░░███ 
 ░███   ░░███ ░███  ░███    ░███  ░███ ░███    ░░░  ░███  ███     ░░███ ░███░███ ░███ 
 ░███    ░███ ░███  ░███    ░███  ░███ ░░█████████  ░███ ░███      ░███ ░███░░███░███ 
 ░███    ░███ ░███  ░░███   ███   ░███  ░░░░░░░░███ ░███ ░███      ░███ ░███ ░░██████ 
 ░███    ███  ░███   ░░░█████░    ░███  ███    ░███ ░███ ░░███     ███  ░███  ░░█████ 
 ██████████   █████    ░░███      █████░░█████████  █████ ░░░███████░   █████  ░░█████
░░░░░░░░░░   ░░░░░      ░░░      ░░░░░  ░░░░░░░░░  ░░░░░    ░░░░░░░    ░░░░░    ░░░░░ 
""")
    elif args == 5:
        print(r"""
 ██████████ █████ █████ ███████████     ███████    ██████   █████ ██████████ ██████   █████ ███████████ █████   █████████   ███████████ █████    ███████    ██████   █████
░░███░░░░░█░░███ ░░███ ░░███░░░░░███  ███░░░░░███ ░░██████ ░░███ ░░███░░░░░█░░██████ ░░███ ░█░░░███░░░█░░███   ███░░░░░███ ░█░░░███░░░█░░███   ███░░░░░███ ░░██████ ░░███ 
 ░███  █ ░  ░░███ ███   ░███    ░███ ███     ░░███ ░███░███ ░███  ░███  █ ░  ░███░███ ░███ ░   ░███  ░  ░███  ░███    ░███ ░   ░███  ░  ░███  ███     ░░███ ░███░███ ░███ 
 ░██████     ░░█████    ░██████████ ░███      ░███ ░███░░███░███  ░██████    ░███░░███░███     ░███     ░███  ░███████████     ░███     ░███ ░███      ░███ ░███░░███░███ 
 ░███░░█      ███░███   ░███░░░░░░  ░███      ░███ ░███ ░░██████  ░███░░█    ░███ ░░██████     ░███     ░███  ░███░░░░░███     ░███     ░███ ░███      ░███ ░███ ░░██████ 
 ░███ ░   █  ███ ░░███  ░███        ░░███     ███  ░███  ░░█████  ░███ ░   █ ░███  ░░█████     ░███     ░███  ░███    ░███     ░███     ░███ ░░███     ███  ░███  ░░█████ 
 ██████████ █████ █████ █████        ░░░███████░   █████  ░░█████ ██████████ █████  ░░█████    █████    █████ █████   █████    █████    █████ ░░░███████░   █████  ░░█████
░░░░░░░░░░ ░░░░░ ░░░░░ ░░░░░           ░░░░░░░    ░░░░░    ░░░░░ ░░░░░░░░░░ ░░░░░    ░░░░░    ░░░░░    ░░░░░ ░░░░░   ░░░░░    ░░░░░    ░░░░░    ░░░░░░░    ░░░░░    ░░░░░ 
""")
    elif args == 6:
        print(r"""
 ███████████     █████████   ██████████   █████   █████████    █████████   ███████████ █████    ███████    ██████   █████
░░███░░░░░███   ███░░░░░███ ░░███░░░░███ ░░███   ███░░░░░███  ███░░░░░███ ░█░░░███░░░█░░███   ███░░░░░███ ░░██████ ░░███ 
 ░███    ░███  ░███    ░███  ░███   ░░███ ░███  ███     ░░░  ░███    ░███ ░   ░███  ░  ░███  ███     ░░███ ░███░███ ░███ 
 ░██████████   ░███████████  ░███    ░███ ░███ ░███          ░███████████     ░███     ░███ ░███      ░███ ░███░░███░███ 
 ░███░░░░░███  ░███░░░░░███  ░███    ░███ ░███ ░███          ░███░░░░░███     ░███     ░███ ░███      ░███ ░███ ░░██████ 
 ░███    ░███  ░███    ░███  ░███    ███  ░███ ░░███     ███ ░███    ░███     ░███     ░███ ░░███     ███  ░███  ░░█████ 
 █████   █████ █████   █████ ██████████   █████ ░░█████████  █████   █████    █████    █████ ░░░███████░   █████  ░░█████
░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░░░░░░   ░░░░░   ░░░░░░░░░  ░░░░░   ░░░░░    ░░░░░    ░░░░░    ░░░░░░░    ░░░░░    ░░░░░ 
""")

def numberEntry1():
    entry = float(input("Enter the first number:\n"))
    return entry

def numberEntry2():
    entry = float(input("Enter the second number:\n"))
    return entry

def add(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def exponentialPower(n1, n2):
    return pow(n1, n2)

def exponentialRoot(n1, n2):
    return n1 ** (1/n2)

mathDict = {
    1: add,
    2: subtraction,
    3: multiplication,
    4: division,
    5: exponentialPower,
    6: exponentialRoot,
}

placeholderValue = 0
answer = ""
while True:
    art(0)
    print("""
Available operations:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Raise a number to a power. 
6. Find the nth root of a number. 
""")

    operationChoice = int(input("\nEnter a number (1 through 6) to select an operation or enter 0 to quit the program:\n"))
    art(operationChoice)

    if operationChoice not in range(1,7):
        print("Invalid entry! Only enter a number from 1 through 6 to select an operation.")
        continue

    if answer == "y":
        choice1 = placeholderValue
        print(f"\nRemember that you're working with currently working with {choice1}!")
    elif answer == "n":
        choice1 = numberEntry1()
    else:
        choice1 = numberEntry1()
    choice2 = numberEntry2()

    if operationChoice == 1:
        sum = mathDict[1](choice1, choice2)
        placeholderValue = sum
        print(f"{choice1} + {choice2} = {sum}")
    elif operationChoice == 2:
        difference = mathDict[2](choice1, choice2)
        placeholderValue = difference
        print(f"{choice1} - {choice2} = {difference}")
    elif operationChoice == 3:
        product = mathDict[3](choice1, choice2)
        placeholderValue = product
        print(f"{choice1} * {choice2} = {product}")
    elif operationChoice == 4:
        if choice2 == 0:
            print("\nDivide by zero error! Make sure the divisor is NOT zero!")
            print("Try again!")
            continue
        quotient = mathDict[4](choice1, choice2)
        placeholderValue = quotient
        print(f"{choice1} / {choice2} = {quotient}")
    elif operationChoice == 5:
        result = mathDict[5](choice1, choice2)
        placeholderValue = result
        print(f"{choice1} raised to the power of {choice2} equals {result}")
    elif operationChoice == 6:
        if choice1 < 0:
            print(f"Evaluating the nth root of a negative number is not supported by this calculator.")
            print(f"Try again!")
            continue
        result = mathDict[6](choice1,int(choice2))
        placeholderValue = result
        if str(choice2)[-3] == "1":
            print(f"The {str(choice2)[0:-2]}st root of {choice1} equals {result}")
        elif str(choice2)[-3] == "2":
            print(f"The {str(choice2)[0:-2]}nd root of {choice1} equals {result}")
        elif str(choice2)[-3] == "3":
            print(f"The {str(choice2)[0:-2]}rd root of {choice1} equals {result}")
        elif str(choice2)[-3] in ["4", "5", "6", "7", "8", "9", "0"]:
            print(f"The {str(choice2)[0:-2]}th root of {choice1} equals {result}")
    elif operationChoice == 0:
        print("Have a good one!")
        sys.exit()

    while True:
        try:
            question = input(f"\nEnter Y to continue calculating with {placeholderValue}, enter N to begin a new calculation, or enter 0 to quit the program:\n").lower().strip()
            if question == "y":
                answer = "y"
                break
            elif question == "n":
                answer = "n"
                break
            elif question == "0":
                print("Have a good one!")
                sys.exit()
            else:
                print("Invalid entry! Only enter y or n!")
        except ValueError:
            print("Try again!")