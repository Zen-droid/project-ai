import sqlite3 as lite

cars = (
    (1, "Audi", 52642),
    (2, "Mercedes", 57127),
    (3, "Honda", 9000),
    (4, "Nissan", 29000),
    (5, "Ferrari", 350000),
    (6, "BMW", 41400),
    (7, "Nissan", 21600),
)

con = lite.connect('test.db')

with con:

    cur = con.cursor()
    
    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
    cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)

    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        if row[1] == "BMW":
            print(row)