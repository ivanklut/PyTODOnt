import sqlite3 as sql

CREATE_TODO_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS todo (
id INTEGER PRIMARY KEY AUTOINCREMENT,
do TEXT NOT NULL,
status INTEGER DEFAULT 0,
period INTEGER,
importance INTEGER DEFAULT 0
)
"""

INSERT_TODO_SQL = """
INSERT INTO todo (
do, status, period, importance)
VALUES (?, ?, ?, ?)
"""


class TodoRepo:
    def __init__(self, db):
        self.db = db
        self.db.execute(CREATE_TODO_TABLE_SQL)

    def add(self, todo):
        self.db.execute(
            INSERT_TODO_SQL,
            (todo.do, todo.status, todo.period, todo.importance),
        )
