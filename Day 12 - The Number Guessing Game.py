import random, sys, os, GuessingGameArt
global chancesLeft

def gameLoop():
    """This function contains all the other functions necessary for the game."""

    while True:
        os.system("clear")
        print(GuessingGameArt.welcomeMessage)
        print(f"Welcome to the game!")
        def randomNumberGenerator():
            """This function generates a random number the user is supposed to guess."""

            randomNum = random.randint(1,100)
            print("I'm thinking of a number between 1 and 100.")
            return randomNum

        numberToGuess = randomNumberGenerator()

        def chances():
            """This function prompts the user to choose the game mode and returns the number of chances to guess the number."""

            while True:
                try:
                    question = input("Enter A to choose Easy Mode or enter B to choose Hard Mode:\n>").strip().lower()
                    if question == "a":
                        print("You have 10 chances to guess the number.")
                        chances = 10
                        return chances
                    elif question == "b":
                        print(f"You have 5 chances to guess the number.")
                        chances = 5
                        return chances
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid entry! Enter only A or B!")

        chancesLeft = chances()

        def guessing():
            """This function prompts the user to guess a number."""

            chances = chancesLeft
            while True:
                try:
                    guess = int(input("Guess a number:\n>"))
                    if guess != numberToGuess:
                        chances -= 1
                        if chances == 0:
                            print(GuessingGameArt.gameOver)
                            print(f"The number was {numberToGuess}!")
                            break
                        elif guess > numberToGuess:
                            print(GuessingGameArt.tooHigh)
                            print(f"You have {chances} remaining attempts to guess the number.")
                            continue
                        elif guess < numberToGuess:
                            print(GuessingGameArt.tooLow)
                            print(f"You have {chances} remaining attempts to guess the number.")
                            continue
                    elif guess == numberToGuess:
                        print(GuessingGameArt.victory)
                        print(f"You guessed correctly!")
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid entry! Only enter valid integer values.")

        guessing()

        def restartGame():
            """This function will allow the user to restart the game and play again if they so desire."""

            while True:
                try:
                    question = input("Would you like to restart the game? Enter Y for yes and N for no:\n>").strip().lower()

                    if question == "y":
                        return "y"
                    elif question == "n":
                        return "n"
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid entry! Only enter Y or N!")

        choice = restartGame()

        if choice == "y":
            continue
        elif choice == "n":
            print(f"Have a good one!")
            sys.exit()

gameLoop()
