from turtle import Turtle
import random

MOVE_DISTANCE = 10
P1_SIDE = -400
P2_SIDE = 400

class Ball(Turtle):
    # create ball object
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color('blue')
        self.speed('normal')
        self.reset()
        self.setheading(self.towards(P1_SIDE, self.get_random_y()))

    def reset(self):
        # place food object at random location within screen boundaries
        self.goto(0, 0)
    
    def move(self):
        # set ball into movement
        self.forward(MOVE_DISTANCE)

    def change_dir(self, player):
        # change direction of ball back to receiving player
        new_y = self.get_random_y()
        if player == "P1":
            self.setheading(self.towards(P1_SIDE, new_y))
        elif player == "P2":
            self.setheading(self.towards(P2_SIDE, new_y))

    def get_random_y(self):
        # get a random y coordinate for change_dir function
        return random.randint(-300, 300)