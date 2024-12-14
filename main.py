from PyQt5.QtWidgets import QApplication
from main_form import MainForm

# Точка входа в приложение
if __name__ == "__main__":
    # Создаем экземпляр приложения
    app = QApplication([])

    # Создаем главное окно приложения
    window = MainForm()

    # Отображаем главное окно
    window.show()

    # Запускаем главный цикл приложения
    app.exec_()
