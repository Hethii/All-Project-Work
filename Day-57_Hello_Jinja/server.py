from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    random_number = random.randint(1, 10)
    year = datetime.now()
    return render_template("index.html", num=random_number, year=year.year)


@app.route("/guess/<name>")
def exercise(name):
    age = requests.get(url=f"https://api.agify.io?name={name}").json()
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}").json()
    return render_template("guess.html", name=name, age=age["age"], gender=gender_response["gender"])


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_post = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", all_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
