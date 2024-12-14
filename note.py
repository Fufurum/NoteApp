import datetime

class Note:
    """
    Класс для представления заметки.

    Содержит заголовок, текст, категорию, дату создания и дату изменения заметки.
    """
    def __init__(self, title: str, content: str, category: str = "Разное"):
        """
        Инициализация заметки.

        :param title: Заголовок заметки.
        :param content: Текст заметки.
        :param category: Категория заметки (по умолчанию "Разное").
        """
        self._title = title  # Заголовок заметки
        self._content = content  # Текст заметки
        self._category = category  # Категория заметки
        self._created_at = datetime.datetime.now()  # Дата и время создания заметки
        self._modified_at = datetime.datetime.now()  # Дата и время последнего изменения заметки

    @property
    def title(self):
        """
        Возвращает заголовок заметки.

        :return: str
        """
        return self._title

    @title.setter
    def title(self, value: str):
        """
        Устанавливает новый заголовок заметки. Обновляет дату изменения.

        :param value: Новый заголовок заметки.
        :raises ValueError: Если заголовок пустой.
        """
        if not value:
            raise ValueError("Заголовок не может быть пустым.")
        self._title = value
        self._modified_at = datetime.datetime.now()  # Обновляем дату изменения

    @property
    def content(self):
        """
        Возвращает текст заметки.

        :return: str
        """
        return self._content

    @content.setter
    def content(self, value: str):
        """
        Устанавливает новый текст заметки. Обновляет дату изменения.

        :param value: Новый текст заметки.
        """
        self._content = value
        self._modified_at = datetime.datetime.now()  # Обновляем дату изменения

    @property
    def category(self):
        """
        Возвращает категорию заметки.

        :return: str
        """
        return self._category

    @category.setter
    def category(self, value: str):
        """
        Устанавливает новую категорию заметки. Обновляет дату изменения.

        :param value: Новая категория заметки.
        """
        self._category = value
        self._modified_at = datetime.datetime.now()  # Обновляем дату изменения

    @property
    def created_at(self):
        """
        Возвращает дату и время создания заметки.

        :return: datetime
        """
        return self._created_at

    @property
    def modified_at(self):
        """
        Возвращает дату и время последнего изменения заметки.

        :return: datetime
        """
        return self._modified_at

    def to_dict(self):
        """
        Преобразует объект заметки в словарь.

        :return: dict
        """
        return {
            "title": self._title,  # Заголовок
            "content": self._content,  # Текст
            "category": self._category,  # Категория
            "created_at": self._created_at.isoformat(),  # Дата создания в формате ISO
            "modified_at": self._modified_at.isoformat(),  # Дата изменения в формате ISO
        }

    @staticmethod
    def from_dict(data):
        """
        Создает объект заметки из словаря.

        :param data: Словарь с данными заметки.
        :return: Note
        """
        note = Note(
            title=data["title"],
            content=data["content"],
            category=data.get("category", "Разное")  # Устанавливаем категорию, если она есть в словаре
        )
        note._created_at = datetime.datetime.fromisoformat(data["created_at"])  # Восстанавливаем дату создания
        note._modified_at = datetime.datetime.fromisoformat(data["modified_at"])  # Восстанавливаем дату изменения
        return note

    def __str__(self):
        """
        Возвращает строковое представление заметки.

        :return: str
        """
        return (
            f"Заголовок: {self.title}\n"
            f"Текст: {self.content}\n"
            f"Категория: {self.category}\n"
            f"Создано: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Изменено: {self.modified_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )
