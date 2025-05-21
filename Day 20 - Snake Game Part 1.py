from turtle import Screen
import time
from SnakeModule import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.snakeOrientationUp, "Up")
screen.onkey(snake.snakeOrientationRight,"Right")
screen.onkey(snake.snakeOrientationLeft, "Left")
screen.onkey(snake.snakeOrientationDown, "Down")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)

    snake.snakeMove()

screen.exitonclick()
