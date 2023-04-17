from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import json
from wtforms import Form, BooleanField, StringField, SelectField, validators, SubmitField

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Api Key
SECRET_API_KEY = 'Fenerbahce'

# Forms
class MyBaseForm(Form):
    class Meta:
        csrf = False  # Enable CSRF
        # csrf_class = ''  # Set the CSRF implementation
        # csrf_secret = 'foobar'  # Some implementations need a secret key.
        # Any other CSRF settings here.

# cafe add form
class AddCafe(MyBaseForm):
    name = StringField("Name of cafe", [validators.InputRequired()])
    map_url = StringField("Google map url", [validators.InputRequired()])
    img_url = StringField("Image url", [validators.InputRequired()])
    location = StringField("Location", [validators.InputRequired()])
    has_sockets = BooleanField("Has Sockets?")
    has_toilet = BooleanField("Has toilet?")
    has_wifi = BooleanField("Has wifi?")
    can_take_calls = BooleanField("Can take phone calls?")
    coffee_price = StringField("Normal Coffe price (e.g. £3.00)", [validators.InputRequired()])
    seats = SelectField("Number of avaible seats", choices=['0-10', '10-20', '20-30','30-50','50+'], )
    submit = SubmitField()

# update coffee proce
class UpdatePrice(MyBaseForm):
    coffee_price = StringField("New Coffe price (e.g. £3.00)", [validators.InputRequired()])
    submit = SubmitField("Change")



##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)



@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random")
def random():
    # obj = db.session.execute(db.select(func.random(Cafe))).scalar()
    obj = db.first_or_404(db.select(Cafe).order_by(func.random()))
    obj_dict = obj.__dict__
    obj_dict = {k:v for k,v in obj_dict.items() if k != '_sa_instance_state'}
    json_obj = json.dumps(obj_dict)
    # return render_template("index.html")
    return jsonify(json_obj)

@app.route("/all")
def all():
    obj = db.session.execute(db.select(Cafe)).scalars()
    list_row_dicts = []
    for row in obj:
        # print(row)
        obj_dict = row.__dict__
        obj_dict = {key:value for key,value in obj_dict.items() if key != '_sa_instance_state'}
        list_row_dicts.append(obj_dict)
    json_obj = json.dumps(list_row_dicts)
    return jsonify(json_obj)

@app.route("/search")
def search():
    location = request.args.get("loc", False)
    print(location)
    obj = Cafe.query.filter_by(location=location).all()
    error = {"error": {"Not Found": "Sorry, we don't have a cafe at that location."}}
    result = error
    if obj:
        result = []
        for row in obj:
            obj_dict = row.__dict__
            obj_dict = {key:value for key,value in obj_dict.items() if key != '_sa_instance_state'}
            result.append(obj_dict)
    return jsonify(result)


## HTTP POST - Create Record

@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddCafe(request.form)
    if request.method == 'POST' and form.validate():
        print("hmm")
        cafe = Cafe(
            name = form.name.data,
            map_url = form.map_url.data,
            img_url = form.img_url.data,
            location = form.location.data,
            seats = form.seats.data,
            has_toilet = form.has_toilet.data,
            has_wifi = form.has_wifi.data,
            has_sockets = form.has_sockets.data,
            can_take_calls = form.can_take_calls.data,
            coffee_price =form.coffee_price.data
        )
        db.session.add(cafe)
        db.session.commit()
        print("work")
        return redirect(url_for('add'))
    return render_template("add.html", form=form)

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if request.method == 'PATCH' and request.args.get("new_price") and cafe:
        cafe.coffee_price = request.args.get("new_price")
        db.session.add(cafe)
        db.session.commit()
        return jsonify({"success":"The coffee price was succesfully updated"})
    return jsonify({"fail":"The coffee price wasn't changed"}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['Delete'])
def delete(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    api_key = request.args.get("api-key")
    if cafe and api_key == SECRET_API_KEY:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({"succes":"The cafe was reported as closed and succesfully deleted from database"})
    if not cafe:
        return jsonify({"error":"Invalid cafe id"}), 404
    return jsonify({"error":"Invalid Api key"}), 403


if __name__ == '__main__':
    app.run(debug=True)
