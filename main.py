# Создать таблицу Car: марка, год выпуска, страна выпуска, объём двигателя, цена, цвет.
# Добавить 10 записей одним запросом (некоторые поля должны быть NULL).
# Написать запрос для вывода списка машин в виде модель автомобиля, страна производитель,
# цвет машины, машин, у которых год выпуска моложе, чем 2000.
# Написать запрос, который выводит количество автомобилей определённой марки.
# Добавить там, где возможно, к каждому запросу сортировку отнросительно фирмы по убыванию.

import mysql.connector
cursor = mysql.connector.connect(user='root',password='mosk159372846mosk',host='127.0.0.1',database='cars').cursor()
insert = "INSERT INTO cars (mark, year, country, engine, price, color) VALUES (%s, %s, %s, %s, %s, %s)"
insert_values = [
    ('BMW', 2000, 'Germany', 2.0, 12000, 'black'),  # 1
    ('audi', 1999, 'Germany', 1.9, 10000, 'white'),  # 2
    ('renault', 1900, 'france', 1.4,  'red'),  # 3
    ('toyota', 2010, 'Germany', 2.0, 12000, 'black'),  # 4
    ('volkswagen', 2003, 'Germany', 1.9, 12000),  # 5
    ('volvo', 2001,  2.0, 12000, 'black'),  # 6
    ('skoda', 1991, 'sweden', 1.0, 12000, 'yellow'),  # 7
    ('audi', 2000, 'Germany', 1.6,  'black'),  # 8
    ('audi', 1993, 'Germany', 1.3, 12000, ),  # 9
    ('BMW', 1963,  3.0, 12000, 'blue'),  # 10
    ('BMW', 1941, 'Germany', 2.6,  'black'),  # 11
    ('renault', 1997, 'denmark', 2.2, 12000, ),  # 12
    ('toyota', 2000, 'Germany', 2.0, 12000, 'black'),  # 13
    ('volkswagen', 2000, 'Germany', 2.0, 12000, 'black'),  # 14
    ('citroen', 2000, 'Germany', 2.0, 12000, 'black'),  # 15
    ('volvo', 2000, 'Germany', 2.0, 12000, 'black'),  # 16
    ('skoda', 2000,  2.0, 12000, 'black'),  # 17
    ('sitroen', 1994, 'Germany', 2.0, 12000, 'black'),  # 18
    ('sitroen', 2012, 'Germany', 2.0,'black'),  # 19
    ('sitroen', 2002, 'Germany',  12000, 'black'),  # 20
]
cursor.executemany(insert, insert_values)

# select = "SELECT * FROM cars"
# curs.execute(select)
# print(curs.fetchall())
