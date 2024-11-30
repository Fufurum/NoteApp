# note_category.py

from note import Note

class NoteCategory:
    """
    Класс, представляющий категорию для заметок.
    """
    def __init__(self, name: str):
        """
        Инициализация категории.
        
        :param name: Название категории.
        """
        self._name = None
        self.notes = []  # Список заметок в данной категории
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Название категории не может быть пустым.")
        self._name = value

    def add_note(self, note: Note):
        """Добавить заметку в категорию."""
        if not isinstance(note, Note):
            raise ValueError("Можно добавлять только объекты типа Note.")
        self.notes.append(note)

    def get_notes(self):
        """Получить все заметки категории."""
        return [str(note) for note in self.notes]

    def __str__(self):
        return f"Категория: {self.name}\nЗаметки: {len(self.notes)}"
