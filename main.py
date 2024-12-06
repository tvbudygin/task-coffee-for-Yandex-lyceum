import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QInputDialog
import sqlite3

a = {"Капучино": 1, "Эспрессо": 2, "Американо": 3, "Латте": 4}
add_val_k = []
add_val_e = []
add_val_a = []
add_val_l = []


class Coffee(QMainWindow):
    def __init__(self):
        super(Coffee, self).__init__()
        uic.loadUi('main.ui', self)
        self.latte.clicked.connect(self.latte_f)
        self.ecsp.clicked.connect(self.ecsp_f)
        self.americ.clicked.connect(self.americ_f)
        self.cap.clicked.connect(self.cap_f)
        self.changes.clicked.connect(self.new_form)

    def latte_f(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee
            WHERE id = 4""")
        for i in result:
            e = list(i)
            if len(add_val_l) > 0:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}\nВаши записи: {e[8]}")
            else:
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
            if len(add_val_e) > 0:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}\nВаши записи: {e[8]}")
            else:
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
            if len(add_val_a) > 0:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}\nВаши записи: {e[8]}")
            else:
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
            if len(add_val_k) > 0:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}\nВаши записи: {e[8]}")
            else:
                self.textB.setText(
                    f"Кофе: {e[7]}\nСорт: {e[1]}\nСтепень обжарки: {e[2]}\n"
                    f"Зерна: {e[3]}\nОписание вкуса: {e[4]}\nЦена: {e[5]}\nОбъем: {e[6]}")
        cur.close()

    def new_form(self):
        self.new_f = Changes()
        self.new_f.show()
        self.textB.clear()


class Changes(QMainWindow):
    def __init__(self):
        super(Changes, self).__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.add.clicked.connect(self.add_v)
        self.change.clicked.connect(self.change_v)

    def add_v(self):
        cofe, ok_pressed = QInputDialog.getItem(
            self, "Выбрать кофе", "Кофе",
            ("Капучино", "Эспрессо", "Американо", "Латте"), 0, False)
        if ok_pressed:
            name, ok_pressed = QInputDialog.getText(self, "Введите новую запись о кофе", "Новая запись")
            if ok_pressed:
                con = sqlite3.connect("coffee.sqlite")
                cur = con.cursor()
                result = cur.execute(f"UPDATE coffee SET новые = ? WHERE id = ?", (name, a[cofe]))
                con.commit()
                cur.close()
                if cofe == "Капучино":
                    add_val_k.append('новые')
                elif cofe == "Эспрессо":
                    add_val_e.append('новые')
                elif cofe == "Американо":
                    add_val_a.append('новые')
                elif cofe == "Латте":
                    add_val_l.append('новые')
                self.close()

    def change_v(self):
        cofe, ok_pressed = QInputDialog.getItem(
            self, "Выбрать колонку", "Колонка",
            ("Капучино", "Эспрессо", "Американо", "Латте"), 0, False)
        if ok_pressed:
            if len(add_val_k) > 0 and cofe == "Капучино":
                tabl, ok_pressed = QInputDialog.getItem(
                    self, "Выбрать колонку", "Колонка",
                    ("сорт", "обжарка", "зерна", "описание", "цена", "упаковка", *add_val_k), 0, False)
            elif len(add_val_e) > 0 and cofe == 'Эспрессо':
                tabl, ok_pressed = QInputDialog.getItem(
                    self, "Выбрать колонку", "Колонка",
                    ("сорт", "обжарка", "зерна", "описание", "цена", "упаковка", *add_val_e), 0, False)
            elif len(add_val_a) > 0 and cofe == "Американо":
                tabl, ok_pressed = QInputDialog.getItem(
                    self, "Выбрать колонку", "Колонка",
                    ("сорт", "обжарка", "зерна", "описание", "цена", "упаковка", *add_val_a), 0, False)
            elif len(add_val_l) > 0 and cofe == "Латте":
                tabl, ok_pressed = QInputDialog.getItem(
                    self, "Выбрать колонку", "Колонка",
                    ("сорт", "обжарка", "зерна", "описание", "цена", "упаковка", *add_val_l), 0, False)
            else:
                tabl, ok_pressed = QInputDialog.getItem(
                    self, "Выбрать колонку", "Колонка",
                    ("сорт", "обжарка", "зерна", "описание", "цена", "упаковка"), 0, False)
        if ok_pressed:
            name, ok_pressed = QInputDialog.getText(self, "Введите новое значение", "Новое значение")
            if ok_pressed:
                con = sqlite3.connect("coffee.sqlite")
                cur = con.cursor()
                result = cur.execute(f"UPDATE coffee SET {tabl} = ? WHERE id = ?", (name, a[cofe]))
                con.commit()
                cur.close()
                self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Coffee()
    form.show()
    sys.exit(app.exec())
