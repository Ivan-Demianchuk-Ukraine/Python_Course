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

# Start = str(input('Hello investor! What do you want today?\n Check balance of my stock - enter 1'
#                   '\n Buy new stock - enter 2\n Sell stock - enter 3\n'))

Full_Balance = {}


class GoogleStock:
    google_price_for_one_stock = 550

    def __init__(self, amount_of_google_stock: int = 0):
        self.amount_of_google_stock = amount_of_google_stock

    def buy_stock(self, amount: int):
        self.amount_of_google_stock = self.amount_of_google_stock + amount
        return f'You successfully bought {amount} stock. \nYour current amount of GoogleStock = {self.amount_of_google_stock}'

    def sell_stock(self, amount: int):
        self.amount_of_google_stock = self.amount_of_google_stock - amount
        return f'You successfully sold {amount} stock. \nYour current amount of GoogleStock = {self.amount_of_google_stock}'

    def get_total_stock_value(self):
        return self.amount_of_google_stock * GoogleStock.google_price_for_one_stock


class FacebookStock:
    pass


class NetflixStock:
    pass


class TeslaStock:
    pass


class Investors(TeslaStock, NetflixStock, FacebookStock, GoogleStock):
    country = 'USA'
    currency = 'dollar'

    @staticmethod
    def get_full_balance():
        return f'You have: {investor.amount_of_google_stock} Google stock.\n' \
               f'You have: . . . Tesla stock.\n' \
               f'You have: . . . Facebook stock.\n' \
               f'You have: . . . Netflix stock.'

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


investor = Investors()
print(investor.buy_stock(25))
print(investor.buy_stock(21))
print(investor.sell_stock(10))
print(investor.get_full_balance())
print(investor.get_total_stock_value())
print(investor.change_currency('euro'))
print(investor.google_price_for_one_stock)
print(investor.get_total_stock_value())
print(investor.change_currency('dollar'))
# End = str(input('Can we end? If you pick YES - all data will lost. If you pick NO - '
#                 'you will get possibility to buy more stock. '))

