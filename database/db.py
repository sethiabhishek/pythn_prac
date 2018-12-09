import sqlite3

db_in_file = sqlite3.connect("dbcheck")
db_cursor = db_in_file.cursor()
db_cursor.execute("create table employee(id INT primary key not null, name VARCHAR(50) not null,department VARCHAR(50))")


db_in_file.close()