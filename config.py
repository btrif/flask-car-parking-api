#  Created by Bogdan Trif on 2022.05.25 , 4:46 PM ; btrif

from dataclasses import dataclass

###     Settings dataclass holding the Parking information variables      ###
@dataclass
class Settings():
    ''' The Parking Settings. You can modify here for customizations '''
    parking_capacity: int = 12
    hourly_tariff: int = 10
    daily_tariff: int = 1
    current_car_number: int = None
    available_places: int = None


HOST = '0.0.0.0'
PORT = 7000