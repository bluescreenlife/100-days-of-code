from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = randint(1, 10)
    current_year = datetime.now().strftime("%Y")
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    name = name.title()

    response = requests.get(f"https://api.agify.io?name={name}&country_id=US")
    age = response.json()["age"]

    response = requests.get(f"https://api.genderize.io?name={name}&country_id=US")
    gender = response.json()["gender"]

    return render_template("guesser.html", age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)