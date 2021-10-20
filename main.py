import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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
def random_cafes():
    random_cafe = random.choice(Cafe.query.all())
    cafe = jsonify(
        name=random_cafe.name,
        map_url=random_cafe.map_url,
        image=random_cafe.img_url,
        location=random_cafe.location,
        has_sockets=random_cafe.has_sockets,
        has_toilet=random_cafe.has_toilet,
        has_wifi=random_cafe.has_wifi,
        can_take_calls=random_cafe.can_take_calls,
        seats=random_cafe.seats,
        coffee_price=random_cafe.coffee_price
    )
    return cafe


@app.route("/all")
def all_cafes():
    cafes = Cafe.query.all()
    list_of_cafes = []
    for cafe in cafes:
        new_cafe = {
                "name":cafe.name,
                "map_url":cafe.map_url,
                "image":cafe.img_url,
                "location":cafe.location,
                "has_sockets":cafe.has_sockets,
                "has_toilet":cafe.has_toilet,
                "has_wifi":cafe.has_wifi,
                "can_take_calls":cafe.can_take_calls,
                "seats":cafe.seats,
                "coffee_price":cafe.coffee_price
        }
        list_of_cafes.append(new_cafe)
    return jsonify(cafes=list_of_cafes)


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
