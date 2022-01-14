from db import SqliteDB
from todorepo import TodoRepo
from todo import Todo

# Это интерфейс к бд
db = SqliteDB("db.sqlite3")

# Это репозиторий в терминах чистой архитектуры,
# инжектим туда бд
repo = TodoRepo(db)

# Это entity
todo = Todo("Task1")
todo = Todo("Task2")

# Кладём entity в репозиторий
repo.add(todo)
