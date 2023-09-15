from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.present_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.present_score}", False, align= ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align= ALIGNMENT, font=FONT)

    def score(self):
        self.present_score += 1
        self.clear()
        self.update_scoreboard()

    #
    # def scoreboard(self):
    #
    #     self.write(self.present_score, False, "center")



