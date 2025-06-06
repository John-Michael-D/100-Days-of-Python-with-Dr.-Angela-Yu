import os, sys, random

os.system("clear")

deck = {
    "Ace of Spades": 4,
    "2 of Clubs": 1,
    "2 of Diamonds": 1,
    "2 of Hearts": 1,
    "2 of Spades": 1,
    "3 of Clubs": 1,
    "3 of Diamonds": 1,
    "3 of Hearts": 1,
    "3 of Spades": 1,
    "4 of Clubs": 1,
    "4 of Diamonds": 1,
    "4 of Hearts": 1,
    "4 of Spades": 1,
    "5 of Clubs": 1,
    "5 of Diamonds": 1,
    "5 of Hearts": 1,
    "5 of Spades": 1,
    "6 of Clubs": 1,
    "6 of Diamonds": 1,
    "6 of Hearts": 1,
    "6 of Spades": 1,
    "7 of Clubs": 1,
    "7 of Diamonds": 1,
    "7 of Hearts": 1,
    "7 of Spades": 1,
    "8 of Clubs": 1,
    "8 of Diamonds": 1,
    "8 of Hearts": 1,
    "8 of Spades": 1,
    "9 of Clubs": 1,
    "9 of Diamonds": 1,
    "9 of Hearts": 1,
    "9 of Spades": 1,
    "10 of Clubs": 1,
    "10 of Diamonds": 1,
    "10 of Hearts": 1,
    "10 of Spades": 1,
    "Jack": 4,
    "Queen": 4,
    "King": 4
}
deckArtList = list(deck)
currentPlayerHand = []
currentDealerHand = []
valuePlayerHand = 0
valueDealerHand = 0
betAmount = 0
winAmount = 0
lossAmount = 0
gameWins = 0
gameLoss = 0
gameDraw = 0

def art(args=0):
    art = [r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⡟⣼⣆⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡿⣰⣿⣿⡄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⢡⣭⣭⣭⣭⡀⠸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⠿⠋⠸⢿⣿⣿⡿⠷⠀⠹⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠟⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠛⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡿⢛⣭⣭⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡁⠉⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣾⣿⡿⠃⣠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⢟⣤⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠟⠁⠛⠛⠛⠋⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠈⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣤⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠋⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣦⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡿⢛⣭⣭⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡇⠉⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣶⣿⡿⠃⣠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⢟⣡⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠁⠛⠛⠛⠋⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⢿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⠾⠻⠿⠿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣯⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣷⣄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡿⢛⣭⣭⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡇⠉⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣶⣿⡿⠃⣠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⢟⣡⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠁⠛⠛⠛⠋⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⡶⠏
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡿⢛⣭⣭⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡁⠉⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣾⣿⡿⠃⣠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⢟⣤⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠟⠁⠛⠛⠛⠋⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠟⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠛⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢛⣭⣭⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣧⣀⣿⣿⣿⠀⣸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⡁⠾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠟⠛⣿⣿⣿⡄⠸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣆⠰⢿⡿⠟⢁⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠈⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣤⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠋⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣦⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢟⣭⣭⣍⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣧⣀⣿⣿⣿⠀⣸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⡁⠶⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠛⣿⣿⣿⡆⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣇⠰⢿⡿⠿⢁⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⢿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⠾⠻⠿⠿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣯⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣷⣄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢟⣭⣭⣍⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣧⣀⣿⣿⣿⠀⣸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⡁⠶⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠛⣿⣿⣿⡆⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣇⠰⢿⡿⠿⢁⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⡶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢛⣭⣭⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣧⣀⣿⣿⣿⠀⣸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⡁⠾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠟⠛⣿⣿⣿⡄⠸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣆⠰⢿⡿⠟⢁⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠟⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠛⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢹⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡟⣱⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢏⣼⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡃⠛⠛⠛⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠈⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣤⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠋⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣦⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢹⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣡⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢏⣼⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡃⠚⠛⠛⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⢿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⠾⠻⠿⠿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣯⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣷⣄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢹⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣡⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢏⣼⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡃⠚⠛⠛⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⡶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢹⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡟⣱⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢏⣼⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡃⠛⠛⠛⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠟⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠛⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⠉⡙⠛⢛⣩⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⣠⣶⣶⣤⠉⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠛⣿⣿⣿⠆⢈⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣆⠰⠿⠿⠟⣠⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠈⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣤⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠋⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣦⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⠉⣙⠛⢛⣫⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⣠⣶⣶⣦⠉⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠛⣿⣿⣿⡇⢈⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣧⡰⠿⠿⠟⣀⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡿⠙⢿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⡿⠏⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⠾⠻⠿⠿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣯⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣷⣄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⠉⣙⠛⢛⣫⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⣠⣶⣶⣦⠉⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠛⣿⣿⣿⡇⢈⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣧⡰⠿⠿⠟⣀⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⡶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⠉⡙⠛⢛⣩⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⣠⣶⣶⣤⠉⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠛⣿⣿⣿⠆⢈⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣆⠰⠿⠿⠟⣠⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠟⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠛⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⡿⢛⣭⣭⠙⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⢠⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠁⠸⣫⣥⣌⠉⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡄⢰⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣷⣌⠻⢿⠿⢃⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠈⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣤⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠋⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣦⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⡿⢛⣭⣭⠙⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿⣿⣦⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠁⠸⣫⣭⣬⠉⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡄⢰⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣷⣄⠻⢿⠿⢃⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⢿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⠾⠻⠿⠿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣯⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣷⣄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⡿⢛⣩⣭⠙⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿⣿⣦⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠁⠸⣫⣭⣬⠉⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡄⢰⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣷⣄⠻⢿⠿⢃⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⡶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⡿⢛⣭⣭⠙⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⢠⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠁⠸⣫⣥⣌⠉⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡄⢰⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣷⣌⠻⢿⠿⢃⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠟⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠛⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠉⣉⣉⣉⡉⢩⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⡿⢡⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠈⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣤⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠋⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣦⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠉⣉⣉⣉⡉⢩⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣇⣾⣿⣿⣿⢣⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⢿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⠾⠻⠿⠿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣯⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣷⣄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠉⣉⣉⣉⡉⢩⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣇⣾⣿⣿⣿⢣⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⡶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠉⣉⣉⣉⡉⢩⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⡿⢡⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠟⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠛⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢟⣩⣭⣍⡛⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡇⠸⢿⣿⣿⠇⣸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⡦⢀⡈⠁⠚⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠋⣴⣿⣿⣷⣦⠈⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣆⡙⠿⠿⠿⢟⣴⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠈⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣤⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠋⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣦⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⠟⣩⣭⣭⡛⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡇⠘⢿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⡦⢀⡈⠁⠚⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠋⣰⣿⣿⣷⣦⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣦⡙⠿⠿⠿⢟⣴⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⡿⠙⢿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⠾⠻⠿⠿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣯⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣷⣄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⠟⣩⣭⣭⡛⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡇⠘⢿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⡦⢀⡈⠁⠚⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠋⣰⣿⣿⣷⣦⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣦⡙⠿⠿⠿⢟⣴⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⡶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⢟⣩⣭⣍⡛⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡇⠸⢿⣿⣿⠇⣸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⡦⢀⡈⠁⠚⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠋⣴⣿⣿⣷⣦⠈⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣆⡙⠿⠿⠿⢟⣴⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠟⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠛⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⠟⣩⣭⣝⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠃⢸⣿⣿⣿⡆⠹⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣄⠘⢿⣿⠿⡁⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⠇⢰⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣇⠀⠿⠿⢏⣠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠈⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣤⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠋⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣦⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⠟⣩⣭⣝⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠃⢰⣿⣿⣿⡇⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣆⠈⠿⣿⠿⡁⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⡇⢠⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣏⠀⠿⠿⢟⣠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⢿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⠾⠻⠿⠿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣯⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣷⣄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⠟⣩⣭⣝⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠃⢰⣿⣿⣿⡇⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣆⠈⠿⣿⠿⡁⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⡇⢠⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣏⠀⠿⠿⢟⣠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⡶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⠟⣩⣭⣝⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠃⢸⣿⣿⣿⡆⠹⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣄⠘⢿⣿⠿⡁⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⠇⢰⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣇⠀⠿⠿⢏⣠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠟⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠛⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⠟⠛⠋⢻⣿⣿⣿⣿⠛⣩⣭⡍⠻⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⠇⢰⣿⣿⣿⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⠀⢸⣿⣿⣿⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⡀⢸⣿⣿⣿⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⡿⠿⠀⠸⠿⣿⣿⣧⡈⠿⠿⠟⣠⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠈⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣤⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠋⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣦⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⠟⠛⠋⢻⣿⣿⣿⣿⠟⣩⣭⣍⠻⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡆⢸⣿⣿⣿⡇⢰⣿⣿⣿⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠀⢸⣿⣿⣿⡇⢸⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡄⢸⣿⣿⣿⠃⢸⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⡿⠿⠃⠸⠿⣿⣿⣷⡀⠿⠿⠟⣠⣾⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⢿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⠾⠻⠿⠿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣯⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣷⣄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⠟⠛⠋⢻⣿⣿⣿⣿⠟⣩⣭⣍⠻⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡆⢸⣿⣿⣿⡇⢰⣿⣿⣿⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠀⢸⣿⣿⣿⡇⢸⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡄⢸⣿⣿⣿⠃⢸⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⡿⠿⠃⠸⠿⣿⣿⣷⡀⠿⠿⠟⣠⣾⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⡶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⠟⠛⠋⢻⣿⣿⣿⣿⠛⣩⣭⡍⠻⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⠇⢰⣿⣿⣿⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⠀⢸⣿⣿⣿⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⡀⢸⣿⣿⣿⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⡿⠿⠀⠸⠿⣿⣿⣧⡈⠿⠿⠟⣠⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠟⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠛⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣷⣀⢀⠀⡀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⠀⢰⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠉⠉⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡰⠾⠿⠟⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠈⠀⠁⠉⢿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣤⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⠾⠻⠿⠿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣯⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣷⣄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡿⠋⣡⣶⣶⣶⣌⠙⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⠁⢸⣿⣿⣿⣿⣿⡆⠈⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡀⠸⡟⣩⣭⡙⢿⠇⢀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣷⣄⠀⠿⠿⠿⠀⢠⣾⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⠀⠘⠿⣿⡿⢿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡴⠋⠀⠀⠙⢿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣶⣶⣦⡶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⡿⠃⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
⣿⠋⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣦⡀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣷⣶⠀⢰⣶⣿⣷⠆⣠⣴⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠀⢸⣿⡟⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠀⠸⣫⡄⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣆⠈⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⡿⠿⠀⠸⠿⣿⡿⠧⠀⠙⠿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⢿⣿⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""]

    logo = r"""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """

    bet = r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣦⣤⣤⣤⣿⣿⣶⣤⣤⣶⣿⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠧⣜⢿⣿⠉⢻⣿⢿⣿⣿⡇⢠⣭⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢿⣿⡄⣺⣿⣤⣿⣿⣿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⣛⣿⣿⣾⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣟⣿⣿⣟⣻⣿⣿⣾⣿⣿⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⢿⠿⠟⠿⣿⢿⡉⠉⢽⡗⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⠋⢉⠟⠀⠀⠀⠀⠀⠈⠀⠙⢄⠀⠉⢿⣇⠏⡵⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⣿⣦⠖⠀⠀⠀⠀⠀⢰⣶⣤⡄⠀⠀⠀⠀⠀⠀⠉⠺⢷⠎⣸⣻⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣾⣷⣿⡟⠁⠀⢀⣴⣾⣯⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡡⢊⡼⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⢏⢗⢸⠟⠃⠀⠀⢠⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠸⡗⣩⠞⡔⣹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠞⣷⢸⡸⠈⠀⠀⠀⠀⢸⣿⣿⡏⠀⣸⣿⣿⡏⠙⢿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠨⠵⣪⠜⡡⣻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡾⢡⣶⡟⠋⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣶⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⣡⢞⡕⢡⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡞⠀⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡵⢋⠔⡿⢡⣿⡀⠀⠀⠀⠀⠀⠀⠀
⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣣⠞⣴⣻⣿⡇⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣴⣧⡀⠀⣿⣿⣿⠀⠹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⣡⣾⢟⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⣤⣿⣿⣿⣀⣠⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣬⣾⢟⣵⣿⡿⣻⡇⠀⠀⠀⠀⠀⠀⠀
⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢞⣥⣿⣿⢟⡕⣹⠁⠀⠀⠀⠀⠀⠀⠀
⠈⣆⢻⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣿⣿⣿⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢟⡻⢟⣽⡿⣋⢴⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⡌⢿⣧⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣇⡠⠊⡠⢊⠔⡻⢫⠞⣡⣿⣤⣤⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠹⣄⠛⣷⣷⣤⣄⠀⠀⠀⠀⠀⢀⣄⡴⣢⢖⡰⢂⠔⣠⠖⣰⣦⢆⣴⣲⣿⢞⣶⠞⡴⢡⢞⠔⣡⣏⣾⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄
⠀⠀⠀⠈⠳⣌⠙⢿⣿⢸⣿⣷⣶⣿⣿⡾⡿⣵⢋⠔⠵⢊⡵⢮⠟⡵⣯⢞⡵⣣⡿⢃⠞⡴⡱⢋⣾⣟⣯⣭⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿
⠀⠀⠀⠀⠀⠿⢷⣦⣭⣭⣭⣥⣭⣤⣤⣤⣤⣤⣤⣤⣶⣞⡒⠒⠲⠃⠌⣹⢿⡿⣷⣣⣞⣴⣟⣛⣒⣺⣿⣿⣿⣟⣷⣶⣶⠦⠤⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠹⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣤⣼⣿⡟⠛⠛⠳⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⡭⠿⠿⢿⣿⣶⣶⣞⣃⣀⣀⣀⡚⠛⠛⠛⠉⠉⠉⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    for i in range(len(deckArtList)):
        if deckArtList[i] in currentPlayerHand and args == 1:
            print(art[i] * currentPlayerHand.count(deckArtList[i]))

    for i in range(len(deckArtList)):
        if deckArtList[i] in currentDealerHand and args == 2:
            print(art[i] * currentDealerHand.count(deckArtList[i]))

    if args == 3:
        print(logo)

    if args == 4:
        print(bet)

def playerHand(args=0):
    global valuePlayerHand
    deckKeysList = list(deck.keys())
    i = 0

    if args == 1:
        while True:
            rng = random.randint(0, len(deckKeysList) - 1)
            if deck[deckKeysList[rng]] != 0:
                currentPlayerHand.append(deckKeysList[rng])
                deck[deckKeysList[rng]] -= 1
                if deckKeysList[rng][0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
                    valuePlayerHand += int(deckKeysList[rng][0])
                elif deckKeysList[rng][0:2] in ["10"]:
                    valuePlayerHand += int(deckKeysList[rng][0:2])
                elif deckKeysList[rng] == "Ace of Spades":
                    valuePlayerHand += 11
                    if valuePlayerHand > 21:
                        valuePlayerHand -= 11
                        valuePlayerHand += 1
                elif deckKeysList[rng] in ["Jack", "Queen", "King"]:
                    valuePlayerHand += 10
                break
            else:
                pass

    while i < 2 and args != 1:
        rng = random.randint(0, len(deckKeysList) - 1)
        if deck[deckKeysList[rng]] != 0:
            currentPlayerHand.append(deckKeysList[rng])
            deck[deckKeysList[rng]] -= 1
            i += 1
        else:
            pass

    if args != 1:
        for cards in currentPlayerHand:
            if cards[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
                valuePlayerHand += int(cards[0])
            elif cards[0:2] in ["10"]:
                valuePlayerHand += int(cards[0:2])
            elif cards == "Ace of Spades":
                valuePlayerHand += 11
                if valuePlayerHand > 21:
                    valuePlayerHand -= 11
                    valuePlayerHand += 1
            elif cards in ["Jack", "Queen", "King"]:
                valuePlayerHand += 10

def dealerHand(args=0):
    global valueDealerHand
    deckKeysList = list(deck.keys())

    if args == 1:
        while valueDealerHand < 17 and len(currentDealerHand) < 3:
            rng = random.randint(0, len(deckKeysList) - 1)
            if deck[deckKeysList[rng]] != 0:
                currentDealerHand.append(deckKeysList[rng])
                deck[deckKeysList[rng]] -= 1
                if deckKeysList[rng][0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
                    valueDealerHand += int(deckKeysList[rng][0])
                elif deckKeysList[rng][0:2] in ["10"]:
                    valueDealerHand += int(deckKeysList[rng][0:2])
                elif deckKeysList[rng] == "Ace of Spades":
                    valueDealerHand += 11
                    if valueDealerHand > 21:
                        valueDealerHand -= 11
                        valueDealerHand += 1
                elif deckKeysList[rng] in ["Jack", "Queen", "King"]:
                    valueDealerHand += 10
            else:
                pass

    while True and args != 1:
        rng = random.randint(0, len(deckKeysList) - 1)
        if deck[deckKeysList[rng]] != 0:
            currentDealerHand.append(deckKeysList[rng])
            deck[deckKeysList[rng]] -= 1
            break
        else:
            pass

    if args != 1:
        for cards in currentDealerHand:
            if cards[0] in ["2", "3", "4", "5", "6", "7", "8", "9"]:
                valueDealerHand += int(cards[0])
            elif cards[0:2] in ["10"]:
                valueDealerHand += int(cards[0:2])
            elif cards == "Ace of Spades":
                valueDealerHand += 11
                if valueDealerHand > 21:
                    valueDealerHand -= 11
                    valueDealerHand += 1
            elif cards in ["Jack", "Queen", "King"]:
                valueDealerHand += 10

def gameBet(args=0):
    global betAmount, winAmount, lossAmount, gameWins, gameLoss, gameDraw
    if args == 0:
        while True:
            try:
                art(4)
                question = int(input("Enter the amount you would like to bet. Enter only valid integer values:\n$"))
                if question < 0:
                    raise ValueError
                elif question > 0:
                    betAmount += question
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid entry! Enter only valid integer values.")
                print("Try again!")

    if args == 1:
        print(f"You've received ${betAmount * 2} in winnings!")
        winAmount += betAmount * 2
        betAmount = betAmount - betAmount
        gameWins += 1
        print(f"You've won a total of ${winAmount} and lost a total of ${lossAmount}.")
        print(f"You've won {gameWins} games, lost {gameLoss} games, and drawn {gameDraw} games.")

    if args == 2:
        print(f"You've lost your bet of ${betAmount}!")
        lossAmount += betAmount
        betAmount = betAmount - betAmount
        gameLoss += 1
        print(f"You've won a total of ${winAmount} and lost a total of ${lossAmount}.")
        print(f"You've won {gameWins} games, lost {gameLoss} games, and drawn {gameDraw} games.")

    if args == 3:
        print(f"Your bet of ${betAmount} has been returned to you!")
        betAmount = betAmount - betAmount
        gameDraw += 1
        print(f"You've won a total of ${winAmount} and lost a total of ${lossAmount}.")
        print(f"You've won {gameWins} games, lost {gameLoss} games, and drawn {gameDraw} games.")

def gameLoop():
    global valueDealerHand, valuePlayerHand
    os.system("clear")

    playerHand()
    print(f"Your current hand is: {currentPlayerHand}. Your hand is worth: {valuePlayerHand} points.")
    art(1)

    dealerHand()
    print(f"The dealer's current hand is: {currentDealerHand}. The dealer's hand is worth: {valueDealerHand} points.")
    art(2)

    while True:
        try:
            question = input("Enter Y to Hit (draw another card) or N to Stand (keep current hand):\n").strip().lower()
            if question == "y":
                os.system("clear")
                playerHand(1)
                print(f"Your current hand is: {currentPlayerHand}. Your hand is worth: {valuePlayerHand} points.")
                art(1)
                dealerHand(1)
                print(f"The dealer's current hand is: {currentDealerHand}. The dealer's hand is worth: {valueDealerHand} points.")
                art(2)
                break
            elif question == "n":
                os.system("clear")
                print(f"Your current hand is: {currentPlayerHand}. Your hand is worth: {valuePlayerHand} points.")
                art(1)
                dealerHand(1)
                print(f"The dealer's current hand is: {currentDealerHand}. The dealer's hand is worth: {valueDealerHand} points.")
                art(2)
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid entry! Only enter Y or N!")
            print("Try again!")

    if valuePlayerHand > 21:
        print("********** YOU LOSE!!! **********")
        gameBet(2)
    elif valuePlayerHand < 21 and valuePlayerHand < valueDealerHand and valueDealerHand <= 21:
        print("********** YOU LOSE!!! **********")
        gameBet(2)
    elif valuePlayerHand <= 21 and valuePlayerHand > valueDealerHand:
        print("********** YOU WIN!!! **********")
        gameBet(1)
    elif valueDealerHand > 21:
        print("********** YOU WIN!!! **********")
        gameBet(1)
    elif valuePlayerHand == valueDealerHand:
        print("********** DRAW!!! **********")
        gameBet(3)

def gameClear():
    global valuePlayerHand, valueDealerHand, deck

    currentPlayerHand.clear()
    currentDealerHand.clear()
    valuePlayerHand = 0
    valueDealerHand = 0

    currentDeck = sum(deck.values())

    if currentDeck < 10:
        for key, value in deck.items():
            if key not in ["Ace of Spades", "King", "Queen", "Jack"]:
                while deck[key] < 1:
                    deck[key] += 1
            else:
                while deck[key] < 4:
                    deck[key] += 1
        print("All discarded cards have now been reshuffled into the deck!")


while True:
    try:
        art(3)
        question = input("Would you like to play Blackjack? Enter Y for yes or N for no:\n").strip().lower()
        if question == "y":
            os.system("clear")
            gameBet()
            gameLoop()
            gameClear()
            continue
        elif question == "n":
            print("Have a good one!")
            sys.exit()
        else:
            raise ValueError
    except ValueError:
        print("Invalid entry! Enter only Y or N.")
        print("Try again!")
