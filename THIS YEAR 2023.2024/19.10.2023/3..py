import sqlite3


def get_result(name):
    db = name
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(
        '''DELETE from films WHERE genre=(select id from genres WHERE title ='фантастика' 
        and year < 2000 and duration > 90)''')
    con.commit()
    con.close()
