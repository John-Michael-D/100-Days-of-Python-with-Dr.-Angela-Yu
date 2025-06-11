import pandas, os

os.system("clear")

natoCSV = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
newDict = {row.letter:row.code for (index, row) in natoCSV.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    userText = input("Enter your text:\n>").upper()
    result = [newDict[n] for n in userText if n in newDict.keys()]
    print(f"Your text converted to the NATO Phonetic Alphabet is: {result}\n")
