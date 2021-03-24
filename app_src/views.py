from flask.helpers import make_response
from flask import request, redirect
from app_src import app
from flask import render_template, jsonify, make_response
import json
import random


@app.route("/")
def index():
    return redirect("rider")


@app.route("/rider")
def riderIndex():
    return render_template("rider_home.html")


@app.route("/driver")
def driverIndex():
    return render_template("driver_home.html")


@app.route("/temp.html")
def temp():
    return render_template("temp.html")


@app.route("/temp2.html")
def temp2():
    with open("data.json") as f:
        data = json.load(f)
    return render_template("temp2.html", driver_data=data)

# @app.route("/getdata")
# def getdata():
#     with open("data.json") as f:
#         data = json.load(f)
#     return make_response(jsonify(data))


@app.route("/sign-up")
def sign_up_landing():
    return render_template("/sign_up.html")

@app.route("/sign-up/success")
def succ():
    return render_template("./signup_success.html")

@app.route("/sign-up/missing/<data>",)
def miss(data):
    return render_template("/signup_missing.html",missing=data)

@app.route("/sign-up/create_app", methods=['POST'])
def sign_up():
    if request.method == "POST":
        print("hello")
        req = request.get_json()
        print(req)
        missing = list()
        
        for k, v in req.items():
            if v == "":
                missing.append(k)

        feedback="OK"
        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            
        return make_response(jsonify({"message": feedback}), 200)

        
    # return render_template("/sign_up.html")
