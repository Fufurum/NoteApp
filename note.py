import datetime

class Note:
    def __init__(self, title: str, content: str, category: str = "Разное"):
        self._title = title
        self._content = content
        self._category = category
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
        self._modified_at = datetime.datetime.now()

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value: str):
        self._content = value
        self._modified_at = datetime.datetime.now()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value: str):
        self._category = value
        self._modified_at = datetime.datetime.now()

    @property
    def created_at(self):
        return self._created_at

    @property
    def modified_at(self):
        return self._modified_at

    def to_dict(self):
        return {
            "title": self._title,
            "content": self._content,
            "category": self._category,
            "created_at": self._created_at.isoformat(),
            "modified_at": self._modified_at.isoformat(),
        }

    @staticmethod
    def from_dict(data):
        note = Note(
            title=data["title"],
            content=data["content"],
            category=data.get("category", "Разное")
        )
        note._created_at = datetime.datetime.fromisoformat(data["created_at"])
        note._modified_at = datetime.datetime.fromisoformat(data["modified_at"])
        return note

    def __str__(self):
        """
        Возвращает строковое представление заметки.
        """
        return (
            f"Заголовок: {self.title}\n"
            f"Текст: {self.content}\n"
            f"Категория: {self.category}\n"
            f"Создано: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Изменено: {self.modified_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )
