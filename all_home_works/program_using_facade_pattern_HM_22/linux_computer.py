from datetime import datetime, timedelta
import random


class Linux:

    @staticmethod
    def turn_on():
        return 'Linux on'

    @staticmethod
    def turn_off():
        return 'Linux off'

    @staticmethod
    def notify_time():
        return f'Now - {datetime.now().time()}\n You still have paid computer time until:' \
               f' {(datetime.now() + timedelta(minutes=random.randint(5, 60))).time()}'
