from datetime import datetime, timedelta
import random


class Mac:
    @staticmethod
    def turn_on():
        return 'Mac on'

    @staticmethod
    def turn_off():
        return 'Mac off'

    @staticmethod
    def notify_time():
        return f'remained paid computer using time until - ' \
               f'{(datetime.now() + timedelta(minutes=random.randint(5, 60))).time()}'

