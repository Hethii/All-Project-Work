import random
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def card_in_view():
    """Card been processed/asked"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    # print(to_learn)
    current_card = random.choice(to_learn)
    # print(current_card)
    canvas.itemconfig(lang_displayed, text="French", fill="black")
    canvas.itemconfig(french_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """For switching to english"""
    canvas.itemconfig(lang_displayed, text="English", fill="white")
    canvas.itemconfig(french_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


def known():
    """Known word is removed from word list"""
    to_learn.remove(current_card)
    # print(to_learn)
    print(len(to_learn))
    yet_to_learn = pandas.DataFrame(to_learn)
    yet_to_learn.to_csv("data/words_to_learn.csv", index=False)
    card_in_view()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Capstone Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)

card_back = PhotoImage(file="./images/card_back.png")

canvas.grid(column=0, row=0, columnspan=2)

# Canvas Text
lang_displayed = canvas.create_text(400, 180, text="French", font=("Arial", 25, "italic"))
french_word = canvas.create_text(400, 270, fill="black", font=("Arial", 40, "bold"))

# button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=card_in_view)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=known)
right_button.grid(column=1, row=1)

card_in_view()
window.mainloop()
