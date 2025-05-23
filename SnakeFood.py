from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, snake):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.positionList = []
        self.snake = snake
        for i in self.snake.segments:
            segmentPosition = i.pos()
            self.positionList.append(segmentPosition)

        while True:
            randomX = random.randint(-480, 480)
            randomY = random.randint(-480, 480)
            if (randomX, randomY) not in self.positionList:
                self.goto(randomX, randomY)
                break
            else:
                pass
        self.positionList.clear()

    def refresh(self):
        for i in self.snake.segments:
            segmentPosition = i.pos()
            self.positionList.append(segmentPosition)

        while True:
            randomX = random.randint(-480, 480)
            randomY = random.randint(-480, 480)
            if (randomX, randomY) not in self.positionList:
                self.goto(randomX, randomY)
                break
            else:
                pass
        self.positionList.clear()