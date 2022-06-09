#  Created by Bogdan Trif on 2022.05.25 , 4:44 PM ; btrif
from flask import request, render_template

from settings import *


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
        return jsonify({'cars': list_of_cars})
    else:
        return {'status': 'error', 'message': "You don't have any cars in your parking lot. Just add some cars"}


@app.route('/add', methods=['GET', 'POST'])
def add_car():  # in browser URL : http://127.0.0.1:7000/add?car_number=CJ45WAY&tariff=hourly

    new_car_number = request.args.get('car_number')
    tariff = request.args.get('tariff')

    # Check if there is no car in the parking with the same car_number:
    existing_car_number_count = Parking.query.filter_by(car_number=new_car_number).count()
    if existing_car_number_count > 0:
        return {'status': 'error', 'message': 'Hey! There is already a car with that number. I will call the Police !'}

    # Check that the tariff is only hourly or daily :
    if tariff not in ['hourly', 'daily']:
        return {'status': 'error', 'message': 'the tariff must be either hourly or daily'}

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
            return 'there was an error adding your car'

    else:
        return {'status': 'error', 'message': 'The Parking is FULL. Please come back later !'}


@app.route('/remove/<int:id>', methods=['GET', 'DELETE', 'POST'])
def delete_car(id):
    car = Parking.query.get_or_404(id)
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
        return {'status': 'error', 'message': f'this car id={car.id} does not exist'}
