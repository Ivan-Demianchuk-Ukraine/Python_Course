CREATE TABLE Persons(name STRING UNIQUE, favorite_color STRING UNIQUE, profit FLOAT UNIQUE);
CREATE TABLE Cars(model STRING UNIQUE, color STRING UNIQUE, price FLOAT UNIQUE);

INSERT INTO Persons (name, favorite_color, profit) VALUES ('John', 'blue', 2500);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Jinny', 'red', 3000);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Nency', 'yellow', 13000);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Rendy', 'black', 5300);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Sara', 'grey', 5200);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Arnold', 'green', 54000);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Karol', 'orange', 950);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Alice', 'purple', 3500);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Bob', 'teal', 6000);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Charlie', 'maroon', 8000);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('David', 'lavender', 4200);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Emily', 'periwinkle', 9200);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('George', 'magenta', 11000);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Helen', 'coral', 6700);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Isaac', 'navy', 9900);
INSERT INTO Persons (name, favorite_color, profit) VALUES ('Jacob', 'olive', 7800);

INSERT INTO Cars (model, color, price) VALUES ('Roadster', 'red', 19500);
INSERT INTO Cars (model, color, price) VALUES ('Cybertrack', 'brown', 2300);
INSERT INTO Cars (model, color, price) VALUES ('ModelY', 'grey', 2500);
INSERT INTO Cars (model, color, price) VALUES ('ModelS', 'blue', 2500);
INSERT INTO Cars (model, color, price) VALUES ('BMW', 'yellow', 4000);
INSERT INTO Cars (model, color, price) VALUES ('Mazda', 'grey', 5300);
INSERT INTO Cars (model, color, price) VALUES ('Porsh', 'orange', 9050);
INSERT INTO Cars (model, color, price) VALUES ('Lexus', 'black', 13000);
INSERT INTO Cars (model, color, price) VALUES ('Gigul', 'white', 150);
INSERT INTO Cars (model, color, price) VALUES ('Hundai', 'green', 2000);
INSERT INTO Cars (model, color, price) VALUES ('Ford', 'chartreuse', 13500);
INSERT INTO Cars (model, color, price) VALUES ('Honda', 'indigo', 9800);
INSERT INTO Cars (model, color, price) VALUES ('Jeep', 'gold', 22000);
INSERT INTO Cars (model, color, price) VALUES ('Kia', 'silver', 15500);
INSERT INTO Cars (model, color, price) VALUES ('Lamborghini', 'turquoise', 98000);
INSERT INTO Cars (model, color, price) VALUES ('Maserati', 'crimson', 79000);
INSERT INTO Cars (model, color, price) VALUES ('Nissan', 'fuchsia', 11200);
INSERT INTO Cars (model, color, price) VALUES ('Porsche', 'plum', 65000);
INSERT INTO Cars (model, color, price) VALUES ('Subaru', 'lime', 9200);
INSERT INTO Cars (model, color, price) VALUES ('Toyota', 'mauve', 14700);



# Со звездочкой по желанию
# 6*. Вывести для каждого человека самый дешевый автомобиль его любимого цвета
# , который он может себе позволить (цена автомобиля должна быть меньше или равна дохода человека).
# Отсортировать по имени чловека в алфавитном порядке.
# Решением должен быть файл с расширением .sql и всеми запросами
# name  model    color  price   profit
# ----  -------  -----  ------  -----
# Anna  Fiat M2  red    1000.0  2000.0
# John  Fiat M2  red    1000.0  1000.0
# Karl  BMW M2   black  1700.0  2500.0

# Результат для 6*
# name   model    color  price   profit
# -----  -------  -----  ------  ------
# Anna   Fiat M2  red    1000.0  2000.0
# James           green          500.0
# John   Fiat M2  red    1000.0  1000.0
# Karl   BMW M2   black  1700.0  2500.0

SELECT name, favorite_color, model, color, price, profit from Persons, Cars WHERE profit >= (SELECT price) AND favorite_color is (Select color) order by name ASC;
