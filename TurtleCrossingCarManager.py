from turtle import Turtle, Screen
import random
import sys

screen = Screen()

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:
    def __init__(self, franklin, score):
        self.cars = []
        self.moveSpeed = -5
        self.spawnAmount = 15
        self.createCarObjects()
        self.spawnCarObjects()
        self.franklin = franklin
        self.score = score

    def createCarObjects(self):
        for i in range(self.spawnAmount):
            car = Turtle()
            car.hideturtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(car)

    def spawnCarObjects(self):
        for i in self.cars:
            randomX = random.randint(-280, 300)
            randomY1 = random.randint(-225, 240)
            i.goto(randomX, randomY1)
            i.showturtle()

    def moveCarObjects(self):
        for i in self.cars:
            newX = i.xcor() + self.moveSpeed
            i.goto(newX, i.ycor())

    def respawnCarObjects(self):
        for i in self.cars:
            if i.xcor() <= -300:
                randomY2 = random.randint(-225, 240)
                i.goto(300, randomY2)

    def increaseSpeed(self):
        self.moveSpeed -= 1

    def clearCarObjects(self):
        for i in self.cars:
            i.hideturtle()
            i.clear()
        self.cars.clear()
        self.createCarObjects()
        self.spawnCarObjects()

    def increaseSpawn(self):
        self.spawnAmount += 2

    def detectCollision(self):
        for i in self.cars:
            if self.franklin.distance(i.pos()) < 20:
                while True:
                    try:
                        question = screen.textinput(title="GAME OVER!",
                        prompt="Franklin got hit by a block!\nWould you like to restart the game? (Y/N)?").strip().lower()

                        if question in ["y", "yes"]:
                            self.spawnAmount = 15
                            self.clearCarObjects()
                            self.moveSpeed = -5
                            self.franklin.speed = 10
                            self.score.clearLevel()
                            self.franklin.turtleRespawn()
                            break
                        elif question in ["n", "no"]:
                            sys.exit()
                        else:
                            raise ValueError

                    except ValueError:
                        pass

