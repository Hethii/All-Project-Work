from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.left(90)

    def go_up(self):
        """moves the turtle up"""
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        """moves the turtle down"""
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_right(self):
        """moves the turtle to the right"""
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_left(self):
        """moves the turtle left"""
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def reset_position(self):
        """moves the back to the beginning after it
        reaches the final point"""
        self.goto(STARTING_POSITION)

    def finish_line(self):
        """detects when turtle is at finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
