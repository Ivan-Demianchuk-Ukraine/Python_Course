import sqlite3

path = 'new.db'  # should be in the separate config file


class ConnectionToDataBase:
    def __init__(self):
        self._connection = sqlite3.connect(path, isolation_level=None)
        self._cursor = self._connection.cursor()


class TableCreate(ConnectionToDataBase):
    def __init__(self):
        super().__init__()
        self._cursor.execute('CREATE TABLE IF NOT EXISTS Cars4(model STRING PRIMARY KEY,'
                             ' color STRING, price FLOAT);')
        self._cursor.execute('CREATE TABLE IF NOT EXISTS Persons4(name STRING PRIMARY KEY,'
                             ' favorite_color STRING, profit FLOAT);')


# class Vendor:
#
#     def __init__(self, car, color, price):
#         self.car = car
#         self.color = color
#         self.price = price


class DataBase(TableCreate):

    # def __repr__(self):

    def get_all_cars(self):
        self._cursor.execute("SELECT * from Cars4;")
        data = self._cursor.fetchall()
        return [list(i) for i in data]

    def insert_new_car(self, model: str, color: str, price: float):
        self._cursor.execute(f"INSERT into Cars4(model, color, price) VALUES (?, ?, ?);", (model, color, price))

    def update_car_price_by_model(self, model: str, price: float):
        self._cursor.execute("UPDATE Cars4 SET price = (?) WHERE model = (?);", (price, model))
        return list(self._cursor.execute("SELECT * from Cars4 where model=(?) and price=(?);", (model, price)))

    def get_cars_where_color(self, color):
        return list(self._cursor.execute('SELECT * from Cars4 WHERE color = (?);', (color,)))

    def find_cars_where_price_range(self, price_min: float, price_max: float):
        return list(self._cursor.execute('SELECT * from Cars4 WHERE price > (?) and price < (?);',
                                         (price_min, price_max)))

    def delete_car_by_color(self, color: str):
        return list(self._cursor.execute('DELETE from Cars4 WHERE color = (?);', (color,)))

    def find_top3_richest_cars(self):
        pass

    def calculate_average_cost_auto_park(self):
        pass

    def find_cars_without_price(self):
        pass


db = DataBase()
# print(db.get_all_cars())
# print(db.update_car_price_by_model('TestaRodsterNew2', 73000))
# print(db.find_cars_where_price_range(2000, 10000))
# print(db.get_cars_where_color('red'))
# print(db.insert_new_car('TestaRodsterNew2', 'orange-purple', 84000))
print(db.delete_car_by_color('orange'))
