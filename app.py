"""Flask app for Cupcakes"""

from flask import Flask, render_template, redirect, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SECRET_KEY'] = "bunnyrabbit"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route("/")
def home():
    return render_template("cupcake.html")

@app.route("/api/cupcakes")
def cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]

    return jsonify(all_cupcakes)

@app.route("/api/cupcakes/<int:cupcake_id>")
def cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes", methods=["POST"])
def cupcakes_post():
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json["image"])

    db.session.add(new_cupcake)
    db.session.commit()

    response_json = jsonify(cupcake=new_cupcake.serialize())

    return(response_json, 201)

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def cupcake_patch(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating) 
    cupcake.image = request.json.get("image", cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def cupcake_delete(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(messgae="deleted")
