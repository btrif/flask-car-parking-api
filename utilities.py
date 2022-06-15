#  Created by Bogdan Trif on 2022.06.13 , 11:17 PM ; btrif
import json


####        Additional functions        ####

def get_time_difference(date_start, date_end):
    '''Computes the time difference between two dates in seconds '''
    time_diff = date_end - date_start
    seconds = time_diff.days * 86400 + time_diff.seconds    # 60*60*24 = 86400 seconds in a day
    return seconds


def compute_fee(tariff_type, tariff_value, seconds):
    ''' Computes the Fee based on the tariff type : hourly or daily.
    If visit is < 15 min then will return $0 Fee.
    :param tariff_type: str, daily or hourly
    :param seconds: the overall time spend
    :return: int, the Fee    '''
    from math import ceil
    if seconds <= 900:  # 15 min * 60 secs = 900 secs
        return 0
    elif tariff_type == 'hourly':
        return ceil(seconds / 3600) * tariff_value
    elif tariff_type == 'daily':
        return ceil(seconds / 86400) * tariff_value
    else:
        return f'Something got wrong. Please check'


class ParkingConfiguration():
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_dict = self.load_parking_configuration()


    def load_parking_configuration(self):
        with open(self.config_file) as json_file:
            data = json.load(json_file)
            # Print the type of data variable
            print("Type:", type(data))
            print("Data:", data)
        return data

    def write_parking_configuration(self):
        with open(self.config_file, 'w') as json_file:
            json.dump(self.config_dict, json_file)

    def get_available_places(self):
        pass


def get_parking_configuration():
    PC = ParkingConfiguration('config.json')
    parking_info = PC.config_dict["parking_info"]
    return parking_info

