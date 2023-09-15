from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def guess():
    return "<h1>Guess a number between 0 and 99</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


answer = random.randint(1, 10)


@app.route("/<int:number>")
def game_function(number):
    if number < answer:
        return "<h2 style='color: red;'>Too low, try again</h2>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > answer:
        return "<h2 style='color: purple;'>Too high, try again</h2>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h2 style='color: green;'>You found me</h2>" \
               "<img src ='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
