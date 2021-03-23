from flask.helpers import make_response
from app_src import app
from flask import render_template, jsonify, make_response
import json
import random

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/temp.html")
def temp():
    return render_template("temp.html")

@app.route("/temp2.html")
def temp2():
    with open("data.json") as f:
        data = json.load(f)
    return render_template("temp2.html", driver_data = data)

# @app.route("/getdata")
# def getdata():
#     with open("data.json") as f:
#         data = json.load(f)
#     return make_response(jsonify(data))
