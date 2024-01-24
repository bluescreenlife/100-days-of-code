from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# initialize flask app
app = Flask(__name__)

# create SQL database
class Base(DeclarativeBase):
    pass

# set SQL database URI in app's config
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book-collection.db"

# create the extension
db = SQLAlchemy(model_class=Base)

# initialize the app
db.init_app(app)

# create table model object for book
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # show book's title when the object is printed
    def __repr__(self):
        return f'<Book {self.title}>'

# create table schema in the database
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # read books from SQL table
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = list(result.scalars())

    return render_template('index.html', books=all_books)

# flask routes

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # add book to SQL table - create record
        new_book = Book(title=request.form["title"],
                        author=request.form["author"], 
                        rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        book_to_update = db.get_or_404(Book, id)
        book_to_update.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for("home"))

    book_to_edit = db.get_or_404(Book, id)
    return render_template("edit_rating.html", book=book_to_edit)

@app.route("/delete/<int:id>")
def delete(id):
    book_to_delete = db.get_or_404(Book, id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
