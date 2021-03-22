from app_src import app
from flask import render_template
import json
import random

@app.route("/")
def index():
    return render_template("home.html")
