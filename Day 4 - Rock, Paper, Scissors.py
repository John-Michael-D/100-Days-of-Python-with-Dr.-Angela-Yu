import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

artList = [rock, paper, scissors]

userInput = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
computerInput = random.randint(0,2)


if userInput >= 3 or userInput < 0:
    print("You typed an invalid number!")
elif userInput == computerInput:
    print(artList[userInput])
    print("Computer chose:")
    print(artList[computerInput])
    print("It's a draw!")
elif userInput == 0 and computerInput == 1:
    print(artList[userInput])
    print("Computer chose:")
    print(artList[computerInput])
    print("You lose!")
elif userInput == 0 and computerInput == 2:
    print(artList[userInput])
    print("Computer chose:")
    print(artList[computerInput])
    print("You win!")
elif userInput == 1 and computerInput == 0:
    print(artList[userInput])
    print("Computer chose:")
    print(artList[computerInput])
    print("You win!")
elif userInput == 1 and computerInput == 2:
    print(artList[userInput])
    print("Computer chose:")
    print(artList[computerInput])
    print("You lose!")
elif userInput == 2 and computerInput == 0:
    print(artList[userInput])
    print("Computer chose:")
    print(artList[computerInput])
    print("You lose!")
elif userInput == 2 and computerInput == 1:
    print(artList[userInput])
    print("Computer chose:")
    print(artList[computerInput])
    print("You win!")