#first solution via using UNIQUE in the parameters of creating tables.

.headers on
.mode column

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

SELECT name, favorite_color, model, color, price, profit from Persons, Cars WHERE profit >= (SELECT price)
AND favorite_color is (Select color) order by name ASC;




#second solution without using UNIQUE.

.headers on
.mode column

CREATE TABLE Persons4(name STRING PRIMARY KEY, favorite_color STRING, profit FLOAT);
CREATE TABLE Cars4(model STRING PRIMARY KEY, color STRING, price FLOAT);

INSERT INTO Persons4 (name, favorite_color, profit) VALUES ('John', 'blue', 2500),
 ('Jinny', 'blue', 3000), ('Nency', 'yellow', 13000), ('Rendy', 'yellow', 5300), ('Sara', 'grey', 5300),
  ('Arnold', 'grey', 54000), ('Karol', 'orange', 54000);

INSERT INTO Cars4 (model, color, price) VALUES ('Roadster', 'red', 19500), ('Cybertrack', 'red', 2300),
('ModelY', 'grey', 2300), ('ModelS', 'grey', 2500), ('BMW', 'yellow', 4000), ('Mazda', 'yellow', 5150),
('Porsh', 'orange', 5150);

SELECT color, price, model from Cars4  inner join Persons4 on Persons4.profit >= Cars4.price and
Cars4.color = Persons4.favorite_color group by name having min(price);