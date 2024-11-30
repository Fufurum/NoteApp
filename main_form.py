import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QLineEdit, QMessageBox
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
        
        try:
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
                raise ValueError("Ошибка: Заголовок и содержание не могут быть пустыми.")
        except ValueError as ve:
            self.display_error("Ошибка сохранения заметки", str(ve))
        except Exception as e:
            self.display_error("Неизвестная ошибка", str(e))

    def load_notes(self):
        """
        Загружает заметки из файла.

        Загружает сериализованные данные из файла и отображает их в текстовом поле.
        Если загрузка данных не удалась, выводится сообщение об ошибке.
        """
        try:
            loaded_data = DataSerializer.load_from_file("notes_data.json")
            if loaded_data:
                notes_text = ""
                for category, notes in loaded_data.items():
                    notes_text += f"Категория: {category}\n"
                    for note in notes:
                        notes_text += f"{note}\n\n"
                self.note_display.setText(notes_text)
            else:
                raise FileNotFoundError("Не удалось загрузить данные. Файл не найден или пуст.")
        except FileNotFoundError as fnf_error:
            self.display_error("Ошибка загрузки данных", str(fnf_error))
        except json.JSONDecodeError as json_error:
            self.display_error("Ошибка чтения данных", "Не удалось прочитать данные из файла.")
        except Exception as e:
            self.display_error("Неизвестная ошибка", str(e))

    def display_error(self, title: str, message: str):
        """
        Отображает всплывающее окно с ошибкой.

        :param title: Заголовок окна.
        :param message: Сообщение ошибки.
        """
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle(title)
        error_dialog.setText(message)
        error_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainForm()
    main_window.show()
    sys.exit(app.exec_())
