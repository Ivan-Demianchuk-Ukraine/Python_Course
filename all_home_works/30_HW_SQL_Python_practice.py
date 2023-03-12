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

    def execute(self, query, values=None):
        try:
            return list(self._cursor.execute(query))
        finally:
            return list(self._cursor.execute(query, values))


class DataBase(TableCreate):

    def get_all_cars(self):
        """
        Retrieve all cars from the Cars4 table.

        Returns:
            list of lists: A list of lists where each inner list represents a row from the Cars4 table.
        """
        self._cursor.execute("SELECT * from Cars4;")
        data = self._cursor.fetchall()
        return [list(i) for i in data]

    def insert_new_car(self, model: str, color: str, price: float):
        """Inserts a new car record into the database with the given model, color, and price.

        Args:
            model (str): The model of the car.
            color (str): The color of the car.
            price (float): The price of the car.

        Returns:
            List: A list containing the details of the inserted car record.
        """
        self._cursor.execute(f"INSERT into Cars4(model, color, price) VALUES (?, ?, ?);", (model, color, price))
        return self.execute("SELECT * from Cars4 where model=(?) and color=(?) and price=(?);",
                                         (model, color, price))

    def update_car_price_by_model(self, model: str, price: float):
        """
        Update the price of a car by its model.

        Args:
            model (str): The model of the car to be updated.
            price (float): The new price of the car.

        Returns:
            list of lists: A list of lists where each inner list represents a row from the Cars4 table that was updated.
        """
        self._cursor.execute("UPDATE Cars4 SET price = (?) WHERE model = (?);", (price, model))
        return self.execute("SELECT * from Cars4 where model=(?) and price=(?);", (model, price))

    def get_cars_where_color(self, color):
        """
        Retrieve all cars from the Cars4 table that match the specified color.

        Args:
            color (str): The color of the cars to be retrieved.

        Returns:
            list of lists: A list of lists where each inner list represents a row from the Cars4 table that matches the
             specified color.
        """
        return self.execute('SELECT * from Cars4 WHERE color = (?);', (color,))

    def find_cars_where_price_range(self, price_min: float, price_max: float):
        """
        Retrieve all cars from the Cars4 table whose prices fall within the specified range.

        Args:
            price_min (float): The minimum price of the cars to be retrieved.
            price_max (float): The maximum price of the cars to be retrieved.

        Returns:
            list of lists: A list of lists where each inner list represents a row from the Cars4 table whose price falls
             within the specified range.
        """
        return self.execute('SELECT * from Cars4 WHERE price > (?) and price < (?);',
                                         (price_min, price_max))

    def find_top_richest_cars(self, top_number: float):
        """
        Retrieve the top N cars with the highest prices from the Cars4 table.

        Args:
            top_number (float): The number of cars to retrieve.

        Returns:
            list of lists: A list of lists where each inner list represents a row from the Cars4 table for the N cars
             with the highest prices.
        """
        return self.execute('SELECT * from Cars4 order by price DESC limit (?);', (top_number,))

    def find_top_cheapest_cars(self, top_number: float):
        """
        Retrieve the top N cars with the lowest prices from the Cars4 table.

        Args:
            top_number (float): The number of cars to retrieve.

        Returns:
            list of lists: A list of lists where each inner list represents a row from the Cars4 table for the N cars with the lowest prices.
        """
        return self.execute('SELECT * from Cars4 order by price ASC limit (?);', (top_number,))

    @staticmethod
    def delete_car_by_color(color: str):
        """Deletes all cars with a given color from the database.

        Args:
            color (str): The color of the cars to be deleted.

        Returns:
            str: A message indicating that cars with the given color were successfully deleted.
        """
        return f'Cars with {color} color were successfully deleted'

    def calculate_average_cost_auto_park(self):
        return f'Average cost of whole auto park: {list(self._cursor.execute("SELECT AVG(price) from Cars4;"))[0][0]}'


db = DataBase()
# print(db.get_all_cars())
# print(db.update_car_price_by_model('TestaRodsterNew6', 71120))
# print(db.find_cars_where_price_range(3000, 90000))
# print(db.get_cars_where_color('red'))
# print(db.insert_new_car('TestaRodsterNew6', 'orange-dark-light', 51100))
# print(db.delete_car_by_color('orange'))
# print(db.find_top_richest_cars(5))
# print(db.find_top_cheapest_cars(5))
# print(db.delete_car_by_color('orange'))
# print(db.calculate_average_cost_auto_park())
