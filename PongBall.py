from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.rng = random.randint(1,1)
        self.xMove = 10
        self.yMove = 10
        self.speedInit = 0.1

    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX, newY)

    def wallCollision(self):
        self.yMove *= -1

    def paddleCollision(self):
        self.xMove *= -1

    def miss(self):
        self.speedInit = 0.1
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.xMove *= -1
        self.move()

    def increaseSpeed(self):
        self.speedInit *= 0.9
