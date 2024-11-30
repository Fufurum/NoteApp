# data_serializer.py

import json
from note import Note
from note_category import NoteCategory

class DataSerializer:
    @staticmethod
    def save_to_file(data, filename: str):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, default=str, ensure_ascii=False)

    @staticmethod
    def load_from_file(filename: str):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Файл не найден.")
            return None
