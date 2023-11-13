import sqlite3

db_name = input()
con = sqlite3.connect(db_name)
cur = con.cursor()
result = cur.execute('''SELECT title FROM films WHERE genre IN (SELECT id FROM genres WHERE title IN
            ('комедия')) and duration >= 60''').fetchall()
for elem in result:
    print(elem[0])
con.close()
