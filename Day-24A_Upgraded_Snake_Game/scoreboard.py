from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.present_score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.present_score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.present_score > self.high_score:
            self.high_score = self.present_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.present_score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align= ALIGNMENT, font=FONT)

    def score(self):
        self.present_score += 1
        self.update_scoreboard()




