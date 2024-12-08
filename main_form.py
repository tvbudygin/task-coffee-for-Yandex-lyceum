import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QTextBrowser


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 600, 800, 600)
        self.setWindowTitle('кофе')

        self.cap = QPushButton(self)
        self.cap.move(0, 0)
        self.cap.resize(387, 32)
        self.cap.setText("Капучино")
        self.cap.clicked.connect(self.run)

        self.americ = QPushButton(self)
        self.americ.move(389, 0)
        self.americ.resize(387, 32)
        self.americ.setText("Американо")
        self.americ.clicked.connect(self.run)

        self.ecsp = QPushButton(self)
        self.ecsp.move(0, 34)
        self.ecsp.resize(387, 32)
        self.ecsp.setText("Эспрессо")
        self.ecsp.clicked.connect(self.run)

        self.latte = QPushButton(self)
        self.latte.move(389, 34)
        self.latte.resize(387, 32)
        self.latte.setText("Латте")
        self.latte.clicked.connect(self.run)

        self.changes = QPushButton(self)
        self.changes.move(0, 68)
        self.changes.resize(387, 32)
        self.changes.setText("больше возможностей")
        self.changes.clicked.connect(self.run)

        self.textB = QTextBrowser(self)
        self.textB.move(12, 122)
        self.textB.resize(776, 445)
        self.show()

    def run(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
