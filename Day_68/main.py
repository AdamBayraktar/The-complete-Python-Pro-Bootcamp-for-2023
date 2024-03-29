from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

# auth
app.secret_key = b'_5#y2l21dsaczL"F4Q8z\n\xec]/'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        check_user_in_db = User.query.where(User.email == email).first()
        if check_user_in_db:
            flash("User with that email exists. Use login form instead")
            return redirect("register")
        user = User(
            email = email,
            password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8),
            name = request.form.get('name')
            )
        db.session.add(user)
        db.session.flush()
        db.session.refresh(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for("secrets", name=user.name))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get('password')
        email = request.form.get('email')
        user = User.query.where(User.email == email).first()
        if not user:
            flash('There is no user with such email.')
        elif user and  check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash('Incorrect password')
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    name = current_user.name
    return render_template("secrets.html", name=name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        'static', path='files/cheat_sheet.pdf', as_attachment=True
    )
    # return send_file(url_for('static', filename= 'files/cheat_sheet.pdf'), as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
