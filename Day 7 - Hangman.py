import random

wordList = [
    # Easy
    "cat", "dog", "sun", "fish", "tree", "book", "ball", "hand", "jump", "love",
    # Medium
    "banana", "guitar", "rocket", "dragon", "planet", "monkey", "orange", "turtle", "castle", "spider",
    # Hard
    "elephant", "kangaroo", "helicopter", "watermelon", "chameleon", "xylophone", "quarantine", "extravaganza",
    # Bonus
    "giraffe", "penguin", "pizza", "unicorn", "microscope"
]

print(r"""

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

""")

chosenWord = random.choice(wordList)
placeholder = ""

def artHangman(arg):
    if arg == 6:
        print(r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""")

    if arg == 5:
        print(r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""")

    if arg == 4:
        print(r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""")

    if arg == 3:
        print(r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""")

    if arg == 2:
        print(r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""")

    if arg == 1:
        print(r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""")

    if arg == 0:
        print(r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""")

for i in chosenWord:
    placeholder += "_"
print(placeholder)

correctLetters = []
incorrectGuesses = []
attempts = 6
while True:
    artHangman(attempts)
    userGuess = input("\nGuess a letter:\n").lower()
    display = ""

    for i in chosenWord:
        if userGuess == i:
            display += userGuess
            correctLetters.append(userGuess)
        elif i in correctLetters:
            display += i
        else:
            display += "_"
    print()
    print(display)

    if userGuess in incorrectGuesses:
        print(f"You have already guessed {userGuess}!")

    if userGuess not in chosenWord and userGuess not in incorrectGuesses:
        attempts -= 1
        incorrectGuesses.append(userGuess)
        print(f"You guessed \"{userGuess}\". That's not in the word.")
        print(f"**************** YOU HAVE {attempts} ATTEMPTS REMAINING! ****************")

    if "_" not in display:
        print("**************** YOU WIN!!!!!!!!!!!! ****************")
        break

    if attempts == 0:
        print("**************** YOU LOSE!!!!!!!!!!!! ****************")
        print(f"The word was {chosenWord}.")
        break