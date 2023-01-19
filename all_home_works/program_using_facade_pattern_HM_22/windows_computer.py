from datetime import datetime, timedelta
import random


class Windows:

    @staticmethod
    def turn_on():
        return 'Windows on'

    @staticmethod
    def turn_off():
        return 'Windows off'

    @staticmethod
    def notify_time():
        return f'Now - {datetime.now().time()}\n You still have paid computer time until:' \
               f' {(datetime.now() + timedelta(minutes=random.randint(5, 60))).time()}'
