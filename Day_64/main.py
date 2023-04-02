from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form, DecimalField
from wtforms.validators import DataRequired
import requests
from add_movie_to_db import AddMovieToDb

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db.init_app(app)

API_KEY = '1e89783fc1b8924a8e42cdab21ca580c'
URL_SEARCH = 'https://api.themoviedb.org/3/search/movie'
URL_ID = 'https://api.themoviedb.org/3/movie'
params = {
    "api_key": API_KEY,
    "language": "en-US" 
}

params_only_api = {
    "api_key": API_KEY
}

# movie search form
class MovieSearch(Form):
    search = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Search")

# movie form to fill missing data, rating and review
class MovieData(Form):
    rating = DecimalField("Your rating out of 10, eg. 7.8", validators=[DataRequired()])
    review = StringField("Your review", validators=[DataRequired()])
    submit = SubmitField("Done")


# defining table for database
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True )
    img_url = db.Column(db.String, nullable=False)
    movie_id = db.Column(db.Integer, unique=True)

with app.app_context():
    db.create_all()

# main page
@app.route("/", methods=["POST", "GET"])
def home():
    id = request.args.get('id', False)
    # update movie data
    if request.method == "POST" and id:
        new_rating = request.form['rating']
        new_review = request.form['review']
        movie = db.get_or_404(Movies, id)
        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()
    # render every movie in db
    movies = db.session.execute(db.select(Movies).order_by(Movies.ranking)).scalars()
    return render_template("index.html", movies=movies)

# page where you type query to find the movie
@app.route("/add")
def add():
    return render_template("add.html", form=MovieSearch())

# select one of the many titles
@app.route("/select", methods=["POST"])
def select():
    # add a seraching title query to params
    params['query'] = request.form.get('search', False)
    if params['query']:
        movies = requests.get(URL_SEARCH, params=params).json()['results']
    return render_template("select.html", movies=movies)

# fill the missing data
@app.route("/edit")
def edit():
    id = request.args.get('id', False)
    if_add = request.args.get('add', False)
    if not id:
        return redirect(url_for('home'))
    # if movies was added recently
    elif if_add:
        # url of movies that was selected
        the_url = f"{URL_ID}/{id}"
        movie = requests.get(the_url, params=params_only_api).json()
        # instance of class that makes easier to add movie to db
        the_movie = AddMovieToDb(movie)
        db.session.add(the_movie.create(Movies))
        db.session.commit()
        new_movie = db.first_or_404(db.select(Movies).order_by(Movies.id.desc()))
        return render_template("edit.html", movie=new_movie, form=MovieData())
    # if movie was added before
    movie = db.get_or_404(Movies, id)
    return render_template("edit.html", movie=movie, form=MovieData())

@app.route("/delete")
def delete():
    id = request.args.get('id', False)
    if id:
        movie = db.get_or_404(Movies, id)
        db.session.delete(movie)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
