from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-290,250)

    def writeLevel(self):
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def updateLevel(self):
        self.clear()
        self.level += 1
        self.writeLevel()

    def clearLevel(self):
        self.clear()
        self.level = 0
        self.writeLevel()