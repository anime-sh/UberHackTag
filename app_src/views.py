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

@app.route("/sign-up", methods=['GET', 'POST'])
def register_for_cause():
    return render_template("/sign_up.html")
    if request.method == "POST":
        req = request.form
        missing = list()
        for k, v in req.items():
            if v == "":
                missing.append(k)
        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("/sign_up.html", feedback=feedback)
        return redirect(request.url)
    return render_template("temp2.html")
