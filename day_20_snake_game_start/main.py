'''Day 1 of 2 for creating snake game; this program only contains the snake and 
its movement capabilities. See day 22 for full snake game.'''
from turtle import Screen
from snake import Snake
import time

# set up screen parameters
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# initalize snake object
snake = Snake()

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

# window to remain open until user click
screen.exitonclick()