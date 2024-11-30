# data_serializer.py

import json
from note import Note
from note_category import NoteCategory

class DataSerializer:
    """
    Класс для сериализации и десериализации данных приложения.
    """
    
    @staticmethod
    def save_to_file(data, filename: str):
        """
        Сохранение данных в файл.
        
        :param data: Данные для сериализации (например, список заметок).
        :param filename: Имя файла для сохранения.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, default=str, ensure_ascii=False)

    @staticmethod
    def load_from_file(filename: str):
        """
        Загрузка данных из файла.
        
        :param filename: Имя файла для загрузки.
        :return: Данные, загруженные из файла.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Файл не найден.")
            return None
