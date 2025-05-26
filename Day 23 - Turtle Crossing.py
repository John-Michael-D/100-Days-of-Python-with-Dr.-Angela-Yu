import time
from turtle import Screen
from TurtleCrossingPlayer import Player
from TurtleCrossingCarManager import CarManager
from TurtleCrossingScoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

screen.textinput(title="Welcome!", prompt="Welcome to the game! The rules are simple:\n"
"\n1. Move Franklin the Blue Turtle forwards and backwards with the Up and Down arrow keys."
"\n2. Move Franklin to the other side of the screen while avoiding the blocks."
"\n3. The amount of blocks and their movement speed as well as Franklin's movement speed "
"will increase everytime Franklin reaches the other side of the screen.\n\nPress the Enter key to begin the game.")

franklin = Player()
score = Scoreboard()
cars = CarManager(franklin, score)

GameIsOn = True
while GameIsOn:
    time.sleep(0.1)
    screen.update()
    cars.detectCollision()
    screen.listen()
    screen.onkey(franklin.moveUp, "Up")
    screen.onkey(franklin.moveDown, "Down")
    score.writeLevel()
    cars.moveCarObjects()
    cars.respawnCarObjects()
    if franklin.ycor() >= 280:
        cars.increaseSpawn()
        cars.clearCarObjects()
        franklin.turtleRespawn()
        score.updateLevel()
        cars.increaseSpeed()
        franklin.increaseSpeed()
