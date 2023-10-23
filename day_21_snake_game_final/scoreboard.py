from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Impact', 20, 'italic')

class ScoreBoard(Turtle):
    # scoreboard object
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.color('lime')
        self.score = 0
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.update()

    def update(self):
        # for use when snake eats food, clear scoreboard and generate new with updated score
        self.clear()
        self.write(f"SNAKEY SCORE: {self.score} HIGH SCORE: {self.high_score}", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update()
