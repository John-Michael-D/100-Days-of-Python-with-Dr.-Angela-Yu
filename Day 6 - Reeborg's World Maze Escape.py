def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def hurdle():
    if wall_on_right() == True:
        turn_left()
    if wall_on_right() == False:
        turn_right()


while not at_goal():
    if front_is_clear() == True:
        move()
    if front_is_clear() == True and wall_on_right == False:
        turn_right()
    else:
        hurdle()