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


class GoogleStock:
    def __init__(self, amount_of_stock: int = 0):
        self.amount_of_stock = amount_of_stock

    def buy_stock(self, amount: int):
        self.amount_of_stock = self.amount_of_stock + amount
        return f'You successfully bought {amount} stock. \nYour current amount of GoogleStock = {self.amount_of_stock}'

    def sell_stock(self, amount: int):
        self.amount_of_stock = self.amount_of_stock - amount
        return f'You successfully sold {amount} stock. \nYour current amount of GoogleStock = {self.amount_of_stock}'


class FacebookStock:
    pass


class NetflixStock:
    pass


class TeslaStock:
    pass


class Investors(TeslaStock, NetflixStock, FacebookStock, GoogleStock):
    country = 'USA'
    currency = '$'


investor = Investors()
print(investor.buy_stock(25))
print(investor.buy_stock(21))
print(investor.sell_stock(10))

# End = str(input('Can we end? If you pick YES - all data will lost. If you pick NO - '
#                 'you will get possibility to buy more stock. '))

