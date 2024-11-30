# main_form.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QLineEdit, QFormLayout
from note import Note
from note_category import NoteCategory
from data_serializer import DataSerializer

class MainForm(QWidget):
    """
    Главная форма приложения NoteApp.

    Этот класс управляет взаимодействием с пользователем, включая создание, редактирование и сохранение заметок,
    а также загрузку заметок из файла.

    Атрибуты:
        work_category (NoteCategory): Категория заметок "Работа".
        personal_category (NoteCategory): Категория заметок "Личное".
    """

    def __init__(self):
        """
        Инициализация главной формы приложения.

        Создает окно приложения и инициализирует категории для заметок.

        Инициализирует UI-компоненты и настраивает поведение окна.
        """
        super().__init__()
        self.setWindowTitle("NoteApp")
        self.setGeometry(100, 100, 600, 400)

        self.work_category = NoteCategory("Работа")
        self.personal_category = NoteCategory("Личное")
        
        self.init_ui()

    def init_ui(self):
        """
        Инициализация пользовательского интерфейса.

        Создает компоненты интерфейса, такие как поля для ввода заголовка и содержания заметки, 
        а также кнопки для сохранения и загрузки заметок. Все элементы добавляются в компоновку.
        """
        layout = QVBoxLayout()
        
        # Заголовок
        self.title_input = QLineEdit(self)
        self.content_input = QTextEdit(self)
        
        # Кнопки
        self.save_button = QPushButton("Сохранить заметку", self)
        self.save_button.clicked.connect(self.save_note)

        self.load_button = QPushButton("Загрузить заметки", self)
        self.load_button.clicked.connect(self.load_notes)

        # Вывод
        self.note_display = QTextEdit(self)
        self.note_display.setReadOnly(True)

        # Добавляем элементы в layout
        layout.addWidget(QLabel("Заголовок"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Содержание"))
        layout.addWidget(self.content_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.load_button)
        layout.addWidget(self.note_display)

        self.setLayout(layout)

    def save_note(self):
        """
        Сохраняет заметку, полученную из полей ввода.

        Создает объект заметки и сохраняет его в соответствующую категорию.
        Также сериализует все заметки и сохраняет их в файл.
        Если заметка успешно сохранена, отображает сообщение с подтверждением.
        """
        title = self.title_input.text()
        content = self.content_input.toPlainText()
        
        if title and content:
            new_note = Note(title, content)
            self.personal_category.add_note(new_note)
            notes_data = {
                "work": self.work_category.get_notes(),
                "personal": self.personal_category.get_notes()
            }
            DataSerializer.save_to_file(notes_data, "notes_data.json")
            self.note_display.setText(f"Заметка '{title}' сохранена!")
        else:
            self.note_display.setText("Ошибка: Заголовок и содержание не могут быть пустыми.")

    def load_notes(self):
        """
        Загружает заметки из файла.

        Загружает сериализованные данные из файла и отображает их в текстовом поле.
        Если загрузка данных не удалась, выводится сообщение об ошибке.
        """
        loaded_data = DataSerializer.load_from_file("notes_data.json")
        if loaded_data:
            notes_text = ""
            for category, notes in loaded_data.items():
                notes_text += f"Категория: {category}\n"
                for note in notes:
                    notes_text += f"{note}\n\n"
            self.note_display.setText(notes_text)
        else:
            self.note_display.setText("Не удалось загрузить данные.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainForm()
    main_window.show()
    sys.exit(app.exec_())
