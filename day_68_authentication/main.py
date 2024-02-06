from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# Configure Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
# UserMixin inheritance initializes required user properties for flask login, thus adding:
# is_authenticated, is_active, is_anonymous, and get_id()
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
 
with app.app_context():
    db.create_all()

# Create a user_loader callback - user record is provided from users db by id
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

# Site Routes

@app.route('/register', methods=["GET", "POST"])
def register():
    # GET: provides user registration form
    # POST: takes form fields, checks for existing user, if none then
    ## runs password through hash function, stores data in db, and logs user in,
    ## then sends them to the secrets page to download PDF
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        name = request.form["name"]

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if user:
            flash("User already exists. Please try logging in.")
            return redirect(url_for("login"))
        else:
            new_user = User(
                email = email,
                password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8),
                name = name
            )

            db.session.add(new_user)
            db.session.commit()

            # login and authenticate user
            login_user(new_user) # makes current_user object available

        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    # GET: provides login screen and fields
    # POST: takes the email and password from login form, retrieves user record from db,
    ## if not found then notifies user and redirects to login page, otherwise 
    ## checks the password hash against the password entered in login field, and if match,
    ## logs user in and redirects to secrets/download page
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # find user by email entered 
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        # Check if user email in db
        if not user:
            flash("Email not found.")
            return redirect(url_for("login"))
        # Check stored password hash against entered password hashed - returns boolean
        elif not check_password_hash(pwhash=user.password, password=password):
            flash("Incorrect password.")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required # only allows access if user is logged in
def secrets():
    print(f"Current user: {current_user.name}")
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required # only allows access if user is logged in
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
