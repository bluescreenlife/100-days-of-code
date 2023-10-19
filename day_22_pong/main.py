'''recreation of the classic Pong arcade game
2 players - player 1 uses W & S for up and down; player 2 uses arrow up and arrow down
10 points to win'''

from turtle import Screen
from paddle import Paddle
from ball import Ball
from midline import Midline
from scoreboard import ScoreBoard
import time

# set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# set up player paddles
player1 = Paddle('P1')
player2 = Paddle('P2')
ball = Ball()
player1_scoreboard = ScoreBoard(1, (-200, 265))
player2_scoreboard = ScoreBoard(2, (200, 265))
Midline()

# listen for keypresses and call appropriate paddle movement functions
screen.listen()
screen.onkey(player1.up, 'w')
screen.onkey(player1.down, 's')
screen.onkey(player2.up, 'Up')
screen.onkey(player2.down, 'Down')

game_is_on = True

# main game loop
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    # detect scoring, assign points, refresh scores
    if ball.xcor() <= -400:
        ball.reset()
        ball.change_dir("P1")
        player2_scoreboard.score += 1
        player2_scoreboard.update()
        if player2_scoreboard.score == 11:
            game_is_on = False
            player2_scoreboard.game_over()
    
    if ball.xcor() >= 400:
        ball.reset()
        ball.change_dir("P2")
        player1_scoreboard.score += 1
        player1_scoreboard.update()
        if player1_scoreboard.score == 11:
            game_is_on = False
            player1_scoreboard.game_over()

    # detect collision with paddles, bounce toward other player side
    for segment in player1.segments:
        if segment.distance(ball) < 10:
            ball.change_dir("P2")
    
    for segment in player2.segments:
        if segment.distance(ball) < 10:
            ball.change_dir("P1")

screen.exitonclick()