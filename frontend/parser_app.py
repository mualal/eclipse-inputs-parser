import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLabel, QTextEdit, QPushButton, QFileDialog, QVBoxLayout, QApplication)


def get_file(text_field):
    file_name, check = QFileDialog.getOpenFileName(None, 'Выберите файл с расширением .inc',
                                              '', 'Text Files (*.txt *.inc)')
    if check:
        with open(file_name, 'r', encoding='UTF-8') as f:
            file_text = f.read()
            text_field.setPlainText(file_text)


def run_action(text):
    print(repr(text))


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        parser_label = QLabel('Скопируйте раздел SCHEDULE в поле ниже или выберите файл', self)
        text_to_parse = QTextEdit(self)
        choose_button = QPushButton('Выбрать файл с разделом SCHEDULE')
        run_button = QPushButton('Запустить парсер')

        widgets = (parser_label, text_to_parse, choose_button, run_button)

        vbox = QVBoxLayout()
        for widget in widgets:
            widget.setFont(QFont('Times New Roman', 12))
            vbox.addWidget(widget)

        choose_button.clicked.connect(lambda: get_file(text_to_parse))
        run_button.clicked.connect(lambda: run_action(text_to_parse.toPlainText()))

        self.setLayout(vbox)

        self.setGeometry(300, 300, 1550, 1050)
        self.setWindowTitle('Парсер входных файлов Eclipse')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
