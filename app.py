#  Created by Bogdan Trif on 2022.05.24 , 11:52 AM ; btrif

from models import Parking, app
from utilities import ParkingConfiguration
from routes import index, list_cars, add_car, delete_car, parking_places

if __name__ == '__main__':
    PC = ParkingConfiguration('config.json')
    server_settings = PC.config_dict['server_settings']
    app.run(debug=True, host=server_settings['HOST'], port=server_settings['PORT'], use_reloader=True)
