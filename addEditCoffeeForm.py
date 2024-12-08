import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(311, 238, 311, 238)
        self.setWindowTitle('изминить кофе')

        self.add = QPushButton(self)
        self.add.move(6, 54)
        self.add.resize(299, 32)
        self.add.setText("добавить запись о кофе")
        self.add.clicked.connect(self.run)

        self.change = QPushButton(self)
        self.change.move(6, 134)
        self.change.resize(299, 32)
        self.change.setText("изминить запись о кофе")
        self.change.clicked.connect(self.run)
        self.show()

    def run(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
