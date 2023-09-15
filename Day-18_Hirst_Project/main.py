# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('image2.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136),
 (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
 (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
 (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
 (176, 192, 208), (168, 99, 102)]

import turtle as t
import random


avia = t.Turtle()
t.colormode(255)
avia.speed("fastest")
avia.penup()
avia.hideturtle()
avia.setheading(225)
avia.forward(300)
avia.setheading(0)
number_of_dots = 100


def draw_spirograph():
    for dot_move in range(1, number_of_dots + 1):
        avia.color(random.choice(color_list))
        avia.dot(20)
        avia.forward(50)

        if dot_move % 10 == 0:
            avia.setheading(90)
            avia.forward(50)
            avia.setheading(180)
            avia.forward(500)
            avia.setheading(0)



draw_spirograph()





screen = t.Screen()
screen.exitonclick()