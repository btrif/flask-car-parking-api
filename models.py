#  Created by Bogdan Trif on 2022.06.13 , 11:11 PM ; btrif
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

####        The definition of our application       ####
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parking.db'
db = SQLAlchemy(app)
datetime_format = '%Y-%m-%d %H:%M:%S'




###      The DB Model of the Parking holding the cars       ####
class Parking(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    car_number = db.Column(db.String(200), nullable=False)
    tariff = db.Column(db.String(10), default='hourly', nullable=False)
    date_start = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'< Car {self.id}.  {self.car_number}  {self.tariff}  {self.date_start} >'


###   Custom error handler for 404
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


# This initiates the creates the DB and makes the correspondiong tables - Ceea ce lipsea
with app.app_context():
    db.create_all()