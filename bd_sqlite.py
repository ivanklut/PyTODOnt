import sqlite3 as sql


with sql.connect('todo.db') as con:
    cur = con.cursor()
    # Почему отрабатывает удаление, если я просто функцию вызываю?
    # cur.execute("DROP TABLE IF EXISTS todo")

    cur.execute(
        """CREATE TABLE IF NOT EXISTS todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        do TEXT NOT NULL,
        status INTEGER DEFAULT 0,
        period INTEGER,
        importance INTEGER DEFAULT 0
        )"""
    )


def zapis(do, status, period, importance):
    with sql.connect('todo.db') as con:
        cur = con.cursor()

        print(f'И вот что {do}, {status}, {period}, {importance}')
        cur.execute(
            """
        INSERT INTO todo (
        do, status, period, importance)
        VALUES (?, ?, ?, ?)
        """,
            (do, status, period, importance),
        )

    print(f'Типа записал в базу: {do}')
