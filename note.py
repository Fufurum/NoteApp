# note.py

import datetime

class Note:
    """
    Класс, представляющий заметку.

    Этот класс предназначен для создания и управления заметками в приложении. Каждая заметка
    имеет заголовок, текст, а также метки времени для отслеживания времени создания и последнего изменения.

    Атрибуты:
        _title (str): Заголовок заметки.
        _content (str): Текст заметки.
        _created_at (datetime): Время создания заметки.
        _modified_at (datetime): Время последнего изменения заметки.
    """
    
    def __init__(self, title: str, content: str):
        """
        Инициализация новой заметки.

        :param title: Заголовок заметки.
        :param content: Текст заметки.
        """
        self._title = None
        self._content = None
        self._created_at = datetime.datetime.now()
        self._modified_at = datetime.datetime.now()
        
        # Устанавливаем начальные значения
        self.title = title
        self.content = content

    @property
    def title(self):
        """
        Получить заголовок заметки.
        
        :return: Заголовок заметки.
        """
        return self._title
    
    @title.setter
    def title(self, value: str):
        """
        Установить заголовок заметки.

        Проверяет, что заголовок не пустой.

        :param value: Заголовок заметки.
        :raises ValueError: Если заголовок пустой.
        """
        if not value:
            raise ValueError("Заголовок не может быть пустым.")
        self._title = value

    @property
    def content(self):
        """
        Получить текст заметки.

        :return: Текст заметки.
        """
        return self._content

    @content.setter
    def content(self, value: str):
        """
        Установить текст заметки.

        Проверяет, что текст заметки не пустой и обновляет время последнего изменения.

        :param value: Текст заметки.
        :raises ValueError: Если текст пустой.
        """
        if not value:
            raise ValueError("Текст заметки не может быть пустым.")
        self._content = value
        self._modified_at = datetime.datetime.now()

    def __str__(self):
        """
        Представление заметки в виде строки.

        :return: Строка, представляющая заметку, включая заголовок, текст, время создания и время последнего изменения.
        """
        return f"Заголовок: {self.title}\nТекст: {self.content}\nСоздано: {self._created_at}\nИзменено: {self._modified_at}"
