'''solution to reeborg's world maze escape game:
https://reeborg.ca/reeborg.html
'''

while not at_goal():
    while not right_is_clear():
        if front_is_clear():
            move()
        else:
            turn_left()
    if at_goal():
        break
    while right_is_clear():
        for _ in range(3):
            turn_left()
        move()
    if at_goal():
        break