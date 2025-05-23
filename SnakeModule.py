from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.initializeSegments()
        self.head = self.segments[0]

    def initializeSegments(self):
        x = 0
        for i in range(3):
            snakeBody = Turtle("square")
            snakeBody.color("white")
            snakeBody.up()
            self.segments.append(snakeBody)
            self.segments[i].goto(x,0)
            x -= 20

    def snakeMove(self):
        for segNum in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segNum - 1].xcor()
            newY = self.segments[segNum - 1].ycor()
            self.segments[segNum].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)
        for i in self.segments:
            i.showturtle()

    def snakeOrientationUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snakeOrientationRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snakeOrientationLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snakeOrientationDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snakeOrientationPause(self):
        self.head.forward(0)
        Screen().textinput(title="PAUSE", prompt="Press enter to resume.")

    def addSegment(self):
        snakeGrowth = Turtle("square")
        snakeGrowth.hideturtle()
        snakeGrowth.color("white")
        snakeGrowth.up()
        self.segments.append(snakeGrowth)
