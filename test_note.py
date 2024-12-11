import pytest
import datetime
from note import Note

def test_note_initialization():
    """Тест инициализации заметки."""
    note = Note("Test Title", "Test Content")
    assert note.title == "Test Title"
    assert note.content == "Test Content"
    assert isinstance(note._created_at, datetime.datetime)
    assert isinstance(note._modified_at, datetime.datetime)

def test_note_title_setter():
    """Тест установки заголовка."""
    note = Note("Initial Title", "Content")
    note.title = "Updated Title"
    assert note.title == "Updated Title"

    # Тест ошибки при пустом заголовке
    with pytest.raises(ValueError):
        note.title = ""

def test_note_content_setter():
    """Тест установки текста заметки."""
    note = Note("Title", "Initial Content")
    modified_at_before = note._modified_at
    note.content = "Updated Content"
    assert note.content == "Updated Content"
    assert note._modified_at > modified_at_before

    # Тест ошибки при пустом содержимом
    with pytest.raises(ValueError):
        note.content = ""

def test_note_to_string():
    """Тест строкового представления заметки."""
    note = Note("Title", "Content")
    note_str = str(note)
    assert "Заголовок: Title" in note_str
    assert "Текст: Content" in note_str
    assert "Создано:" in note_str
    assert "Изменено:" in note_str

def test_note_to_dict():
    """Тест сериализации заметки в словарь."""
    note = Note("Title", "Content")
    note_dict = note.to_dict()
    assert note_dict["title"] == "Title"
    assert note_dict["content"] == "Content"
    assert isinstance(note_dict["created_at"], str)
    assert isinstance(note_dict["modified_at"], str)

def test_note_from_dict():
    """Тест десериализации заметки из словаря."""
    note_data = {
        "title": "Title",
        "content": "Content",
        "created_at": datetime.datetime.now().isoformat(),
        "modified_at": datetime.datetime.now().isoformat()
    }
    note = Note.from_dict(note_data)
    assert note.title == "Title"
    assert note.content == "Content"
    assert note._created_at.isoformat() == note_data["created_at"]
    assert note._modified_at.isoformat() == note_data["modified_at"]
