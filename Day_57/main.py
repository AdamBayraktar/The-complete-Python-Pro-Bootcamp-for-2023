from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blogs = requests.get('https://api.npoint.io/7ee1404e281973a3bcdb').json()
    return render_template("index.html", blogs=blogs)

@app.route('/post/<int:post_id>')
def get_blog_post(post_id):
    blogs = requests.get('https://api.npoint.io/7ee1404e281973a3bcdb').json()
    for blog in blogs:
        if blog['id'] == post_id:
            the_blog = blog
    return render_template("post.html", the_blog=the_blog)

if __name__ == "__main__":
    app.run(debug=True)
