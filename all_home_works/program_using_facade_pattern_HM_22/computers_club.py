from mac_computer import Mac
from windows_computer import Windows
from linux_computer import Linux


class ComputersClub:
    def __init__(self):
        self.mac = Mac()
        self.windows = Windows()
        self.linux = Linux()

    def turn_on_all(self):
        self.mac.turn_on()
        self.windows.turn_on()
        self.linux.turn_on()
        return 'All devices turned on.'

    @staticmethod
    def turn_on_mac_comps():
        for i in mac_users:
            i.turn_on()
        return 'all computers with mac systems are on'

    @staticmethod
    def turn_on_windows_comps():
        for i in windows_users:
            i.turn_on()
        return 'all computers with windows systems are on'

    @staticmethod
    def turn_on_linux_comps():
        for i in linux_users:
            i.turn_on()
        return 'all computers with linux systems are on'

    def turn_off_all(self):
        self.mac.turn_off()
        self.windows.turn_off()
        self.linux.turn_off()
        return 'All devices turned off.'

    @staticmethod
    def turn_off_mac_comps():
        for i in mac_users:
            i.turn_on()
        return 'all computers with mac systems are off'

    @staticmethod
    def turn_off_windows_comps():
        for i in windows_users:
            i.turn_on()
        return 'all computers with windows systems are off'

    @staticmethod
    def turn_off_linux_comps():
        for i in linux_users:
            i.turn_on()
        return 'all computers with linux systems are off'

    def time_notify_all(self):
        self.mac.notify_time()
        self.windows.notify_time()
        self.linux.notify_time()
        return f'All users received notification about the remained time.\n' \
               f'Mac-user: {self.mac.notify_time()}\n' \
               f'Windows-user: {self.mac.notify_time()}\n' \
               f'Linux-user: {self.mac.notify_time()}\n'


user_1 = Mac()
user_2 = Windows()
user_3 = Linux()
user_4 = Mac()
user_5 = Windows()
user_6 = Linux()
user_7 = Mac()

mac_users = [user_1, user_4, user_7]
windows_users = [user_2, user_5]
linux_users = [user_3, user_6]
