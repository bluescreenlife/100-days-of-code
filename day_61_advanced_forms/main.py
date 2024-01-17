from crypt import methods
from ensurepip import bootstrap
from tokenize import String
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = "radmobile"

bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[Email(message="Please enter a valid email address.")])
    password = PasswordField(label="Password", validators=[Length(min= 8, message="Password must be at least %(min)d characters long.", )])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html", form=login_form)
        else:
            return render_template("denied.html", form=login_form, bootstrap=bootstrap)
    else:
        return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
