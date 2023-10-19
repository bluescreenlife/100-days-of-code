from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Impact', 20, 'italic')

class ScoreBoard(Turtle):
    # create scoreboard object
    def __init__(self, player_num, position):
        super().__init__()
        self.hideturtle()
        self.goto(position)
        self.color('lime')
        self.score = 0
        self.player_num = player_num
        self.update()

    def update(self):
        # for use when snake eats food, clear scoreboard and generate new with updated score
        self.clear()
        self.write(f"PLAYER {self.player_num}: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        # text to be displayed in center of screen when game ends
        self.goto(0, 0)
        self.write(f"GAME OVER\nPLAYER {self.player_num} WINS", align = 'center', font = FONT)