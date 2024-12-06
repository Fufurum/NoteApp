import json

class DataSerializer:
    @staticmethod
    def save_to_file(data, filename: str):
        """Сохраняет данные в файл"""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, default=str, ensure_ascii=False)

    @staticmethod
    def load_from_file(filename: str):
        """Загружает данные из файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Файл не найден. Будет создан новый.")
            return None
