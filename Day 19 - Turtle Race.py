from turtle import Turtle, Screen
import random

isRaceOn = False
screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
turtleRacers = []

i2 = 75
for turtleIndex in range(0,6):
    turtleRacer = Turtle(shape="turtle")
    turtleRacer.color(colors[turtleIndex])
    turtleRacers.append(turtleRacer)
    turtleRacer.up()
    turtleRacer.goto(x=-230, y=i2)
    i2 -= 25

if userBet:
    isRaceOn = True

while isRaceOn:
    for turtles in turtleRacers:
        paces = random.randint(0, 5)
        turtles.forward(paces)
        if turtles.xcor() > 230:
            winningTurtle = turtles.pencolor()
            isRaceOn = False
            if userBet in winningTurtle:
                print(f"You win! The {winningTurtle} turtle won the race!")
            else:
                print(f"You lose! The {winningTurtle} turtle won the race!")

screen.exitonclick()