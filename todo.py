# Импорт модуля уже может быть примером инверсии зависимостей,
# но тут нужна теория, поэтому пока закомментируем.
#  import bd_sqlite as bd


class Todo:
    """
    Класс для описания дела (to do).
    do - описание дела. Обязательный параметр.
    status - статус выполнения: False - не выполнено, True - выполнено.
    period - когда нужно сделать. ??не просто дата и время, а отрезок времени ?? Метка автоповторения
    importance - флаг важности дела. Значения: 0 - обычное, 1 - важное 2 - суперважное
    id - идентификатор дела
    Методы: save - создать, put - изменить, get - получить, det - удалить
    """

    def __init__(self, db, id=None, do='', status=False, period=0, importance=0):
        # Здесть происходит инверсия зависимостей (Dependency Inversion),
        # через использование паттерна "инжекции зависимости" (Dependency Injection) через конструктор.
        # Это происходит на уровне класса.
        self.db = db

        self.do = do
        self.status = status
        self.period = period
        self.importance = importance

    def save(self, data):
        # Это какой-то костыль, полагаю так не должно быть:
        if 'do' in data:
            self.do = data['do']
        if 'status' in data:
            self.status = data['status']

        # Здесь мы используем "интерфейс" для БД self.bd.zapis
        # Это возможно сказать из-за динамичности питона и "утиной" типизации.
        # Это можно почувствовать если попробовать написать тест без использования БД.
        self.bd.zapis(self.do, self.status, self.period, self.importance)

    def put(self):
        pass

    def get(self):
        pass

    def det(self):
        pass
