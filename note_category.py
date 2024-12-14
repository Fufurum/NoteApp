from note import Note

class NoteCategory:
    """
    Класс для управления категориями заметок.
    Каждая категория содержит список заметок.
    """
    def __init__(self, name: str):
        """
        Инициализация категории.

        :param name: Название категории.
        """
        self._name = name  # Название категории
        self.notes = []  # Список заметок в категории

    @property
    def name(self):
        """
        Возвращает название категории.

        :return: str
        """
        return self._name

    @name.setter
    def name(self, value: str):
        """
        Устанавливает название категории. Название не может быть пустым.

        :param value: Новое название категории.
        :raises ValueError: Если значение пустое.
        """
        if not value:
            raise ValueError("Название категории не может быть пустым.")
        self._name = value

    def add_note(self, note: Note):
        """
        Добавляет заметку в категорию.

        :param note: Объект типа Note.
        :raises ValueError: Если переданный объект не является экземпляром Note.
        """
        if not isinstance(note, Note):
            raise ValueError("Можно добавлять только объекты типа Note.")
        self.notes.append(note)

    def remove_note_by_title(self, title: str):
        """
        Удаляет заметку из категории по её заголовку.

        :param title: Заголовок заметки, которую нужно удалить.
        """
        self.notes = [note for note in self.notes if note.title != title]

    def get_notes(self):
        """
        Возвращает список заметок в категории.

        :return: list of Note
        """
        return self.notes
