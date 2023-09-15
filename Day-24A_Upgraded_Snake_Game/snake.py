from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # x_positions = [0, -20, -40]
        self.new_avia = []
        self.body()
        self.head= self.new_avia[0]

    def body(self):
        # for create_turtle in range(0,3):
        # print("Entered body")
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        avia = Turtle("square")
        avia.penup()
        avia.color("white")
        # avia.goto(x_positions[create_turtle], 0)
        avia.goto(position)
        self.new_avia.append(avia)

    def reset(self):
        for seg in self.new_avia:
            seg.goto(1000, 1000)
        self.new_avia.clear()
        self.body()
        self.head = self.new_avia[0]

    def extend(self):
        self.add_segment(self.new_avia[-1].position())

    def move(self):
        # print("Entered move")
        for avia_num in range(len(self.new_avia) - 1, 0, -1):
            new_x = self.new_avia[avia_num - 1].xcor()
            new_y = self.new_avia[avia_num - 1].ycor()
            # print(new_x, new_y)

            self.new_avia[avia_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)