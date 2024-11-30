# data_serializer.py

import json
from note import Note
from note_category import NoteCategory

class DataSerializer:
    """
    Класс для сериализации и десериализации данных.

    Этот класс отвечает за сохранение данных в файл и загрузку данных из файла. Он использует
    формат JSON для хранения данных о заметках и категориях заметок.

    Методы:
        save_to_file(data, filename): Сохраняет данные в файл.
        load_from_file(filename): Загружает данные из файла.
    """

    @staticmethod
    def save_to_file(data, filename: str):
        """
        Сохраняет данные в указанный файл в формате JSON.

        :param data: Данные для сериализации, которые будут сохранены в файл.
        :param filename: Имя файла, в который будет сохранен сериализованный объект.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            # Сериализация данных в JSON формат с поддержкой строковых объектов
            json.dump(data, file, default=str, ensure_ascii=False)

    @staticmethod
    def load_from_file(filename: str):
        """
        Загружает данные из файла.

        Попытка загрузить данные из файла с указанным именем. Если файл не найден, выводится
        сообщение об ошибке, и возвращается None.

        :param filename: Имя файла, из которого будут загружены данные.
        :return: Загруженные данные, или None, если файл не найден.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                # Десериализация данных из JSON файла
                return json.load(file)
        except FileNotFoundError:
            print("Файл не найден.")
            return None
