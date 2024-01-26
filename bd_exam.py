import sqlite3

conn = sqlite3.connect('exam_2.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS SGL_ (id INTEGER PRIMARY KEY AUTOINCREMENT, Diagn TEXT, Patients integer)""")


k=input("введите диагноз")
v=int(input('введите количество пациентов'))

cursor.execute("""INSERT INTO SGL_ (Diagn,Patients) VALUES(?,?)""", (k,v))
conn.commit()

print(cursor.fetchall())
