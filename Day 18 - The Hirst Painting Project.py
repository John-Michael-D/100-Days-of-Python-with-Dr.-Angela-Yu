from turtle import *
#import colorgram

#colorsExtracted = colorgram.extract("HirstPainting.jpg", 30)
#colorsList = []
trueColorsList = [(196, 166, 105), (133, 167, 194), (46, 103, 147), (147, 89, 40), (9, 21, 54), (189, 156, 33), (225, 208, 112), (62, 22, 9), (68, 120, 77), (58, 12, 23), (185, 140, 166), (136, 181, 149), (136, 28, 12), (131, 76, 105), (14, 42, 26), (18, 53, 137), (121, 26, 41), (170, 101, 137), (92, 152, 97), (175, 189, 217), (86, 121, 184), (183, 99, 86), (22, 93, 65), (67, 153, 170), (210, 177, 204), (89, 77, 14)]

#for i in range(len(colorsExtracted)):
    #colorsList.append(colorsExtracted[i].rgb)

#for i in range(len(colorsList)):
    #trueColorsList.append((colorsList[i][0], colorsList[i][1], colorsList[i][2]))

franklin = Turtle()
screen = Screen()
franklin.shape("turtle")
franklin.color("blue")
franklin.speed(3)
screen.colormode(255)
franklin.pensize(10)
screen.screensize(4000,4000)

i1 = 0
def colors():
    global i1
    rgb1 = trueColorsList[i1][0]
    rgb2 = trueColorsList[i1][1]
    rgb3 = trueColorsList[i1][2]
    i1 += 1
    if i1 == (len(trueColorsList) - 1):
        i1 -= i1
    return rgb1, rgb2, rgb3

def circles(args):
    franklin.pencolor(args)
    franklin.dot(20)
    franklin.up()
    franklin.forward(50)

i2 = 0
y = 0
for a in range(10):
    for b in range(10):
        circles(colors())
        i2 += 1
        if i2 == 10:
            i2 -= i2
            y += 50
            franklin.goto(0, y)

screen.exitonclick()
