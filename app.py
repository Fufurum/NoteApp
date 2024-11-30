# app.py

from note import Note
from note_category import NoteCategory
from data_serializer import DataSerializer

def main():
    # Создаем категории
    work_category = NoteCategory("Работа")
    personal_category = NoteCategory("Личное")
    
    # Создаем заметки
    note1 = Note("Заметка 1", "Текст заметки 1")
    note2 = Note("Заметка 2", "Текст заметки 2")
    note3 = Note("Заметка 3", "Текст заметки 3")
    
    # Добавляем заметки в категории
    work_category.add_note(note1)
    personal_category.add_note(note2)
    personal_category.add_note(note3)
    
    # Сериализация данных
    notes_data = {
        "work": work_category.get_notes(),
        "personal": personal_category.get_notes()
    }
    
    # Сохранение данных
    DataSerializer.save_to_file(notes_data, "notes_data.json")
    
    # Загрузка данных
    loaded_data = DataSerializer.load_from_file("notes_data.json")
    if loaded_data:
        print("Загруженные данные:")
        for category, notes in loaded_data.items():
            print(f"Категория: {category}")
            for note in notes:
                print(note)
    
if __name__ == "__main__":
    main()
