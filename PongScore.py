from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.middleMark()
        self.player1Score = 0
        self.p1Score()
        self.player2Score = 0
        self.p2Score()

    def p1Score(self):
        self.goto(100, 200)
        self.write(self.player1Score, align="center", font=("Courier", 65, "normal"))

    def p2Score(self):
        self.goto(-100, 200)
        self.write(self.player2Score, align="center", font=("Courier", 65, "normal"))

    def player1Win(self):
        self.clear()
        self.player1Score += 1
        self.p1Score()
        self.p2Score()
        self.middleMark()

    def player2Win(self):
        self.clear()
        self.player2Score += 1
        self.p1Score()
        self.p2Score()
        self.middleMark()

    def middleMark(self):
        self.goto(0,300)
        self.pendown()
        self.pensize(5)
        self.goto(0,-300)
        self.penup()
