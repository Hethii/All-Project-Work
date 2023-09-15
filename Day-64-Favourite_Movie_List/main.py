from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///all_time_movies.db"
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by "
#                 "an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation"
#                 " with the caller leads to a jaw-dropping climax.",
#     rating=9,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family "
#                 "(Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each "
#                 "other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )


# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()

API_KEY = "ec726f8d66c6faa8323da31f93f0fd68"
url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"

# url_with_id = f"https://api.themoviedb.org/3/movie/{597}?language=en-US"
# params = {"api_key": API_KEY}
# response = requests.get(url_with_id, params=params).json()
# print(response)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g 7.5')
    review = StringField('Your Review')
    submit = SubmitField('Done')


class AddMovie(FlaskForm):
    movie_title = StringField('Movie Title')
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_movie = AddMovie()
    if request.method == "POST":
        add_movie_title = add_movie.movie_title.data
        params = {
            "api_key": API_KEY,
            "query": add_movie_title
        }
        response = requests.get(url, params=params).json()
        data = response["results"]
        return render_template("select.html", result=data)

    return render_template("add.html", form=add_movie)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    num = request.args.get("id")
    movie_to_update = db.get_or_404(Movie, num)
    if request.method == "POST":
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie_to_update, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/find")
def find():
    movie_db_id = request.args.get("movie_id")
    if movie_db_id:
        url_with_id = f"https://api.themoviedb.org/3/movie/{movie_db_id}?language=en-US"
        params = {"api_key": API_KEY}
        response = requests.get(url_with_id, params=params).json()
        image_url_original = "https://image.tmdb.org/t/p/original"
        image_url_postal = "https://image.tmdb.org/t/p/w500"
        new_movie = Movie(title=response["title"], img_url=f"{image_url_postal}{response['poster_path']}",
                          year=response["release_date"].split("-")[0],
                          description=response["overview"])
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
