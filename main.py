from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import random
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рандомайзер числа')
        self.resize(400, 100)

        main_l = QVBoxLayout()
        self.label = QLabel('Нажмите кнопку для выдачи рандомного числа')
        self.label.setStyleSheet("font-size: 18px;")
        main_l.addWidget(self.label)

        self.button_ran = QPushButton('ВЫДАТЬ РАНДОМНОЕ ЧИСЛО')
        self.button_ran.setFixedSize(400, 50)
        self.button_ran.clicked.connect(self.random)
        main_l.addWidget(self.button_ran)

        self.button_cls = QPushButton('ЗАКРЫТЬ ПРИЛОЖЕНИЕ')
        self.button_cls.setFixedSize(400, 50)
        self.button_cls.clicked.connect(self.close)
        main_l.addWidget(self.button_cls)

        self.setLayout(main_l)

    def random(self):
        random_numb = random.randint(0, 100)
        self.label.setText(f'Ваше число: {random_numb}')


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
