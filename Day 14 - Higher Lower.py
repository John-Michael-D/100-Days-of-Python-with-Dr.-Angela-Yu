import HigherLowerGameData, HigherLowerArt, random, os

score = 0
previousAnswer = []

def gameLoop():
    global score

    while True:
        os.system("clear")
        print(HigherLowerArt.logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")

        def comparison1():

            randomSelection1 = random.randint(0, 49)
            selectionName = HigherLowerGameData.data[randomSelection1]["name"]
            selectionDescription = HigherLowerGameData.data[randomSelection1]["description"]
            selectionCountry = HigherLowerGameData.data[randomSelection1]["country"]
            selectionFollowers = HigherLowerGameData.data[randomSelection1]["follower_count"]
            string = f"{selectionName}, a(n) {selectionDescription}, from {selectionCountry}."

            return [string, selectionFollowers]

        if len(previousAnswer) == 2:
            comparison1Var = previousAnswer
        else:
            comparison1Var = comparison1()

        print(f"\nCompare A: {comparison1Var[0]}")

        def comparison2():

            while True:
                randomSelection2 = random.randint(0,49)
                selectionName = HigherLowerGameData.data[randomSelection2]["name"]
                selectionDescription = HigherLowerGameData.data[randomSelection2]["description"]
                selectionCountry = HigherLowerGameData.data[randomSelection2]["country"]
                selectionFollowers = HigherLowerGameData.data[randomSelection2]["follower_count"]
                string = f"{selectionName}, a(n) {selectionDescription}, from {selectionCountry}."

                if string == comparison1Var[0]:
                    pass
                else:
                    return [string, selectionFollowers]

        print(HigherLowerArt.vs)
        comparison2Var = comparison2()
        print(f"\nAgainst B: {comparison2Var[0]}")

        def userAnswer():
            global score

            while True:
                try:
                    question = input("\nWho has more followers on Instagram? Enter A or B:\n>").strip().lower()

                    if question == "a" and comparison1Var[1] > comparison2Var[1]:
                        score += 1
                        return True
                    elif question == "a" and comparison1Var[1] < comparison2Var[1]:
                        return False
                    elif question == "b" and comparison2Var[1] > comparison1Var[1]:
                        score += 1
                        return True
                    elif question == "b" and comparison2Var[1] < comparison1Var[1]:
                        return False
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid entry! Enter only A or B!")

        response = userAnswer()

        def gameRestart():
            os.system("clear")
            print(HigherLowerArt.logo)
            print(f"Sorry that's wrong. Final score: {score}.")

            while True:
                try:
                    question = input("Would you like to restart the game? Y or N?\n>").strip().lower()
                    if question == "y":
                        return True
                    elif question == "n":
                        return False
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid entry! Enter only Y or N!")

        if response == True:
            previousAnswer.clear()
            previousAnswer.append(comparison2Var[0])
            previousAnswer.append(comparison2Var[1])
        elif response == False:
            restart = gameRestart()
            if restart == True:
                previousAnswer.clear()
                score -= score
                os.system("clear")
                continue
            elif restart == False:
                print("Have a good one!")
                break

gameLoop()