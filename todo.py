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

    def __init__(self, do, pk=None, status=False, period=0, importance=0):

        self.pk = pk
        self.do = do
        self.status = status
        self.period = period
        self.importance = importance
