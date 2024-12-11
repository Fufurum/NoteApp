import pytest
import json
import datetime
from note import Note

def test_note_serialization():
    """Тест сериализации заметки в JSON."""
    note = Note("Test Title", "Test Content")
    note_dict = note.to_dict()
    note_json = json.dumps(note_dict)

    assert isinstance(note_json, str)
    deserialized_data = json.loads(note_json)
    assert deserialized_data["title"] == "Test Title"
    assert deserialized_data["content"] == "Test Content"

def test_note_deserialization():
    """Тест десериализации заметки из JSON."""
    note_data = {
        "title": "Title",
        "content": "Content",
        "created_at": datetime.datetime.now().isoformat(),
        "modified_at": datetime.datetime.now().isoformat()
    }
    note_json = json.dumps(note_data)
    deserialized_data = json.loads(note_json)
    note = Note.from_dict(deserialized_data)

    assert note.title == "Title"
    assert note.content == "Content"
    assert note._created_at.isoformat() == note_data["created_at"]
    assert note._modified_at.isoformat() == note_data["modified_at"]
