from flask.helpers import make_response
from flask import request, redirect
from app_src import app
from flask import render_template, jsonify, make_response, send_file
import json
import random
import gmaps
import gmplot
from statistics import mean
import os


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


@app.route(
    "/sign-up/missing/<data>", )
def miss(data):
    return render_template("/signup_missing.html", missing=data)


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

        feedback = "OK"
        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"

        return make_response(jsonify({"message": feedback}), 200)


    # return render_template("/sign_up.html")
@app.route("/rider/booked", methods=["GET", "POST"])
def booked_cars():
    if request.method == "POST":
        print("HELLO")
        req = request.get_json()
        print(req)
        total_dict = {}
        with open("./data.json") as f:
            total_dict = json.load(f)
        from_dict = total_dict["locations"][req["source"]]
        to_dict = total_dict["locations"][req["dest"]]
        # api_key = os.environ['GOOGLE_API_KEY']
        # gmaps.configure(None)
        # lats = [float(from_dict['lat']), float(to_dict['lat'])]
        # longs = [float(from_dict['long']), float(to_dict['long'])]
        # gmap = gmplot.GoogleMapPlotter(mean(lats), mean(longs), 13)
        # gmap.scatter(lats, longs, 'black', size=20)
        # gmap.draw(f'app_src/templates/gmplot_{req["source"]}_{req["dest"]}.html')
        fare_key = req['source'][-1:] + req['dest'][-1:]
        base_fare = total_dict["fares"][fare_key]
        extra_fare = int(0.15 * float(base_fare))
        print(fare_key, base_fare, extra_fare)
        return make_response(
            jsonify({
                "message": "ok",
                "base": base_fare,
                "extra": extra_fare
            }), 200)


@app.route('/gmplot_pickup1_dropoff1')
def show_map1():
    return render_template('gmplot_pickup1_dropoff1.html')


@app.route('/gmplot_pickup1_dropoff2')
def show_map2():
    return render_template('gmplot_pickup1_dropoff2.html')

@app.route('/gmplot_pickup2_dropoff1')
def show_map3():
    return render_template('gmplot_pickup2_dropoff1.html')

@app.route('/gmplot_pickup2_dropoff2')
def show_map4():
    return render_template('gmplot_pickup2_dropoff2.html')



index = -1
fare = 0
extrafare = 0
rfc = 0


@app.route("/rider/riding", methods=["GET", "POST"])
def ride_car():
    global index
    global fare
    global extrafare
    global rfc
    if (request.method == "POST"):
        print(request.args)
        with open('./data.json') as f:
            var = (json.load(f))
        dicto = {}
        if (index == -1):
            #rfc = request.args['rfc'] //needs to be called via animesh
            rfc = 1
            if (rfc == 1):
                index = random.randint(0, len(var['drivers']['Cause']) - 1)
            else:
                index = random.randint(0, len(var['drivers']['normal']) - 1)
            #fare =int(request.args['fare'])
            #extrafare = int(request.args['extrafare'])
            fare = 100
            extrafare = 200
            print(index)
        else:
            fare = int(request.args['fare'])
            extrafare = int(request.args['extrafare']) + int(
                request.args['addition'])
            #index = request.args['index']
            #fare = int(request.args['fare'])
            #extrafare = int(request.args['extrafare'])

        index = int(index)
        if (rfc):
            dicto = var['drivers']['Cause'][index]
        else:
            dicto = var['drivers']['normal'][index]
        if not rfc:
            return render_template('/x.html',
                                   name=dicto['name'],
                                   car=dicto['car'],
                                   rating=dicto['rating'],
                                   carnumber=dicto['carnumber'],
                                   kyd=dicto['kyd'],
                                   index=index,
                                   fare=fare,
                                   extrafare=extrafare,
                                   rfc=rfc)
        else:
            return render_template('/x.html',
                                   name=dicto['name'],
                                   car=dicto['car'],
                                   rating=dicto['rating'],
                                   carnumber=dicto['carnumber'],
                                   kyd=dicto['kyd'],
                                   index=index,
                                   fare=fare,
                                   extrafare=extrafare,
                                   rfc=rfc,
                                   needinfo=dicto['needinfo'],
                                   amountraised=dicto['amountraised'],
                                   amountneeded=dicto['amountneeded'])

