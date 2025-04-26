print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossRoad = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right':\n")
if crossRoad == "left":
    river = input("You come across a river. Do you attempt to swim or do you wait? Type 'swim' or 'wait':\n")
    if river == "wait":
        print("You wait for a few hours and a kind fisherman offers to take you to the other side of the river.")
        final_choice = input("When you reach the other side of the river. You find a castle, a cabin, and a mansion. Which one do you investigate?\nType 'castle', 'cabin', or 'mansion':\n")
        if final_choice == "castle":
            print("The king of the castle arrests you for trespassing. Game over.")
        elif final_choice == "mansion":
            print("The perimeter of the mansion is booby-trapped. You fall into one of the traps. Game over.")
        else:
            print("The treasure is inside the cabin! You win the game!")
    else:
        print("You attempt to swim through the river and reach the shore. However, the current is too strong and you drown. Game over.")
else:
    print("You're attacked by bandits. Game over.")