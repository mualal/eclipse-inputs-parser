import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLabel, QTextEdit, QPushButton, QFileDialog, QVBoxLayout, QApplication)
from lib import pre_parser, parser


def get_file(text_field, status_field):
    file_name, check = QFileDialog.getOpenFileName(None,
                                                   'Выберите файл с расширением .inc',
                                                   os.path.dirname(os.getcwd()).replace(os.sep, '/'),
                                                   'Text Files (*.txt *.inc)')
    if check:
        with open(file_name, 'r', encoding='UTF-8') as f:
            file_text = f.read()
            text_field.setPlainText(file_text)
        status_field.setText('Статус: текущие данные взяты из файла: ' + file_name)


def run_action(text_field, status_field):
    cleaned_text = pre_parser.clean_schedule(text_field.toPlainText())
    text_field.setPlainText(cleaned_text)

    output_file_path = os.path.join(os.path.dirname(os.getcwd()), 'output', 'schedule_output.csv')

    status_field.setText('Статус: данные в текстовом поле очищены и результат парсинга <a href=' +
                         output_file_path.replace(os.sep, '/') +
                         '>записан в csv файл</a>')
    status_field.setOpenExternalLinks(True)

    keywords = ("DATES", "COMPDAT", "COMPDATL")
    parameters = ("Date", "Well name", "Local grid name", "I", "J", "K upper", "K lower", "Flag on connection",
                  "Saturation table", "Transmissibility factor", "Well bore diameter", "Effective Kh",
                  "Skin factor", "Skin factor", "Skin factor", "D-factor")

    parser.transform_schedule(keywords, parameters, None, output_file_path, text_field.toPlainText())


def update_status(status_field):
    status_field.setText('Статус: текущие данные в текстовом поле редактируются пользователем')


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        parser_label = QLabel('Скопируйте раздел SCHEDULE в поле ниже или выберите файл', self)
        text_to_parse = QTextEdit(self)
        choose_button = QPushButton('Выбрать файл с разделом SCHEDULE')
        run_button = QPushButton('Запустить парсер')

        status_bar = QLabel('Статус: требуется файл для парсинга', self)
        status_bar.setStyleSheet('background-color: yellow; border: 1px solid black;')

        widgets = (parser_label, text_to_parse, choose_button, run_button, status_bar)

        vbox = QVBoxLayout()
        for widget in widgets:
            widget.setFont(QFont('Times New Roman', 12))
            vbox.addWidget(widget)

        choose_button.clicked.connect(lambda: get_file(text_to_parse, status_bar))
        run_button.clicked.connect(lambda: run_action(text_to_parse, status_bar))
        text_to_parse.textChanged.connect(lambda: update_status(status_bar))

        self.setLayout(vbox)

        self.setGeometry(300, 300, 1550, 1050)
        self.setWindowTitle('Парсер входных файлов Eclipse')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
