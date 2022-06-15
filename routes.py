#  Created by Bogdan Trif on 2022.05.25 , 4:44 PM ; btrif
from flask import request, render_template

import config
from config import *
from models import app, Parking, db
from utilities import *
from datetime import datetime

####         Routes         #####


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/parking_info')
def parking_places():
    return {'parking_capacity': Settings.parking_capacity, 'available_places': Settings.available_places,
            'hourly_tariff': Settings.hourly_tariff, 'daily_tariff': Settings.daily_tariff}


@app.route('/cars')
def list_cars():
    cars = Parking.query.all()
    list_of_cars = []

    for car in cars:
        car_Data = {'id': car.id, 'car_number': car.car_number, 'tariff': car.tariff, 'date_start': str(car.date_start)}
        list_of_cars.append(car_Data)

    if cars:
        return {'status': 'success', 'cars': list_of_cars}
    else:
        return {'status': 'error', 'message': "You don't have any cars in your parking lot. Just add some cars"}


@app.route('/add', methods=['GET', 'POST'])
def add_car():  # in browser URL : http://127.0.0.1:7000/add?car_number=CJ45WAY&tariff=hourly

    new_car_number = request.args.get('car_number')
    tariff = request.args.get('tariff')

    # Check if there is no car in the parking with the same car_number:
    existing_car_number = Parking.query.filter_by(car_number=new_car_number)
    if existing_car_number.count() > 0:     # Here we suppose that only one park may already exist within park. Not multiple
        date_start = Parking.query.filter_by(car_number='CT33M').all()[0].date_start
        position = Parking.query.filter_by(car_number='CT33M').all()[0].id
        return {'status': 'error', 'message': f"There is already a parked car with this number since {date_start}"
                                              f". It can be found at the position {position}"}

    # Check that the tariff is only hourly or daily :
    if tariff not in ['hourly', 'daily']:
        return {'status': 'error', 'message': f"{tariff} is not a Tariff Plan. tariff must be either `hourly` or `daily`"}

    # Check whether a new_car_number is alphanumeric
    if not str(new_car_number).isalnum():
        raise {'status': 'error', 'message': 'the new_car_number must be compose only of letters and digits'}

    # Also to note here that for further checks we must use a URL Validator as if one types :
    # http://127.0.0.1:7000/add?car_number=CT33M&OM&tariff=hourly a car will be added because
    #  &OM string will be ignored as it is undefined. and the new_car_number=CT33M will be added instead

    # Check if there are enough available places in the Parking :
    if Settings.available_places > 0:
        # Form the object of the car :
        new_car = Parking(car_number=new_car_number, tariff=tariff)
        try:
            db.session.add(new_car)
            db.session.commit()
            Settings.available_places -= 1  # Update available places
            return {'status': 'success', 'id': new_car.id, 'new_car_number': new_car.car_number,
                    'tariff': new_car.tariff, 'date_start': new_car.date_start,
                    'available_places': Settings.available_places}
        except Exception:
            return {'status': 'error', 'message': 'The car was not added. Connection problem with the database.'}

    else:
        return {'status': 'error', 'message': 'The Parking is FULL. Please come back later !'}


@app.route('/remove/<int:id>', methods=['GET', 'DELETE'])
def delete_car(id):
    car = Parking.query.get(id)
    if car:
        try:
            db.session.delete(car)
            db.session.commit()
            date_end = datetime.utcnow()
            seconds = get_time_difference(car.date_start, date_end)
            fee = compute_fee(car.tariff, seconds)
            Settings.available_places += 1  # Update available places, one place is available
            return {'status': 'success', 'message': {'id': car.id, 'car_number': car.car_number,
                                                     'tariff': car.tariff, 'date_start': car.date_start,
                                                     'date_end': datetime.utcnow(), 'fee': fee,
                                                     'available_places': Settings.available_places,
                                                     'time_diff': str(date_end - car.date_start), 'seconds': seconds}
                    }
        except Exception:
            return {'status': 'error', 'message': f"there was an error removing your car with id {car.id}"}

    else:
        return {'status': 'error', 'message': f'The car with id {id} does not exist in the Parking'}



@app.route('/configuration', methods=['GET', 'POST'])
def configuration():

    if request.method == "POST":
        # getting input with name = hourly in HTML form
        hourly_tariff = request.form.get("hourly")
        # getting input with name = daily in HTML form
        daily_tariff = request.form.get("daily")
        # Update the Settings dataclass
        if hourly_tariff and daily_tariff :
            config.Settings.hourly_tariff = hourly_tariff
            config.Settings.daily_tariff = daily_tariff
            return {"status":"success", "message": f"hourly_tariff tariff was updated to {hourly_tariff} and daily tariff was updated to {daily_tariff}"}
        else :
            {"status":"error", "message": f"You must input integer or float"}
    return render_template("configuration.html")



@app.route('/hello/<user>')
def hello_world(user=None):
    user = user or 'Shalabh'
    return '''
    <html>
        <head>
            <title>Templating in Flask</title>
        </head>
        <body>
            <h1>Hello %s!</h1>
            <p>Welcome to the world of Flask!</p>
        </body>
    </html>''' % user