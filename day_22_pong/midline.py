from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Impact', 20, 'italic')

class Midline(Turtle):
    # create midline halfway between player sides
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, -300)
        self.color('white')
        self.setheading(90)
        self.draw_line()
    
    def draw_line(self):
        while self.ycor() <= 300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)