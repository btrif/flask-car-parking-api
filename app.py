#  Created by Bogdan Trif on 2022.05.24 , 11:52 AM ; btrif

from settings import *
from routes import index, list_cars, add_car, delete_car, parking_places


if __name__ == '__main__':
    current_car_number = Parking.query.count()
    Settings.current_car_number = current_car_number
    Settings.available_places = Settings.parking_capacity - current_car_number
    app.run(debug=True, host='0.0.0.0' , port = 7000, use_reloader=True)
