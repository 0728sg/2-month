# data base
#SQL - Structured Query Language
#no SQL
#SQLite3
#СУБД - истема управления базы данных
#PosgreSQL, mongoDB
#CRUD

import sqlite3 as sql3
# db = sql3.connect('user.db')
# cursor = db.cursor()
# db.commit()
# db.close()
with sql3.connect('user.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
    fullname STRING NOT NULL , 
    pol INTEGER NOT NULL ,
    bdate DATE 
    )''')
    cursor.execute('''INSERT INTO students(fullname,pol,bdate)
     VALUES('Maktan',1,'1999-11-01'),('Gaukhar',2,'2006-07-28')''')
#read
    # cursor.execute('''SELECT rowid,* FROM students''')
    # for row in cursor.fetchall():
    #     print(row)