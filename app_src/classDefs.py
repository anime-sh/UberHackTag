import datetime
import json


class Location:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def toJSON(self):
        return self.__dict__


class Payment:
    def __init__(self, upiid):
        self.upiid = upiid


class User:
    def __init__(self, name, phnum, paymentdetails):
        self.name = name
        self.phnum = phnum
        self.paymentdetails = paymentdetails


class Driver:
    def __init__(self, name, car, rating, kyd, carno):
        self.name = name
        self.car = car
        self.rating = rating
        self.kyd = kyd
        self.carnumber = carno

    def toJSON(self):
        return self.__dict__


class Ride:
    def __init__(self, t, fro, usr, driv, fr, com, datetime, rfc=False, expay=0):
        self.to = t
        self.fro = fro
        self.user = usr
        self.driver = driv
        self.fare = fr
        self.completed = com
        self.date_time = datetime
        self.isrideforcause = rfc
        self.extrapay = expay


class CauseDriver(Driver):
    def __init__(self, name, car, rating, kyd, carno, needinf, amtneeded, amtraised):
        super().__init__(name, car, rating, kyd, carno)
        self.needinfo = needinf
        self.amountraised = amtraised
        self.amountneeded = amtneeded

    def toJSON(self):
        return self.__dict__
