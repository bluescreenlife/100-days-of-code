from turtle import Turtle

P1_START_POS = [(-380, 20), (-380, 0), (-380, -20)]
P2_START_POS = [(375, 20), (375, 0), (375, -20)]
MOVEMENT_SPEED = 10

class Paddle:
    # create paddle for player
    def __init__(self, player):
        self.segments = []
        self.player = player
        self.starting_positions = []

        if self.player == "P1":
            self.starting_positions = P1_START_POS
        elif self.player == "P2":
            self.starting_positions = P2_START_POS

        self.create_paddle()
        self.handle = self.segments[1]

    def create_paddle(self):
        for position in self.starting_positions:
            new_segment = Turtle(shape='square')
            new_segment.speed(0)
            new_segment.penup()
            new_segment.setpos(position)
            new_segment.color('magenta')
            self.segments.append(new_segment)

    def up(self):
        # move paddle up
        for segment in self.segments:
            segment.setheading(90)
            segment.forward(MOVEMENT_SPEED)
    
    def down(self):
        # move paddle down
        for segment in self.segments:
            segment.setheading(270)
            segment.forward(MOVEMENT_SPEED)