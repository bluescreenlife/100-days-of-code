'''recreation of the original Nokia mobile Snake game'''
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# set up screen parameters
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# initalize snake, food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# listen for keypresses and call appropriate fns
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# game on/of
game_is_on = True

# loop to refresh screen each .1 second and move snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.update()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        scoreboard.update()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# window to remain open until user click
screen.exitonclick()