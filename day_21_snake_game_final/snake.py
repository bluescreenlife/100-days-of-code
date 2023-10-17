from turtle import Turtle

# constants for snark start positon, move distance, and turn degrees
STARTING_POSITIONS = [(0,0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # each turtle object in segments list, appended as snake eats/grows
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # snake head and indicator of motion is first turtle object in segments
    
    def create_snake(self):
        # create a new snake of 3 segments in length
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # add a segment to the snake
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.setpos(position)
        new_segment.color('magenta')
        self.segments.append(new_segment)
    
    def extend(self):
        # duplicate last segment of snake at the end, for use when snake eats food
        self.add_segment(self.segments[-1].position())

    def move(self):
        # movement function for snake; each segment follows the coordinates of
        # the one before it, directed by head of snake
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # redirection functions
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)