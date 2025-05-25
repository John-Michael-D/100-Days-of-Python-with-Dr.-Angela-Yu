from turtle import Screen
from PongPaddle import FirstPaddle,SecondPaddle
from PongBall import Ball
from PongScore import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

while True:
    try:
        modeSelect = screen.textinput(title="Select your mode!",
        prompt="Enter 1 for singleplayer or 2 for multiplayer (enter only integers):").strip().lower()
        if modeSelect in ["1", "2"]:
            if modeSelect == "1":
                break
            elif modeSelect == "2":
                break
        else:
            raise ValueError
    except ValueError:
        pass

playerPaddle1 = FirstPaddle()
playerPaddle2 = SecondPaddle(modeSelect)
pongBall = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(playerPaddle1.paddleUp, "Up")
screen.onkey(playerPaddle1.paddleDown,"Down")
screen.onkey(playerPaddle2.paddleUp, "w")
screen.onkey(playerPaddle2.paddleDown, "s")

gameIsOn = True
while gameIsOn:
    time.sleep(pongBall.speedInit)
    screen.update()
    pongBall.move()
    playerPaddle2.mode()
    if pongBall.ycor() > 280 or pongBall.ycor() < -280:
        pongBall.wallCollision()
    if (pongBall.xcor() > 320 and pongBall.distance(playerPaddle1) < 50) or (pongBall.xcor() < -320 and pongBall.distance(playerPaddle2) < 50):
        pongBall.paddleCollision()
        pongBall.increaseSpeed()
    elif pongBall.xcor() > 400:
        pongBall.miss()
        score.player2Win()
    elif pongBall.xcor() < -400:
        pongBall.miss()
        score.player1Win()

screen.exitonclick()