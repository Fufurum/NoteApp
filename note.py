import datetime

class Note:
    def __init__(self, title: str, content: str):
        self._title = title
        self._content = content
        self._created_at = datetime.datetime.now()
        self._modified_at = datetime.datetime.now()

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

    def to_dict(self):
        """Преобразование заметки в словарь для сериализации"""
        return {
            "title": self.title,
            "content": self.content,
            "created_at": str(self._created_at),
            "modified_at": str(self._modified_at)
        }

    @classmethod
    def from_dict(cls, data):
        """Создание заметки из словаря"""
        note = cls(data['title'], data['content'])
        note._created_at = datetime.datetime.fromisoformat(data['created_at'])
        note._modified_at = datetime.datetime.fromisoformat(data['modified_at'])
        return note
