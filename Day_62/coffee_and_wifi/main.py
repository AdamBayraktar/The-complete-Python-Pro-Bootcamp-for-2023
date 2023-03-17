from flask import Flask, render_template, url_for, redirect
# from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, URL, Regexp
import csv
from add_cafe_to_csv import AddCafe

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Bootstrap(app)


coffee_emojis = [('☕️'*quantity if quantity > 0 else '✘') for quantity in range(0, 6)]
wifi_emojis = [('💪'*quantity if quantity > 0 else '✘') for quantity in range(0, 6)]
power_emojis = [('🔌'*quantity if quantity > 0 else '✘') for quantity in range(0, 6)]

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    map_link = StringField('Cafe Location on Map (URL)', validators=[DataRequired(), URL()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired(), Regexp('[0-1]?[0-9](:[0-5][0-9])?[AP]M$', message="You have to use correct format, for example: 10AM or 12:30PM")])
    close = StringField('Closing Time e.g. 5PM', validators=[DataRequired(), Regexp('[0-1]?[0-9](:[0-5][0-9])?[AP]M$', message="You have to use correct format, for example: 10AM or 12:30PM")])
    coffee = SelectField('Coffe Rating', choices=coffee_emojis, validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=wifi_emojis, validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=power_emojis, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        AddCafe(form).add_to_csv('cafe-data.csv')
        return redirect(url_for('cafes'))

        
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
