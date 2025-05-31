import turtle, pandas

FONT = ("Calibri", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turtleWriter = turtle.Turtle()
turtleWriter.hideturtle()
turtleWriter.color("black")
turtleWriter.penup()

statesCSVData = pandas.read_csv("50_states.csv")
statesList = statesCSVData.state.to_list()
knownStates = []
statesToLearn = []

def stateWriter(answer):
    inputState = statesCSVData[statesCSVData.state == answer]
    coordinateX = inputState.x.iloc[0]
    coordinateY = inputState.y.iloc[0]
    turtleWriter.goto(coordinateX, coordinateY)
    turtleWriter.pendown()
    turtleWriter.write(answer, align="center", font=FONT)
    turtleWriter.penup()

remainingStates = 50
while remainingStates > 0:
    answerState = screen.textinput(title="Guess a state!"
    , prompt=f"{remainingStates} out of 50 states remaining.\nEnter a state's name:").strip().title()

    if answerState in statesList and answerState not in knownStates:
        stateWriter(answerState)
        remainingStates += -1
        knownStates.append(answerState)
    elif answerState == "Exit":
        for i in statesList:
            if i not in knownStates:
                statesToLearn.append(i)
        educational = pandas.DataFrame(statesToLearn)
        educational.to_csv("States_I_Need_To_Learn.csv")
        break
    else:
        pass