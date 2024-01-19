from random import choice
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SelectField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Google Maps Link', validators=[DataRequired(), URL()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Close Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Quality', choices=[('⭐️', "Poor"), ('⭐️⭐️', "Drinkable"), (
        '⭐️⭐️⭐️', "Good"), ('⭐️⭐️⭐️⭐️', "Great"), ('⭐️⭐️⭐️⭐️⭐️', "Fantastic")], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Speed', choices=[('🛜', "Dial-Up"), ('🛜🛜', "Acceptable"), (
        '🛜🛜🛜', "Good"), ('🛜🛜🛜🛜', "Fast"), ('🛜🛜🛜🛜🛜', "Fiber-Optic-Light-Speed")], validators=[DataRequired()])
    outlet_availability_rating = SelectField('Outlet Availability', choices=[('🔌', "Extension Cord Needed"), ('🔌🔌', "Hug The Wall"), (
        '🔌🔌🔌', "Good"), ('🔌🔌🔌🔌', "Great"), ('🔌🔌🔌🔌🔌', "Outlet At Every Table")], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
