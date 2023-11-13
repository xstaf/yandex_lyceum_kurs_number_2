import sqlite3

con = sqlite3.connect("events.db")
cur = con.cursor()

speed = int(input())
min_duration = int(input())
choice = {"event":[],"extension":[], "importance":[]}
result = cur.execute("""select type,size,quantity from Fish where size>=? and weight<=? ORDER BY type,size; """, ()).fetchall()
res = []
result = cur.execute('''SELECT title FROM films WHERE genre IN (SELECT id FROM genres WHERE title IN
            ('музыка', 'анимация')) and year >= 1997''').fetchall()
for elem in result:
    print(elem[0])
con.close()