#  Created by Bogdan Trif on 2022.05.24 , 11:52 AM ; btrif

from config import *
from models import Parking, app
from routes import index, list_cars, add_car, delete_car, parking_places

if __name__ == '__main__':
    ### Set at runtime :
    Settings.daily_tariff = 19.5
    Settings.hourly_tariff = 2.5
    Settings.parking_capacity = 21

    current_car_number = Parking.query.count()
    Settings.current_car_number = current_car_number
    Settings.available_places = Settings.parking_capacity - current_car_number
    app.run(debug=True, host=HOST, port=PORT, use_reloader=True)
