from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 10, "italic"))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.text = self.canvas.create_text(150, 125,
                                            width=280,
                                            text="Hello",
                                            fill="black",
                                            font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.true = Button(image=true_img, highlightthickness=0, command=self.right_answer)
        self.true.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.false = Button(image=false_img, highlightthickness=0, command=self.wrong_answer)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """for getting next question and checking if question still remains"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the questions")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def right_answer(self):
        """for checking if the answer is True"""
        self.get_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        """for checking if the answer is False"""
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)

    def get_feedback(self, is_right):
        """for colour feedback i.e green if correct and red if wrong"""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
