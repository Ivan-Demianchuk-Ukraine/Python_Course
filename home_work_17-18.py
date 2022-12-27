# Выбрать систему, которая может быть описана несколькими классами.
# Описать исползуя классы и применить принципы ООП:
# - Наследование
#
# - Абстрактные классы и/или интерфейсы
#
# - Сокрытие
#
# - Инкапсуляция
#
# У классов должно быть состояние (поля) и реализация поведения через методы.
#
# Требований к типам полей (экземпляра/класса) и методов (экземпляра/класса/статические) нет, по необходимости как вы видите.
#
# Написать код который создает необходимые экземпляры и демонстрирует работу систему.
#
# Ограничений на количество классов нет, но конечно их тут будет не пара.
#
# Это задание на это и следующие занятие. Пока советую выбрать систему, и порисовать из чего она состоит.
start = str

while start != '4':

    class GoogleStock:
        google_price_for_one_stock = 550

        def __init__(self, amount_of_google_stock: int = 0):
            self.amount_of_google_stock = amount_of_google_stock

        def buy_google_stock(self, amount: int):
            self.amount_of_google_stock = self.amount_of_google_stock + amount
            return f'You successfully bought {amount} google stock. \nYour current amount of GoogleStock =' \
                   f' {self.amount_of_google_stock}'

        def sell_google_stock(self, amount: int):
            self.amount_of_google_stock = self.amount_of_google_stock - amount
            return f'You successfully sold {amount} google stock. \nYour current amount of GoogleStock = {self.amount_of_google_stock}'

        def get_total_google_stock_value(self):
            if Investors.currency == 'dollar':
                return f'You own Google shares worth: {self.amount_of_google_stock * GoogleStock.google_price_for_one_stock} ' \
                       f'dollars.'
            elif Investors.currency == 'euro':
                return f'You own Google shares worth: {self.amount_of_google_stock * GoogleStock.google_price_for_one_stock} ' \
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

        def buy_tesla_stock(self, amount: int):
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
        country = 'USA'
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

    #will be error because you need to change sequence of classes in the 103 line)
    investor = Investors(0, 0, 0, 0)

    start = str(input('What do you want today?\nTo check your balance of all stock - enter 1'
                    '\nTo buy new stock - enter 2\nTo sell stock - enter 3\n'
                    'End program. - enter 4'))
    if start == '1':
        print(investor.get_full_balance())

    elif start == '2':
        pass

    elif start == '3':
        pass

    elif start == '4':
        pass

    else:
        print('-'*10, 'Ops. Seems that you entered incorrect value. Please, choose digit between 1,2,3 and 4.', '-'*10)

    # # End = str(input('Can we end? If you pick YES - all data will lost. If you pick NO - '
# #                 'you will get possibility to buy more stock. '))