from turtle import Turtle

scoreTotal = 0

class Scoreboard(Turtle):
    def __init__(self):
        global scoreTotal
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(0,450)
        self.write(arg=f"Score: {scoreTotal}", move=False, align="Center", font=("Calibri", 24, "normal"))

    def plusOne(self):
        global scoreTotal
        self.clear()
        scoreTotal += 1

    def scoreClear(self):
        global scoreTotal
        self.clear()
        scoreTotal -= scoreTotal