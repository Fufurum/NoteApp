# note.py

import datetime

class Note:
    """
    Класс, представляющий заметку.
    """
    def __init__(self, title: str, content: str):
        self._title = None
        self._content = None
        self._created_at = datetime.datetime.now()
        self._modified_at = datetime.datetime.now()
        
        # Устанавливаем начальные значения
        self.title = title
        self.content = content

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value: str):
        if not value:
            raise ValueError("Заголовок не может быть пустым.")
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value: str):
        if not value:
            raise ValueError("Текст заметки не может быть пустым.")
        self._content = value
        self._modified_at = datetime.datetime.now()

    def __str__(self):
        return f"Заголовок: {self.title}\nТекст: {self.content}\nСоздано: {self._created_at}\nИзменено: {self._modified_at}"
