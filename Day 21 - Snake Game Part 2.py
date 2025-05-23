from turtle import Screen
import time, sys
from SnakeModule import Snake
from SnakeFood import Food
from SnakeScore import Scoreboard

screen = Screen()
def screenInitialize():
    screen.setup(width=1200,height=1200)
    screen.bgcolor("black")
    screen.title("SNAKE GAME")
    screen.tracer(0)
screenInitialize()

snake = Snake()
food = Food(snake)
score = Scoreboard()

def screenListening():
    screen.listen()
    screen.onkey(snake.snakeOrientationUp, "Up")
    screen.onkey(snake.snakeOrientationRight,"Right")
    screen.onkey(snake.snakeOrientationLeft, "Left")
    screen.onkey(snake.snakeOrientationDown, "Down")
    screen.onkey(snake.snakeOrientationPause, "space")

def gameOverEvent(args):
    if args == 1:
        condition = "Your snake crashed into the wall."
    elif args == 2:
        condition = "Your snake crashed into itself."

    gameOverPrompt = screen.textinput(title="GAME OVER!!!!!", prompt=f"{condition} "
                    f"Would you like to restart the game? Enter Y to restart or enter N to quit the game.").strip().lower()

    if gameOverPrompt == "y":
        return "y"
    elif gameOverPrompt == "n":
        return "n"
    else:
        pass

def gameRestart():
    global score, snake, food
    screen.clear()
    screenInitialize()
    snake = Snake()
    screenListening()
    food = Food(snake)
    score.scoreClear()
    score = Scoreboard()

startMessage = screen.textinput(title="Welcome to the Snake Game!",
prompt="Here are the rules:\n\n1. Control the snake with the arrow keys."
"\n2. Make your snake eat its food (the blue circles) by moving its head into the food."
"\n3. Don't crash your snake into itself or into the walls.\n4. You can press the spacebar to pause the game."
"\n\nPress enter to start the game.")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)

    snake.snakeMove()
    screenListening()

    if snake.head.distance(food) < 20:
        food.refresh()
        score.plusOne()
        snake.addSegment()
        score = Scoreboard()

    if snake.head.xcor() > 580 or snake.head.xcor() < -580 or snake.head.ycor() > 495 or snake.head.ycor() < -495:
        gameOver1 = gameOverEvent(1)
        if gameOver1 == "y":
            gameRestart()
        elif gameOver1 == "n":
            sys.exit()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameOver2 = gameOverEvent(2)
            if gameOver2 == "y":
                gameRestart()
            elif gameOver2 == "n":
                sys.exit()

screen.exitonclick()