from flask import Flask

app = Flask(__name__)

from app_src import views

import json
from .classDefs import User,CauseDriver,Driver,Location,Payment,Ride