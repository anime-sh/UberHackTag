from flask.helpers import make_response
from flask import request, redirect
from app_src import app
from flask import render_template, jsonify, make_response
import json
import random


@app.route("/rider/book/", methods=["POST"])
def book_first():
    if (request.is_json):
        req = request.get_json()  # contains
        source = req['source']
        dest = req['dest']
        is_rfc = req['rfc']

        return render_template()