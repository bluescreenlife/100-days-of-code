'''program to recreate a Damien Hirst dot painting using the python turtle
library, and color palette sourced from a Hirst dot painting'''
import turtle as t
import random

# # code used to get RGB values from image of Hirst painting --> color_list below
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(211, 154, 97), (52, 107, 131), (179, 78, 32), (200, 142, 34), (124, 80, 97), 
              (116, 154, 170), (122, 176, 158), (227, 198, 128), (194, 85, 106), (55, 39, 20), 
              (12, 49, 63), (193, 123, 143), (44, 168, 126), (54, 121, 116), (166, 21, 31), 
              (226, 93, 78), (5, 29, 27), (244, 163, 160), (80, 147, 168), 
              (166, 26, 22), (238, 164, 169), (19, 80, 90), (172, 207, 188), (104, 126, 158), (28, 84, 80)]

def hirst_dots(dot_size, dot_spacing):
    t.colormode(255) # use RGB colors
    hirst = t.Turtle() # create dot painter
    hirst.shape("circle") # set circle as shape to paint
    hirst.speed("fastest") # set paint speed to fastest
    hirst.hideturtle()
    hirst.penup() # start with pen up

    screen = t.Screen() # create screen
    screen.screensize(500,500) # set screen size
    screen.bgcolor(250, 250, 245) # set hirst-like background color
    dot_size = dot_size # take dot size from fn parameters
    dot_spacing = dot_spacing # take dot spacing from fn parameters

    # begin at lower left
    x = -325
    y = -325

    # loop to paint grid of dots, moving left to right, bottom to top
    while y <= 325:
        while x <= 325:
            random_color = random.choice(color_list)
            hirst.goto(x, y)
            hirst.pendown()
            hirst.dot(dot_size, random_color)
            hirst.penup()
            x += dot_spacing
        x = -325
        y += 50

    # keep window open when compelte, click to close
    screen.exitonclick()

while __name__ == "__main__":
    hirst_dots(20, 50)