from crypt import methods
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from h11 import Data
from numpy import integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, null
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import requests
from urllib.parse import quote

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE MODEL
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[integer] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)


# CREATE TABLE SCHEMA IN DB
with app.app_context():
    db.create_all()

# WTForm templates
class UpdateForm(FlaskForm):
    updated_rating = StringField(label="New Rating")
    updated_review = StringField(label="New Review")
    submit = SubmitField("Update Movie")

class AddForm(FlaskForm):
    movie_title = StringField(label="Movie Title")
    submit = SubmitField("Add Movie")

@app.route("/")
def home():

    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars()

    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()

    if add_form.validate_on_submit():
        user_search = add_form.movie_title.data
        formatted_search = quote(user_search)
        
        API_KEY = "5ffa087d721280239f790e5b12c35a7a"
        URL = f"https://api.themoviedb.org/3/search/movie?query={formatted_search}&include_adult=true&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZmZhMDg3ZDcyMTI4MDIzOWY3OTBlNWIxMmMzNWE3YSIsInN1YiI6IjY1YjE4N2ViM2M0MzQ0MDE5MzY2NWEwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XrpR9fQ53p5hXs9o8_jYP1Eu_meEvqpOXCHNqCaPC9U"
        } 

        top_5_results_ids = []

        response = requests.get(URL, headers=headers)
        if response.status_code == 200:
            movie_results = response.json()["results"][:4] # top 5 movie results
            print(f"\n{movie_results}\n")
            top_5_results_ids = []




    return render_template("add.html", form=add_form)

@app.route("/update", methods=["GET", "POST"])
def update():
    update_form = UpdateForm()
    movie_id = request.args.get("id")
    movie_to_update = db.get_or_404(Movie, movie_id)

    if update_form.validate_on_submit():
        movie_to_update.rating = float(update_form.updated_rating.data)
        movie_to_update.review = update_form.updated_review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", movie=movie_to_update, form=update_form)

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
