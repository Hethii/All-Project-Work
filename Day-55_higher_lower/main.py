from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapped_bold():
        return f"<b>{function()}</b>"
    return wrapped_bold

def make_italic(function):
    def wrapped_italic():
        return f"<em>{function()}<em>"
    return wrapped_italic
def make_underline(function):
    def wrapped_underline():
        return "<u>" + function() + "</u>"
    return wrapped_underline


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center;'>Hello, World!</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://media.giphy.com/media/7kn27lnYSAE9O/giphy.gif' width=200>"
    # "<img src='https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_640.jpg' width=200>"


# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_italic
@make_underline
def bye():
    return "Bye!"


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}!, you are {number} years old"


@app.route("/<name>")
def yello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
