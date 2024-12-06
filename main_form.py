import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QComboBox, QListWidget, QDialog, QDialogButtonBox
from PyQt5.QtCore import Qt
from note import Note
from note_category import NoteCategory
from data_serializer import DataSerializer

class NoteEditorDialog(QDialog):
    def __init__(self, note=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Создание/Редактирование заметки")
        self.setGeometry(150, 150, 400, 300)

        self.note = note
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Заголовок")
        if self.note:
            self.title_input.setText(self.note.title)

        self.content_input = QTextEdit(self)
        self.content_input.setPlaceholderText("Содержание")
        if self.note:
            self.content_input.setPlainText(self.note.content)

        button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.save_note)
        button_box.rejected.connect(self.reject)

        layout.addWidget(QLabel("Заголовок"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Содержание"))
        layout.addWidget(self.content_input)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def save_note(self):
        title = self.title_input.text()
        content = self.content_input.toPlainText()

        if title and content:
            if self.note:
                self.note.title = title
                self.note.content = content
            else:
                self.note = Note(title, content)

            self.accept()
        else:
            self.reject()

    def get_note(self):
        return self.note


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NoteApp")
        self.setGeometry(100, 100, 600, 400)

        # Инициализация категорий
        self.work_category = NoteCategory("Работа")
        self.personal_category = NoteCategory("Личное")

        # Загружаем данные из файла
        self.load_notes_from_file()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Кнопка для создания новой заметки
        self.create_button = QPushButton("Создать новую заметку", self)
        self.create_button.clicked.connect(self.create_note)

        # Кнопка для редактирования выбранной заметки
        self.edit_button = QPushButton("Редактировать заметку", self)
        self.edit_button.clicked.connect(self.edit_note)

        # Кнопка для удаления выбранной заметки
        self.delete_button = QPushButton("Удалить заметку", self)
        self.delete_button.clicked.connect(self.delete_note)

        # Выпадающий список для выбора категории
        self.category_selector = QComboBox(self)
        self.category_selector.addItem("Работа")
        self.category_selector.addItem("Личное")
        self.category_selector.currentTextChanged.connect(self.update_note_selector)

        # Список для отображения заметок
        self.note_selector = QListWidget(self)
        self.note_selector.clicked.connect(self.select_note)

        # Вывод заметок
        self.note_display = QTextEdit(self)
        self.note_display.setReadOnly(True)

        # Добавляем элементы в layout
        layout.addWidget(self.create_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(QLabel("Выберите категорию"))
        layout.addWidget(self.category_selector)
        layout.addWidget(self.note_selector)
        layout.addWidget(self.note_display)

        self.setLayout(layout)

        # Словарь для категорий
        self.categories = {
            "работа": self.work_category,
            "личное": self.personal_category
        }

    def load_notes_from_file(self):
        """Загружает заметки из файла JSON"""
        loaded_data = DataSerializer.load_from_file("notes_data.json")
        if loaded_data:
            for category, notes in loaded_data.items():
                for note_data in notes:
                    note = Note(note_data['title'], note_data['content'])
                    if category == "work":
                        self.work_category.add_note(note)
                    elif category == "personal":
                        self.personal_category.add_note(note)
        else:
            print("Файл не найден или пуст.")

    def update_note_selector(self):
        """Обновляет список заметок для выбранной категории"""
        self.note_selector.clear()

        category_name = self.category_selector.currentText().lower()
        selected_category = self.categories.get(category_name)

        if selected_category:
            # Список заметок из выбранной категории
            notes = selected_category.notes
            for note in notes:
                self.note_selector.addItem(note.title)

    def create_note(self):
        """Открывает окно для создания новой заметки"""
        dialog = NoteEditorDialog(parent=self)
        if dialog.exec_() == QDialog.Accepted:
            new_note = dialog.get_note()
            if new_note:
                category_name = self.category_selector.currentText().lower()
                selected_category = self.categories.get(category_name)
                selected_category.add_note(new_note)
                self.update_note_selector()

                # Сохраняем данные в файл
                notes_data = {
                    "work": [note.to_dict() for note in self.work_category.notes],
                    "personal": [note.to_dict() for note in self.personal_category.notes]
                }
                DataSerializer.save_to_file(notes_data, "notes_data.json")
                self.note_display.setText(f"Заметка '{new_note.title}' сохранена!")

    def edit_note(self):
        """Открывает окно для редактирования выбранной заметки"""
        selected_item = self.note_selector.currentItem()
        if selected_item:
            category_name = self.category_selector.currentText().lower()
            selected_category = self.categories.get(category_name)
            note_title = selected_item.text()
            note = next((n for n in selected_category.notes if n.title == note_title), None)

            if note:
                dialog = NoteEditorDialog(note, parent=self)
                if dialog.exec_() == QDialog.Accepted:
                    updated_note = dialog.get_note()
                    if updated_note:
                        self.update_note_selector()

                        # Сохраняем обновленные данные
                        notes_data = {
                            "work": [note.to_dict() for note in self.work_category.notes],
                            "personal": [note.to_dict() for note in self.personal_category.notes]
                        }
                        DataSerializer.save_to_file(notes_data, "notes_data.json")
                        self.note_display.setText(f"Заметка '{updated_note.title}' обновлена!")

    def delete_note(self):
        """Удаляет выбранную заметку"""
        selected_item = self.note_selector.currentItem()
        if selected_item:
            category_name = self.category_selector.currentText().lower()
            selected_category = self.categories.get(category_name)
            note_title = selected_item.text()
            note = next((n for n in selected_category.notes if n.title == note_title), None)

            if note:
                selected_category.notes.remove(note)
                self.update_note_selector()

                # Сохраняем обновленные данные
                notes_data = {
                    "work": [note.to_dict() for note in self.work_category.notes],
                    "personal": [note.to_dict() for note in self.personal_category.notes]
                }
                DataSerializer.save_to_file(notes_data, "notes_data.json")
                self.note_display.setText(f"Заметка '{note.title}' удалена.")

    def select_note(self):
        """Выбирает заметку из списка для отображения"""
        selected_item = self.note_selector.currentItem()
        if selected_item:
            category_name = self.category_selector.currentText().lower()
            selected_category = self.categories.get(category_name)
            note_title = selected_item.text()
            note = next((n for n in selected_category.notes if n.title == note_title), None)
            if note:
                self.note_display.setText(f"Заметка:\n\n{note.title}\n\n{note.content}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainForm()
    main_window.show()
    sys.exit(app.exec_())
