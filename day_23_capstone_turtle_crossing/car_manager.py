from turtle import Turtle
import random

COLORS = ["turquoise", "pale goldenrod", "peach puff", "orchid", "dark salmon", "silver"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_CARS = 10

class CarManager:
    # class to manage list of car objects
    def __init__(self):
        self.num_cars = NUM_CARS
        self.active_cars = []

    # set cars into motion
    def run_cars(self):
        for car in self.active_cars:
            car.forward(car.speed)
        
class Car(Turtle):
    # car object
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.turtlesize(stretch_wid = 1, stretch_len = 2, outline = None)
        self.goto(310, (random.randint(-250, 250)))
        self.setheading(180)
        self.speed = random.randint(5, 20)