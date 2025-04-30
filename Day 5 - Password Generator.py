import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letterLength = len(letters)
numbersLength = len(numbers)
symbolsLength = len(symbols)
passwordPrelim = []
passwordFinal = ""

print("Welcome to the PyPassword Generator!")

while True:
    try:
        nrLetters = int(input("How many letters would you like in your password?\n"))
        if nrLetters > letterLength:
            print(f"Invalid entry! You entered in {nrLetters} and there are only {letterLength} available letters to be used by this generator.")
            continue
        else:
            break
    except ValueError:
        print("Try again!")

while True:
    try:
        nrSymbols = int(input(f"How many symbols would you like?\n"))
        if nrSymbols > symbolsLength:
            print(f"Invalid entry! You entered in {nrSymbols} and there are only {symbolsLength} available symbols to be used by this generator.")
            continue
        else:
            break
    except ValueError:
        print("Try again!")

while True:
    try:
        nrNumbers = int(input(f"How many numbers would you like?\n"))
        if nrNumbers > numbersLength:
            print(f"Invalid entry! You entered in {nrNumbers} and there are only {numbersLength} available numbers to be used by this generator.")
            continue
        else:
            break
    except ValueError:
        print("Try again!")

for value in range(nrLetters):
    passwordPrelim.append(letters[random.randint(0, letterLength - 1)])
for value in range(nrSymbols):
    passwordPrelim.append(symbols[random.randint(0, symbolsLength - 1)])
for value in range(nrNumbers):
    passwordPrelim.append(numbers[random.randint(0, numbersLength - 1)])
random.shuffle(passwordPrelim)

for value in passwordPrelim:
    passwordFinal += value

print(f"Your generated password is: {passwordFinal}")
