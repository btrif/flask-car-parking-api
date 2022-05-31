#  Created by Bogdan Trif on 2022.05.25 , 4:46 PM ; btrif

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from datetime import datetime

####        The definition of our application       ####
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parking.db'
db = SQLAlchemy(app)
datetime_format = '%Y-%m-%d %H:%M:%S'

###   Custom error handler for 404
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


###      The DB Model of the Parking holding the cars       ####
class Parking(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    car_number = db.Column(db.String(200), nullable=False)
    tariff = db.Column(db.String(10), default='hourly', nullable=False)
    date_start = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'< Car {self.id}.  {self.car_number}  {self.tariff}  {self.date_start} >'


###     Settings dataclass holding the Parking information variables      ###
@dataclass
class Settings():
    ''' The Parking Settings. You can modify here for customizations '''
    parking_capacity: int = 12
    hourly_tariff: int = 1
    daily_tariff: int = 10
    current_car_number: int = None
    available_places: int = None


####        Additional functions        ####

def get_time_difference(date_start, date_end):
    '''Computes the time difference between two dates in seconds '''
    time_diff = date_end - date_start
    seconds = time_diff.days * 86400 + time_diff.seconds  # 60*60*24 = 86400 seconds in a day
    return seconds


def compute_fee(tariff, seconds):
    ''' Computes the Fee based on the tariff type : hourly or daily.
    If visit is < 15 min then will return $0 Fee.
    :param tariff: str, daily or hourly
    :param seconds: the overall time spend
    :return: int, the Fee    '''
    from math import ceil
    if seconds <= 960:  # 15 min * 60 secs = 960 secs
        return 0
    elif tariff == 'hourly':
        return ceil(seconds / 3600) * Settings.hourly_tariff
    elif tariff == 'daily':
        return ceil(seconds / 86400) * Settings.daily_tariff
    else:
        return f'Something got wrong. Please check'
