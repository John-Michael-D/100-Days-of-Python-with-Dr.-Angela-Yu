from turtle import Turtle

STARTING_POSITION = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("blue")
        self.goto(STARTING_POSITION)
        self.speed = 10

    def moveUp(self):
        self.forward(self.speed)

    def moveDown(self):
        self.backward(self.speed)

    def turtleRespawn(self):
        self.goto(STARTING_POSITION)

    def increaseSpeed(self):
        self.speed += 2