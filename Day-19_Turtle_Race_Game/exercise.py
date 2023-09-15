from turtle import Turtle, Screen

avia = Turtle()
screen = Screen()


def move_forwards():
    avia.forward(10)

def move_backwards():
    avia.backward(10)
def turn_left():
    new_heading = avia.heading() + 10
    avia.setheading(new_heading)

def turn_right():
    new_heading = avia.heading() - 10
    avia.setheading(new_heading)
def clear():
    avia.clear()
    avia.penup()
    avia.home()
    avia.pendown()



screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(clear, "c")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.exitonclick()
