# - Сокрытие - Easy
# - Инкапсуляция - Easy
# У классов должно быть состояние (поля) и реализация поведения через методы. - maybe done.

# - Абстрактные классы и/или интерфейсы

import time
# print('H', end='')
# time.sleep(0.3)
# print('e', end='')
# time.sleep(0.3)
# print('l', end='')
# time.sleep(0.3)
# print('l', end='')
# time.sleep(0.3)
# print('o', end=' ')
# time.sleep(0.3)
#
# print('i', end='')
# time.sleep(0.3)
# print('n', end='')
# time.sleep(0.3)
# print('v', end='')
# time.sleep(0.3)
# print('e', end='')
# time.sleep(0.3)
# print('s', end='')
# time.sleep(0.3)
# print('t', end='')
# time.sleep(0.3)
# print('o', end='')
# time.sleep(0.3)
# print('r', end='')
# time.sleep(0.3)
# print('!')
# time.sleep(1)
#
#
#
# print('l', end='')
# time.sleep(0.3)
# print('e', end='')
# time.sleep(0.3)
# print('t', end='')
# time.sleep(0.3)
# print("'", end='')
# time.sleep(0.3)
# print('s', end=' ')
# time.sleep(0.3)
#
# print('g', end='')
# time.sleep(0.3)
# print("o", end='')
# time.sleep(0.3)
# print('?')
# time.sleep(0.5)
# print('.', end='')
# time.sleep(0.3)
# print('.', end='')
# time.sleep(0.3)
# print('.')
# time.sleep(0.3)
# print('.', end='')
# time.sleep(0.3)
# print('.', end='')
# time.sleep(0.3)
# print('.')
# time.sleep(2)

start = str


class GoogleStock:
    google_price_for_one_stock = 550

    def __init__(self, amount_of_google_stock: int = 0):
        self.amount_of_google_stock = amount_of_google_stock

    def buy_stocks(self, amount: int):
        self.amount_of_google_stock = self.amount_of_google_stock + amount
        return f'You successfully bought {amount} google stock. \nYour current amount of GoogleStock =' \
               f' {self.amount_of_google_stock}'

    def sell_google_stock(self, amount: int):
        self.amount_of_google_stock = self.amount_of_google_stock - amount
        return f'You successfully sold {amount} google stock. \nYour current amount of GoogleStock = {self.amount_of_google_stock}'

    def get_total_google_stock_value(self):
        if Investors.currency == 'dollar':
            return f'All your Google shares are valued at: {self.amount_of_google_stock * GoogleStock.google_price_for_one_stock} ' \
                   f'dollars.'
        elif Investors.currency == 'euro':
            return f'All your Google shares are valued at: {self.amount_of_google_stock * GoogleStock.google_price_for_one_stock} ' \
                   f'euros.'


class FacebookStock:
    facebook_price_for_one_stock = 400

    def __init__(self, amount_of_facebook_stock: int = 0):
        self.amount_of_facebook_stock = amount_of_facebook_stock

    def buy_facebook_stock(self, amount: int):
        self.amount_of_facebook_stock = self.amount_of_facebook_stock + amount
        return f'You successfully bought {amount} facebook stock. \nYour current amount of FacebookStock = ' \
               f'{self.amount_of_facebook_stock}'

    def sell_facebook_stock(self, amount: int):
        self.amount_of_facebook_stock = self.amount_of_facebook_stock - amount
        return f'You successfully sold {amount} facebook stock. \nYour current amount of FacebookStock =' \
               f' {self.amount_of_facebook_stock}'

    def get_total_facebook_stock_value(self):
        return self.amount_of_facebook_stock * FacebookStock.facebook_price_for_one_stock


class NetflixStock:
    netflix_price_for_one_stock = 330

    def __init__(self, amount_of_netflix_stock: int = 0):
        self.amount_of_netflix_stock = amount_of_netflix_stock

    def buy_netflix_stock(self, amount: int):
        self.amount_of_netflix_stock = self.amount_of_netflix_stock + amount
        return f'You successfully bought {amount} netflix stock. \nYour current amount of NetflixStock =' \
               f' {self.amount_of_netflix_stock}'

    def sell_netflix_stock(self, amount: int):
        self.amount_of_netflix_stock = self.amount_of_netflix_stock - amount
        return f'You successfully sold {amount} netflix stock. \nYour current amount of NetflixStock =' \
               f' {self.amount_of_netflix_stock}'

    def get_total_netflix_stock_value(self):
        return self.amount_of_netflix_stock * NetflixStock.netflix_price_for_one_stock


class TeslaStock:
    tesla_price_for_one_stock = 270

    def __init__(self, amount_of_tesla_stock: int = 0):
        self.amount_of_tesla_stock = amount_of_tesla_stock

    def buy_stocks(self, amount: int):
        self.amount_of_tesla_stock = self.amount_of_tesla_stock + amount
        return f'You successfully bought {amount} tesla stock. \nYour current amount of TeslaStock =' \
               f' {self.amount_of_tesla_stock}'

    def sell_tesla_stock(self, amount: int):
        self.amount_of_tesla_stock = self.amount_of_tesla_stock - amount
        return f'You successfully sold {amount} tesla stock. \nYour current amount of GoogleStock =' \
               f' {self.amount_of_tesla_stock}'

    def get_total_tesla_stock_value(self):
        if Investors.currency == 'dollar':
            return f'You own Tesla shares worth: {self.amount_of_tesla_stock * TeslaStock.tesla_price_for_one_stock} ' \
                   f'dollars.'
        elif Investors.currency == 'euro':
            return f'You own Tesla shares worth: {self.amount_of_tesla_stock * TeslaStock.tesla_price_for_one_stock} ' \
                   f'euros.'


class Investors(TeslaStock, NetflixStock, FacebookStock, GoogleStock):
    _country = 'USA'
    currency = 'dollar'

    def __init__(self, amount_of_tesla_stock, amount_of_netflix_stock, amount_of_facebook_stock, amount_of_google_stock):
        TeslaStock.__init__(self, amount_of_tesla_stock)
        NetflixStock.__init__(self, amount_of_netflix_stock)
        FacebookStock.__init__(self, amount_of_facebook_stock)
        GoogleStock.__init__(self, amount_of_google_stock)

    @staticmethod
    def get_full_balance():
        return f'You have: {investor.amount_of_google_stock} Google stock.\n' \
               f'You have: {investor.amount_of_tesla_stock} Tesla stock.\n' \
               f'You have: {investor.amount_of_facebook_stock} Facebook stock.\n' \
               f'You have: {investor.amount_of_netflix_stock} Netflix stock.'

    @classmethod
    def change_currency(cls, new_currency):
        if cls.currency == 'dollar' and new_currency == 'euro':
            cls.currency = 'euro'
            old_value = GoogleStock.google_price_for_one_stock
            GoogleStock.google_price_for_one_stock = GoogleStock.google_price_for_one_stock * 1.05
            return f'your {old_value} dollars for 1 stock was changed on {GoogleStock.google_price_for_one_stock}' \
                   f' euro for 1 stock'

        elif cls.currency == 'euro' and new_currency == 'dollar':
            cls.currency = 'dollar'
            old_value = GoogleStock.google_price_for_one_stock
            GoogleStock.google_price_for_one_stock = GoogleStock.google_price_for_one_stock / 1.05
            return f'your {old_value} euro for 1 stock was changed on {GoogleStock.google_price_for_one_stock}' \
                   f' dollar for 1 stock'


investor = Investors(0, 0, 0, 0)


while start != '5':
    start = str(input('What do you want?\nI want to check my actives - enter 1'
                    '\nI want to buy new stock - enter 2\nI want to sell stock - enter 3\n'
                    'Change currency - enter 4\n'
                    'End program - enter 5'))
    if start == '1':
        # print('.', end='')
        # time.sleep(0.3)
        # print('.', end='')
        # time.sleep(0.3)
        # print('.')
        # time.sleep(0.3)
        # print('.', end='')
        # time.sleep(0.3)
        # print('.', end='')
        # time.sleep(0.3)
        # print('.')
        # time.sleep(0.5)
        check_what = str
        while check_what != '6':
            check_what = str(input('What do you need to check?\n'
                                    'My Google stocks - press 1\n'
                                    'My Netflix stocks - press 2\n'
                                    'My Facebook stocks - press 3\n'
                                    'My Tesla stocks - press 4\n'
                                    'I want to check all my stocks in all companies - press 5\n'
                                    'Quit - press 6'))

            if check_what == '1':
                print(f'Actual price for one google stock now - '
                      f'{GoogleStock.google_price_for_one_stock} {Investors.currency}')
                print(GoogleStock.get_total_google_stock_value(investor))
                print('You have -', investor.amount_of_google_stock, 'stocks.')

            elif check_what == '2':
                pass

            elif check_what == '3':
                pass

            elif check_what == '4':
                pass

            elif check_what == '5':
                print(investor.get_full_balance())

            elif check_what == '6':
                pass

            else:
                print('-' * 10, 'Ops. Seems that you entered incorrect value. Please, choose digit 1,2,3,4 or 5.',
                      '-' * 10)

    elif start == '2':
        buy_what = str
        while buy_what != '6':
            buy_what = str(input('What do you want to buy?\n'
                                    'Google stocks - press 1\n'
                                    'Netflix stocks - press 2\n'
                                    'Facebook stocks - press 3\n'
                                    'Tesla stocks - press 4\n'
                                    'I want to buy stocks in all companies at once - press 5\n'
                                    'Quit - press 6'))

            if buy_what == '1':
                how_much = int(input('How much stock do you want ?'))
                GoogleStock.buy_stocks(investor, how_much)
                print('Thank you! Your purchase was successfully.')
                print('Now you have:', investor.amount_of_google_stock, 'google stocks.')
                print(investor.get_total_google_stock_value())
    elif start == '3':
        pass

    elif start == '4':
        pass

    elif start == '5':
        pass

    else:
        print('-'*10, 'Ops. Seems that you entered incorrect value. Please, choose digit 1,2,3,4 or 5.', '-'*10)

    # # End = str(input('Can we end? If you pick YES - all data will lost. If you pick NO - '
# #                 'you will get possibility to buy more stock. '))


# print(investor._country) - hiding
