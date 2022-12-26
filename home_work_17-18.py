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

Start = str(input(' Hello investor! What do you want today? \n Check balance of my stock - enter 1'
                  ' \n Buy new stock - enter 2 \n Sell stock - enter 3\n'))



class GoogleStock:
    def __init__(self, amount_of_stock: int = None):
        self.amount_of_stock = amount_of_stock


class FacebookStock:
    pass


class NetflixStock:
    pass


class TeslaStock:
    pass


class Investors(TeslaStock, NetflixStock, FacebookStock, GoogleStock):
    country = 'USA'
    currency = '$'


investor = Investors(25)
print(investor.amount_of_stock)

End = str(input(' Can we end? If you pick YES - all data will lost. If you pick NO - '
                'you will get possibility to buy more stock. '))

