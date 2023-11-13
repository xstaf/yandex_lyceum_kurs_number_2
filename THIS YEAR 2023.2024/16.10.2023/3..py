import sqlite3

db = input()
con = sqlite3.connect(db)
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT year FROM films
    WHERE title like 'Х%'""").fetchall()
for elem in result:
    print(elem[0])
con.close()
