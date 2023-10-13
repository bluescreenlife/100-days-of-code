''' practice with turtle library drawing some algorithmic art'''
import turtle as t
import random

# initialize turtle and RGB color mode
timmy = t.Turtle()
t.colormode(255)
timmy.shape("arrow")

# set up screen
screen = t.Screen()
screen.bgcolor("black")

def rand_color():
    # get a random RGB color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def timmy_rand_walk(cycles):
    # random walk function
    timmy.pensize(10)
    timmy.speed("fastest")
    directions = [0, 90, 180, 270]  

    for _ in range(cycles):
        timmy.setheading(random.choice(directions))
        timmy.color(rand_color())
        timmy.forward(50)

def timmy_draw_spirograph(gap_size):
    # spirohraph function
    timmy.speed("fastest")
    timmy.pensize(5)

    for direction in range(int(360/gap_size)):
        timmy.setheading(timmy.heading() + gap_size)
        timmy.color(rand_color())
        timmy.circle(100)

# comment/un-comment appropriate function to see each
timmy_draw_spirograph(5)
# timmy_rand_walk(100)

screen.exitonclick()