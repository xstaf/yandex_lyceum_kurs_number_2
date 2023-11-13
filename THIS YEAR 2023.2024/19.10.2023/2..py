import sqlite3


def get_result(name):
    db = name
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('''DELETE from films WHERE title=(select title from films WHERE title like 'Я%а')''''')
    con.commit()
