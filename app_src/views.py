from app_src import app
from flask import render_template
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
    return render_template("temp2.html")
