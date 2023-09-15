import smtplib

from flask import Flask, render_template, request
import requests

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/57169349affeafc82a62").json()
MY_EMAIL = ""
MY_PASSWORD = ""

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     name = request.form["name"]
#     email = request.form["email"]
#     phone_num = request.form["phone"]
#     message = request.form["message"]
#     print(f"{name}\n{email}\n{phone_num}\n{message}")
#     return "<h1>Successfully sent your message</h1>"


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_num = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="mine",
                                msg=f"Subject:New Message\n\n"
                                    f"Name: {name}\nEmail: {email}\nPhone Number: {phone_num}\nMessage: {message}")
        return render_template("contact.html")
    else:
        return render_template("contact.html")

# Angela's code:
# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     if request.method == "POST":
#         data = request.form
#         print(data["name"])
#         print(data["email"])
#         print(data["phone"])
#         print(data["message"])
#         return render_template("contact.html", msg_sent=True)
#     return render_template("contact.html", msg_sent=False)



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
