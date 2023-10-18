from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
'''recreation of the classic Pong game'''
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
scoreboard = ScoreBoard()

# listen for keypresses and call appropriate fns
screen.listen()
screen.onkey(player1.up, 'w')
screen.onkey(player1.down, 's')
screen.onkey(player2.up, 'Up')
screen.onkey(player2.down, 'Down')

game_is_on = True

# main game loop
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # detect collision with walls, assign points, refresh scores
    if ball.xcor() <= -400:
        ball.reset()
        scoreboard.p2_score += 1
        scoreboard.update()
    
    if ball.xcor() >= 400:
        ball.reset()
        scoreboard.p1_score += 1
        scoreboard.update()

    # detect collision with paddles, bounce toward other player side
    for segment in player1.segments:
        if segment.distance(ball) < 10:
            ball.change_dir("P2")
    
    for segment in player2.segments:
        if segment.distance(ball) < 10:
            ball.change_dir("P1")

screen.exitonclick()