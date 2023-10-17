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
        self.update()

    def update(self):
        # for use when snake eats food, clear scoreboard and generate new with updated score
        self.clear()
        self.write(f"SNAKEY SCORE: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        # text to be displayed in center of screen when game ends
        self.goto(0, 0)
        self.write(f"GAME OVER", align = 'center', font = FONT)
