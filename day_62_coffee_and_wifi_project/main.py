from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SelectField, SubmitField
from wtforms.validators import DataRequired, url
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[
                       DataRequired("Please enter a cafe name.")])
    location = URLField('Google Maps Link', validators=[DataRequired(), url()])
    open_time = StringField('Open Time', validators=[
                            DataRequired("Please enter the shop's open time.")])
    close_time = StringField('Close Time', validators=[
                             DataRequired("Please enter the shop's close time.")])
    coffee_rating = SelectField('Coffee Quality', choices=[('⭐️'), ('⭐️⭐️'), (
        '⭐️⭐️⭐️'), ('⭐️⭐️⭐️⭐️'), ('⭐️⭐️⭐️⭐️⭐️')], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Speed', choices=[('🛜'), ('🛜🛜'), (
        '🛜🛜🛜'), ('🛜🛜🛜🛜'), ('🛜🛜🛜🛜🛜')], validators=[DataRequired()])
    outlet_availability_rating = SelectField('Outlet Availability', choices=[('🔌'), ('🔌🔌'), (
        '🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow([form.cafe.data, form.location.data,
                            form.open_time.data, form.close_time.data,
                            form.coffee_rating.data, form.wifi_rating.data,
                            form.outlet_availability_rating.data])
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
