import sqlite3

class SqliteDB:
    def __init__(self, dbfile):
        self.dbfile = dbfile

    def execute(self, sql, params=None):
        with sqlite3.connect(self.dbfile) as con:
            cur = con.cursor()
            # Почему отрабатывает удаление, если я просто функцию вызываю?
            # cur.execute("DROP TABLE IF EXISTS todo")

            if params is None:
                cur.execute(sql)
            else:
                cur.execute(sql, params)
