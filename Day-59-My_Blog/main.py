import requests
from flask import Flask, render_template

app = Flask(__name__)
# response = requests.get("https://api.npoint.io/57169349affeafc82a62").json()
# print(response[0]["id"])


@app.route("/")
def hello():
    response = requests.get("https://api.npoint.io/57169349affeafc82a62").json()
    return render_template("index.html", all_posts=response)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/<int:num>")
def get_post(num):
    num -= 1
    response = requests.get("https://api.npoint.io/57169349affeafc82a62").json()
    return render_template("post.html", posts=response, num=num)



if __name__ == "__main__":
    app.run(debug=True)
