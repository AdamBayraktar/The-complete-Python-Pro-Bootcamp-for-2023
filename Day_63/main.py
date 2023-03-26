from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db-books.db"

db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    review = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    books = db.paginate(db.select(Books))
    id = request.args.get('id', "")
    # edit book
    if request.method == 'POST':
        book = db.get_or_404(Books, id)
        book.review = request.form.get('rating', book.review)
        db.session.commit()
        return redirect(url_for('home'))
        pass
    # delete
    if id:
        book = db.get_or_404(Books, id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('home'))
    # return main home page
    return render_template('index.html', all_books=books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        book = Books( title = request.form['title'], 
                     author = request.form['author'], 
                     review = request.form['rating']
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit")
def edit():
    id = request.args.get('id', '')
    if id:
        book = db.paginate(db.select(Books).where(Books.id == id))
        # book = db.paginate(db.select(Books).where(Books.id == int(id)))
        return render_template("edit.html", books=book)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

