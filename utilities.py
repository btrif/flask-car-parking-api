#  Created by Bogdan Trif on 2022.06.13 , 11:17 PM ; btrif
from config import Settings

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

