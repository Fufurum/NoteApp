# main_form.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QLineEdit, QFormLayout
from note import Note
from note_category import NoteCategory
from data_serializer import DataSerializer

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NoteApp")
        self.setGeometry(100, 100, 600, 400)

        self.work_category = NoteCategory("Работа")
        self.personal_category = NoteCategory("Личное")
        
        self.init_ui()

    def init_ui(self):
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

    def load_notes(self):
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
