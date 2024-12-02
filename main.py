import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
import sqlite3


class Coffee(QMainWindow):
    def __init__(self):
        super(Coffee, self).__init__()
        uic.loadUi('main.ui', self)
        self.latte.clicked.connect(self.latte_f)
        self.ecsp.clicked.connect(self.ecsp_f)
        self.americ.clicked.connect(self.americ_f)
        self.cap.clicked.connect(self.cap_f)

    def latte_f(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee
            WHERE id = 4""")
        for i in result:
            e = list(i)
            self.textB.setText(
                f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}")
        cur.close()

    def ecsp_f(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee
                    WHERE id = 2""")
        for i in result:
            e = list(i)
            self.textB.setText(
                f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}")
        cur.close()

    def americ_f(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee
                    WHERE id = 3""")
        for i in result:
            e = list(i)
            self.textB.setText(
                f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}")
        cur.close()

    def cap_f(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee
                    WHERE id = 1""")
        for i in result:
            e = list(i)
            self.textB.setText(
                f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}")
        cur.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Coffee()
    form.show()
    sys.exit(app.exec())
