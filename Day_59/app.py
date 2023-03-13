from flask import Flask, render_template, request
import requests
from mail import Mail

app = Flask(__name__)


@app.route("/")
def index():
    blogs = requests.get("https://api.npoint.io/cd34c8dd29e1fb764cc8").json()
    return render_template("index.html", blogs=blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        message = {}
        message['name'] = request.form['name']
        message['email'] = request.form['email']
        message['phone'] = request.form['phone']
        message['message'] = request.form['message']
        # you have to first connect with your email in mail.py
        Mail().send_email(message)
        return render_template("contact.html", title="Successfully sent your messages")
    return render_template("contact.html", title="Contact Me")

@app.route("/post/<int:id>")
def post(id):
    blogs = requests.get("https://api.npoint.io/cd34c8dd29e1fb764cc8").json()
    for blog in blogs:
        if blog['id'] == id:
            the_blog = blog
            return render_template('post.html', the_blog=the_blog)


    

if __name__ == "__main__":
    app.run(debug=True)