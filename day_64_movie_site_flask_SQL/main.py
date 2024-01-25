from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
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
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[integer] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# CREATE TABLE SCHEMA IN DB
with app.app_context():
    db.create_all()

# WTForm templates
class UpdateForm(FlaskForm):
    updated_rating = StringField(label="Your Rating:")
    updated_review = StringField(label="Your Review:")
    submit = SubmitField("Update Movie")

class AddForm(FlaskForm):
    movie_title = StringField(label="Movie Title")
    submit = SubmitField("Add Movie")
    
# Flask routes
    
@app.route("/")
def home():

    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    # assign movie.ranking to its position in the list
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()

    if add_form.validate_on_submit():
        user_search = add_form.movie_title.data
        formatted_search = quote(user_search)
        
        # API_KEY = "5ffa087d721280239f790e5b12c35a7a"
        URL = f"https://api.themoviedb.org/3/search/movie?query={formatted_search}&include_adult=true&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZmZhMDg3ZDcyMTI4MDIzOWY3OTBlNWIxMmMzNWE3YSIsInN1YiI6IjY1YjE4N2ViM2M0MzQ0MDE5MzY2NWEwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XrpR9fQ53p5hXs9o8_jYP1Eu_meEvqpOXCHNqCaPC9U"
        } 

        response = requests.get(URL, headers=headers)
        if response.status_code == 200:
            data = response.json()
            movie_search_data = [movie for movie in data["results"][:9]]

            if movie_search_data:
                return render_template("select.html", data=movie_search_data)
            else:
                print("Failed to retrieve movie search data.")

    return render_template("add.html", form=add_form)

@app.route("/find")
def find():
    selection_id = request.args.get("id")
    print(f"Retrieved selection id: {selection_id}")

    # lookup movie details
    URL = f"https://api.themoviedb.org/3/movie/{selection_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZmZhMDg3ZDcyMTI4MDIzOWY3OTBlNWIxMmMzNWE3YSIsInN1YiI6IjY1YjE4N2ViM2M0MzQ0MDE5MzY2NWEwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XrpR9fQ53p5hXs9o8_jYP1Eu_meEvqpOXCHNqCaPC9U"
    } 

    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # print(data)
    else:
        print(f"\nData retrieval error: {response.status_code}\n")

    # add movie to database
    movie_to_add = Movie(title=data["original_title"], img_url=f"https://image.tmdb.org/t/p/original{data['poster_path']}", year=data['release_date'].split("-")[0], description=data['overview'])
    
    db.session.add(movie_to_add)
    db.session.commit()

    # redirect to home
    return redirect(url_for("update", id=movie_to_add.id))

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
