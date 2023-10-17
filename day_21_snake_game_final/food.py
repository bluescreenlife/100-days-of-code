from turtle import Turtle
import random

class Food(Turtle):
    # create food object
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        # place food object at random location within screen boundaries
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)