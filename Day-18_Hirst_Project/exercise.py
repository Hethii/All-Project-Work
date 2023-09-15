import turtle as t
import random

avia = t.Turtle()
t.colormode(255)


def randomcolour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


# colours = ["wheat", "khaki", "lime green", "pink", "goldenrod", "dark magenta",
#            "dark blue", "steel blue", "peach puff", "pale violet red", "dark olive green",
#            "medium purple", "saddle brown", "aquamarine", "light sky blue",
#            "medium blue"]
#
# avia.pensize(1)
# direction = [0, 90, 180, 270]
avia.speed("fastest")


# for creating random walks
def draw_spirograph(size_of_gap):

    for shape_colour in range(int(360 / size_of_gap)):
        avia.color(randomcolour())
        avia.circle(100)
        # avia.left(20)
        # avia.right(15)
        avia.setheading(avia.heading() + size_of_gap)


draw_spirograph(5)


    # avia.forward(30)
    # avia.setheading(random.choice(direction))



# for creating triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# def draw_shape(num_of_shapes):
#     angle = 360 / num_of_shapes
#     for _ in range(num_of_shapes):
#         avia.forward(100)
#         avia.right(angle)
#
#
# for shape_value in range(3, 11):
#     avia.color(random.choice(colours))
#     draw_shape(shape_value)

# creating dash lines
# for move in range(50):
#     avia.forward(4)
#     avia.penup()
#     avia.forward(4)
#     avia.pendown()

# creating a square
# def square():
#     for y in range(4):
#         avia.right(90)
#         avia.forward(100)
#
#
# square()

# from turtle import *
# speed(10)
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(150)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

screen = t.Screen()
screen.exitonclick()

# for creating a very nice concept


