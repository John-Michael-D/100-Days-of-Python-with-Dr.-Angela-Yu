from turtle import Turtle

Y_COR_MAX = 250
Y_COR_MIN = -250

class FirstPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(350,0)

    def paddleUp(self):
        currentY1 = self.ycor()
        if currentY1 <= Y_COR_MAX:
            self.goto(self.xcor(), currentY1 + 20)

    def paddleDown(self):
        currentY2 = self.ycor()
        if currentY2 >= Y_COR_MIN:
            self.goto(self.xcor(), currentY2 - 20)

class SecondPaddle(Turtle):
    def __init__(self, modeSelect):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(-350,0)
        self.direction = 0
        self.modeSelect = modeSelect

    def mode(self):
        if self.modeSelect == "1":
           if self.ycor() <= Y_COR_MAX and self.direction == 0:
               self.goto(self.xcor(), self.ycor() + 20)
           else:
               self.direction = 1

           if self.ycor() >= Y_COR_MIN and self.direction == 1:
               self.goto(self.xcor(), self.ycor() - 20)
           else:
               self.direction = 0

    def paddleUp(self):
        if self.modeSelect == "2":
            currentY1 = self.ycor()
            if currentY1 <= Y_COR_MAX:
                self.goto(self.xcor(), currentY1 + 20)

    def paddleDown(self):
        if self.modeSelect == "2":
            currentY2 = self.ycor()
            if currentY2 >= Y_COR_MIN:
                self.goto(self.xcor(), currentY2 - 20)